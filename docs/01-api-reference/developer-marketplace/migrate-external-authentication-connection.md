# Migrate external authentication connection

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/marketplace/external-auth/migration` |
| **Scopes Required** | `marketplace-external-auth-migration.write` |
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
| **type** | `string` | No |  |
| **locationId** | `string` | No |  |
| **appId** | `string` | No |  |
| **appVersionId** | `string` | No |  |
| **accountId** | `string` | No |  |
| **apiKey** | `string` | No |  |
| **basicCredentials** | `object` | No |  |
| **accessToken** | `string` | No |  |
| **refreshToken** | `string` | No |  |
| **expiryIn** | `number` | No |  |
| **expiryAt** | `number` | No |  |
| **scopes** | `string[]` | No |  |
| **displayName** | `string` | No |  |
| **isDefault** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true,
  "identifier": "migration_12345",
  "message": "Connection migrated successfully"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **identifier** | `str` |  |
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
curl --request POST \
  --url https://services.leadconnectorhq.com/marketplace/external-auth/migration \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/marketplace/external-auth/migration', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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
  url: 'https://services.leadconnectorhq.com/marketplace/external-auth/migration',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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
  'path': '/marketplace/external-auth/migration',
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
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/marketplace/external-auth/migration',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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

unirest('POST', 'https://services.leadconnectorhq.com/marketplace/external-auth/migration')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/marketplace/external-auth/migration"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/marketplace/external-auth/migration', [
  'headers' => $headers,
  'body' => '{
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/marketplace/external-auth/migration"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"type\": \"string\",
  \"locationId\": \"string\",
  \"appId\": \"string\",
  \"appVersionId\": \"string\",
  \"accountId\": \"string\",
  \"apiKey\": \"string\",
  \"basicCredentials\": \"string\",
  \"accessToken\": \"string\",
  \"refreshToken\": \"string\",
  \"expiryIn\": 123,
  \"expiryAt\": 123,
  \"scopes\": \"string\",
  \"displayName\": \"string\",
  \"isDefault\": true
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
  url := "https://services.leadconnectorhq.com/marketplace/external-auth/migration"
  payload := strings.NewReader(`{
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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

url = URI("https://services.leadconnectorhq.com/marketplace/external-auth/migration")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
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
  "type": "string",
  "locationId": "string",
  "appId": "string",
  "appVersionId": "string",
  "accountId": "string",
  "apiKey": "string",
  "basicCredentials": "string",
  "accessToken": "string",
  "refreshToken": "string",
  "expiryIn": 123,
  "expiryAt": 123,
  "scopes": "string",
  "displayName": "string",
  "isDefault": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/marketplace/external-auth/migration' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
