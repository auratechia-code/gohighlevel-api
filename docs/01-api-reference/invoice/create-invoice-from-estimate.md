# Create Invoice from Estimate

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice` |
| **Scopes Required** | `invoices/estimate.write` |
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
| **estimateId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **markAsInvoiced** | `boolean` | No |  |
| **version** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "estimate": {
    "altId": "6578278e879ad2646715ba9c",
    "altType": "location",
    "_id": "67ac9a51106ee8311e911XXXX",
    "liveMode": true,
    "deleted": false,
    "name": "Estimate Name",
    "currency": "USD",
    "businessDetails": {
      "logoUrl": "your_image-url",
      "name": "Business name",
      "address": {
        "addressLine1": "address line 1",
        "city": "Test City",
        "state": "State Name",
        "countryCode": "US",
        "postalCode": "12345"
      },
      "phoneNo": "+1 1234567890",
      "website": "www.example.com",
      "customValues": [
        {
          "name": "Test",
          "fieldKey": "{{custom_values.test}}",
          "id": "5DYTWoiQvWiIJZXX44XXX",
          "value": "Test's Custom Value"
        }
      ]
    },
    "items": [
      {
        "taxes": [],
        "taxInclusive": false,
        "_id": "67ac9a51106ee8311e911XXXX",
        "description": "<p>Futuristic anti-gravity racing</p>",
        "currency": "USD",
        "productId": "67ac9a51106ee8311e911XXXX",
        "priceId": "67ac9a51106ee8311e911XXXX",
        "amount": 9.99,
        "qty": 1,
        "name": "TEST",
        "type": "one_time"
      },
      {
        "taxes": [
          {
            "_id": "67ac9a51106ee8311e911XXXX",
            "name": "TaxTwo",
            "rate": 8.5,
            "calculation": "exclusive"
          }
        ],
        "taxInclusive": true,
        "_id": "67ac9a51106ee8311e911XXXX",
        "productId": "67ac9a51106ee8311e911XXXX",
        "priceId": "67ac9a51106ee8311e911XXXX",
        "currency": "USD",
        "name": "TEST2",
        "qty": 1,
        "amount": 500,
        "description": "",
        "type": "recurring"
      }
    ],
    "discount": {
      "type": "percentage",
      "value": 0
    },
    "title": "ESTIMATE",
    "estimateNumberPrefix": "EST-",
    "attachments": [
      {
        "id": "6241712be68f7a98102ba272",
        "name": "Electronics.pdf",
        "url": "https://example.com/digital-delivery",
        "type": "string",
        "size": 10000
      }
    ],
    "updatedBy": "3HIpOF9NIc5ltriQXXXX",
    "total": 1222.03,
    "createdAt": "2025-02-12T13:17:47.416Z",
    "updatedAt": "2025-02-12T13:17:47.416Z",
    "__v": 0,
    "automaticTaxesEnabled": false,
    "termsNotes": "<p>All services are subject to availability.</p>",
    "companyId": "COMP12345",
    "contactDetails": {
      "id": "jvzfKTNdE7OYXXXXXX",
      "name": "Contact Name",
      "phoneNo": "+911111111114",
      "email": "email@test.com",
      "address": {
        "countryCode": "US"
      }
    },
    "issueDate": "2023-06-15T00:00:00.000Z",
    "expiryDate": "2023-07-15T00:00:00.000Z",
    "sentBy": "user@example.com",
    "automaticTaxesCalculated": true,
    "meta": {
      "key": "value"
    },
    "estimateActionHistory": [
      {
        "action": "Created",
        "timestamp": "2023-06-15T10:00:00.000Z"
      }
    ],
    "sentTo": {
      "email": [
        "test@example.com"
      ],
      "phoneNo": [
        "+1 99444444444"
      ]
    },
    "frequencySettings": {
      "enabled": true,
      "schedule": {
        "executeAt": "string",
        "rrule": {
          "intervalType": "monthly",
          "interval": 2,
          "startDate": "2023-01-01",
          "startTime": "20:45:00",
          "endDate": "2029-11-01",
          "endTime": "18:45:00",
          "dayOfMonth": 15,
          "dayOfWeek": "mo",
          "numOfWeek": -1,
          "monthOfYear": "jan",
          "count": 10,
          "daysBefore": 5,
          "useStartAsPrimaryUserAccepted": true,
          "endType": "by"
        }
      }
    },
    "lastVisitedAt": "2023-06-20T08:30:00.000Z",
    "totalamountInUSD": 1500.75,
    "autoInvoice": {
      "enabled": true,
      "directPayments": false
    },
    "traceId": "010c7a01-857f-4619-970d-xyxyxyxy"
  },
  "invoice": {
    "_id": "6578278e879ad2646715ba9c",
    "status": "draft",
    "liveMode": false,
    "amountPaid": 0,
    "altId": "6578278e879ad2646715ba9c",
    "altType": "location",
    "name": "New Invoice",
    "businessDetails": {
      "name": "Alex",
      "address": {
        "addressLine1": "9931 Beechwood",
        "city": "St. Houston",
        "state": "TX",
        "countryCode": "USA",
        "postalCode": "559-6993"
      },
      "phoneNo": "+1-214-559-6993",
      "website": "www.example.com"
    },
    "invoiceNumber": "19",
    "currency": "USD",
    "contactDetails": {
      "id": "c6tZZU0rJBf30ZXx9Gli",
      "phoneNo": "+1-214-559-6993",
      "email": "alex@example.com",
      "customFields": [],
      "name": "Alex",
      "address": {
        "countryCode": "US"
      }
    },
    "issueDate": "2023-01-01",
    "dueDate": "2023-01-01",
    "discount": {
      "type": "percentage",
      "value": 0
    },
    "invoiceItems": [
      {
        "taxes": [],
        "_id": "c6tZZU0rJBf30ZXx9Gli",
        "productId": "c6tZZU0rJBf30ZXx9Gli",
        "priceId": "c6tZZU0rJBf30ZXx9Gli",
        "currency": "USD",
        "name": "Macbook Pro",
        "qty": 1,
        "amount": 999
      }
    ],
    "total": 999,
    "title": "INVOICE",
    "amountDue": 999,
    "createdAt": "2023-12-12T09:27:42.355Z",
    "updatedAt": "2023-12-12T09:27:42.355Z",
    "automaticTaxesEnabled": true,
    "automaticTaxesCalculated": true,
    "paymentSchedule": {}
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **estimate** | `dict` |  |
| **invoice** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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
  url: 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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
  'path': '/invoices/estimate/:estimateId/invoice',
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
  "markAsInvoiced": true,
  "version": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"markAsInvoiced\": true,
  \"version\": \"string\"
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
  url := "https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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

url = URI("https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "markAsInvoiced": true,
  "version": "string"
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
  "markAsInvoiced": true,
  "version": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId/invoice' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
