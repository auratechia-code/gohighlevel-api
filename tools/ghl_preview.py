import json
import os
import re
from datetime import datetime

# Configuration
SOURCE_JSON = 'data-agregated/ALL_DOCS.json'
SCOPES_JSON = 'data-agregated/SCOPES_MAP.json'
OUTPUT_DIR = 'final_docs/01-resources'
VERSION = "2021-07-28"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def format_table(headers, rows):
    if not rows:
        return "No parameters defined."
    
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    
    body_rows = []
    for row in rows:
        vals = [str(row.get(h, '')).replace('|', '\\|').strip() for h in headers]
        line = "| " + " | ".join(vals) + " |"
        body_rows.append(line)
    
    return "\n".join([header_row, separator_row] + body_rows)

class CodeGenerator:
    @staticmethod
    def generate_curl(method, url, headers, body=None):
        cmd = f"curl -l -X {method} \\\n  {url} \\\n"
        for k, v in headers.items():
            cmd += f"  -H \"{k}: {v}\" \\\n"
        if body:
            cmd += f"  -d '{json.dumps(body, indent=2)}'"
        return cmd.strip().strip('\\')

    @staticmethod
    def generate_node_sdk(method, path, body=None):
        resource = path.split('/')[1] if len(path.split('/')) > 1 else 'resource'
        body_str = json.dumps(body, indent=2) if body else "{}"
        return f"const {resource} = await ghl.{resource}.{method.lower()}(\n  'ID',\n  {body_str}\n);"

    @staticmethod
    def generate_axios(method, url, headers, body=None):
        body_str = json.dumps(body) if body else "{}"
        return f"const axios = require('axios');\n\nawait axios({{\n  method: '{method.lower()}',\n  url: '{url}',\n  headers: {json.dumps(headers, indent=2)},\n  data: {body_str}\n}});"

    @staticmethod
    def generate_python(method, url, headers, body=None):
        body_str = json.dumps(body) if body else "{}"
        return f"import requests\n\nurl = \"{url}\"\nheaders = {json.dumps(headers, indent=2)}\n\nresponse = requests.{method.lower()}(url, headers=headers, json={body_str})\nprint(response.json())"

    @staticmethod
    def generate_php(method, url, headers, body=None):
        header_str = ", ".join([f"\"{k}: {v}\"" for k, v in headers.items()])
        body_str = json.dumps(body) if body else ""
        return f"$curl = curl_init();\ncurl_setopt_array($curl, [\n  CURLOPT_URL => \"{url}\",\n  CURLOPT_CUSTOMREQUEST => \"{method}\",\n  CURLOPT_HTTPHEADER => [{header_str}],\n  CURLOPT_POSTFIELDS => '{body_str}',\n  CURLOPT_RETURNTRANSFER => true,\n]);\n$response = curl_exec($curl);"

    @staticmethod
    def generate_go(method, url, headers, body=None):
        return f"package main\n\nimport (\n  \"fmt\"\n  \"net/http\"\n)\n\nfunc main() {{\n  req, _ := http.NewRequest(\"{method}\", \"{url}\", nil)\n  req.Header.Add(\"Version\", \"{headers['Version']}\")\n  req.Header.Add(\"Authorization\", \"Bearer <TOKEN>\")\n  res, _ := http.DefaultClient.Do(req)\n  fmt.Println(res)\n}}"

    @staticmethod
    def generate_ruby(method, url, headers, body=None):
        return f"require 'net/http'\nrequire 'json'\n\nuri = URI('{url}')\nreq = Net::HTTP::{method.capitalize()}.new(uri)\nreq['Version'] = '{headers['Version']}'\nreq['Authorization'] = 'Bearer <TOKEN>'\n\nres = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {{ |http| http.request(req) }}"

    @staticmethod
    def generate_powershell(method, url, headers, body=None):
        header_str = "@{\n" + "\n".join([f"  '{k}' = '{v}'" for k, v in headers.items()]) + "\n}"
        body_str = json.dumps(body) if body else ""
        body_arg = f" -Body '{body_str}'" if body_str else ""
        return f"$headers = {header_str}\nInvoke-RestMethod -Uri '{url}' -Method {method} -Headers $headers{body_arg}"

def parse_endpoint(entry):
    path_raw = entry.get('endpoint_path', '')
    method_raw = entry.get('http_method', 'GET')
    
    if path_raw and ' ' in path_raw:
        parts = path_raw.split(' ')
        method = parts[0].upper()
        path = parts[1]
    else:
        method = method_raw.upper() if method_raw else 'GET'
        path = path_raw if path_raw else '/v1/resource'
    
    if method not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        method = 'GET'
    
    return method, path

