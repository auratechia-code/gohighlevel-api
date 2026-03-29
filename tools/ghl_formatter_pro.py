import json
import os
import re
from pathlib import Path
from rich.console import Console

console = Console()

class GHLFormatterPro:
    def __init__(self, json_file: str, output_base: str = "ghl_docs_pro"):
        self.json_file = Path(json_file)
        self.output_base = Path(output_base)
        self.data = {}
        
    def load_data(self):
        if not self.json_file.exists():
            console.print(f"[red]Error:[/] {self.json_file} no encontrado.")
            return False
        self.data = json.loads(self.json_file.read_text(encoding="utf-8"))
        return True

    def sanitize_filename(self, name):
        name = name.lower().replace(" ", "-").replace("/", "-").replace(":", "")
        return re.sub(r'[^a-zA-Z0-9.\-_]', '', name)

    def generate_markdown_endpoint(self, item):
        title = item["meta"]["title"]
        method = item["endpoint"]["method"]
        url = item["endpoint"]["url"]
        
        md = f"# {title}\n\n"
        md += f"**Method:** `{method}` | **URL:** `{url}`\n\n"
        
        # Requirements
        md += "## 🔐 Requirements\n"
        md += f"```text\n{item['meta'].get('security', 'N/A')}\n```\n\n"
        
        # Parameters Table
        md += "## 📥 Parameters\n"
        for p_type in ["path", "query", "header"]:
            params_list = item["parameters"].get(p_type, [])
            if params_list:
                md += f"### {p_type.capitalize()} Parameters\n"
                md += "| Name | Required | Description |\n"
                md += "| :--- | :--- | :--- |\n"
                for p in params_list:
                    req = "✅" if p.get("required") else "❌"
                    md += f"| `{p['name']}` | {req} | {p['details']} |\n"
                md += "\n"

        # Body Schema (Request)
        body = item["parameters"].get("body", {})
        if body and "example" in body:
            md += "### 📦 Request Body\n"
            md += f"```json\n{json.dumps(body['example'], indent=2)}\n```\n\n"

        # Response Examples
        md += "## 📤 Responses\n"
        for code, content in item.get("responses", {}).items():
            md += f"<details>\n<summary>Response {code}</summary>\n\n"
            md += f"```json\n{content}\n```\n</details>\n\n"

        # Code Examples (ALL LANGUAGES)
        md += "## 💻 Code Examples\n\n"
        for lang, content in item.get("code_examples", {}).items():
            lang_slug = lang.lower().replace(" ", "")
            md += f"### {lang}\n"
            if isinstance(content, dict):
                for variant, variant_code in content.items():
                    md += f"#### {variant}\n"
                    md += f"```{lang_slug}\n{variant_code}\n```\n\n"
            else:
                md += f"```{lang_slug}\n{content}\n```\n\n"

        return md

    def generate_markdown_webhook(self, item):
        title = item["title"]
        category = item["category"]
        event_type = item["event_type"]
        description = item["description"]
        
        md = f"# {title}\n\n"
        md += f"**Category:** `{category}` | **Event Type:** `{event_type}`\n\n"
        md += f"{description}\n\n"
        
        if item.get("payload_schema"):
            md += "## 📐 Payload Schema\n"
            md += f"```json\n{item['payload_schema']}\n```\n\n"
            
        if item.get("payload_example"):
            md += "## 📦 Payload Example\n"
            md += f"```json\n{item['payload_example']}\n```\n\n"
            
        md += f"**Source:** [GHL Documentation]({item['source_url']})\n"
        return md

    def generate_markdown_generic(self, item):
        title = item["title"]
        content = item["content"]
        
        md = f"# {title}\n\n"
        md += f"{content}\n\n"
        
        if item.get("code_blocks"):
            md += "## 💻 Code Snippets\n\n"
            for cb in item["code_blocks"]:
                lang = cb["lang"] if cb["lang"] else "text"
                md += f"```{lang}\n{cb['code']}\n```\n\n"
                
        md += f"**Source:** [GHL Documentation]({item['source_url']})\n"
        return md

    def format_all(self):
        self.output_base.mkdir(exist_ok=True)
        counts = {"endpoints": 0, "webhooks": 0, "concepts": 0}
        
        # 1. Procesar Endpoints
        endpoint_base = self.output_base / "endpoints"
        endpoint_base.mkdir(exist_ok=True)
        for item in self.data.get("data", {}).get("endpoint", []):
            try:
                cat_name = self.sanitize_filename(item["meta"].get("category", "general"))
                cat_dir = endpoint_base / cat_name
                cat_dir.mkdir(exist_ok=True)
                filename = self.sanitize_filename(item["meta"]["title"]) + ".md"
                (cat_dir / filename).write_text(self.generate_markdown_endpoint(item), encoding="utf-8")
                counts["endpoints"] += 1
            except Exception: pass

        # 2. Procesar Webhooks
        webhook_base = self.output_base / "webhooks"
        webhook_base.mkdir(exist_ok=True)
        for item in self.data.get("data", {}).get("webhook", []):
            try:
                cat_name = self.sanitize_filename(item.get("category", "general"))
                cat_dir = webhook_base / cat_name
                cat_dir.mkdir(exist_ok=True)
                filename = self.sanitize_filename(item["title"]) + ".md"
                (cat_dir / filename).write_text(self.generate_markdown_webhook(item), encoding="utf-8")
                counts["webhooks"] += 1
            except Exception: pass

        # 3. Procesar Conceptos y Otros
        concept_base = self.output_base / "concepts"
        concept_base.mkdir(exist_ok=True)
        for category in ["concept_page", "sdk", "module", "policy"]:
            for item in self.data.get("data", {}).get(category, []):
                try:
                    filename = self.sanitize_filename(item["title"]) + ".md"
                    (concept_base / filename).write_text(self.generate_markdown_generic(item), encoding="utf-8")
                    counts["concepts"] += 1
                except Exception: pass
        
        console.print(f"[bold green]✓ Formateo Finalizado.[/]")
        console.print(f"   [cyan]Endpoints:[/] {counts['endpoints']}")
        console.print(f"   [cyan]Webhooks:[/] {counts['webhooks']}")
        console.print(f"   [cyan]Conceptos:[/] {counts['concepts']}")

if __name__ == "__main__":
    INPUT_FILE = "ghl_kb_output_pro/ghl_kb_pro_v7_final.json"
    OUTPUT_DIR = Path("ghl_docs_pro")
    formatter = GHLFormatterPro(INPUT_FILE, OUTPUT_DIR)
    if formatter.load_data():
        formatter.format_all()
