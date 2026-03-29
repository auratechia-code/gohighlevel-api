import json
import os
from pathlib import Path
from datetime import datetime

# ── Config ────────────────────────────────────────────────────────
INPUT_FILE = Path("ghl_kb_output/ghl_kb_full.json")
OUTPUT_DIR = Path("ghl_kb_reference")
# ─────────────────────────────────────────────────────────────────

class GHLKBFormatter:
    def __init__(self, input_json: Path, output_dir: Path):
        self.input_json = input_json
        self.output_dir = output_dir
        self.data = {}
        self.summary = []

    def load_data(self):
        if not self.input_json.exists():
            print(f"Error: {self.input_json} no encontrado.")
            return False
        with open(self.input_json, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        return True

    def create_frontmatter(self, title, source_url, tags=[]):
        fm = "---\n"
        fm += f"title: \"{title}\"\n"
        fm += f"source: \"{source_url}\"\n"
        fm += f"generated_at: \"{datetime.now().isoformat()}\"\n"
        if tags:
            fm += f"tags: {json.dumps(tags)}\n"
        fm += "---\n\n"
        return fm

    def format_params_table(self, params, title):
        if not params:
            return ""
        md = f"### {title}\n\n"
        md += "| Name | Description |\n"
        md += "| :--- | :--- |\n"
        for p in params:
            md += f"| `{p.get('name', 'N/A')}` | {p.get('description', 'No description')} |\n"
        md += "\n"
        return md

    def format_endpoint(self, item):
        meta = item.get("meta", {})
        ep = item.get("endpoint", {})
        
        md = self.create_frontmatter(meta.get("title"), meta.get("source_url"), tags=["api", "endpoint", ep.get("method")])
        md += f"# {meta.get('title')}\n\n"
        md += f"{meta.get('description', '')}\n\n"
        
        md += f"## Endpoint Information\n\n"
        md += f"> [!IMPORTANT]\n"
        md += f"> **Method:** `{ep.get('method')}`  \n"
        md += f"> **URL:** `{ep.get('url')}`\n\n"
        
        # Parameters
        md += self.format_params_table(item.get("path_parameters"), "Path Parameters")
        md += self.format_params_table(item.get("query_parameters"), "Query Parameters")
        md += self.format_params_table(item.get("headers", {}).get("required"), "Required Headers")
        
        # Request Body
        body = item.get("body", {})
        if body.get("example"):
            md += "### Request Body Example\n\n"
            md += "```json\n"
            md += json.dumps(body.get("example"), indent=2) + "\n"
            md += "```\n\n"
            
        # Code Examples (Using Markdown headers as separators)
        examples = item.get("code_examples", {})
        if examples:
            md += "## Code Examples\n\n"
            for lang, code in examples.items():
                md += f"#### {lang.upper()}\n"
                md += f"```{'javascript' if lang == 'nodejs' else lang}\n"
                md += code + "\n"
                md += "```\n\n"
                
        # Response
        resp = item.get("response", {})
        if resp.get("body", {}).get("example"):
            md += "## Response\n\n"
            for status, body_ex in resp.get("body", {}).get("example").items():
                md += f"### HTTP {status}\n"
                md += "```json\n"
                md += body_ex + "\n"
                md += "```\n\n"
                
        return md

    def format_webhook(self, item):
        title = item.get("event", "Webhook Event")
        md = self.create_frontmatter(title, item.get("source_url"), tags=["webhook", "event"])
        md += f"# Webhook: {title}\n\n"
        md += f"{item.get('description', '')}\n\n"
        
        if item.get("payload_example"):
            md += "## Payload Example\n\n"
            md += "```json\n"
            md += json.dumps(item.get("payload_example"), indent=2) + "\n"
            md += "```\n"
        return md

    def format_generic(self, item):
        title = item.get("title", "Documentation Page")
        md = self.create_frontmatter(title, item.get("source_url"), tags=["docs", "concept"])
        md += f"# {title}\n\n"
        md += item.get("content_text", "")
        
        if item.get("code_blocks"):
            md += "\n\n## Code Snippets\n\n"
            for block in item.get("code_blocks"):
                lang = block.get("lang", "")
                md += f"```{lang}\n"
                md += block.get("code", "") + "\n"
                md += "```\n\n"
        return md

    def sanitize_filename(self, name):
        """Sanitiza nombres de archivo para Windows."""
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            name = name.replace(char, "")
        return name.strip().lower().replace(" ", "-")

    def process(self):
        if not self.load_data():
            return
            
        self.output_dir.mkdir(exist_ok=True)
        
        sections = self.data.get("data", {})
        for cat, items in sections.items():
            if not items: continue
            
            cat_dir = self.output_dir / f"{cat}s"
            cat_dir.mkdir(exist_ok=True)
            
            # Sub-carpetas por recurso para endpoints
            for item in items:
                try:
                    if cat == "endpoint":
                        # Intentar sacar el recurso del path (ej. /ghl/contacts/ -> contacts)
                        path_parts = item.get("endpoint", {}).get("path", "").split("/")
                        resource = path_parts[2] if len(path_parts) > 2 else "general"
                        resource_dir = cat_dir / resource
                        resource_dir.mkdir(exist_ok=True)
                        
                        title = item.get("meta", {}).get("title", "endpoint")
                        filename = self.sanitize_filename(title) + ".md"
                        content = self.format_endpoint(item)
                        (resource_dir / filename).write_text(content, encoding="utf-8")
                        self.summary.append((cat, resource, title, f"{cat}s/{resource}/{filename}"))

                    elif cat == "webhook":
                        event = item.get("event", "webhook")
                        filename = self.sanitize_filename(event) + ".md"
                        content = self.format_webhook(item)
                        (cat_dir / filename).write_text(content, encoding="utf-8")
                        self.summary.append((cat, None, event, f"{cat}s/{filename}"))
                        
                    else:
                        title = item.get("title", "page")
                        filename = self.sanitize_filename(title) + ".md"
                        content = self.format_generic(item)
                        (cat_dir / filename).write_text(content, encoding="utf-8")
                        self.summary.append((cat, None, title, f"{cat}s/{filename}"))
                except Exception as e:
                    print(f"Error procesando {cat}: {str(e)}")

        self.generate_index()

    def generate_index(self):
        md = "# GoHighLevel Documentation Index\n\n"
        md += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Agrupar por categoría
        grouped = {}
        for cat, res, title, path in self.summary:
            if cat not in grouped: grouped[cat] = {}
            if res not in grouped[cat]: grouped[cat][res] = []
            grouped[cat][res].append((title, path))
            
        for cat, resources in grouped.items():
            md += f"## {cat.capitalize()}s\n"
            for res, items in resources.items():
                if res:
                    md += f"### {res.capitalize()}\n"
                for title, path in items:
                    md += f"* [{title}]({path})\n"
                md += "\n"
                
        (self.output_dir / "SUMMARY.md").write_text(md, encoding="utf-8")
        (self.output_dir / "README.md").write_text(md, encoding="utf-8")
        print(f"✓ Formateado completado en {self.output_dir}/")

if __name__ == "__main__":
    formatter = GHLKBFormatter(INPUT_FILE, OUTPUT_DIR)
    formatter.process()
