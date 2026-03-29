# Get Transaction by ID

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/payments/transactions/:transactionId` |
| **Scopes Required** | `payments/transactions.readonly` |
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
| **transactionId** | `` | No |  |

### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `` | Yes | altId string required AltId is the unique identifier e.g: location id. Example: 3SwdhCu3svxI8AKsPJt6 |
| **altId** | `` | Yes | altType string required AltType is the type of identifier. Example: location |
| **altType** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "_id": "61dd0feac077f72010f78804",
  "altType": "location",
  "altId": "3SwdhCu3svxI8AKsPJt6",
  "contactId": "XPLSw2SVagl12LMDeTmQ",
  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",
  "currency": "USD",
  "amount": "100",
  "status": "succeeded",
  "liveMode": "false",
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "entityType": "order",
  "entityId": "61dd0fe9c077f73e67f78803",
  "entitySource": "{ type: \"funnel\", id: \"BDBMEghdIUaqMPEsK349\", subType: \"two_step_order_form\", name: \"new funnel\" }",
  "chargeId": "in_1KGcXDCScnf89tZohCsmImwE",
  "chargeSnapshot": "{ id: \"in_1KGcXDCScnf89tZohCsmImwE\", object: \"invoice\", account_country: \"US\",  account_name:  \"GHL-Testing\" }",
  "invoiceId": "in_1KGcXDCScnf89tZohCsmImwE",
  "subscriptionId": "sub_1KGcXDCScnf89tZoVkoEMCEL",
  "paymentProvider": "{ type: \"stripe\", connectedAccount: { _id: \"612ca676b484b241fef9d962\", accountId: \"acct_1Ihw53CScnf89tZo\" } }",
  "ipAddress": "107.178.194.224",
  "meta": "{ stepId: \"af7c731e-e36f-4152-bd1a-3f69a31d6d6d\", pageId: \"A8ltotc2jZxurJba4e3Y\", pageUrl: \"/v2/preview/A8ltotc2jZxurJba4e3Y\" }",
  "markAsTest": "false",
  "isParent": "false",
  "amountRefunded": "10",
  "receiptId": "6492fbea489bc07892c6defb",
  "qboSynced": "false",
  "qboResponse": "{ domain: \"QBO\", sparse: false, Id: \"180\", SyncToken: \"0\", TotalAmt: 25 }",
  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",
  "mergedFromContactId": "XPLSw2SVagl12LMDeTmQ",
  "createdBy": "user123"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **altType** | `str` |  |
| **altId** | `str` |  |
| **contactId** | `str` |  |
| **contactSnapshot** | `str` |  |
| **currency** | `str` |  |
| **amount** | `str` |  |
| **status** | `str` |  |
| **liveMode** | `str` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |
| **entityType** | `str` |  |
| **entityId** | `str` |  |
| **entitySource** | `str` |  |
| **chargeId** | `str` |  |
| **chargeSnapshot** | `str` |  |
| **invoiceId** | `str` |  |
| **subscriptionId** | `str` |  |
| **paymentProvider** | `str` |  |
| **ipAddress** | `str` |  |
| **meta** | `str` |  |
| **markAsTest** | `str` |  |
| **isParent** | `str` |  |
| **amountRefunded** | `str` |  |
| **receiptId** | `str` |  |
| **qboSynced** | `str` |  |
| **qboResponse** | `str` |  |
| **traceId** | `str` |  |
| **mergedFromContactId** | `str` |  |
| **createdBy** | `str` |  |

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
  --url https://services.leadconnectorhq.com/payments/transactions/:transactionId \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/payments/transactions/:transactionId', {
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
  url: 'https://services.leadconnectorhq.com/payments/transactions/:transactionId',
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
  'path': '/payments/transactions/:transactionId',
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
  'url': 'https://services.leadconnectorhq.com/payments/transactions/:transactionId',
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

unirest('GET', 'https://services.leadconnectorhq.com/payments/transactions/:transactionId')
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

url = "https://services.leadconnectorhq.com/payments/transactions/:transactionId"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/payments/transactions/:transactionId', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/payments/transactions/:transactionId"))
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
  url := "https://services.leadconnectorhq.com/payments/transactions/:transactionId"
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

url = URI("https://services.leadconnectorhq.com/payments/transactions/:transactionId")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/transactions/:transactionId' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
