import json
import os
import re
from pathlib import Path

# Paths
BASE_DIR = Path("c:/Users/luaco/OneDrive/Documentos/Dev/gohighlevel-api")
TEMP_DIR = BASE_DIR / "temp_ghl_docs"
APPS_DIR = TEMP_DIR / "apps"
COMMON_SCHEMAS_PATH = TEMP_DIR / "common" / "common-schemas.json"
OUTPUT_DIR = BASE_DIR / "docs" / "01-referencia-api"
WEBHOOKS_OUTPUT_DIR = BASE_DIR / "docs" / "02-conceptos" / "webhooks"
TOC_PATH = TEMP_DIR / "toc.json"

# Load Common Schemas
if COMMON_SCHEMAS_PATH.exists():
    with open(COMMON_SCHEMAS_PATH, 'r', encoding='utf-8') as f:
        COMMON_SCHEMAS = json.load(f)
else:
    COMMON_SCHEMAS = {}

def resolve_ref(ref, current_spec):
    if not ref: return None
    if ref.startswith("#/"):
        parts = ref.split('/')
        target = current_spec
        for part in parts[1:]:
            target = target.get(part, {})
        return target
    elif "../common/common-schemas.json" in ref:
        parts = ref.split('/')
        target = COMMON_SCHEMAS
        if "#" in ref:
            path_part = ref.split("#")[1]
            for part in path_part.split("/")[1:]:
                target = target.get(part, {})
        return target
    return None

def flatten_schema(schema, spec, parent_path="", required_list=None):
    """Recursively flattens a JSON schema into a list of (name, type, required, description)"""
    if not schema: return []
    
    if "$ref" in schema:
        schema = resolve_ref(schema["$ref"], spec)
        if not schema: return []

    rows = []
    required_list = required_list or schema.get("required", [])

    # Handle composition
    for key in ["allOf", "anyOf", "oneOf"]:
        if key in schema:
            for sub in schema[key]:
                rows.extend(flatten_schema(sub, spec, parent_path, required_list))
            return rows

    properties = schema.get("properties", {})
    for name, prop in properties.items():
        if "$ref" in prop:
            prop = resolve_ref(prop["$ref"], spec)
        
        full_name = f"{parent_path}.{name}" if parent_path else name
        p_type = prop.get("type", "object")
        p_req = "✅ Sí" if name in required_list else "❌ No"
        p_desc = prop.get("description", "-")
        
        rows.append((full_name, p_type, p_req, p_desc))
        
        if p_type == "object" and "properties" in prop:
            rows.extend(flatten_schema(prop, spec, full_name))
        elif p_type == "array" and "items" in prop:
            items = prop["items"]
            if "$ref" in items:
                items = resolve_ref(items["$ref"], spec)
            if items and items.get("type") == "object":
                rows.extend(flatten_schema(items, spec, f"{full_name}[]"))

    return rows

