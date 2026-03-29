# Set google business locations

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId` |
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
| **locationId** | `` | Yes | accountId string required Account Id Example: w37swmmLbA02zgqKPpxITe |
| **accountId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **location** | `object` | Yes | name string required Location name storeCode string Store code title string required Location title storefrontAddress object Storefront address details metadata object Additional metadata maxLocation boolean Whether this is a max location isVerified boolean Whether the location is verified isConnected boolean Whether the location is connected |
| **name** | `string` | No |  |
| **storeCode** | `string` | No |  |
| **title** | `string` | No |  |
| **storefrontAddress** | `object` | No |  |
| **metadata** | `object` | No |  |
| **maxLocation** | `boolean` | No |  |
| **isVerified** | `boolean` | No |  |
| **isConnected** | `boolean` | No |  |
| **account** | `object` | Yes | name string required Account name identifier accountName string required Display name of the account type string required Type of the account verificationState string required State of account verification vettedState string required Vetting state of the account |
| **name** | `string` | No |  |
| **accountName** | `string` | No |  |
| **type** | `string` | No |  |
| **verificationState** | `string` | No |  |
| **vettedState** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true,
  "statusCode": 201,
  "message": "Added Google Business Account",
  "results": {
    "_id": "65f2d989a4f2f1e5322c3856",
    "oAuthId": "u37swmmLbA02zgqKPpxITe2",
    "locationId": "u37swmmLbA02zgqKPpxITe2",
    "platform": "google",
    "type": "location",
    "name": "Account Name",
    "active": true
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **statusCode** | `int` |  |
| **message** | `str` |  |
| **results** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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
  url: 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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
  'path': '/social-media-posting/oauth/:locationId/google/locations/:accountId',
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
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId', [
  'headers' => $headers,
  'body' => '{
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"location\": \"string\",
  \"name\": \"string\",
  \"storeCode\": \"string\",
  \"title\": \"string\",
  \"storefrontAddress\": \"string\",
  \"metadata\": \"string\",
  \"maxLocation\": true,
  \"isVerified\": true,
  \"isConnected\": true,
  \"account\": \"string\",
  \"accountName\": \"string\",
  \"type\": \"string\",
  \"verificationState\": \"string\",
  \"vettedState\": \"string\"
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
  url := "https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId"
  payload := strings.NewReader(`{
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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

url = URI("https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
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
  "location": "string",
  "name": "string",
  "storeCode": "string",
  "title": "string",
  "storefrontAddress": "string",
  "metadata": "string",
  "maxLocation": true,
  "isVerified": true,
  "isConnected": true,
  "account": "string",
  "accountName": "string",
  "type": "string",
  "verificationState": "string",
  "vettedState": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/oauth/:locationId/google/locations/:accountId' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
