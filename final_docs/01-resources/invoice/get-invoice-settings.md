# Get Invoice Settings

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/settings` |
| **Scopes Required** | `invoices.readonly` |
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
| **altId** | `` | Yes | altType string required Possible values: [ location ] |
| **altType** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "termsNote": "Payment is due within 30 days.",
  "estimatesTermsNote": "This estimate is valid for 30 days.",
  "title": "INVOICE",
  "estimatesTitle": "ESTIMATE",
  "invoiceNumberPrefix": "INV-",
  "estimateNumberPrefix": "EST-",
  "dueAfterXDays": 30,
  "estimatesExpireAfterXDays": 30,
  "minimumPercentagePartialPayment": 25,
  "customFields": [
    "6578278e879ad2646715baxc",
    "6901e9fb77ac4d701ba0b996"
  ],
  "customNotification": {
    "customerSendInvoice": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamPaymentSuccess": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerPaymentSuccess": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamAutoPaymentSuccess": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerAutoPaymentSuccess": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamPaymentFailure": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerPaymentFailure": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamAutoPaymentFailure": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerAutoPaymentFailure": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerAutoPaymentInfo": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerAutoPaymentAmountChanged": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamAutoPaymentSkip": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamRecurringSendInvoiceFailed": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "customerSendEstimate": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamEstimateAccepted": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    },
    "teamEstimateDeclined": {
      "enabled": true,
      "emailTemplate": "string",
      "smsTemplate": "string",
      "fromName": "Alex",
      "fromEmail": "alex@example.com",
      "emailSubject": "Thank you for purchasing",
      "defaultEmailTemplateId": "dhwjqi2899012990w2u"
    }
  },
  "businessDetails": {
    "logoUrl": "string",
    "name": "string",
    "phoneNo": "string",
    "address": {
      "addressLine1": "string",
      "addressLine2": "string",
      "city": "string",
      "state": "string",
      "countryCode": "AF",
      "postalCode": "string"
    },
    "website": "string",
    "customValues": [
      "string"
    ]
  },
  "senderConfiguration": {
    "fromName": "Alex",
    "fromEmail": "alex@example.com"
  },
  "productSettings": {
    "enableImportProductDescription": true,
    "descriptionOptional": true
  },
  "reminderSettings": {
    "defaultEmailTemplateId": "dhwjqi2899012990w2u",
    "reminders": [
      {
        "enabled": true,
        "emailTemplate": "default",
        "smsTemplate": "default",
        "emailSubject": "Reminder",
        "reminderId": "9333e45f-a27d-4659-90e5-76c5ef06d094",
        "reminderName": "Special Reminder",
        "reminderTime": "before",
        "intervalType": "daily",
        "maxReminders": 3,
        "reminderInvoiceCondition": "invoice_sent",
        "reminderNumber": 10,
        "startTime": "9:00 AM",
        "endTime": "5:00 PM",
        "timezone": "businessTZ"
      }
    ]
  },
  "lateFeesConfiguration": {
    "enable": true,
    "value": 10,
    "type": "fixed",
    "frequency": {
      "intervalCount": 10,
      "interval": "day"
    },
    "grace": {
      "intervalCount": 10,
      "interval": "day"
    },
    "maxLateFees": {
      "type": "fixed",
      "value": "10"
    }
  },
  "tipsConfiguration": {
    "tipsPercentage": [
      5,
      10,
      15
    ],
    "tipsEnabled": true
  },
  "paymentMethods": {
    "stripe": {
      "enableBankDebitOnly": false
    }
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **termsNote** | `str` |  |
| **estimatesTermsNote** | `str` |  |
| **title** | `str` |  |
| **estimatesTitle** | `str` |  |
| **invoiceNumberPrefix** | `str` |  |
| **estimateNumberPrefix** | `str` |  |
| **dueAfterXDays** | `int` |  |
| **estimatesExpireAfterXDays** | `int` |  |
| **minimumPercentagePartialPayment** | `int` |  |
| **customFields** | `list` |  |
| **customNotification** | `dict` |  |
| **businessDetails** | `dict` |  |
| **senderConfiguration** | `dict` |  |
| **productSettings** | `dict` |  |
| **reminderSettings** | `dict` |  |
| **lateFeesConfiguration** | `dict` |  |
| **tipsConfiguration** | `dict` |  |
| **paymentMethods** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/invoices/settings \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/invoices/settings', {
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
  url: 'https://services.leadconnectorhq.com/invoices/settings',
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
  'path': '/invoices/settings',
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
  'url': 'https://services.leadconnectorhq.com/invoices/settings',
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

unirest('GET', 'https://services.leadconnectorhq.com/invoices/settings')
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

url = "https://services.leadconnectorhq.com/invoices/settings"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/invoices/settings', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/settings"))
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
  url := "https://services.leadconnectorhq.com/invoices/settings"
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

url = URI("https://services.leadconnectorhq.com/invoices/settings")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/settings' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
