# Update template late fees configuration

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PATCH |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration` |
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
| **templateId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **lateFeesConfiguration** | `object` | Yes | late fees configuration enable boolean required Enable late fees Example: true value number required Late Fees Value Example: 10 type string required Late Fees Type Possible values: [ fixed , percentage ] Example: fixed frequency object required Late Fees Frequency intervalCount number required Late fees interval count Example: 10 interval string required Late fees interval Possible values: [ minute , hour , day , week , month , one_time ] Example: day grace object Late Fees Grace intervalCount number required Late fees grace interval count Example: 10 interval string required Late fees grace interval Possible values: [ day ] Example: day maxLateFees object Max late fees payable type string required Possible values: [ fixed ] Example: fixed value number required Max late fees to pay Example: 10 |
| **enable** | `boolean` | No |  |
| **value** | `number` | No |  |
| **type** | `string` | No |  |
| **frequency** | `object` | Yes | Late Fees Frequency intervalCount number required Late fees interval count Example: 10 interval string required Late fees interval Possible values: [ minute , hour , day , week , month , one_time ] Example: day |
| **intervalCount** | `number` | No |  |
| **interval** | `string` | No |  |
| **grace** | `object` | Yes | Late Fees Grace intervalCount number required Late fees grace interval count Example: 10 interval string required Late fees grace interval Possible values: [ day ] Example: day |
| **intervalCount** | `number` | No |  |
| **interval** | `string` | No |  |
| **maxLateFees** | `object` | Yes | Max late fees payable type string required Possible values: [ fixed ] Example: fixed value number required Max late fees to pay Example: 10 |
| **type** | `string` | No |  |
| **value** | `number` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "_id": "6578278e879ad2646715ba9c",
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "New Template",
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
  "invoiceNumberPrefix": "INV-",
  "total": 999,
  "createdAt": "2023-12-12T09:27:42.355Z",
  "updatedAt": "2023-12-12T09:27:42.355Z"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **name** | `str` |  |
| **businessDetails** | `dict` |  |
| **currency** | `str` |  |
| **discount** | `dict` |  |
| **items** | `list` |  |
| **invoiceNumberPrefix** | `str` |  |
| **total** | `int` |  |
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
curl --request PATCH \
  --url https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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
    const response = await ghl.api.request('PATCH', 'https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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
  url: 'https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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
  'path': '/invoices/template/:templateId/late-fees-configuration',
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
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PATCH',
  'url': 'https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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

unirest('PATCH', 'https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PATCH", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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
$response = $client->request('PATCH', 'https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PATCH", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"lateFeesConfiguration\": \"string\",
  \"enable\": true,
  \"value\": 123,
  \"type\": \"string\",
  \"frequency\": \"string\",
  \"intervalCount\": 123,
  \"interval\": \"string\",
  \"grace\": \"string\",
  \"maxLateFees\": \"string\"
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
  url := "https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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

url = URI("https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
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
  "lateFeesConfiguration": "string",
  "enable": true,
  "value": 123,
  "type": "string",
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/template/:templateId/late-fees-configuration' -Method 'PATCH' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
