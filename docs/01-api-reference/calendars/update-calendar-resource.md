# Update Calendar Resource

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id` |
| **Scopes Required** | `calendars/resources.write` |
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
| **resourceType** | `` | Yes | id string required Calendar Resource ID |
| **id** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **name** | `string` | No |  |
| **description** | `string` | No |  |
| **quantity** | `number` | No |  |
| **outOfService** | `number` | No |  |
| **capacity** | `number` | No |  |
| **calendarIds** | `string[]` | No |  |
| **isActive** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "locationId": "string",
  "name": "yoga room",
  "resourceType": "equipments",
  "isActive": true,
  "description": "string",
  "quantity": 0,
  "outOfService": 0,
  "capacity": 85
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **locationId** | `str` |  |
| **name** | `str` |  |
| **resourceType** | `str` |  |
| **isActive** | `bool` |  |
| **description** | `str` |  |
| **quantity** | `int` |  |
| **outOfService** | `int` |  |
| **capacity** | `int` |  |

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
  --url https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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
  url: 'https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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
  'path': '/calendars/resources/:resourceType/:id',
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
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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

unirest('PUT', 'https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"name\": \"string\",
  \"description\": \"string\",
  \"quantity\": 123,
  \"outOfService\": 123,
  \"capacity\": 123,
  \"calendarIds\": \"string\",
  \"isActive\": true
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
  url := "https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id"
  payload := strings.NewReader(`{
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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

url = URI("https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "name": "string",
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
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
  "description": "string",
  "quantity": 123,
  "outOfService": 123,
  "capacity": 123,
  "calendarIds": "string",
  "isActive": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/resources/:resourceType/:id' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
