# Create a new category queue

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/social-media-posting/category/queues` |
| **Scopes Required** | `socialplanner/category.write` |
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
| **categoryId** | `string` | No |  |
| **timeSlots** | `object[]` | Yes | Array [ dayOfWeek number required Day of the week (0-6) Example: 0 time string required Time in HH:mm format Example: 09:00 ] |
| **dayOfWeek** | `number` | No |  |
| **time** | `string` | No |  |
| **enableFuturePosts** | `boolean` | No |  |
| **prioritizeNewContent** | `boolean` | No |  |
| **userId** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true,
  "statusCode": 201,
  "results": {
    "message": "Queue created successfully",
    "queue": {
      "_id": "686ebf10c78c233e45c28d66",
      "locationId": "Qp26qppJgfrTZis7jsBy",
      "categoryId": "683702938b19583ce320e5eb",
      "timeSlots": [
        {
          "_id": "686ebf10c78c23d665c28d67",
          "dayOfWeek": 0,
          "time": "00:00"
        }
      ],
      "enableFuturePosts": true,
      "prioritizeNewContent": true,
      "status": "draft",
      "startDate": "2025-07-09T19:12:16.363Z",
      "skipDateTime": [],
      "totalPosts": 0,
      "lastScheduledTime": null,
      "createdBy": "uefV3MmLHs2sjJr2KfmL",
      "createdAt": "2025-07-09T19:12:16.366Z",
      "updatedAt": "2025-07-09T19:12:16.366Z"
    }
  },
  "traceId": "string"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **statusCode** | `int` |  |
| **results** | `dict` |  |
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
  --url https://services.leadconnectorhq.com/social-media-posting/category/queues \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/social-media-posting/category/queues', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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
  url: 'https://services.leadconnectorhq.com/social-media-posting/category/queues',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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
  'path': '/social-media-posting/category/queues',
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
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/social-media-posting/category/queues',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/social-media-posting/category/queues')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/social-media-posting/category/queues"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/social-media-posting/category/queues', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/social-media-posting/category/queues"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"categoryId\": \"string\",
  \"timeSlots\": \"string\",
  \"dayOfWeek\": 123,
  \"time\": \"string\",
  \"enableFuturePosts\": true,
  \"prioritizeNewContent\": true,
  \"userId\": \"string\"
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
  url := "https://services.leadconnectorhq.com/social-media-posting/category/queues"
  payload := strings.NewReader(`{
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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

url = URI("https://services.leadconnectorhq.com/social-media-posting/category/queues")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
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
  "categoryId": "string",
  "timeSlots": "string",
  "dayOfWeek": 123,
  "time": "string",
  "enableFuturePosts": true,
  "prioritizeNewContent": true,
  "userId": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/category/queues' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
