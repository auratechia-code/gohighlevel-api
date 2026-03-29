# Update a template with settings

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PATCH |
| **Endpoint URL** | `https://services.leadconnectorhq.com/emails/builder/:templateId` |
| **Scopes Required** | `emails/builder.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **templateId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **updatedBy** | `string` | No |  |
| **editorContent** | `object` | Yes | Editor content - can be HTML string, plain text string, or DND builder object depending on editorType. When editorType is "html" or "text", this should be a string. When editorType is "builder", this should be a DND object with elements, attrs, and templateSettings. Must be provided together with editorType. oneOf MOD1 IBuilderJsonMapper string Example: <html><body>Hello World</body></html> elements string[] required Array of VNode elements representing the email structure attrs object required Object mapping element IDs to their attributes and styles templateSettings object required Template-level settings and configuration |
| **** | `string` | No |  |
| **elements** | `string[]` | No |  |
| **attrs** | `object` | No |  |
| **templateSettings** | `object` | No |  |
| **editorType** | `string` | No |  |
| **previewText** | `string` | No |  |
| **subjectLine** | `string` | No |  |
| **fromName** | `string` | No |  |
| **fromEmail** | `string` | No |  |
| **name** | `string` | No |  |
| **archived** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "ok": true,
  "id": "507f1f77bcf86cd799439011",
  "name": "My Email Template",
  "archived": false,
  "builderVersion": "2",
  "fromName": "John Doe",
  "fromEmail": "john@example.com",
  "subjectLine": "Welcome to our newsletter",
  "previewText": "Check out our latest updates",
  "previewUrl": "https://example.com/preview/template123",
  "type": "builder",
  "lastUpdated": "2024-01-15T10:30:00Z",
  "createdAt": "2024-01-01T08:00:00Z",
  "isPlainText": false
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **ok** | `bool` |  |
| **id** | `str` |  |
| **name** | `str` |  |
| **archived** | `bool` |  |
| **builderVersion** | `str` |  |
| **fromName** | `str` |  |
| **fromEmail** | `str` |  |
| **subjectLine** | `str` |  |
| **previewText** | `str` |  |
| **previewUrl** | `str` |  |
| **type** | `str` |  |
| **lastUpdated** | `str` |  |
| **createdAt** | `str` |  |
| **isPlainText** | `bool` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PATCH \
  --url https://services.leadconnectorhq.com/emails/builder/:templateId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}'
```

### 2. NODE SDK

```javascript
const { HighLevel } = require('@gohighlevel/api-client');

const ghl = new HighLevel({
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET'
});

async function executeRequest() {
  try {
    const response = await ghl.api.request('PATCH', 'https://services.leadconnectorhq.com/emails/builder/:templateId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}
    });
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

### 3. AXIOS

```javascript
const axios = require('axios');

const config = {
  method: 'patch',
  url: 'https://services.leadconnectorhq.com/emails/builder/:templateId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}
};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```

### 4. NATIVE NODE

```javascript
const https = require('follow-redirects').https;

const options = {
  'method': 'PATCH',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/emails/builder/:templateId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};

const req = https.request(options, (res) => {
  let chunks = [];
  res.on("data", (chunk) => chunks.push(chunk));
  res.on("end", () => console.log(Buffer.concat(chunks).toString()));
});

req.write(JSON.stringify({
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PATCH',
  'url': 'https://services.leadconnectorhq.com/emails/builder/:templateId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
})
};

request(options, (error, response) => {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

### 6. UNIREST NODE

```javascript
const unirest = require('unirest');

unirest('PATCH', 'https://services.leadconnectorhq.com/emails/builder/:templateId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/emails/builder/:templateId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PATCH", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}))
print(response.text)
```

### 8. PHP

```php
<?php
use GuzzleHttp\Client;
$client = new Client();
$headers = [
  'Authorization' => 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version' => '2021-07-28',
  'Content-Type' => 'application/json'
];
$response = $client->request('PATCH', 'https://services.leadconnectorhq.com/emails/builder/:templateId', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}'
]);
echo $response->getBody();
```

### 9. JAVA

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://services.leadconnectorhq.com/emails/builder/:templateId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PATCH", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"updatedBy\": \"string\",
  \"editorContent\": \"string\",
  \"\": \"string\",
  \"elements\": \"string\",
  \"attrs\": \"string\",
  \"templateSettings\": \"string\",
  \"editorType\": \"string\",
  \"previewText\": \"string\",
  \"subjectLine\": \"string\",
  \"fromName\": \"string\",
  \"fromEmail\": \"string\",
  \"name\": \"string\",
  \"archived\": true
}"))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

### 10. GO

```go
package main
import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)
func main() {
  url := "https://services.leadconnectorhq.com/emails/builder/:templateId"
  payload := strings.NewReader(`{
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}`)
  req, _ := http.NewRequest("PATCH", url, payload)
  req.Header.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
  req.Header.Add("Version", "2021-07-28")
  req.Header.Add("Content-Type", "application/json")
  res, _ := http.DefaultClient.Do(req)
  defer res.Body.Close()
  body, _ := ioutil.ReadAll(res.Body)
  fmt.Println(string(body))
}
```

### 11. RUBY

```ruby
require 'net/http'
require 'uri'
require 'json'

url = URI("https://services.leadconnectorhq.com/emails/builder/:templateId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
})
response = http.request(request)
puts response.read_body
```

### 12. POWERSHELL

```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "2021-07-28")
$headers.Add("Content-Type", "application/json")

$body = '{
  "locationId": "string",
  "updatedBy": "string",
  "editorContent": "string",
  "": "string",
  "elements": "string",
  "attrs": "string",
  "templateSettings": "string",
  "editorType": "string",
  "previewText": "string",
  "subjectLine": "string",
  "fromName": "string",
  "fromEmail": "string",
  "name": "string",
  "archived": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/emails/builder/:templateId' -Method 'PATCH' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
