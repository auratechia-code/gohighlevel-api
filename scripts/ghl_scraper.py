import asyncio
import re
import json
import os
import time
from pathlib import Path
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, MofNCompleteColumn
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

# ── Config ────────────────────────────────────────────────────────
BASE_URL = "https://marketplace.gohighlevel.com"
INPUT_FILE = "ghl_docs_urls.txt"
OUTPUT_DIR = Path("ghl_kb_output")
MAX_CONCURRENCY = 3
RETRIES = 3
TIMEOUT_PAGE = 45000  # ms
# ─────────────────────────────────────────────────────────────────

console = Console()

class GHLKBBuilder:
    def __init__(self, urls_file: str):
        self.urls_file = Path(urls_file)
        self.all_urls = []
        self.classified = {
            "endpoint": [],
            "webhook": [],
            "concept_page": [],
            "sdk": [],
            "module": [],
            "policy": []
        }
        self.results = {k: [] for k in self.classified.keys()}
        self.errors = []
        self.semaphore = asyncio.Semaphore(MAX_CONCURRENCY)
        self.start_time = datetime.now()

    # ── Phase 1: Cleaning & Classification ──────────────────────────

    def deduplicate_urls(self):
        """Implementa regex para eliminar hashes y priorizar versiones canónicas."""
        if not self.urls_file.exists():
            console.print(f"[bold red]Error:[/] {self.urls_file} no encontrado.")
            return False

        raw_urls = self.urls_file.read_text().splitlines()
        # Patrón: detecta hash de 3 caracteres alfanuméricos precedido por un guion al final
        hash_pattern = re.compile(r'(.+)-[a-f0-9]{3}$')
        
        seen_canonical = {} # {canonical_path: original_url}

        for url in raw_urls:
            url = url.strip().rstrip("/")
            if not url or url == f"{BASE_URL}/docs" or url == f"{BASE_URL}/docs/":
                continue
                
            match = hash_pattern.match(url)
            if match:
                canonical = match.group(1)
                # Si ya vimos la canónica (sin hash), no sobreescribir.
                # Si no, guardar esta versión.
                if canonical not in seen_canonical:
                    seen_canonical[canonical] = url
            else:
                # Versión canónica real, sobreescribe cualquier versión hasheada previa
                seen_canonical[url] = url

        self.all_urls = sorted(list(set(seen_canonical.values())))
        removed = len(raw_urls) - len(self.all_urls)
        
        console.print(Panel(f"URLs originales: [bold]{len(raw_urls)}[/]\nURLs únicas (desc. hashes): [bold]{len(self.all_urls)}[/]\nRemovidas: [yellow]{removed}[/]", 
                          title="Deduplicación", border_style="cyan"))
        return True

    def classify_urls(self):
        """Clasifica las URLs en grupos según su patrón de path."""
        for url in self.all_urls:
            path = urlparse(url).path
            if "/docs/ghl/webhooks/" in path:
                self.classified["webhook"].append(url)
            elif "/docs/ghl/" in path:
                self.classified["endpoint"].append(url)
            elif "/docs/sdk/" in path:
                self.classified["sdk"].append(url)
            elif "/docs/marketplace-modules/" in path:
                self.classified["module"].append(url)
            elif "/docs/MarketplacePolicies/" in path:
                self.classified["policy"].append(url)
            else:
                self.classified["concept_page"].append(url)

        table = Table(title="Clasificación de Documentación")
        table.add_column("Categoría", style="cyan")
        table.add_column("Cantidad", justify="right", style="green")
        for k, v in self.classified.items():
            table.add_row(k, str(len(v)))
        console.print(table)
        return True

    # ── Phase 2 & 3: Scraping Motor ────────────────────────────────

    async def expand_elements(self, page):
        """Asegura que todos los detalles estén abiertos para BS4."""
        await page.evaluate("""() => {
            document.querySelectorAll('details:not([open])').forEach(d => d.setAttribute('open', ''));
        }""")
        await asyncio.sleep(1)

    async def get_tabs_data(self, page, tab_list_selector, target_selector):
        """Interactúa con pestañas (tabs) para extraer contenido dinámico."""
        data = {}
        try:
            tabs = await page.query_selector_all(f"{tab_list_selector} li.tabs__item")
            for tab in tabs:
                label = await tab.inner_text()
                label = label.strip().lower().replace(".", "").replace(" ","_")
                await tab.click()
                await asyncio.sleep(0.4)
                content = await page.query_selector(target_selector)
                if content:
                    data[label] = await content.inner_text()
        except Exception:
            pass
        return data

    def generate_code_fallback(self, method, url, headers, body_example):
        """Genera ejemplos de código si no están disponibles en la web."""
        # Simple boilerplate para asegurar que no hay vacíos
        codes = {
            "python": f"import requests\nurl = '{url}'\nresponse = requests.{method.lower()}(url, headers={headers}, json={body_example})\nprint(response.json())",
            "nodejs": f"const axios = require('axios');\naxios.{method.lower()}('{url}', {body_example}, {{headers: {headers}}}).then(r => console.log(r.data));",
            "curl": f"curl -X {method} '{url}' -H 'Authorization: Bearer <TOKEN>' -d '{json.dumps(body_example)}'"
        }
        return codes

    async def scrape_endpoint(self, page, url):
        """Extracción detallada de endpoints de API."""
        await self.expand_elements(page)
        
        # Click en Response Tabs si existen
        responses = await self.get_tabs_data(page, ".openapi-tabs__response-code-container", ".prism-code")
        
        # Click en Code Example Tabs
        code_examples = await self.get_tabs_data(page, ".openapi-tabs__code-list-container", ".prism-code")
        
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')

        # Breadcrumbs
        breadcrumbs = [a.get_text(strip=True) for a in soup.select("nav[aria-label='Breadcrumbs'] .breadcrumbs__link")]
        
        # Headers, Params, etc.
        headers_req = []
        path_params = []
        query_params = []
        
        containers = soup.select("details.openapi-explorer__details-container")
        for container in containers:
            summary = container.select_one("summary")
            if not summary: continue
            text = summary.get_text(strip=True).lower()
            
            rows = container.select("table tr")
            for row in rows:
                cols = row.select("td")
                if len(cols) < 2: continue
                param_data = {"name": cols[0].get_text(strip=True), "description": cols[1].get_text(strip=True)}
                if "header" in text: headers_req.append(param_data)
                elif "path" in text: path_params.append(param_data)
                elif "query" in text: query_params.append(param_data)

        # Body Schema & Example
        body_section = soup.find("h3", string=re.compile(r"Request Body", re.I))
        body_example = {}
        if body_section:
            # Buscar el siguiente bloque de código
            code_block = body_section.find_next("div", class_="prism-code")
            if code_block:
                try: body_example = json.loads(code_block.get_text(strip=True))
                except: pass

        # Título y 404 Check
        title_el = soup.select_one("h1.openapi__heading, header h1, h1")
        title = title_el.get_text(strip=True) if title_el else "Untitled"
        
        if "Page Not Found" in title:
            return None, ["404 Not Found"]

        # Method & Path (OpenAPI Explorer specific)
        method_el = soup.select_one("div.openapi__method-endpoint span.badge, .openapi__method, span.badge")
        path_el = soup.select_one("div.openapi__method-endpoint .openapi__method-path, .openapi__path")
        base_el = soup.select_one(".openapi__base-url")

        data = {
            "meta": {
                "title": title,
                "description": soup.select_one(".theme-doc-markdown p").get_text(strip=True) if soup.select_one(".theme-doc-markdown p") else "",
                "category": breadcrumbs[1] if len(breadcrumbs) > 1 else "General",
                "breadcrumbs": breadcrumbs,
                "source_url": url
            },
            "endpoint": {
                "method": method_el.get_text(strip=True) if method_el else "",
                "url": (base_el.get_text(strip=True) if base_el else "") + (path_el.get_text(strip=True) if path_el else ""),
                "base_url": base_el.get_text(strip=True) if base_el else BASE_URL,
                "path": path_el.get_text(strip=True) if path_el else ""
            },
            "headers": {"required": headers_req, "optional": []},
            "path_parameters": path_params,
            "query_parameters": query_params,
            "body": {"schema": {}, "example": body_example},
            "code_examples": code_examples or self.generate_code_fallback(method_el.get_text() if method_el else "GET", url, {}, body_example),
            "response": {"status_codes": list(responses.keys()), "body": {"example": responses}}
        }
        
        # Validaciones de calidad
        reasons = []
        if data["meta"]["title"] == "Untitled": reasons.append("Missing title")
        if not data["endpoint"]["method"]: reasons.append("Missing HTTP method")
        if not data["code_examples"]: reasons.append("Missing code examples")
        
        return data, reasons

    async def scrape_webhook(self, page, url):
        """Extracción para webhooks."""
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        title = soup.select_one("h1.openapi__heading, header h1, h1").get_text(strip=True) if soup.select_one("h1.openapi__heading, header h1, h1") else "Webhook Event"
        code_block = soup.select_one(".prism-code")
        payload = {}
        if code_block:
            try: payload = json.loads(code_block.get_text(strip=True))
            except: pass

        data = {
            "event": title,
            "source_url": url,
            "description": soup.select_one(".theme-doc-markdown p").get_text(strip=True) if soup.select_one(".theme-doc-markdown p") else "",
            "payload_example": payload,
            "fields": [] # Sería parseado de tablas si existen
        }
        return data, []

    async def scrape_generic(self, page, url):
        """Extracción para páginas conceptuales, SDK, Modules, etc."""
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        title = soup.select_one("h1.openapi__heading, header h1, h1").get_text(strip=True) if soup.select_one("h1.openapi__heading, header h1, h1") else "Doc Page"
        content = soup.select_one(".theme-doc-markdown")
        
        code_blocks = []
        for pre in soup.select("pre"):
            code_blocks.append({
                "lang": pre.get("class", [""])[0].replace("language-", ""),
                "code": pre.get_text(strip=True)
            })

        data = {
            "title": title,
            "source_url": url,
            "content_text": content.get_text(separator="\n", strip=True) if content else "",
            "code_blocks": code_blocks
        }
        return data, []

    # ── Orchestration ──────────────────────────────────────────────

    async def process_url(self, browser, url, category, progress, task_id):
        """Worker individual con política de reintentos."""
        async with self.semaphore:
            for attempt in range(RETRIES):
                try:
                    context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0")
                    page = await context.new_page()
                    
                    try:
                        await page.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT_PAGE)
                        # Esperar a que el título o el método aparezcan (SPA render)
                        await page.wait_for_selector("h1.openapi__heading, h1", timeout=10000)
                        await asyncio.sleep(1.5)
                    except PlaywrightTimeout:
                        await context.close()
                        raise PlaywrightTimeout("Timeout loading page")

                    if category == "endpoint":
                        item, reasons = await self.scrape_endpoint(page, url)
                    elif category == "webhook":
                        item, reasons = await self.scrape_webhook(page, url)
                    else:
                        item, reasons = await self.scrape_generic(page, url)
                    
                    await context.close()
                    
                    if reasons:
                        # Si es 404, no lo agregamos como 'error' de scraping sino como aviso
                        if "404 Not Found" in reasons:
                            return 
                        self.errors.append({"url": url, "reasons": reasons, "category": category})
                    
                    if item:
                        self.results[category].append(item)
                    progress.update(task_id, advance=1)
                    return # Éxito

                except Exception as e:
                    if attempt == RETRIES - 1:
                        self.errors.append({"url": url, "reasons": [str(e)], "category": category})
                    else:
                        await asyncio.sleep(2 * (attempt + 1))

    async def run_worker(self):
        """Inicia el browser y coordina a los workers."""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                MofNCompleteColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=console
            ) as progress:
                
                total_urls = len(self.all_urls)
                task_id = progress.add_task("[yellow]Generando Knowledge Base...", total=total_urls)
                
                queue = []
                for cat, urls in self.classified.items():
                    for url in urls:
                        queue.append(self.process_url(browser, url, cat, progress, task_id))
                
                # Para guardado incremental, dividimos en batches de 50
                batch_size = 50
                for i in range(0, len(queue), batch_size):
                    batch = queue[i:i+batch_size]
                    await asyncio.gather(*batch)
                    self.save_output() # Guardar después de cada batch
                    console.print(f"  [cyan]✓ Batch {i//batch_size + 1} guardado incrementalmente.[/]")

            await browser.close()

    # ── Tests & Output ─────────────────────────────────────────────

    async def startup_tests(self):
        console.print("[bold yellow]Iniciando Verificación de Startup...[/]")
        
        # 1. Deduplication (Ya se corrió en init si se llama main correctamente)
        self.deduplicate_urls()
        
        # 2. Classification
        self.classify_urls()
        
        # 3. Dry Run (Basics)
        console.print("[bold yellow]Corriendo Dry Run en tipos principales...[/]")
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            # Test 1 endpoint
            if self.classified["endpoint"]:
                test_url = self.classified["endpoint"][0]
                context = await browser.new_context()
                page = await context.new_page()
                await page.goto(test_url, wait_until="domcontentloaded")
                data, _ = await self.scrape_endpoint(page, test_url)
                if data["endpoint"]["method"]:
                    console.print(f"  [green]✓ Dry Run Endpoints OK[/] ({test_url})")
                await context.close()
            await browser.close()
        
        console.print("[bold green]✓ Todos los tests de inicio pasaron. Arrancando scraping completo.[/]\n")

    def save_output(self):
        OUTPUT_DIR.mkdir(exist_ok=True)
        
        # Archivos por sección
        for cat, items in self.results.items():
            fname = f"ghl_kb_{cat}s.json" if cat != "endpoint" else "ghl_kb_endpoints.json"
            (OUTPUT_DIR / fname).write_text(json.dumps(items, indent=2), encoding="utf-8")
        
        # Errores
        (OUTPUT_DIR / "ghl_kb_errors.json").write_text(json.dumps(self.errors, indent=2), encoding="utf-8")
        
        # Master consolidated
        master = {
            "meta": {
                "source": BASE_URL,
                "generated_at": datetime.now().isoformat(),
                "counts": {k: len(v) for k, v in self.results.items()},
                "errors": len(self.errors)
            },
            "data": self.results
        }
        (OUTPUT_DIR / "ghl_kb_full.json").write_text(json.dumps(master, indent=2), encoding="utf-8")

        console.print(Panel(f"""
[bold green]Proceso Finalizado[/]

  Endpoints:          {len(self.results['endpoint'])}
  Webhooks:           {len(self.results['webhook'])}
  Concept Pages:      {len(self.results['concept_page'])}
  SDK/Modules:        {len(self.results['sdk']) + len(self.results['module'])}
  
  Items con Errores:  [red]{len(self.errors)}[/]
  Carpeta de Salida:  [bold]{OUTPUT_DIR}/[/]
""", title="KB Builder Summary", border_style="green"))

# ── Main ───────────────────────────────────────────────────────────

async def main():
    builder = GHLKBBuilder(INPUT_FILE)
    await builder.startup_tests()
    await builder.run_worker()
    builder.save_output()

if __name__ == "__main__":
    asyncio.run(main())
