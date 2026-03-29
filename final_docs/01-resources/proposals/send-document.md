# Send document

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/proposals/document/send` |
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

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **documentId** | `string` | No |  |
| **documentName** | `string` | No |  |
| **medium** | `string` | No |  |
| **ccRecipients** | `object[]` | Yes | CC Recipient Array [ email string required Email Example: jim@gmail.com id string required Contact ID Example: contactId imageUrl string required Contact Image URL Example: https://example.com/image.jpg contactName string required Contact Name Example: Jim Anton firstName string required First Name Example: Jim lastName string required Last Name Example: Anton ] |
| **email** | `string` | No |  |
| **id** | `string` | No |  |
| **imageUrl** | `string` | No |  |
| **contactName** | `string` | No |  |
| **firstName** | `string` | No |  |
| **lastName** | `string` | No |  |
| **notificationSettings** | `object` | Yes | receive object required templateId string required subject string required sender object required fromEmail string required fromName string required |
| **receive** | `object` | Yes | templateId string required subject string required |
| **templateId** | `string` | No |  |
| **subject** | `string` | No |  |
| **sender** | `object` | Yes | fromEmail string required fromName string required |
| **fromEmail** | `string` | No |  |
| **fromName** | `string` | No |  |
| **sentBy** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true,
  "links": [
    {
      "referenceId": "550e8400-e29b-41d4-a716-446655440000",
      "documentId": "c1e87a91-93b2-4b78-821f-85cf0e1f925b",
      "recipientId": "u240JcS0E5qE0ziHnwMm",
      "entityName": "contacts",
      "recipientCategory": "recipient",
      "documentRevision": 1,
      "createdBy": "b6d8fa28-1112-4dc7-b9d2-f22b75a477ea",
      "deleted": false
    }
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **links** | `list` |  |

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
  --url https://services.leadconnectorhq.com/proposals/document/send \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/proposals/document/send', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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
  url: 'https://services.leadconnectorhq.com/proposals/document/send',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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
  'path': '/proposals/document/send',
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
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/proposals/document/send',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/proposals/document/send')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/proposals/document/send"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/proposals/document/send', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/proposals/document/send"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"documentId\": \"string\",
  \"documentName\": \"string\",
  \"medium\": \"string\",
  \"ccRecipients\": \"string\",
  \"email\": \"string\",
  \"id\": \"string\",
  \"imageUrl\": \"string\",
  \"contactName\": \"string\",
  \"firstName\": \"string\",
  \"lastName\": \"string\",
  \"notificationSettings\": \"string\",
  \"receive\": \"string\",
  \"templateId\": \"string\",
  \"subject\": \"string\",
  \"sender\": \"string\",
  \"fromEmail\": \"string\",
  \"fromName\": \"string\",
  \"sentBy\": \"string\"
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
  url := "https://services.leadconnectorhq.com/proposals/document/send"
  payload := strings.NewReader(`{
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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

url = URI("https://services.leadconnectorhq.com/proposals/document/send")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
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
  "documentId": "string",
  "documentName": "string",
  "medium": "string",
  "ccRecipients": "string",
  "email": "string",
  "id": "string",
  "imageUrl": "string",
  "contactName": "string",
  "firstName": "string",
  "lastName": "string",
  "notificationSettings": "string",
  "receive": "string",
  "templateId": "string",
  "subject": "string",
  "sender": "string",
  "fromEmail": "string",
  "fromName": "string",
  "sentBy": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/proposals/document/send' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
