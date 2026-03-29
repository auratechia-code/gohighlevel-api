# Update Rebilling

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/saas/update-rebilling/:companyId` |
| **Scopes Required** | `N/A` |
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
| **companyId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **product** | `string` | No |  |
| **locationIds** | `string[]` | No |  |
| **config** | `object` | No | Configuration for rebilling settings optIn boolean Enable the product for the locations Example: true enabled boolean Enable the rebilling for the locations Example: true markup number Additional value to be added in terms of percentage. For example, if the product price is $100 and the markup is 5, the amount charged to will be $105. Example: 5 |
| **optIn** | `boolean` | No |  |
| **enabled** | `boolean` | No |  |
| **markup** | `number` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "product": "contentAI",
  "locationIds": [
    "zzyG7A4x6bRJl5SlhQhH",
    "Vygq7VgXCDfg3xnl8TBR"
  ],
  "config": {
    "optIn": true,
    "enabled": true,
    "markup": 5
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **product** | `str` |  |
| **locationIds** | `list` |  |
| **config** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/saas/update-rebilling/:companyId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/saas/update-rebilling/:companyId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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
  url: 'https://services.leadconnectorhq.com/saas/update-rebilling/:companyId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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
  'path': '/saas/update-rebilling/:companyId',
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
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/saas/update-rebilling/:companyId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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

unirest('POST', 'https://services.leadconnectorhq.com/saas/update-rebilling/:companyId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/saas/update-rebilling/:companyId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/saas/update-rebilling/:companyId', [
  'headers' => $headers,
  'body' => '{
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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
    .uri(URI.create("https://services.leadconnectorhq.com/saas/update-rebilling/:companyId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"product\": \"string\",
  \"locationIds\": \"string\",
  \"config\": \"string\",
  \"optIn\": true,
  \"enabled\": true,
  \"markup\": 123
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
  url := "https://services.leadconnectorhq.com/saas/update-rebilling/:companyId"
  payload := strings.NewReader(`{
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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

url = URI("https://services.leadconnectorhq.com/saas/update-rebilling/:companyId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
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
  "product": "string",
  "locationIds": "string",
  "config": "string",
  "optIn": true,
  "enabled": true,
  "markup": 123
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/saas/update-rebilling/:companyId' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
