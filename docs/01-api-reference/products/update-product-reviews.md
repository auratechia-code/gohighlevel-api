# Update Product Reviews

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/products/reviews/:reviewId` |
| **Scopes Required** | `products.write` |
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
| **reviewId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **productId** | `string` | No |  |
| **status** | `string` | No |  |
| **reply** | `object[]` | Yes | Reply of the review Array [ headline string required Headline of the Review Possible values: <= 200 characters Example: Amazing product with great quality comment string required Detailed Review of the product Possible values: <= 5000 characters Example: This product exceeded my expectations in terms of quality and performance. Highly recommended! user object User who is giving the review/reply name string required Name of the customer Possible values: non-empty and <= 100 characters Example: John Doe email string required Email of the customer Example: example@example.com phone string Phone no of the customer Example: +1-555-555-5555 isCustomer boolean Is the person an admin or customer Example: true ] |
| **headline** | `string` | No |  |
| **comment** | `string` | No |  |
| **user** | `object` | Yes | User who is giving the review/reply name string required Name of the customer Possible values: non-empty and <= 100 characters Example: John Doe email string required Email of the customer Example: example@example.com phone string Phone no of the customer Example: +1-555-555-5555 isCustomer boolean Is the person an admin or customer Example: true |
| **name** | `string` | No |  |
| **email** | `string` | No |  |
| **phone** | `string` | No |  |
| **isCustomer** | `boolean` | No |  |
| **rating** | `number` | No |  |
| **headline** | `string` | No |  |
| **detail** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "status": true,
  "message": "Successfully created"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **status** | `bool` |  |
| **message** | `str` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/products/reviews/:reviewId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/products/reviews/:reviewId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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
  method: 'put',
  url: 'https://services.leadconnectorhq.com/products/reviews/:reviewId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/products/reviews/:reviewId',
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
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/products/reviews/:reviewId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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

unirest('PUT', 'https://services.leadconnectorhq.com/products/reviews/:reviewId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/products/reviews/:reviewId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/products/reviews/:reviewId', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/products/reviews/:reviewId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"productId\": \"string\",
  \"status\": \"string\",
  \"reply\": \"string\",
  \"headline\": \"string\",
  \"comment\": \"string\",
  \"user\": \"string\",
  \"name\": \"string\",
  \"email\": \"string\",
  \"phone\": \"string\",
  \"isCustomer\": true,
  \"rating\": 123,
  \"detail\": \"string\"
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
  url := "https://services.leadconnectorhq.com/products/reviews/:reviewId"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
}`)
  req, _ := http.NewRequest("PUT", url, payload)
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

url = URI("https://services.leadconnectorhq.com/products/reviews/:reviewId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
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
  "productId": "string",
  "status": "string",
  "reply": "string",
  "headline": "string",
  "comment": "string",
  "user": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "isCustomer": true,
  "rating": 123,
  "detail": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/reviews/:reviewId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
