# Create Product Collection

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/products/collections` |
| **Scopes Required** | `products/collection.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **collectionId** | `string` | No |  |
| **name** | `string` | No |  |
| **slug** | `string` | No |  |
| **image** | `string` | No |  |
| **seo** | `object` | No | The metadata information which will be displayed in SEO previews title string The title which will be displayed as an SEO format Example: Best Sellers description string The description which would be displayed in preview purposes Example: Collections where all the best products are available |
| **title** | `string` | No |  |
| **description** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "data": {
    "_id": "655b33a82209e60b6adb87a5",
    "altId": "Z4Bxl8J4SaPEPLq9IQ8g",
    "name": "Best Sellers",
    "slug": "best-sellers",
    "image": "http://example.com/watermark.png",
    "seo": {
      "title": "Best Sellers",
      "description": "Collections where all the best products are available"
    },
    "createdAt": "2024-02-22T09:27:19.728Z"
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
curl --request POST \
  --url https://services.leadconnectorhq.com/products/collections \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/products/collections', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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
  method: 'post',
  url: 'https://services.leadconnectorhq.com/products/collections',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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
  'method': 'POST',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/products/collections',
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
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/products/collections',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/products/collections')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/products/collections"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/products/collections', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/products/collections"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"collectionId\": \"string\",
  \"name\": \"string\",
  \"slug\": \"string\",
  \"image\": \"string\",
  \"seo\": \"string\",
  \"title\": \"string\",
  \"description\": \"string\"
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
  url := "https://services.leadconnectorhq.com/products/collections"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
}`)
  req, _ := http.NewRequest("POST", url, payload)
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

url = URI("https://services.leadconnectorhq.com/products/collections")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
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
  "altId": "string",
  "altType": "string",
  "collectionId": "string",
  "name": "string",
  "slug": "string",
  "image": "string",
  "seo": "string",
  "title": "string",
  "description": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/collections' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
