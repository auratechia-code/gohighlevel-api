# Record Order Payment

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment` |
| **Scopes Required** | `payments/orders.collectPayment` |
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
| **orderId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **mode** | `string` | No |  |
| **card** | `object` | Yes | Details of Card if used for payment type string required Possible values: [ visa , mastercard , other ] Example: mastercard last4 string required Last 4 digit of the card Example: 1234 |
| **type** | `string` | No |  |
| **last4** | `string` | No |  |
| **cheque** | `object` | Yes | Details of the Cheque if used for payment number string required check number Example: 129-129-129-912 |
| **number** | `string` | No |  |
| **notes** | `string` | No |  |
| **amount** | `number` | No |  |
| **meta** | `object` | No |  |
| **isPartialPayment** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |

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
  --url https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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
  url: 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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
  'path': '/payments/orders/:orderId/record-payment',
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
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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

unirest('POST', 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"mode\": \"string\",
  \"card\": \"string\",
  \"type\": \"string\",
  \"last4\": \"string\",
  \"cheque\": \"string\",
  \"number\": \"string\",
  \"notes\": \"string\",
  \"amount\": 123,
  \"meta\": \"string\",
  \"isPartialPayment\": true
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
  url := "https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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

url = URI("https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
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
  "mode": "string",
  "card": "string",
  "type": "string",
  "last4": "string",
  "cheque": "string",
  "number": "string",
  "notes": "string",
  "amount": 123,
  "meta": "string",
  "isPartialPayment": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/orders/:orderId/record-payment' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
