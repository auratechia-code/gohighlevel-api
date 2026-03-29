# Update a Brand Board

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PATCH |
| **Endpoint URL** | `https://services.leadconnectorhq.com/brand-boards/:locationId/:id` |
| **Scopes Required** | `brand-boards/design-kit.write` |
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
| **locationId** | `` | Yes | id string required Brand board ID to update, retrieve, or delete Example: 507f1f77bcf86cd799439011 |
| **id** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **name** | `string` | No |  |
| **logos** | `object[]` | Yes | Array of logos for the brand board Array [ id string required Unique identifier for the logo Example: logo_abc123 url string required Public URL of the logo image. Used for uploading to the brand board folder in media library Example: https://storage.googleapis.com/bucket/logos/my-logo.png label string required Display label for the logo (e.g., Primary, Secondary) Example: Primary Logo path string required Storage path of the logo in the media library Example: /locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png ] |
| **id** | `string` | No |  |
| **url** | `string` | No |  |
| **label** | `string` | No |  |
| **path** | `string` | No |  |
| **colors** | `object[]` | Yes | Array of colors for the brand board Array [ id string required Unique identifier for the color Example: color_xyz789 hexa string required Color in HEXA format (with alpha) Example: #FF5733FF rgba string required Color in RGBA format Example: rgba(255, 87, 51, 1) hex string required Color in HEX format Example: #FF5733 rgb string required Color in RGB format Example: rgb(255, 87, 51) label string required Display label for the color Example: Brand Orange ] |
| **id** | `string` | No |  |
| **hexa** | `string` | No |  |
| **rgba** | `string` | No |  |
| **hex** | `string` | No |  |
| **rgb** | `string` | No |  |
| **label** | `string` | No |  |
| **fonts** | `object[]` | Yes | Array of fonts for the brand board Array [ id string required Unique identifier for the font Example: font_def456 font string required Font family name Example: Montserrat fallback string required Fallback font family Example: sans-serif label string required Display label for the font Example: Heading Font ] |
| **id** | `string` | No |  |
| **font** | `string` | No |  |
| **fallback** | `string` | No |  |
| **label** | `string` | No |  |
| **default** | `boolean` | No |  |
| **parentId** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "My Brand Board",
  "logos": [
    {
      "id": "logo_abc123",
      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",
      "label": "Primary Logo",
      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"
    }
  ],
  "colors": [
    {
      "id": "color_xyz789",
      "hexa": "#FF5733FF",
      "rgba": "rgba(255, 87, 51, 1)",
      "hex": "#FF5733",
      "rgb": "rgb(255, 87, 51)",
      "label": "Brand Orange"
    }
  ],
  "fonts": [
    {
      "id": "font_def456",
      "font": "Montserrat",
      "fallback": "sans-serif",
      "label": "Heading Font"
    }
  ],
  "default": false,
  "deleted": false,
  "parentId": "507f1f77bcf86cd799439011",
  "folderId": "507f1f77bcf86cd799439011",
  "originId": "507f1f77bcf86cd799439011",
  "meta": {
    "updatedBy": "user_abc123",
    "lastAction": "UPDATE",
    "sourceId": "507f1f77bcf86cd799439011",
    "sourceType": "blank"
  },
  "createdAt": "2024-01-05T12:00:00.000Z",
  "updatedAt": "2024-01-05T12:00:00.000Z"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **locationId** | `str` |  |
| **name** | `str` |  |
| **logos** | `list` |  |
| **colors** | `list` |  |
| **fonts** | `list` |  |
| **default** | `bool` |  |
| **deleted** | `bool` |  |
| **parentId** | `str` |  |
| **folderId** | `str` |  |
| **originId** | `str` |  |
| **meta** | `dict` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |

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
  --url https://services.leadconnectorhq.com/brand-boards/:locationId/:id \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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
    const response = await ghl.api.request('PATCH', 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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
  url: 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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
  'path': '/brand-boards/:locationId/:id',
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
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PATCH',
  'url': 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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

unirest('PATCH', 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/brand-boards/:locationId/:id"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PATCH", url, headers=headers, data=json.dumps({
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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
$response = $client->request('PATCH', 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id', [
  'headers' => $headers,
  'body' => '{
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/brand-boards/:locationId/:id"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PATCH", HttpRequest.BodyPublishers.ofString("{
  \"name\": \"string\",
  \"logos\": \"string\",
  \"id\": \"string\",
  \"url\": \"string\",
  \"label\": \"string\",
  \"path\": \"string\",
  \"colors\": \"string\",
  \"hexa\": \"string\",
  \"rgba\": \"string\",
  \"hex\": \"string\",
  \"rgb\": \"string\",
  \"fonts\": \"string\",
  \"font\": \"string\",
  \"fallback\": \"string\",
  \"default\": true,
  \"parentId\": \"string\"
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
  url := "https://services.leadconnectorhq.com/brand-boards/:locationId/:id"
  payload := strings.NewReader(`{
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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

url = URI("https://services.leadconnectorhq.com/brand-boards/:locationId/:id")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
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
  "name": "string",
  "logos": "string",
  "id": "string",
  "url": "string",
  "label": "string",
  "path": "string",
  "colors": "string",
  "hexa": "string",
  "rgba": "string",
  "hex": "string",
  "rgb": "string",
  "fonts": "string",
  "font": "string",
  "fallback": "string",
  "default": true,
  "parentId": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/brand-boards/:locationId/:id' -Method 'PATCH' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
