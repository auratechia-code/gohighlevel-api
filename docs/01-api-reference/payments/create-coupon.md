# Create Coupon

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/payments/coupon` |
| **Scopes Required** | `payments/coupons.write` |
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
| **name** | `string` | No |  |
| **code** | `string` | No |  |
| **discountType** | `string` | No |  |
| **discountValue** | `number` | No |  |
| **startDate** | `string` | No |  |
| **endDate** | `string` | No |  |
| **usageLimit** | `number` | No |  |
| **productIds** | `string[]` | No |  |
| **priceIds** | `string[]` | No |  |
| **variantIds** | `string[]` | No |  |
| **applyToFuturePayments** | `boolean` | No |  |
| **applyToFuturePaymentsConfig** | `object` | Yes | If coupon is applicable on upcoming subscription transactions, how many months should it be applicable for a subscription type string required Type of the config Possible values: [ forever , fixed ] Example: forever | fixed duration number required Duration the coupon to be applied in a subscription Example: 5 durationType string required Type of the duration Possible values: [ months ] Example: months |
| **type** | `string` | No |  |
| **duration** | `number` | No |  |
| **durationType** | `string` | No |  |
| **limitPerCustomer** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
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
  "userId": "q0m15dTLGeiGOXG123123",
  "createdAt": "2025-04-09T18:49:22.026Z",
  "updatedAt": "2025-04-09T18:49:22.026Z",
  "traceId": "c667b18d-8f5e-44cf-a914"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **usageCount** | `int` |  |
| **limitPerCustomer** | `int` |  |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **name** | `str` |  |
| **code** | `str` |  |
| **discountType** | `str` |  |
| **discountValue** | `int` |  |
| **status** | `str` |  |
| **startDate** | `str` |  |
| **endDate** | `str` |  |
| **applyToFuturePayments** | `bool` |  |
| **applyToFuturePaymentsConfig** | `dict` |  |
| **userId** | `str` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |
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
curl --request POST \
  --url https://services.leadconnectorhq.com/payments/coupon \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/payments/coupon', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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
  url: 'https://services.leadconnectorhq.com/payments/coupon',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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
  'path': '/payments/coupon',
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
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/payments/coupon',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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

unirest('POST', 'https://services.leadconnectorhq.com/payments/coupon')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/payments/coupon"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/payments/coupon', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/payments/coupon"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"name\": \"string\",
  \"code\": \"string\",
  \"discountType\": \"string\",
  \"discountValue\": 123,
  \"startDate\": \"string\",
  \"endDate\": \"string\",
  \"usageLimit\": 123,
  \"productIds\": \"string\",
  \"priceIds\": \"string\",
  \"variantIds\": \"string\",
  \"applyToFuturePayments\": true,
  \"applyToFuturePaymentsConfig\": \"string\",
  \"type\": \"string\",
  \"duration\": 123,
  \"durationType\": \"string\",
  \"limitPerCustomer\": true
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
  url := "https://services.leadconnectorhq.com/payments/coupon"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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

url = URI("https://services.leadconnectorhq.com/payments/coupon")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
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
  "name": "string",
  "code": "string",
  "discountType": "string",
  "discountValue": 123,
  "startDate": "string",
  "endDate": "string",
  "usageLimit": 123,
  "productIds": "string",
  "priceIds": "string",
  "variantIds": "string",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": "string",
  "type": "string",
  "duration": 123,
  "durationType": "string",
  "limitPerCustomer": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/coupon' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