def generate_doc(entry, scopes_map):
    url_source = entry.get('url', '')
    title = entry.get('title', 'Endpoint')
    method, path = parse_endpoint(entry)
    full_url = f"https://services.leadconnectorhq.com{path}"
    
    # Metadata lookup
    scope_key = f"{method} {path}"
    meta = scopes_map.get(scope_key, {
        "scope": "Review Required",
        "auth_type": "OAuth Access Token, Private Integration Token",
        "token_type": "Review Required"
    })

    md = f"# {method} {path} — {title}\n\n"
    md += f"**Source:** {url_source}  \n"
    md += f"**Extracted:** {datetime.now().strftime('%Y-%m-%d')}  \n\n---\n\n"
    
    md += "## Overview\n\n"
    md += format_table(["Field", "Value"], [
        {"Field": "**Method**", "Value": f"`{method}`"},
        {"Field": "**Endpoint**", "Value": f"`{full_url}`"},
        {"Field": "**Summary**", "Value": title}
    ]) + "\n\n---\n\n"

    md += "## Requirements\n\n"
    md += format_table(["Field", "Value"], [
        {"Field": "**Scope(s)**", "Value": f"`{meta['scope']}`"},
        {"Field": "**Auth Method(s)**", "Value": meta['auth_type']},
        {"Field": "**Token Type(s)**", "Value": meta['token_type']}
    ]) + "\n\n---\n\n"

    md += "## Request\n\n### Header Parameters\n\n"
    headers_info = [
        {"Name": "`Version`", "Type": "string", "Required": "✅ Yes", "Possible Values": f"`{VERSION}`", "Description": "API Version"},
        {"Name": "`Authorization`", "Type": "string", "Required": "✅ Yes", "Possible Values": "`Bearer <TOKEN>`", "Description": "Auth token"},
        {"Name": "`Accept`", "Type": "string", "Required": "✅ Yes", "Possible Values": "`application/json`", "Description": "Response format"}
    ]
    md += format_table(["Name", "Type", "Required", "Possible Values", "Description"], headers_info) + "\n\n"
    
    params = entry.get('parameters', [])
    if params:
        md += "### Parameters\n\nValue Example para Path params, o Descripcion para Query params.\n\n"
        md += format_table(["Name", "Type", "Required", "Description"], params) + "\n\n"
    
    if entry.get('request_body'):
        md += "### Request Body\n\n```json\n" + json.dumps(entry['request_body'], indent=2) + "\n```\n\n"

    md += "---\n\n## Responses\n\n"
    resp_body = entry.get('response_body', {})
    if not resp_body: resp_body = {"message": "Operation successful"}
    md += "### 200 — Successful Response\n\n"
    md += f"```json\n{json.dumps(resp_body, indent=2)}\n```\n\n---\n\n"

    md += "## Code Examples\n\n"
    sample_headers = {"Version": VERSION, "Authorization": "Bearer <TOKEN>", "Accept": "application/json"}
    body_val = entry.get('request_body')
    
    gen = CodeGenerator()
    md += "### cURL\n```bash\n" + gen.generate_curl(method, full_url, sample_headers, body_val) + "\n```\n\n"
    md += "### Node.js (Axios)\n```javascript\n" + gen.generate_axios(method, full_url, sample_headers, body_val) + "\n```\n\n"
    md += "### Python (Requests)\n```python\n" + gen.generate_python(method, full_url, sample_headers, body_val) + "\n```\n\n"
    md += "### PHP (cURL)\n```php\n" + gen.generate_php(method, full_url, sample_headers, body_val) + "\n```\n\n"
    md += "### Go (Native)\n```go\n" + gen.generate_go(method, full_url, sample_headers, body_val) + "\n```\n\n"
    md += "### Ruby\n```ruby\n" + gen.generate_ruby(method, full_url, sample_headers, body_val) + "\n```\n\n"
    md += "### PowerShell\n```powershell\n" + gen.generate_powershell(method, full_url, sample_headers, body_val) + "\n```\n"

    md += "\n---\n\n## Nuestras Notas\n\n> [!NOTE]\n> Este endpoint requiere un Sub-Account Token. Asegúrate de incluir el header `Version: 2021-07-28`."
    
    category = entry.get('breadcrumbs', ['General', 'API'])[1] if len(entry.get('breadcrumbs', [])) > 1 else 'General'
    md += f"\n\n**Navigation:** [Index](../../SUMMARY.md) > [{category}](index.md) > {title}\n"
    
    return md, category

if __name__ == "__main__":
    with open(SOURCE_JSON, 'r', encoding='utf-8') as f: data = json.load(f)
    with open(SCOPES_JSON, 'r', encoding='utf-8') as f: scopes_map = json.load(f)

    # Preview
    for entry in data:
        if entry.get('title') == "Create appointment":
            content, category = generate_doc(entry, scopes_map)
            filename = "create-appointment-preview.md"
            out_path = os.path.join(OUTPUT_DIR, slugify(category), filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f: f.write(content)
            print(f"Preview generated: {out_path}")
            break
