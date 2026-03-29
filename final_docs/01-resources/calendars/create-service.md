# Create Service

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/services/catalog` |
| **Scopes Required** | `calendars.write` |
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
| **locationId** | `string` | No |  |
| **name** | `string` | No |  |
| **slug** | `string` | No |  |
| **staff** | `object[]` | Yes | Assigned staff members (at least one required) Array [ id string required Staff ID Example: 65e5f6dfacf123513228d384 ] |
| **id** | `string` | No |  |
| **description** | `string` | No |  |
| **eventColor** | `string` | No |  |
| **coverImage** | `string` | No |  |
| **serviceCategoryId** | `string` | No |  |
| **payment** | `object` | No | Payment details (default amount is 0, currency configured in Service Global Settings is used.) amount number Service price Example: 50 deposit number Deposit amount or percentage value Example: 20 depositType string Deposit type Possible values: [ percentage , amount ] Example: amount |
| **amount** | `number` | No |  |
| **deposit** | `number` | No |  |
| **depositType** | `string` | No |  |
| **serviceDuration** | `number` | No |  |
| **serviceDurationUnit** | `string` | No |  |
| **preBuffer** | `number` | No |  |
| **preBufferUnit** | `string` | No |  |
| **postBuffer** | `number` | No |  |
| **postBufferUnit** | `string` | No |  |
| **isPrivate** | `boolean` | No |  |
| **formId** | `string` | No |  |
| **variations** | `object[]` | Yes | Service variations (pass empty array for no variations) Array [ serviceDuration number This controls the duration of the appointment Example: 30 serviceDurationUnit string Duration unit Possible values: [ mins , hours ] Example: mins preBuffer number Pre-Buffer is additional time that can be added before an appointment, allowing for extra time to get ready Example: 10 preBufferUnit string Pre-buffer unit Possible values: [ mins , hours ] Example: mins postBuffer number Post-buffer: Additional time that can be added after an appointment, allowing for extra time to wrap up Example: 15 postBufferUnit string Post-buffer unit Possible values: [ mins , hours ] Example: mins payment object Payment details amount number Service price Example: 50 deposit number Deposit amount or percentage value Example: 20 depositType string Deposit type Possible values: [ percentage , amount ] Example: amount name string required Variation name Example: Standard Haircut ] |
| **serviceDuration** | `number` | No |  |
| **serviceDurationUnit** | `string` | No |  |
| **preBuffer** | `number` | No |  |
| **preBufferUnit** | `string` | No |  |
| **postBuffer** | `number` | No |  |
| **postBufferUnit** | `string` | No |  |
| **payment** | `object` | No | Payment details amount number Service price Example: 50 deposit number Deposit amount or percentage value Example: 20 depositType string Deposit type Possible values: [ percentage , amount ] Example: amount |
| **amount** | `number` | No |  |
| **deposit** | `number` | No |  |
| **depositType** | `string` | No |  |
| **name** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "service": {
    "id": "65e5f6dfacf123513228d384",
    "locationId": "0007BWpSzSwfiuSl0tR2",
    "name": "Hair Styling",
    "description": "Full hair styling session",
    "slug": "hair-styling",
    "eventColor": "#66C61C",
    "coverImage": "https://example.com/cover.jpg",
    "serviceCategoryId": "65e5f6dfacf123513228d381",
    "payment": {
      "amount": 50,
      "deposit": 20,
      "depositType": "amount"
    },
    "serviceDuration": 60,
    "serviceDurationUnit": "mins",
    "preBuffer": 10,
    "preBufferUnit": "mins",
    "postBuffer": 15,
    "postBufferUnit": "mins",
    "isPrivate": false,
    "formId": "65e5f6dfacf123513228d390",
    "variations": [
      {
        "id": "65e5f6dfacf123513228d384",
        "name": "Standard Haircut",
        "serviceDuration": 30,
        "serviceDurationUnit": "mins",
        "payment": {
          "amount": 50,
          "deposit": 20,
          "depositType": "amount"
        },
        "preBuffer": 10,
        "preBufferUnit": "mins",
        "postBuffer": 15,
        "postBufferUnit": "mins"
      }
    ],
    "staff": [
      {
        "id": "65e5f6dfacf123513228d384"
      }
    ]
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **service** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/calendars/services/catalog \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/calendars/services/catalog', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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
  url: 'https://services.leadconnectorhq.com/calendars/services/catalog',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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
  'path': '/calendars/services/catalog',
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
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/calendars/services/catalog',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/calendars/services/catalog')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/services/catalog"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/calendars/services/catalog', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/services/catalog"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"name\": \"string\",
  \"slug\": \"string\",
  \"staff\": \"string\",
  \"id\": \"string\",
  \"description\": \"string\",
  \"eventColor\": \"string\",
  \"coverImage\": \"string\",
  \"serviceCategoryId\": \"string\",
  \"payment\": \"string\",
  \"amount\": 123,
  \"deposit\": 123,
  \"depositType\": \"string\",
  \"serviceDuration\": 123,
  \"serviceDurationUnit\": \"string\",
  \"preBuffer\": 123,
  \"preBufferUnit\": \"string\",
  \"postBuffer\": 123,
  \"postBufferUnit\": \"string\",
  \"isPrivate\": true,
  \"formId\": \"string\",
  \"variations\": \"string\"
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
  url := "https://services.leadconnectorhq.com/calendars/services/catalog"
  payload := strings.NewReader(`{
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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

url = URI("https://services.leadconnectorhq.com/calendars/services/catalog")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
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
  "locationId": "string",
  "name": "string",
  "slug": "string",
  "staff": "string",
  "id": "string",
  "description": "string",
  "eventColor": "string",
  "coverImage": "string",
  "serviceCategoryId": "string",
  "payment": "string",
  "amount": 123,
  "deposit": 123,
  "depositType": "string",
  "serviceDuration": 123,
  "serviceDurationUnit": "string",
  "preBuffer": 123,
  "preBufferUnit": "string",
  "postBuffer": 123,
  "postBufferUnit": "string",
  "isPrivate": true,
  "formId": "string",
  "variations": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/services/catalog' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
