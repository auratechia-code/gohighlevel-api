import json
import os
import re

# Constants
SOURCE_JSON = 'ghl_kb_output_pro/ghl_kb_pro_v7_final.json'
OUTPUT_DIR = 'final_docs/01-resources'
VERSION = '2021-07-28'

def slugify(text):
    # Remove vertical bars and other illegal filename characters
    text = re.sub(r'[|:?*<>"\'\\]', '', text)
    # Replace spaces and slashes with hyphens
    return re.sub(r'[\s/]+', '-', text.lower()).strip('-')

def generate_table(params, is_response=False):
    if not params:
        return "N/A\n"
    
    if is_response:
        header = "| Name | Type | Description |\n| :--- | :--- | :--- |\n"
        rows = ""
        for p in params:
            name = p.get('name', 'N/A')
            ptype = p.get('type', 'string')
            details = p.get('details', '').replace('\n', ' ')
            rows += f"| **{name}** | `{ptype}` | {details} |\n"
    else:
        header = "| Name | Type | Required | Description |\n| :--- | :--- | :--- | :--- |\n"
        rows = ""
        for p in params:
            name = p.get('name', 'N/A')
            ptype = p.get('type', 'string')
            required = "Yes" if p.get('required') else "No"
            details = p.get('details', '').replace('\n', ' ')
            rows += f"| **{name}** | `{ptype}` | {required} | {details} |\n"
    
    return header + rows + "\n"

def extract_scopes(security_str):
    if not security_str:
        return "N/A"
    match = re.search(r'scopes:\s*(.*)', security_str)
    if match:
        return match.group(1).strip()
    return "N/A"

def prettify_json(json_str):
    try:
        data = json.loads(json_str)
        return json.dumps(data, indent=2)
    except:
        return json_str

def generate_response_table(json_str):
    try:
        data = json.loads(json_str)
        if isinstance(data, dict):
            params = []
            for k, v in data.items():
                ptype = type(v).__name__
                params.append({'name': k, 'type': ptype, 'details': ''})
            return generate_table(params, is_response=True)
    except:
        pass
    return "N/A\n"

def generate_code_snippets(method, url, body_params):
    # Prepare dummy data for examples
    payload = {}
    for p in body_params:
        name = p.get('name')
        ptype = p.get('type', 'string')
        if ptype == 'boolean':
            payload[name] = True
        elif ptype == 'number' or ptype == 'integer':
            payload[name] = 123
        else:
            payload[name] = "string"

    json_payload = json.dumps(payload, indent=2)
    
    snippets = {}
    
    # 1. cURL
    snippets['CURL'] = f"""```bash
curl --request {method} \\
  --url {url} \\
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \\
  --header 'Version: {VERSION}' \\
  --header 'Content-Type: application/json' \\
  --header 'Accept: application/json' \\
  --data '{json_payload}'
```"""

    # 2. Node.js SDK
    snippets['NODE_SDK'] = f"""```javascript
const {{ HighLevel }} = require('@gohighlevel/api-client');

const ghl = new HighLevel({{
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET'
}});

async function executeRequest() {{
  try {{
    const response = await ghl.api.request('{method}', '{url}', {{
      headers: {{ 'Version': '{VERSION}' }},
      body: {json_payload}
    }});
    console.log(response);
  }} catch (error) {{
    console.error(error);
  }}
}}
```"""

    # 3. Node.js Axios
    snippets['AXIOS'] = f"""```javascript
const axios = require('axios');

const config = {{
  method: '{method.lower()}',
  url: '{url}',
  headers: {{ 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '{VERSION}', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  }},
  data : {json_payload}
}};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```"""

    url_parts = url.split("//")
    hostname = url_parts[1].split("/")[0] if len(url_parts) > 1 else "services.leadconnectorhq.com"
    path = "/" + "/".join(url_parts[1].split("/")[1:]) if len(url_parts) > 1 else url

    # 4. Node.js Native
    snippets['NATIVE_NODE'] = f"""```javascript
const https = require('follow-redirects').https;

const options = {{
  'method': '{method}',
  'hostname': '{hostname}',
  'path': '{path}',
  'headers': {{
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '{VERSION}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }}
}};

const req = https.request(options, (res) => {{
  let chunks = [];
  res.on("data", (chunk) => chunks.push(chunk));
  res.on("end", () => console.log(Buffer.concat(chunks).toString()));
}});

req.write(JSON.stringify({json_payload}));
req.end();
```"""

    # 5. Node.js Request
    snippets['REQUEST_NODE'] = f"""```javascript
const request = require('request');

const options = {{
  'method': '{method}',
  'url': '{url}',
  'headers': {{
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '{VERSION}',
    'Content-Type': 'application/json'
  }},
  body: JSON.stringify({json_payload})
}};

request(options, (error, response) => {{
  if (error) throw new Error(error);
  console.log(response.body);
}});
```"""

    # 6. Node.js Unirest
    snippets['UNIREST_NODE'] = f"""```javascript
const unirest = require('unirest');

unirest('{method}', '{url}')
  .headers({{
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '{VERSION}',
    'Content-Type': 'application/json'
  }})
  .send(JSON.stringify({json_payload}))
  .end(res => console.log(res.raw_body));
```"""

    # 7. Python Requests
    snippets['PYTHON'] = f"""```python
import requests
import json

url = "{url}"
headers = {{
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '{VERSION}',
  'Content-Type': 'application/json'
}}
response = requests.request("{method}", url, headers=headers, data=json.dumps({json_payload}))
print(response.text)
```"""

    # 8. PHP Guzzle
    snippets['PHP'] = f"""```php
<?php
use GuzzleHttp\\Client;
$client = new Client();
$headers = [
  'Authorization' => 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version' => '{VERSION}',
  'Content-Type' => 'application/json'
];
$response = $client->request('{method}', '{url}', [
  'headers' => $headers,
  'body' => '{json_payload}'
]);
echo $response->getBody();
```"""

    # 9. Java HttpClient
    snippets['JAVA'] = f"""```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("{url}"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "{VERSION}")
    .header("Content-Type", "application/json")
    .method("{method}", HttpRequest.BodyPublishers.ofString("{json_payload.replace('"', '\\"') }"))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```"""

    # 10. Go
    snippets['GO'] = f"""```go
package main
import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)
func main() {{
  url := "{url}"
  payload := strings.NewReader(`{json_payload}`)
  req, _ := http.NewRequest("{method}", url, payload)
  req.Header.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
  req.Header.Add("Version", "{VERSION}")
  req.Header.Add("Content-Type", "application/json")
  res, _ := http.DefaultClient.Do(req)
  defer res.Body.Close()
  body, _ := ioutil.ReadAll(res.Body)
  fmt.Println(string(body))
}}
```"""

    # 11. Ruby
    snippets['RUBY'] = f"""```ruby
require 'net/http'
require 'uri'
require 'json'

url = URI("{url}")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::{method.capitalize()}.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "{VERSION}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({json_payload})
response = http.request(request)
puts response.read_body
```"""

    # 12. PowerShell
    snippets['POWERSHELL'] = f"""```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "{VERSION}")
$headers.Add("Content-Type", "application/json")

$body = '{json_payload}'

$response = Invoke-RestMethod '{url}' -Method '{method}' -Headers $headers -Body $body
$response | ConvertTo-Json
```"""

    return snippets

