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
OUTPUT_DIR = Path("ghl_kb_output_pro")
MAX_CONCURRENCY = 3 # Reducido ligeramente para evitar colisiones de foco en clics
RETRIES = 3
TIMEOUT_PAGE = 60000  # ms
# ─────────────────────────────────────────────────────────────────

console = Console()

class GHLDeepScraper:
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

    def deduplicate_urls(self):
        if not self.urls_file.exists():
            console.print(f"[bold red]Error:[/] {self.urls_file} no encontrado.")
            return False
        raw_urls = self.urls_file.read_text().splitlines()
        hash_pattern = re.compile(r'(.+)-[a-f0-9]{3}$')
        seen_canonical = {}
        for url in raw_urls:
            url = url.strip().rstrip("/")
            if not url or url == f"{BASE_URL}/docs" or url == f"{BASE_URL}/docs/":
                continue
            match = hash_pattern.match(url)
            if match:
                canonical = match.group(1)
                if canonical not in seen_canonical: seen_canonical[canonical] = url
            else:
                seen_canonical[url] = url
        self.all_urls = sorted(list(set(seen_canonical.values())))
        return True

    def classify_urls(self):
        for url in self.all_urls:
            url_clean = url.strip().rstrip("/")
            parsed = urlparse(url_clean)
            path = parsed.path
            
            # Webhooks
            if "/webhooks" in path.lower():
                self.classified["webhook"].append(url)
                continue
            
            # SDKs
            if "/sdk/" in path.lower():
                self.classified["sdk"].append(url)
                continue

            # Policies
            if "/MarketplacePolicies/" in path.lower():
                self.classified["policy"].append(url)
                continue

            # Modules
            if "/marketplace-modules/" in path.lower():
                self.classified["module"].append(url)
                continue

            # Concept Pages
            concept_keywords = ["oauth-2-0", "api-basics", "concepts", "authorization", "rate-limits", "changelog"]
            if any(kw in path.lower() for kw in concept_keywords):
                self.classified["concept_page"].append(url)
                continue
            
            # Module Intro Pages (special case: ends in the same name as category or category-api)
            # marketplace.gohighlevel.com/docs/ghl/agent-studio/agent-studio-apis
            pts = [p for p in path.split("/") if p]
            if len(pts) >= 2:
                cat_name = pts[-2]
                page_name = pts[-1]
                if page_name == cat_name or page_name == f"{cat_name}-api" or page_name == f"{cat_name}-apis" or page_name == "introduction":
                    self.classified["module"].append(url)
                    continue

            # Default is Endpoint
            self.classified["endpoint"].append(url)
        
        console.print("[bold green]URL Classification Summary:[/]")
        for cat, urls in self.classified.items():
            if urls: console.print(f"  [cyan]»[/] {cat}: {len(urls)}")
        return True

    async def get_deep_tabs_data(self, page, tab_list_selector, target_selector, click_delay=0.6, is_response=False):
        """Interactúa con pestañas capturando el contenido que aparece al cliquear.
        Soporta variantes (sub-pestañas) y espera a que el contenido cambie.
        """
        data = {}
        try:
            # Seleccionar los tabs dentro del contenedor dado
            tabs = await page.query_selector_all(f"{tab_list_selector} .tabs__item")
            for i, tab in enumerate(tabs):
                try:
                    label = (await tab.inner_text()).strip()
                    if not label: continue
                    
                    # Usar un timeout corto para que no se bloquee si el tab no es cliqueable/visible
                    await tab.click(timeout=2000)
                    await asyncio.sleep(click_delay) 
                    
                    # Manejar variantes de código (ej. NodeJS -> AXIOS, SDK, etc)
                    variant_tabs = await page.query_selector_all(".openapi-tabs__code-item--variant")
                    if variant_tabs and not is_response:
                        variants = {}
                        for v_tab in variant_tabs:
                            try:
                                v_label = (await v_tab.inner_text()).strip()
                                await v_tab.click(timeout=1000)
                                await asyncio.sleep(0.3)
                                v_content_el = await page.query_selector(target_selector)
                                if v_content_el:
                                    variants[v_label] = await v_content_el.inner_text()
                            except: continue
                        data[label] = variants
                    else:
                        # Si es respuesta, intentar forzar 'Example' en lugar de 'Schema'
                        if is_response:
                            example_tab = await page.query_selector("li.openapi-tabs__schema-item:has-text('Example')")
                            if example_tab and await example_tab.is_visible():
                                try: await example_tab.click(timeout=1000)
                                except: pass
                                await asyncio.sleep(0.3)
                            
                        content_el = await page.query_selector(target_selector)
                        if content_el:
                            data[label] = await content_el.inner_text()
                            
                except Exception as e:
                    # Si falla un tab, logueamos brevemente y seguimos con el siguiente
                    pass
        except Exception:
            pass
        return data

    async def scrape_endpoint_pro(self, page, url):
        """Versión Profunda: Scopes, Múltiples Lenguajes, Múltiples Respuestas."""
        
        # 0. Capturar Breadcrumbs para categorización
        breadcrumbs = await page.evaluate("""() => {
            return Array.from(document.querySelectorAll('.breadcrumbs__link')).map(el => el.innerText.trim());
        }""")

        # 1. Expandir todos los detalles de parámetros y seguridad
        await page.evaluate("""() => {
            document.querySelectorAll('details:not([open])').forEach(d => d.setAttribute('open', ''));
        }""")
        await asyncio.sleep(1)

        # 2. Capturar Seguridad (Scopes, Auth)
        security_html = await page.query_selector(".openapi-security__details")
        security_info = await security_html.inner_text() if security_html else "N/A"

        # 3. Capturar Todas las Respuestas (Status Codes + Ejemplos)
        response_data = await self.get_deep_tabs_data(page, ".openapi-tabs__response-list-container.tabs", "pre.prism-code.language-json", click_delay=0.5, is_response=True)

        # 4. Capturar Todos los lenguajes de código
        # Manejo de la 'flecha' si existe para revelar más tabs (NodeJS, etc)
        for _ in range(3): # Intentar clickear la flecha varias veces por si acaso
            # Manejo de la 'flecha' si existe para revelar más tabs (SDKs que no se ven a simple vista)
            arrow = await page.query_selector(".tabs-scrollbar-button--right")
            if arrow and await arrow.is_visible(): 
                try: 
                    await arrow.click(timeout=1000)
                    await asyncio.sleep(0.3)
                except:
                    pass
        
        code_examples = await self.get_deep_tabs_data(page, ".openapi-tabs__code-list-container", "pre.openapi-explorer__code-block", click_delay=0.8)

        # 5. Parsear el resto con BeautifulSoup para mayor precisión en tablas
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        title_el = soup.select_one("h1.openapi__heading, h1")
        title = title_el.get_text(strip=True) if title_el else "Untitled"
        if not breadcrumbs and title_el:
            # Fallback if eval failed
            breadcrumbs = [title]

        if "Page Not Found" in title: return None, ["404"]

        # Intentar obtener el path directamente del contenedor superior
        method_endpoint_el = soup.select_one(".openapi__method-endpoint")
        if method_endpoint_el:
            method_el = method_endpoint_el.select_one(".badge")
            # El path está en un h2 con clase .openapi__method-endpoint-path
            endpoint_el = method_endpoint_el.select_one(".openapi__method-endpoint-path")
        else:
            method_el = soup.select_one(".openapi-explorer__method, .badge")
            endpoint_el = soup.select_one(".openapi-explorer__url, .openapi__path, .openapi__method-endpoint-path")
            
        base_el = soup.select_one(".openapi__base-url")

        # Extraer parámetros de forma estructurada
        params = {"header": [], "path": [], "query": [], "body": {}}
        
        # El sitio usa .openapi-markdown__details para agrupar secciones (Header, Query, etc)
        details_blocks = soup.select("details.openapi-markdown__details")
        for block in details_blocks:
            summary = block.select_one("summary")
            if not summary: continue
            section_text = summary.get_text(strip=True).lower()
            
            # Cada parámetro suele estar en un div que contiene a un strong.openapi-schema__property
            # IMPORTANTE: A veces los parámetros están en una tabla, a veces en divs.
            param_names = block.select("strong.openapi-schema__property, .openapi-schema__property")
            
            if not param_names:
                # Fallback a tabla si no hay schema containers
                rows = block.select("table tr")
                for row in rows:
                    cols = row.select("td")
                    if len(cols) < 2: continue
                    p_name = cols[0].get_text(strip=True)
                    p_desc = cols[1].get_text(separator=" ", strip=True)
                    p_type = ""
                    if ":" in p_name: 
                        parts = p_name.split(":")
                        p_name = parts[0]
                        p_type = parts[1]
                    
                    p_required = "required" in p_name.lower() or "required" in p_desc.lower()
                    item_data = {"name": p_name.replace("required", "").strip(), "type": p_type, "required": p_required, "details": p_desc}
                    
                    if "header" in section_text: params["header"].append(item_data)
                    elif "path" in section_text: params["path"].append(item_data)
                    elif "query" in section_text: params["query"].append(item_data)
            else:
                for p_name_el in param_names:
                    p_container = p_name_el.parent
                    p_type_el = p_container.select_one(".openapi-schema__name")
                    
                    p_name = p_name_el.get_text(strip=True)
                    p_type = p_type_el.get_text(strip=True) if p_type_el else ""
                    
                    # La descripción suele estar en el siguiente div hermano del contenedor del container
                    p_parent = p_container.parent
                    desc_el = p_parent.find_next_sibling("div")
                    p_desc = desc_el.get_text(separator=" ", strip=True) if desc_el else ""
                    
                    p_required = "required" in p_name.lower() or "required" in p_desc.lower()
                    
                    item_data = {
                        "name": p_name.replace("required", "").strip(), 
                        "type": p_type,
                        "required": p_required, 
                        "details": p_desc
                    }
                    
                    if "header" in section_text: params["header"].append(item_data)
                    elif "path" in section_text: params["path"].append(item_data)
                    elif "query" in section_text: params["query"].append(item_data)
                    elif "body" in section_text or "payload" in section_text:
                        if "fields" not in params["body"]: params["body"]["fields"] = []
                        params["body"]["fields"].append(item_data)

        # Body Schema (Request)
        body_section = soup.find(re.compile(r"h[34]"), string=re.compile(r"Request Body", re.I))
        if body_section:
            code_block = body_section.find_next("div", class_="prism-code")
            if code_block:
                try: params["body"] = {"example": json.loads(code_block.get_text(strip=True))}
                except: params["body"] = {"example": code_block.get_text(strip=True)}

        data = {
            "meta": {
                "title": title,
                "category": breadcrumbs[1] if len(breadcrumbs) > 1 else "General",
                "breadcrumbs": breadcrumbs,
                "source_url": url,
                "security": security_info
            },
            "endpoint": {
                "method": method_el.get_text(strip=True) if method_el else "UNK",
                "url": (base_el.get_text(strip=True) if base_el else "") + (endpoint_el.get_text(strip=True) if endpoint_el else ""),
            },
            "parameters": params,
            "code_examples": code_examples,
            "responses": response_data
        }
        return data, []

    async def process_url(self, browser, url, category, progress, task_id):
        # logging simple para ver progreso si la barra rich se congela
        console.print(f"[dim][*] Iniciando {url}...[/]")
        async with self.semaphore:
            for attempt in range(RETRIES):
                try:
                    context = await browser.new_context(viewport={'width': 1280, 'height': 800})
                    page = await context.new_page()
                    await page.goto(url, wait_until="domcontentloaded", timeout=TIMEOUT_PAGE)
                    
                    # Detectar 'This page crashed' o errores de hidratación de React/Docusaurus
                    content_check = await page.content()
                    if "This page crashed" in content_check or "Something went wrong" in content_check:
                        console.print(f"[yellow]  [!] Hydration crash detected on {url}. Reloading...[/]")
                        await page.reload(wait_until="domcontentloaded")
                        await asyncio.sleep(2)

                    # Esperar renderizado SPA más inteligente
                    if category == "endpoint":
                        try:
                            await page.wait_for_selector(".openapi-explorer__method, h1", timeout=15000)
                        except:
                            # Si falla el selector de endpoint, quizás es una página de intro mal clasificada
                            await page.wait_for_selector("h1", timeout=10000)
                    else:
                        await page.wait_for_selector("h1", timeout=15000)
                    
                    await asyncio.sleep(1.5)

                    if category == "endpoint":
                        item, reasons = await self.scrape_endpoint_pro(page, url)
                    elif category == "webhook":
                        item, reasons = await self.scrape_webhook_pro(page, url)
                    else:
                        item, reasons = await self.scrape_generic_pro(page, url)
                    
                    await context.close()
                    if item: 
                        self.results[category].append(item)
                        self.save_incremental() # Guardar después de cada URL exitosa
                    progress.update(task_id, advance=1)
                    return
                except Exception as e:
                    if attempt == RETRIES - 1: self.errors.append({"url": url, "error": str(e)})
                    else: await asyncio.sleep(3)

    async def scrape_webhook_pro(self, page, url):
        """Específico para Webhooks de GHL."""
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Selectores obtenidos del análisis visual
        category_el = soup.select_one("article h1")
        category = category_el.get_text(strip=True) if category_el else "Unknown"
        
        event_name_el = soup.select(".breadcrumbs__item")
        event_name = event_name_el[-1].get_text(strip=True) if event_name_el else "Unknown"
        
        description_el = soup.select_one("article h1 + p")
        description = description_el.get_text(strip=True) if description_el else ""
        
        # Extraer Schema y Example
        schema_code = ""
        schema_header = soup.find("h4", id="schema")
        if schema_header:
            code_el = schema_header.find_next("code")
            if code_el: schema_code = code_el.get_text(strip=True)
            
        example_code = ""
        example_header = soup.find("h4", id="example")
        if example_header:
            code_el = example_header.find_next("code")
            if code_el: example_code = code_el.get_text(strip=True)

        data = {
            "title": f"Webhook: {event_name}",
            "source_url": url,
            "category": category,
            "event_type": event_name,
            "description": description,
            "payload_schema": schema_code,
            "payload_example": example_code
        }
        return data, []

    async def scrape_generic_pro(self, page, url):
        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one("h1").get_text(strip=True) if soup.select_one("h1") else "Document"
        content = soup.select_one(".theme-doc-markdown")
        
        # Capturar todos los pre/code con lenguaje
        code_blocks = []
        for pre in soup.select("pre"):
            code_blocks.append({
                "lang": pre.get("class", [""])[0].replace("language-", ""),
                "code": pre.get_text(strip=True)
            })

        data = {
            "title": title,
            "source_url": url,
            "content": content.get_text(separator="\n", strip=True) if content else "",
            "code_blocks": code_blocks
        }
        return data, []

    async def run(self):
        self.deduplicate_urls()
        self.classify_urls()
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                MofNCompleteColumn(),
                TimeElapsedColumn(),
                console=console
            ) as progress:
                
                total_urls = len(self.all_urls)
                task_id = progress.add_task("[yellow]Deep Scraping GHL...", total=total_urls)
                
                tasks = []
                for cat, urls in self.classified.items():
                    for url in urls:
                        tasks.append(self.process_url(browser, url, cat, progress, task_id))
                
                # Al usar gather con todas las tareas, el Semaphore controla la concurrencia real
                await asyncio.gather(*tasks)

            await browser.close()

    def save_incremental(self):
        OUTPUT_DIR.mkdir(exist_ok=True)
        master = {
            "generated_at": datetime.now().isoformat(),
            "data": self.results
        }
        (OUTPUT_DIR / "ghl_kb_pro_v7_final.json").write_text(json.dumps(master, indent=2), encoding="utf-8")

if __name__ == "__main__":
    scraper = GHLDeepScraper(INPUT_FILE)
    asyncio.run(scraper.run())
