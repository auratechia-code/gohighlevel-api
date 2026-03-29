# Update Redirect By Id

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PATCH |
| **Endpoint URL** | `https://services.leadconnectorhq.com/funnels/lookup/redirect/:id` |
| **Scopes Required** | `funnels/redirect.write` |
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
| **id** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **target** | `string` | No |  |
| **action** | `string` | No |  |
| **locationId** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "data": {
    "id": "6p2RxpgtMKQwO3E6IUaT",
    "locationId": "6p2RxpgtMKQwO3E6IUaT",
    "domain": "www.example.com",
    "path": "/old-path",
    "pathLowercase": "/old-path",
    "type": "Permanent",
    "target": "https://www.example.com/new-path",
    "action": "url"
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **data** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/funnels/lookup/redirect/:id \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "target": "string",
  "action": "string",
  "locationId": "string"
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
    const response = await ghl.api.request('PATCH', 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "target": "string",
  "action": "string",
  "locationId": "string"
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
  url: 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "target": "string",
  "action": "string",
  "locationId": "string"
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
  'path': '/funnels/lookup/redirect/:id',
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
  "target": "string",
  "action": "string",
  "locationId": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PATCH',
  'url': 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "target": "string",
  "action": "string",
  "locationId": "string"
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

unirest('PATCH', 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "target": "string",
  "action": "string",
  "locationId": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/funnels/lookup/redirect/:id"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PATCH", url, headers=headers, data=json.dumps({
  "target": "string",
  "action": "string",
  "locationId": "string"
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
$response = $client->request('PATCH', 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id', [
  'headers' => $headers,
  'body' => '{
  "target": "string",
  "action": "string",
  "locationId": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/funnels/lookup/redirect/:id"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PATCH", HttpRequest.BodyPublishers.ofString("{
  \"target\": \"string\",
  \"action\": \"string\",
  \"locationId\": \"string\"
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
  url := "https://services.leadconnectorhq.com/funnels/lookup/redirect/:id"
  payload := strings.NewReader(`{
  "target": "string",
  "action": "string",
  "locationId": "string"
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

url = URI("https://services.leadconnectorhq.com/funnels/lookup/redirect/:id")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "target": "string",
  "action": "string",
  "locationId": "string"
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
  "target": "string",
  "action": "string",
  "locationId": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/funnels/lookup/redirect/:id' -Method 'PATCH' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