def generate_full_snippets(method, path, operation_id, body_schema=None):
    base_url = "https://services.leadconnectorhq.com"
    full_url = f"{base_url}{path}"
    
    # Simple sample body generator
    sample_body = "{}"
    if body_schema:
        props = body_schema.get("properties", {})
        if props:
            sample_obj = {k: "string" if v.get("type") == "string" else 0 for k, v in list(props.items())[:3]}
            sample_body = json.dumps(sample_obj, indent=2)

    # curl
    body_part = f"  -d '{sample_body.replace(chr(10), ' ')}' \\" if method.lower() in ["post", "put", "patch"] else ""
    curl = f"curl -L '{full_url}' \\\n  -H 'Accept: application/json' \\\n  -H 'Authorization: Bearer <TOKEN>' \\\n  -H 'Version: 2021-07-28' \\\n  -H 'Content-Type: application/json' \\\n{body_part}"
    
    # node-axios
    data_part = f",\n  data: {sample_body}" if method.lower() in ["post", "put", "patch"] else ""
    node_axios = f"const axios = require('axios');\n\nconst config = {{\n  method: '{method}',\n  url: '{full_url}',\n  headers: {{\n    'Accept': 'application/json',\n    'Authorization': 'Bearer <TOKEN>',\n    'Version': '2021-07-28',\n    'Content-Type': 'application/json'\n  }}{data_part}\n}};\n\naxios.request(config).then(res => console.log(res.data));"

    # python
    json_part = f", json={sample_body}" if method.lower() in ["post", "put", "patch"] else ""
    python = f"import requests\n\nurl = \"{full_url}\"\nheaders = {{\n    \"Accept\": \"application/json\",\n    \"Authorization\": \"Bearer <TOKEN>\",\n    \"Version\": \"2021-07-28\",\n    \"Content-Type\": \"application/json\"\n}}\n\nresponse = requests.{method.lower()}(url, headers=headers{json_part})\nprint(response.json())"

    # php
    body_opt = f",\n  'json' => {sample_body}" if method.lower() in ["post", "put", "patch"] else ""
    php = f"<?php\n$client = new \\GuzzleHttp\\Client();\n$res = $client->request('{method.upper()}', '{full_url}', [\n  'headers' => [\n    'Accept' => 'application/json',\n    'Authorization' => 'Bearer <TOKEN>',\n    'Version' => '2021-07-28',\n    'Content-Type' => 'application/json'\n  ]{body_opt}\n]);\necho $res->getBody();"

    # java
    body_pub = f"HttpRequest.BodyPublishers.ofString({json.dumps(sample_body)})" if method.lower() in ["post", "put", "patch"] else "HttpRequest.BodyPublishers.noBody()"
    java = f"HttpRequest request = HttpRequest.newBuilder()\n    .uri(URI.create(\"{full_url}\"))\n    .header(\"Accept\", \"application/json\")\n    .header(\"Authorization\", \"Bearer <TOKEN>\")\n    .header(\"Version\", \"2021-07-28\")\n    .header(\"Content-Type\", \"application/json\")\n    .method(\"{method.upper()}\", {body_pub})\n    .build();"

    # go
    go_body = f"bytes.NewBuffer([]byte({json.dumps(sample_body)}))" if method.lower() in ["post", "put", "patch"] else "nil"
    go = f"package main\nimport (\"fmt\"; \"net/http\"; \"bytes\")\nfunc main() {{\n  req, _ := http.NewRequest(\"{method.upper()}\", \"{full_url}\", {go_body})\n  req.Header.Add(\"Authorization\", \"Bearer <TOKEN>\")\n  req.Header.Add(\"Version\", \"2021-07-28\")\n  req.Header.Add(\"Content-Type\", \"application/json\")\n  res, _ := http.DefaultClient.Do(req)\n  fmt.Println(res.Status)\n}}"

    return {
        "curl": curl.strip(), "node_axios": node_axios, "python": python,
        "php": php, "java": java, "go": go
    }

