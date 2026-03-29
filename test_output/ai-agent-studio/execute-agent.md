# Execute Agent

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute` |
| **Scopes Required** | `agent-studio.write` |
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
| **agentId** | `` | No |  |

### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **source** | `` | No |  |

### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **message** | `string` | No |  |
| **executionId** | `string` | No |  |
| **inputVariables** | `object` | No |  |
| **versionId** | `string` | No |  |
| **attachments** | `object[]` | Yes | Attachments for the message Array [ type string required Type of attachment Example: image imageUrl string required URL of the image attachment Example: https://example.com/image.png ] |
| **type** | `string` | No |  |
| **imageUrl** | `string` | No |  |
| **locationId** | `string` | No |  |
| **contactId** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true,
  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",
  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",
  "response": "I can help you with various tasks...",
  "type": "text",
  "nextExpectedInput": "text",
  "goalCompletion": false,
  "executionStatus": "completed",
  "flowSwitch": false,
  "attachments": [],
  "generativeOutputs": []
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **executionId** | `str` |  |
| **interactionId** | `str` |  |
| **response** | `str` |  |
| **type** | `str` |  |
| **nextExpectedInput** | `str` |  |
| **goalCompletion** | `bool` |  |
| **executionStatus** | `str` |  |
| **flowSwitch** | `bool` |  |
| **attachments** | `list` |  |
| **generativeOutputs** | `list` |  |

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
  --url https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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
  url: 'https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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
  'path': '/agent-studio/agent/:agentId/execute',
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
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute', [
  'headers' => $headers,
  'body' => '{
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"message\": \"string\",
  \"executionId\": \"string\",
  \"inputVariables\": \"string\",
  \"versionId\": \"string\",
  \"attachments\": \"string\",
  \"type\": \"string\",
  \"imageUrl\": \"string\",
  \"locationId\": \"string\",
  \"contactId\": \"string\"
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
  url := "https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute"
  payload := strings.NewReader(`{
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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

url = URI("https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
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
  "message": "string",
  "executionId": "string",
  "inputVariables": "string",
  "versionId": "string",
  "attachments": "string",
  "type": "string",
  "imageUrl": "string",
  "locationId": "string",
  "contactId": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/agent-studio/agent/:agentId/execute' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
