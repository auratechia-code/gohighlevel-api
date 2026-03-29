# List Coupons

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/payments/coupon/list` |
| **Scopes Required** | `payments/coupons.readonly` |
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

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `` | Yes | altType string required Possible values: [ location ] Alt Type Example: location |
| **altType** | `` | No | limit number Maximum number of coupons to return Default value: 100 Example: 10 |
| **limit** | `` | No | offset number Number of coupons to skip for pagination Default value: 0 Example: 0 |
| **offset** | `` | No | status string Possible values: [ scheduled , active , expired ] Filter coupons by status Example: active |
| **status** | `` | No | search string Search term to filter coupons by name or code Example: DEAL50 |
| **search** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "data": [
    {
      "_id": "67f6c132d9485f9dacd5f123",
      "usageCount": 12,
      "limitPerCustomer": 5,
      "altId": "79t07PzK8Tvf73d12312",
      "altType": "location",
      "name": "NEWT6",
      "code": "NEWT6",
      "discountType": "percentage",
      "discountValue": 25,
      "status": "scheduled",
      "startDate": "2025-04-30T18:30:00.000Z",
      "endDate": "2025-05-30T18:30:00.000Z",
      "applyToFuturePayments": true,
      "applyToFuturePaymentsConfig": {
        "type": "fixed",
        "duration": 3,
        "durationType": "months"
      },
      "productIds": [
        "6241712be68f7a98102ba272"
      ],
      "priceIds": [
        "6241712be68f7a98102ba272"
      ],
      "variantIds": [
        "6241712be68f7a98102ba272"
      ],
      "userId": "q0m15dTLGeiGOXG123123",
      "createdAt": "2025-04-09T18:49:22.026Z",
      "updatedAt": "2025-04-09T18:49:22.026Z"
    }
  ],
  "totalCount": 20,
  "traceId": "c667b18d-8f5e-44cf-a914"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **data** | `list` |  |
| **totalCount** | `int` |  |
| **traceId** | `str` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/payments/coupon/list \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{}'
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/payments/coupon/list', {
      headers: { 'Version': '2021-07-28' },
      body: {}
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
  method: 'get',
  url: 'https://services.leadconnectorhq.com/payments/coupon/list',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {}
};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```

### 4. NATIVE NODE

```javascript
const https = require('follow-redirects').https;

const options = {
  'method': 'GET',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/payments/coupon/list',
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

req.write(JSON.stringify({}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'GET',
  'url': 'https://services.leadconnectorhq.com/payments/coupon/list',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({})
};

request(options, (error, response) => {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

### 6. UNIREST NODE

```javascript
const unirest = require('unirest');

unirest('GET', 'https://services.leadconnectorhq.com/payments/coupon/list')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/payments/coupon/list"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=json.dumps({}))
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/payments/coupon/list', [
  'headers' => $headers,
  'body' => '{}'
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
    .uri(URI.create("https://services.leadconnectorhq.com/payments/coupon/list"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("GET", HttpRequest.BodyPublishers.ofString("{}"))
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
  url := "https://services.leadconnectorhq.com/payments/coupon/list"
  payload := strings.NewReader(`{}`)
  req, _ := http.NewRequest("GET", url, payload)
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

url = URI("https://services.leadconnectorhq.com/payments/coupon/list")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({})
response = http.request(request)
puts response.read_body
```

### 12. POWERSHELL

```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "2021-07-28")
$headers.Add("Content-Type", "application/json")

$body = '{}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/coupon/list' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
