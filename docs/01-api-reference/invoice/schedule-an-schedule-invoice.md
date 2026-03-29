# Schedule an schedule invoice

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule` |
| **Scopes Required** | `invoices/schedule.write` |
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
| **scheduleId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **liveMode** | `boolean` | No |  |
| **autoPayment** | `object` | Yes | auto-payment configuration enable boolean required type string paymentMethodId string customerId string card object brand string required last4 string required usBankAccount object bank_name string required last4 string required sepaDirectDebit object bank_code string required last4 string required branch_code string required bacsDirectDebit object sort_code string required last4 string required becsDirectDebit object bsb_number string required last4 string required cardId string provider object |
| **enable** | `boolean` | No |  |
| **type** | `string` | No |  |
| **paymentMethodId** | `string` | No |  |
| **customerId** | `string` | No |  |
| **card** | `object` | Yes | brand string required last4 string required |
| **brand** | `string` | No |  |
| **last4** | `string` | No |  |
| **usBankAccount** | `object` | Yes | bank_name string required last4 string required |
| **bank_name** | `string` | No |  |
| **last4** | `string` | No |  |
| **sepaDirectDebit** | `object` | Yes | bank_code string required last4 string required branch_code string required |
| **bank_code** | `string` | No |  |
| **last4** | `string` | No |  |
| **branch_code** | `string` | No |  |
| **bacsDirectDebit** | `object` | Yes | sort_code string required last4 string required |
| **sort_code** | `string` | No |  |
| **last4** | `string` | No |  |
| **becsDirectDebit** | `object` | Yes | bsb_number string required last4 string required |
| **bsb_number** | `string` | No |  |
| **last4** | `string` | No |  |
| **cardId** | `string` | No |  |
| **provider** | `object` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
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
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **status** | `str` |  |
| **liveMode** | `bool` |  |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **name** | `str` |  |
| **schedule** | `dict` |  |
| **invoices** | `list` |  |
| **businessDetails** | `dict` |  |
| **currency** | `str` |  |
| **contactDetails** | `dict` |  |
| **discount** | `dict` |  |
| **items** | `list` |  |
| **total** | `int` |  |
| **title** | `str` |  |
| **termsNotes** | `str` |  |
| **compiledTermsNotes** | `str` |  |
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
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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
  url: 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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
  'path': '/invoices/schedule/:scheduleId/schedule',
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
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"liveMode\": true,
  \"autoPayment\": \"string\",
  \"enable\": true,
  \"type\": \"string\",
  \"paymentMethodId\": \"string\",
  \"customerId\": \"string\",
  \"card\": \"string\",
  \"brand\": \"string\",
  \"last4\": \"string\",
  \"usBankAccount\": \"string\",
  \"bank_name\": \"string\",
  \"sepaDirectDebit\": \"string\",
  \"bank_code\": \"string\",
  \"branch_code\": \"string\",
  \"bacsDirectDebit\": \"string\",
  \"sort_code\": \"string\",
  \"becsDirectDebit\": \"string\",
  \"bsb_number\": \"string\",
  \"cardId\": \"string\",
  \"provider\": \"string\"
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
  url := "https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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

url = URI("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
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
  "liveMode": true,
  "autoPayment": "string",
  "enable": true,
  "type": "string",
  "paymentMethodId": "string",
  "customerId": "string",
  "card": "string",
  "brand": "string",
  "last4": "string",
  "usBankAccount": "string",
  "bank_name": "string",
  "sepaDirectDebit": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bacsDirectDebit": "string",
  "sort_code": "string",
  "becsDirectDebit": "string",
  "bsb_number": "string",
  "cardId": "string",
  "provider": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