def main():
    if not os.path.exists(SOURCE_JSON):
        print(f"Source file {SOURCE_JSON} not found.")
        return

    with open(SOURCE_JSON, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    # Robust access: could be a list (from test) or a dict (full source)
    if isinstance(raw_data, list):
        endpoints = raw_data
    elif isinstance(raw_data, dict):
        endpoints = raw_data.get('data', {}).get('endpoint', [])
    else:
        endpoints = []

    for item in endpoints:
        meta = item.get('meta', {})
        title = meta.get('title', 'Untitled Endpoint')
        category = meta.get('category', 'General')
        security = meta.get('security', '')
        
        endpoint = item.get('endpoint', {})
        method = endpoint.get('method', 'GET')
        url = endpoint.get('url', '')
        
        params = item.get('parameters', {})
        headers = params.get('header', [])
        path_p = params.get('path', [])
        query_p = params.get('query', [])
        body_p = params.get('body', {}).get('fields', [])
        
        responses = item.get('responses', {})
        success_schema = responses.get('200', responses.get('201', '{}'))
        
        # Create Directory
        cat_slug = slugify(category)
        full_dir = os.path.join(OUTPUT_DIR, cat_slug)
        if not os.path.exists(full_dir):
            os.makedirs(full_dir)
        
        # Build MD
        scopes = extract_scopes(security)
        
        md = f"# {title}\n\n"
        md += f"---\n\n## 1. METADATA\n\n"
        md += f"| Property | Value |\n| :--- | :--- |\n"
        md += f"| **HTTP Method** | {method} |\n"
        md += f"| **Endpoint URL** | `{url}` |\n"
        md += f"| **Scopes Required** | `{scopes}` |\n"
        md += f"| **Authentication** | OAuth Access Token / Private Integration Token |\n"
        md += f"| **Token Type** | Sub-Account Token |\n\n"
        
        md += f"---\n\n## 2. REQUEST\n\n"
        md += "### Header Parameters\n\n"
        # Always add Version if not present
        temp_headers = list(headers)
        if not any(h.get('name') == 'Version' for h in temp_headers):
            temp_headers.append({'name': 'Version', 'type': 'string', 'required': True, 'details': f'API version. Use `{VERSION}`.'})
        md += generate_table(temp_headers)
        
        md += "### Path Parameters\n\n"
        md += generate_table(path_p)
        
        md += "### Query Parameters\n\n"
        md += generate_table(query_p)
        
        md += "### Body Parameters\n\n"
        md += generate_table(body_p)
        
        md += f"---\n\n## 3. RESPONSE\n\n"
        md += "### Success Schema (200/201 OK)\n\n"
        pretty_success = prettify_json(success_schema)
        md += f"```json\n{pretty_success}\n```\n\n"
        
        md += "### Response Field Table\n\n"
        md += generate_response_table(success_schema)
        
        md += "### Error Codes\n\n"
        md += "| Status Code | Description |\n| :--- | :--- |\n| **400 Bad Request** | Invalid input parameters. |\n| **401 Unauthorized** | Invalid Token. |\n\n"

        md += f"---\n\n## 4. CODE EXAMPLES\n\n"
        snippets = generate_code_snippets(method, url, body_p)
        for i, (lang, code) in enumerate(snippets.items(), 1):
            md += f"### {i}. {lang.replace('_', ' ')}\n\n{code}\n\n"
        
        md += f"---\n\n## 5. NOTES\n\n- Ensure the `Version: {VERSION}` header is included.\n"

        # Save File
        file_name = slugify(title) + ".md"
        with open(os.path.join(full_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(md)

    print(f"Generated {len(endpoints)} documentation files.")

if __name__ == "__main__":
    main()
