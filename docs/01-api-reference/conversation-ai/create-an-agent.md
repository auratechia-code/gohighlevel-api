# Create an Agent

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/conversation-ai/agents` |
| **Scopes Required** | `conversation-ai.write` |
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
| **name** | `string` | No |  |
| **businessName** | `string` | No |  |
| **mode** | `string` | No |  |
| **channels** | `string[]` | No |  |
| **isPrimary** | `boolean` | No |  |
| **waitTime** | `number` | No |  |
| **waitTimeUnit** | `string` | No |  |
| **sleepEnabled** | `boolean` | No |  |
| **sleepTime** | `number` | No |  |
| **sleepTimeUnit** | `string` | No |  |
| **personality** | `string` | No |  |
| **goal** | `string` | No |  |
| **instructions** | `string` | No |  |
| **autoPilotMaxMessages** | `number` | No |  |
| **knowledgeBaseIds** | `string[]` | No |  |
| **respondToImages** | `boolean` | No |  |
| **respondToAudio** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "id": "emp_123",
  "name": "John Doe",
  "businessName": "Tech Corp",
  "mode": "auto-pilot",
  "channels": [
    "SMS",
    "Live_Chat"
  ],
  "waitTime": 30,
  "waitTimeUnit": "seconds",
  "sleepEnabled": false,
  "sleepTime": 2,
  "sleepTimeUnit": "hours",
  "actions": [
    {
      "id": "actionId123",
      "type": "triggerWorkflow"
    }
  ],
  "isPrimary": false,
  "autoPilotMaxMessages": 25,
  "goal": "Assist customers with inquiries",
  "personality": "Friendly and helpful",
  "instructions": "Provide excellent customer service",
  "knowledgeBaseIds": [
    "kb_123",
    "kb_456"
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **id** | `str` |  |
| **name** | `str` |  |
| **businessName** | `str` |  |
| **mode** | `str` |  |
| **channels** | `list` |  |
| **waitTime** | `int` |  |
| **waitTimeUnit** | `str` |  |
| **sleepEnabled** | `bool` |  |
| **sleepTime** | `int` |  |
| **sleepTimeUnit** | `str` |  |
| **actions** | `list` |  |
| **isPrimary** | `bool` |  |
| **autoPilotMaxMessages** | `int` |  |
| **goal** | `str` |  |
| **personality** | `str` |  |
| **instructions** | `str` |  |
| **knowledgeBaseIds** | `list` |  |

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
  --url https://services.leadconnectorhq.com/conversation-ai/agents \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/conversation-ai/agents', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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
  url: 'https://services.leadconnectorhq.com/conversation-ai/agents',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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
  'path': '/conversation-ai/agents',
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
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/conversation-ai/agents',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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

unirest('POST', 'https://services.leadconnectorhq.com/conversation-ai/agents')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/conversation-ai/agents"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/conversation-ai/agents', [
  'headers' => $headers,
  'body' => '{
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/conversation-ai/agents"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"name\": \"string\",
  \"businessName\": \"string\",
  \"mode\": \"string\",
  \"channels\": \"string\",
  \"isPrimary\": true,
  \"waitTime\": 123,
  \"waitTimeUnit\": \"string\",
  \"sleepEnabled\": true,
  \"sleepTime\": 123,
  \"sleepTimeUnit\": \"string\",
  \"personality\": \"string\",
  \"goal\": \"string\",
  \"instructions\": \"string\",
  \"autoPilotMaxMessages\": 123,
  \"knowledgeBaseIds\": \"string\",
  \"respondToImages\": true,
  \"respondToAudio\": true
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
  url := "https://services.leadconnectorhq.com/conversation-ai/agents"
  payload := strings.NewReader(`{
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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

url = URI("https://services.leadconnectorhq.com/conversation-ai/agents")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
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
  "name": "string",
  "businessName": "string",
  "mode": "string",
  "channels": "string",
  "isPrimary": true,
  "waitTime": 123,
  "waitTimeUnit": "string",
  "sleepEnabled": true,
  "sleepTime": 123,
  "sleepTimeUnit": "string",
  "personality": "string",
  "goal": "string",
  "instructions": "string",
  "autoPilotMaxMessages": 123,
  "knowledgeBaseIds": "string",
  "respondToImages": true,
  "respondToAudio": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversation-ai/agents' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
