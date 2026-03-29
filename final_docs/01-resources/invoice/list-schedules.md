# List schedules

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/schedule` |
| **Scopes Required** | `invoices/schedule.readonly` |
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
| **altType** | `` | No | status string status to be filtered |
| **status** | `` | No | startAt string startAt in YYYY-MM-DD format Example: 2023-01-01 |
| **startAt** | `` | No | endAt string endAt in YYYY-MM-DD format Example: 2023-01-01 |
| **endAt** | `` | No | search string To search for an invoice by id / name / email / phoneNo Example: Alex |
| **search** | `` | No | paymentMode string Possible values: [ default , live , test ] payment mode Example: live |
| **paymentMode** | `` | Yes | limit string required Limit the number of items to return Example: 10 |
| **limit** | `` | Yes | offset string required Number of items to skip Example: 10 |
| **offset** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "schedules": [
    {
      "_id": "6578278e879ad2646715ba9c",
      "status": "draft",
      "liveMode": false,
      "altId": "6578278e879ad2646715ba9c",
      "altType": "location",
      "name": "New Invoice",
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
      },
      "invoices": [
        {
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
      ],
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
      "discount": {
        "type": "percentage",
        "value": 0
      },
      "items": [
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
      "termsNotes": "Confidential",
      "compiledTermsNotes": "Confidential",
      "createdAt": "2023-12-12T09:27:42.355Z",
      "updatedAt": "2023-12-12T09:27:42.355Z"
    }
  ],
  "total": 100
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **schedules** | `list` |  |
| **total** | `int` |  |

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
  --url https://services.leadconnectorhq.com/invoices/schedule \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/invoices/schedule', {
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
  url: 'https://services.leadconnectorhq.com/invoices/schedule',
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
  'path': '/invoices/schedule',
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
  'url': 'https://services.leadconnectorhq.com/invoices/schedule',
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

unirest('GET', 'https://services.leadconnectorhq.com/invoices/schedule')
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

url = "https://services.leadconnectorhq.com/invoices/schedule"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/invoices/schedule', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/schedule"))
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
  url := "https://services.leadconnectorhq.com/invoices/schedule"
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

url = URI("https://services.leadconnectorhq.com/invoices/schedule")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/schedule' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