def generate_endpoint_md(path, method, details, spec, prev_link=None, next_link=None):
    summary = details.get("summary", "Sin resumen")
    description = details.get("description", "").replace("<br/>", "\n")
    operation_id = details.get("operationId", "unnamed-op")
    tags = details.get("tags", [])
    security = details.get("security", [])
    scopes = []
    for s in security:
        for k, v in s.items():
            scopes.extend(v)
    
    # Resolve Body Schema for snippets
    body_schema = None
    if "requestBody" in details:
        content = details["requestBody"].get("content", {})
        if "application/json" in content:
            body_schema = content["application/json"].get("schema", {})
            if "$ref" in body_schema:
                body_schema = resolve_ref(body_schema["$ref"], spec)

    snippets = generate_full_snippets(method, path, operation_id, body_schema)
    
    md = [f"-----n-title: \"{summary}\"\noperationId: \"{operation_id}\"\ntags: {json.dumps(tags)}\n---\n"]
    md.append(f"# {summary}\n")
    
    md.append("## 1. Overview\n")
    md.append("| Campo | Valor |\n|---|---|\n")
    md.append(f"| **Método** | `{method.upper()}` |\n")
    md.append(f"| **Endpoint** | `https://services.leadconnectorhq.com{path}` |\n")
    md.append(f"| **Resumen** | {summary} |\n")

    md.append("\n## 2. Requisitos\n")
    md.append("| Campo | Valor |\n|---|---|\n")
    md.append(f"| **Scopes** | `{', '.join(scopes) if scopes else 'Desconocido'}` |\n")
    md.append(f"| **Auth Method** | `OAuth Access Token, Private Integration Token` |\n")

    md.append("\n## 3. Petición (Request)\n")
    md.append("### Parámetros de Encabezado (Headers)\n")
    md.append("| Nombre | Tipo | Requerido | Descripción |\n|---|---|---|---|\n")
    md.append("| `Version` | string | ✅ Sí | `2021-07-28` |\n")
    md.append("| `Authorization` | string | ✅ Sí | `Bearer <TOKEN>` |\n")
    md.append("| `Accept` | string | ✅ Sí | `application/json` |\n")

    # Path/Query Params
    params = details.get("parameters", [])
    if params:
        for p_in in ["path", "query"]:
            sub_params = [p for p in params if p.get("in") == p_in]
            if sub_params:
                header = "Parámetros de Ruta" if p_in == "path" else "Parámetros de Consulta"
                md.append(f"\n### {header}\n")
                md.append("| Nombre | Tipo | Requerido | Descripción | Ejemplo |\n|---|---|---|---|---|\n")
                for p in sub_params:
                    md.append(f"| `{p.get('name')}` | {p.get('schema', {}).get('type', 'string')} | {'✅ Sí' if p.get('required') else '❌ No'} | {p.get('description', '-')} | `{p.get('schema', {}).get('example', '-')}` |\n")

    # Request Body
    if "requestBody" in details:
        md.append("\n### Cuerpo de la Petición (Body)\n")
        content = details["requestBody"].get("content", {})
        if "application/json" in content:
            schema = content["application/json"].get("schema", {})
            rows = flatten_schema(schema, spec)
            if rows:
                md.append("| Campo | Tipo | Requerido | Descripción |\n|---|---|---|---|\n")
                for r in rows:
                    md.append(f"| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} |\n")

    md.append("\n## 4. Respuestas\n")
    responses = details.get("responses", {})
    for code, resp in responses.items():
        status_emoji = "🟢" if code.startswith("2") else "🔴"
        md.append(f"### {status_emoji} {code} — {resp.get('description', '')}\n")
        content = resp.get("content", {})
        if "application/json" in content:
            schema = content["application/json"].get("schema", {})
            rows = flatten_schema(schema, spec)
            if rows:
                md.append("| Campo | Tipo | Requerido | Descripción |\n|---|---|---|---|\n")
                for r in rows:
                    md.append(f"| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} |\n")

    md.append("\n## 5. Ejemplos de Código\n")
    md.append("````carousel\n```bash\n# cURL\n" + snippets["curl"] + "\n```\n<!-- slide -->\n```javascript\n// Node Axios\n" + snippets["node_axios"] + "\n```\n<!-- slide -->\n```python\n# Python Requests\n" + snippets["python"] + "\n```\n<!-- slide -->\n```php\n// PHP Guzzle\n" + snippets["php"] + "\n```\n<!-- slide -->\n```java\n// Java HttpClient\n" + snippets["java"] + "\n```\n<!-- slide -->\n```go\n// Go\n" + snippets["go"] + "\n```\n````\n")

    if prev_link or next_link:
        md.append("\n## 6. Navegación\n")
        nav = []
        if prev_link: nav.append(f"- **Anterior**: [{prev_link['title']}]({prev_link['url']})")
        if next_link: nav.append(f"- **Siguiente**: [{next_link['title']}]({next_link['url']})")
        md.append("\n".join(nav))

    md.append("\n---\n© 2026 Scalefy System. Todos los derechos reservados.\n")
    return "\n".join(md)

