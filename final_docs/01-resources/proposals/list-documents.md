# List documents

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/proposals/document` |
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

N/A
### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `` | No | status string Possible values: [ draft , sent , viewed , completed , accepted ] Document status, pass as comma separated values Example: draft |
| **status** | `` | No | paymentStatus string Possible values: [ waiting_for_payment , paid , no_payment ] Payment status, pass as comma separated values Example: paid |
| **paymentStatus** | `` | No | limit number Limit to fetch number of records Example: 10 |
| **limit** | `` | No | skip number Skip number of records Example: 0 |
| **skip** | `` | No | query string Search string Example: document |
| **query** | `` | No | dateFrom string Date start from (ISO 8601), dateFrom & DateTo must be provided together Example: 2025-02-03T18:30:00.000Z |
| **dateFrom** | `` | No | dateTo string Date to (ISO 8601), dateFrom & DateTo must be provided together Example: 2025-02-14T18:29:59.999Z |
| **dateTo** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "documents": [
    {
      "locationId": "hTlkh7t8gujsahgg93",
      "documentId": "hTlkh7t8gujsahgg93",
      "_id": "67ac9a51106ee8311e911XXXX",
      "name": "Document Name",
      "type": "proposal",
      "deleted": false,
      "isExpired": false,
      "documentRevision": 1,
      "fillableFields": [
        {
          "fieldId": "text_field_1",
          "isRequired": true,
          "hasCompleted": true,
          "recipient": "John Doe",
          "entityType": "contacts",
          "id": "2d0a6fe1-d519-4198-8785-3da1d7cab925",
          "type": "TextField",
          "value": "John Doe"
        }
      ],
      "grandTotal": {
        "amount": 100,
        "currency": "USD",
        "discountPercentage": 15,
        "discounts": [
          {
            "id": "123456",
            "value": 10,
            "type": "percentage"
          }
        ]
      },
      "locale": "en-US",
      "status": "draft",
      "paymentStatus": "paid",
      "recipients": [
        {
          "id": "u240JcS0E5qE0ziHnwMm",
          "email": "jim@gmail.com",
          "imageUrl": "",
          "contactName": "Jim Anton",
          "firstName": "Jim",
          "lastName": "Anton",
          "role": "signer",
          "hasCompleted": true,
          "signingOrder": 1,
          "imgUrl": "base64 image url",
          "ip": "123.123.123.123"
        }
      ],
      "links": [
        {
          "referenceId": "550e8400-e29b-41d4-a716-446655440000",
          "documentId": "c1e87a91-93b2-4b78-821f-85cf0e1f925b",
          "recipientId": "u240JcS0E5qE0ziHnwMm",
          "entityName": "contacts",
          "recipientCategory": "recipient",
          "documentRevision": 1,
          "createdBy": "b6d8fa28-1112-4dc7-b9d2-f22b75a477ea",
          "deleted": false
        }
      ],
      "updatedAt": "2025-02-03T18:30:00.000Z",
      "createdAt": "2025-02-14T18:29:59.999Z"
    }
  ],
  "total": 10,
  "whiteLabelBaseUrl": "https://example.com",
  "whiteLabelBaseUrlForInvoice": "https://example.com"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **documents** | `list` |  |
| **total** | `int` |  |
| **whiteLabelBaseUrl** | `str` |  |
| **whiteLabelBaseUrlForInvoice** | `str` |  |

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
  --url https://services.leadconnectorhq.com/proposals/document \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/proposals/document', {
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
  url: 'https://services.leadconnectorhq.com/proposals/document',
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
  'path': '/proposals/document',
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
  'url': 'https://services.leadconnectorhq.com/proposals/document',
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

unirest('GET', 'https://services.leadconnectorhq.com/proposals/document')
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

url = "https://services.leadconnectorhq.com/proposals/document"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/proposals/document', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/proposals/document"))
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
  url := "https://services.leadconnectorhq.com/proposals/document"
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

url = URI("https://services.leadconnectorhq.com/proposals/document")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/proposals/document' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
