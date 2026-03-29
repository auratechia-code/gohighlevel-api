# Update Followup Settings

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PATCH |
| **Endpoint URL** | `https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings` |
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

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **agentId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **actionIds** | `string[]` | No |  |
| **followupSettings** | `object` | Yes | dynamicChannelSwitching boolean required Whether to dynamically switch channels for followups Default value: true Example: true followUpHours boolean Whether to respect working hours for followups Example: true workingHours object[] Working hours configuration for followups Array [ dayOfTheWeek number required Day of the week (0=Sunday, 1=Monday, etc.) Example: 1 intervals object[] Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] ] timezoneToUse string Timezone to use for followups, contact or location Possible values: [ contact , business ] |
| **dynamicChannelSwitching** | `boolean` | No |  |
| **followUpHours** | `boolean` | No |  |
| **workingHours** | `object[]` | Yes | Working hours configuration for followups Array [ dayOfTheWeek number required Day of the week (0=Sunday, 1=Monday, etc.) Example: 1 intervals object[] Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] ] |
| **dayOfTheWeek** | `number` | No |  |
| **intervals** | `object[]` | Yes | Time intervals for this day Array [ startHour number required Start hour (24-hour format) Example: 9 startMinute number required Start minute Example: 0 endHour number required End hour (24-hour format) Example: 17 endMinute number required End minute Example: 30 ] |
| **startHour** | `number` | No |  |
| **startMinute** | `number` | No |  |
| **endHour** | `number` | No |  |
| **endMinute** | `number` | No |  |
| **timezoneToUse** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "data": {
    "id": "actionId123",
    "name": "Trigger Workflow",
    "type": "triggerWorkflow",
    "agentId": "agentId123",
    "details": {
      "workflowIds": [
        "workflow123",
        "workflow456"
      ],
      "triggerCondition": "When user requests appointment",
      "triggerMessage": "Workflow triggered successfully"
    }
  },
  "success": true
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **data** | `dict` |  |
| **success** | `bool` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PATCH \
  --url https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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
    const response = await ghl.api.request('PATCH', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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
  method: 'patch',
  url: 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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
  'method': 'PATCH',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/conversation-ai/agents/:agentId/followup-settings',
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
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PATCH',
  'url': 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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

unirest('PATCH', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PATCH", url, headers=headers, data=json.dumps({
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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
$response = $client->request('PATCH', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings', [
  'headers' => $headers,
  'body' => '{
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PATCH", HttpRequest.BodyPublishers.ofString("{
  \"actionIds\": \"string\",
  \"followupSettings\": \"string\",
  \"dynamicChannelSwitching\": true,
  \"followUpHours\": true,
  \"workingHours\": \"string\",
  \"dayOfTheWeek\": 123,
  \"intervals\": \"string\",
  \"startHour\": 123,
  \"startMinute\": 123,
  \"endHour\": 123,
  \"endMinute\": 123,
  \"timezoneToUse\": \"string\"
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
  url := "https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings"
  payload := strings.NewReader(`{
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
}`)
  req, _ := http.NewRequest("PATCH", url, payload)
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

url = URI("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
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
  "actionIds": "string",
  "followupSettings": "string",
  "dynamicChannelSwitching": true,
  "followUpHours": true,
  "workingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "startMinute": 123,
  "endHour": 123,
  "endMinute": 123,
  "timezoneToUse": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings' -Method 'PATCH' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
