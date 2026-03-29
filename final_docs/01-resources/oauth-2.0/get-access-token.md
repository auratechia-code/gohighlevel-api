# Get Access Token

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/oauth/token` |
| **Scopes Required** | `N/A` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `string` | Yes | API version. Use `2021-07-28`. |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **client_id** | `string` | No |  |
| **client_secret** | `string` | No |  |
| **grant_type** | `string` | No |  |
| **code** | `string` | No |  |
| **refresh_token** | `string` | No |  |
| **user_type** | `string` | No |  |
| **redirect_uri** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",
  "token_type": "Bearer",
  "expires_in": 86399,
  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",
  "scope": "conversations/message.readonly conversations/message.write",
  "userType": "Location",
  "locationId": "l1C08ntBrFjLS0elLIYU",
  "companyId": "l1C08ntBrFjLS0elLIYU",
  "approvedLocations": [
    "l1C08ntBrFjLS0elLIYU"
  ],
  "userId": "l1C08ntBrFjLS0elLIYU",
  "planId": "l1C08ntBrFjLS0elLIYU",
  "isBulkInstallation": "Bearer",
  "installToFutureLocations": true,
  "approveAllLocations": true
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **access_token** | `str` |  |
| **token_type** | `str` |  |
| **expires_in** | `int` |  |
| **refresh_token** | `str` |  |
| **scope** | `str` |  |
| **userType** | `str` |  |
| **locationId** | `str` |  |
| **companyId** | `str` |  |
| **approvedLocations** | `list` |  |
| **userId** | `str` |  |
| **planId** | `str` |  |
| **isBulkInstallation** | `str` |  |
| **installToFutureLocations** | `bool` |  |
| **approveAllLocations** | `bool` |  |

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
  --url https://services.leadconnectorhq.com/oauth/token \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/oauth/token', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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
  url: 'https://services.leadconnectorhq.com/oauth/token',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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
  'path': '/oauth/token',
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
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/oauth/token',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/oauth/token')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/oauth/token"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/oauth/token', [
  'headers' => $headers,
  'body' => '{
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/oauth/token"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"client_id\": \"string\",
  \"client_secret\": \"string\",
  \"grant_type\": \"string\",
  \"code\": \"string\",
  \"refresh_token\": \"string\",
  \"user_type\": \"string\",
  \"redirect_uri\": \"string\"
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
  url := "https://services.leadconnectorhq.com/oauth/token"
  payload := strings.NewReader(`{
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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

url = URI("https://services.leadconnectorhq.com/oauth/token")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
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
  "client_id": "string",
  "client_secret": "string",
  "grant_type": "string",
  "code": "string",
  "refresh_token": "string",
  "user_type": "string",
  "redirect_uri": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/oauth/token' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
