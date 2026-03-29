import json
import os
import re
from datetime import datetime

# Configuration
SOURCE_JSON = 'data-agregated/ALL_DOCS.json'
SCOPES_JSON = 'data-agregated/SCOPES_MAP.json'
SUPPLEMENTAL_JSON = 'data-agregated/SUPPLEMENTAL_DATA.json'
OUTPUT_DIR = 'final_docs/01-resources'
VERSION = "2021-07-28"

def slugify(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def format_table(headers, rows):
    if not rows:
        return "| Name | Type | Required | Description |\n| --- | --- | --- | --- |\n| N/A | N/A | N/A | N/A |"
    
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"
    
    body_rows = []
    for row in rows:
        vals = [str(row.get(h, '')).replace('|', '\\|').strip() for h in headers]
        line = "| " + " | ".join(vals) + " |"
        body_rows.append(line)
    
    return "\n".join([header_row, separator_row] + body_rows)

class CodeGenerator:
    def __init__(self, method, url, path, headers, body=None):
        self.method = method.upper()
        self.url = url
        self.path = path
        self.headers = headers
        self.body = body
        self.body_json = json.dumps(body) if body else "{}"

    def generate_all(self):
        return {
            "cURL": self.curl(),
            "Node (Axios)": self.node_axios(),
            "Node SDK": self.node_sdk(),
            "Node (Native)": self.node_native(),
            "Node (Request)": self.node_request(),
            "Node (Unirest)": self.node_unirest(),
            "Python": self.python(),
            "PHP (Guzzle)": self.php_guzzle(),
            "Go": self.go(),
            "Ruby": self.ruby(),
            "PowerShell": self.powershell(),
            "Java": self.java()
        }

    def curl(self):
        cmd = f"curl -l -X {self.method} \\\n  {self.url} \\\n"
        for k, v in self.headers.items():
            cmd += f"  -H \"{k}: {v}\" \\\n"
        if self.body:
            cmd += f"  -d '{json.dumps(self.body, indent=2)}'"
        return cmd.strip().strip('\\')

    def node_axios(self):
        return f"const axios = require('axios');\n\nawait axios({{\n  method: '{self.method.lower()}',\n  url: '{self.url}',\n  headers: {json.dumps(self.headers, indent=2)},\n  data: {self.body_json}\n}});"

    def node_sdk(self):
        res = self.path.split('/')[1] if len(self.path.split('/')) > 1 else 'resource'
        return f"const {{ GHL }} = require('@gohighlevel/api-client');\nconst ghl = new GHL({{ accessToken: '<TOKEN>' }});\n\nconst response = await ghl.{res}.{self.method.lower()}(\n  {self.body_json}\n);"

    def node_native(self):
        return f"const https = require('https');\n\nconst options = {{\n  method: '{self.method}',\n  hostname: 'services.leadconnectorhq.com',\n  path: '{self.path}',\n  headers: {json.dumps(self.headers, indent=2)}\n}};\n\nconst req = https.request(options, (res) => {{ /* handle */ }});\nreq.write({self.body_json});\nreq.end();"

    def node_request(self):
        return f"const request = require('request');\n\nconst options = {{\n  method: '{self.method}',\n  url: '{self.url}',\n  headers: {json.dumps(self.headers, indent=2)},\n  body: {self.body_json},\n  json: true\n}};\n\nrequest(options, (err, res, body) => {{ /* handle */ }});"

    def node_unirest(self):
        return f"const unirest = require('unirest');\n\nconst req = unirest('{self.method}', '{self.url}')\n  .headers({json.dumps(self.headers, indent=2)})\n  .send({self.body_json})\n  .end((res) => {{ /* handle */ }});"

    def python(self):
        return f"import requests\n\nurl = \"{self.url}\"\nheaders = {json.dumps(self.headers, indent=2)}\n\nresponse = requests.{self.method.lower()}(url, headers=headers, json={self.body_json})\nprint(response.json())"

    def php_guzzle(self):
        return f"<?php\n\n$client = new \\GuzzleHttp\\Client();\n$response = $client->request('{self.method}', '{self.url}', [\n  'headers' => {json.dumps(self.headers, indent=2)},\n  'json' => {self.body_json}\n]);\n\necho $response->getBody();"

    def go(self):
        return f"package main\n\nimport (\n  \"fmt\"\n  \"strings\"\n  \"net/http\"\n)\n\nfunc main() {{\n  payload := strings.NewReader(`{self.body_json}`)\n  req, _ := http.NewRequest(\"{self.method}\", \"{self.url}\", payload)\n  req.Header.Add(\"Version\", \"{VERSION}\")\n  req.Header.Add(\"Authorization\", \"Bearer <TOKEN>\")\n  res, _ := http.DefaultClient.Do(req)\n  fmt.Println(res)\n}}"

    def ruby(self):
        return f"require 'net/http'\nrequire 'json'\n\nuri = URI('{self.url}')\nreq = Net::HTTP::{self.method.capitalize()}.new(uri)\nreq['Version'] = '{VERSION}'\nreq['Authorization'] = 'Bearer <TOKEN>'\nreq.body = {self.body_json}.to_json\n\nres = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) {{ |http| http.request(req) }}"

    def powershell(self):
        h_str = "@{\n" + "\n".join([f"  '{k}' = '{v}'" for k, v in self.headers.items()]) + "\n}"
        body_arg = f" -Body '{self.body_json}'" if self.body else ""
        return f"$headers = {h_str}\nInvoke-RestMethod -Uri '{self.url}' -Method {self.method} -Headers $headers{body_arg}"

    def java(self):
        return f"import java.net.http.*;\nimport java.net.URI;\n\npublic class Main {{\n  public static void main(String[] args) throws Exception {{\n    HttpClient client = HttpClient.newHttpClient();\n    HttpRequest request = HttpRequest.newBuilder()\n      .uri(URI.create(\"{self.url}\"))\n      .header(\"Version\", \"{VERSION}\")\n      .header(\"Authorization\", \"Bearer <TOKEN>\")\n      .method(\"{self.method}\", HttpRequest.BodyPublishers.ofString(\"{self.body_json.replace('\"', '\\\"')}\"))\n      .build();\n    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());\n    System.out.println(response.body());\n  }}\n}}"

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
    if method not in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']: method = 'GET'
    return method, path

def generate_doc(entry, scopes_map, supplemental_data):
    title = entry.get('title', 'Endpoint')
    method, path = parse_endpoint(entry)
    full_url = f"https://services.leadconnectorhq.com{path}"
    
    # Supplemental overrides
    key = f"{method} {path}"
    supp_body = supplemental_data.get('body_params', {}).get(key)
    
    # Metadata
    meta = scopes_map.get(key, {
        "scope": "Review Required",
        "auth_type": "OAuth 2.0 / Private Integration",
        "token_type": "Review Required"
    })

    md = f"# {method} {path} — {title}\n\n"
    md += f"**Source:** {entry.get('url', '')}  \n"
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
    md += format_table(["Name", "Type", "Required", "Possible Values", "Description"], [
        {"Name": "`Version`", "Type": "string", "Required": "✅ Yes", "Possible Values": f"`{VERSION}`", "Description": "API Version"},
        {"Name": "`Authorization`", "Type": "string", "Required": "✅ Yes", "Possible Values": "`Bearer <TOKEN>`", "Description": "Auth token"},
        {"Name": "`Accept`", "Type": "string", "Required": "✅ Yes", "Possible Values": "`application/json`", "Description": "Response format"}
    ]) + "\n\n"
    
    md += "### Path Parameters\n\n"
    path_matches = re.findall(r':(\w+)', path)
    path_rows = [{"Name": f"`{m}`", "Type": "string", "Required": "✅ Yes", "Description": "Unique identifier"} for m in path_matches]
    md += format_table(["Name", "Type", "Required", "Description"], path_rows) + "\n\n"

    md += "### Query Parameters\n\n"
    query_params = [p for p in entry.get('parameters', []) if p.get('in') == 'query']
    md += format_table(["Name", "Type", "Required", "Description"], query_params) + "\n\n"

    md += "### Body Parameters\n\n"
    body_params = supp_body if supp_body else [p for p in entry.get('parameters', []) if p.get('in') == 'body']
    md += format_table(["Name", "Type", "Required", "Description"], body_params) + "\n\n"
    
    # Body JSON Example
    if method in ['POST', 'PUT', 'PATCH']:
        default_body = entry.get('request_body') or {}
        if not default_body and supp_body:
            default_body = {p['name']: f"<{p['type'].upper()}>" for p in supp_body}
        md += "### Request Body\n\n```json\n" + json.dumps(default_body, indent=2) + "\n```\n\n"

    md += "---\n\n## Responses\n\n"
    
    # 200 Success
    md += "### 200 — Successful Response\n\n"
    resp_body = entry.get('response_body') or {"message": "Operation successful"}
    md += f"```json\n{json.dumps(resp_body, indent=2)}\n```\n\n"
    
    # Errors from supplemental
    errors = supplemental_data.get('errors', {})
    for code, schema in errors.items():
        md += f"### {code} — Error Response\n\n```json\n{json.dumps(schema, indent=2)}\n```\n\n"

    md += "---\n\n## Code Examples\n\n"
    h = {"Version": VERSION, "Authorization": "Bearer <TOKEN>", "Accept": "application/json"}
    actual_body = entry.get('request_body') or ( {p['name']: "..." for p in supp_body} if supp_body else None )
    codegen = CodeGenerator(method, full_url, path, h, actual_body)
    examples = codegen.generate_all()
    
    for lang, code in examples.items():
        lang_id = slugify(lang.split('(')[0].strip())
        if 'php' in lang_id: lang_id = 'php'
        if 'node' in lang_id: lang_id = 'javascript'
        md += f"### {lang}\n```{lang_id}\n{code}\n```\n\n"

    md += "---\n\n## Nuestras Notas\n\n> [!NOTE]\n> Este endpoint es parte de la API 2.0. Asegúrate de usar el scope correcto y el header `Version: 2021-07-28`."
    
    category = entry.get('breadcrumbs', ['General', 'API'])[1] if len(entry.get('breadcrumbs', [])) > 1 else 'General'
    md += f"\n\n**Navigation:** [Index](../../SUMMARY.md) > [{category}](index.md) > {title}\n"
    
    return md, category, title

if __name__ == "__main__":
    with open(SOURCE_JSON, 'r', encoding='utf-8') as f: data = json.load(f)
    with open(SCOPES_JSON, 'r', encoding='utf-8') as f: scopes_map = json.load(f)
    with open(SUPPLEMENTAL_JSON, 'r', encoding='utf-8') as f: supplemental_data = json.load(f)

    # Process ALL or specific preview
    preview_only = True # Toggle this for preview
    
    count = 0
    for entry in data:
        if preview_only and entry.get('title') != "Create appointment": continue
        
        try:
            content, category, title = generate_doc(entry, scopes_map, supplemental_data)
            out_file = "create-appointment-preview-v2.md" if preview_only else f"{slugify(title)}.md"
            cat_dir = os.path.join(OUTPUT_DIR, slugify(category))
            os.makedirs(cat_dir, exist_ok=True)
            
            with open(os.path.join(cat_dir, out_file), 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Generated: {out_file}")
            count += 1
            if preview_only: break
        except Exception as e:
            print(f"Error {entry.get('title')}: {e}")

    print(f"Completed {count} files.")