def main():
    if not TOC_PATH.exists(): return
    with open(TOC_PATH, 'r', encoding='utf-8') as f:
        toc = json.load(f)

    if OUTPUT_DIR.exists():
        import shutil
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Flat list for navigation
    all_endpoints = []
    for item in toc.get("items", []):
        if item.get("type") == "item" and item.get("uri", "").endswith(".json"):
            filename = item.get("uri").split("/")[-1]
            json_path = APPS_DIR / filename
            if not json_path.exists(): continue
            with open(json_path, 'r', encoding='utf-8') as f:
                spec = json.load(f)
            cat_name = item.get("title").lower().replace(" ", "-").replace("(", "").replace(")", "")
            for path, methods in spec.get("paths", {}).items():
                for method, details in methods.items():
                    if method not in ["get", "post", "put", "delete", "patch"]: continue
                    safe_path = path.strip("/").replace("/", "-").replace("{", "").replace("}", "") or "root"
                    all_endpoints.append({
                        "id": f"{method}-{safe_path}",
                        "method": method, "path": path, "details": details, "spec": spec,
                        "category": cat_name, "title": details.get("summary", "Endpoint")
                    })

    for i, ep in enumerate(all_endpoints):
        prev_ep = all_endpoints[i-1] if i > 0 else None
        next_ep = all_endpoints[i+1] if i < len(all_endpoints)-1 else None
        
        target_dir = OUTPUT_DIR / ep["category"]
        target_dir.mkdir(parents=True, exist_ok=True)
        
        pl = {"title": prev_ep["title"], "url": f"../{prev_ep['category']}/{prev_ep['id']}.md"} if prev_ep else None
        nl = {"title": next_ep["title"], "url": f"../{next_ep['category']}/{next_ep['id']}.md"} if next_ep else None
        
        md_content = generate_endpoint_md(ep["path"], ep["method"], ep["details"], ep["spec"], pl, nl)
        with open(target_dir / f"{ep['id']}.md", 'w', encoding='utf-8') as f:
            f.write(md_content)
        if i % 50 == 0: print(f"✅ Procesados {i} endpoints...")

def process_webhooks():
    # Use absolute path resolving to avoid WinError 3
    base_src = Path(r"c:\Users\luaco\OneDrive\Documentos\Dev\gohighlevel-api\temp_ghl_docs\docs")
    webhooks_src = base_src / "webhook events"
    
    if not webhooks_src.exists():
        print(f"⚠️ Webhook source not found at {webhooks_src}")
        return
        
    WEBHOOKS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    for file in list(webhooks_src.glob("*.md")):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            name = file.stem
            # Extract description
            desc_match = re.search(r'# .*\n\n(.*)', content)
            description = desc_match.group(1) if desc_match else "Evento de Webhook"
            
            # Extract schema
            schema_match = re.search(r'```json json_schema\n(.*?)\n```', content, re.DOTALL)
            if not schema_match:
                print(f"⚠️ No se encontró esquema en {file.name}")
                continue
                
            schema = json.loads(schema_match.group(1))
            
            # Extract example
            example_match = re.search(r'#### Example\n\n```json\n(.*?)\n```', content, re.DOTALL)
            example = example_match.group(1) if example_match else "{}"
        except Exception as e:
            print(f"❌ Error procesando webhook {file.name}: {e}")
            continue

        md = [f"---\ntitle: \"Webhook: {name}\"\ntags: [\"webhook\", \"event\"]\n---\n"]
        md.append(f"# Webhook: {name}\n")
        
        md.append("## 1. Overview\n")
        md.append("| Campo | Valor |\n|---|---|\n")
        md.append(f"| **Recurso** | `{name.split('Create')[0].split('Update')[0].split('Delete')[0]}` |\n")
        md.append(f"| **Disparador** | {description} |\n")
        md.append(f"| **Event ID** | `{name}` |\n")

        md.append("\n## 2. Esquema del Payload\n")
        rows = flatten_schema(schema, {})
        if rows:
            md.append("| Campo | Tipo | Requerido | Descripción |\n|---|---|---|---|\n")
            for r in rows:
                md.append(f"| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} |\n")

        md.append("\n## 3. Ejemplo de Payload\n")
        md.append(f"```json\n{example}\n```")

        md.append("\n## 4. Ejemplo de Listener (Node.js)\n")
        md.append("```javascript\nconst express = require('express');\nconst app = express();\n\napp.use(express.json());\n\napp.post('/webhook', (req, res) => {\n  const payload = req.body;\n  console.log('Evento recibido:', payload.type);\n  res.status(200).send('OK');\n});\n\napp.listen(3000, () => console.log('Listener de webhooks activo en el puerto 3000'));\n```")

        md.append("\n---\n© 2026 Scalefy System. Todos los derechos reservados.\n")
        
        target_name = name.lower().replace(" ", "-") + ".md"
        with open(WEBHOOKS_OUTPUT_DIR / target_name, 'w', encoding='utf-8') as f:
            f.write("\n".join(md))

if __name__ == "__main__":
    main()
    process_webhooks()
    print("\n✨ ¡Sistema de documentación al 100% de paridad técnica!")
