# Patch Agent

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PATCH |
| **Endpoint URL** | `https://services.leadconnectorhq.com/voice-ai/agents/:agentId` |
| **Scopes Required** | `voice-ai-agents.write` |
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
| **locationId** | `` | No |  |

### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **agentName** | `string` | No |  |
| **businessName** | `string` | No |  |
| **welcomeMessage** | `string` | No |  |
| **agentPrompt** | `string` | No |  |
| **voiceId** | `string` | No |  |
| **language** | `VoiceAILanguage (string)` | No |  |
| **patienceLevel** | `PatienceLevel (string)` | No |  |
| **maxCallDuration** | `number` | No |  |
| **sendUserIdleReminders** | `boolean` | No |  |
| **reminderAfterIdleTimeSeconds** | `number` | No |  |
| **inboundNumber** | `string` | No |  |
| **numberPoolId** | `string` | No |  |
| **callEndWorkflowIds** | `string[]` | No |  |
| **sendPostCallNotificationTo** | `object` | Yes | Configuration for post-call email notifications to various recipients. Default: [] admins boolean required Enables post-call notifications to all admin users in the location. Default: true Example: true allUsers boolean required Enables post-call notifications to all users in the location. Default: false Example: false contactAssignedUser boolean required Enables post-call notifications to the user assigned to the contact. Default: false Example: false specificUsers string[] required Array of specific user IDs to receive post-call notifications. Default: [] Example: ["user_507f1f77bcf86cd799439011"] customEmails string[] required Array of custom email addresses to receive post-call notifications. Default: [] Example: ["manager@company.com"] |
| **admins** | `boolean` | No |  |
| **allUsers** | `boolean` | No |  |
| **contactAssignedUser** | `boolean` | No |  |
| **specificUsers** | `string[]` | No |  |
| **customEmails** | `string[]` | No |  |
| **agentWorkingHours** | `object[]` | Yes | Time intervals defining when the agent accepts calls, organized by day of week. Default: [] (available 24/7) Array [ dayOfTheWeek number required Day of the week for this working hours configuration (Monday=1 to Sunday=7) Possible values: [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] Example: 1 intervals object[] required Array of time intervals when the agent is available on this day Array [ startHour number required Starting hour of the working interval in 24-hour format (0-23) Possible values: <= 23 Example: 9 endHour number required Ending hour of the working interval in 24-hour format (0-23) Possible values: <= 23 Example: 17 startMinute number required Starting minute of the working interval (0-59) Possible values: <= 59 Example: 0 endMinute number required Ending minute of the working interval (0-59) Possible values: <= 59 Example: 30 ] ] |
| **dayOfTheWeek** | `number` | No |  |
| **intervals** | `object[]` | Yes | Array of time intervals when the agent is available on this day Array [ startHour number required Starting hour of the working interval in 24-hour format (0-23) Possible values: <= 23 Example: 9 endHour number required Ending hour of the working interval in 24-hour format (0-23) Possible values: <= 23 Example: 17 startMinute number required Starting minute of the working interval (0-59) Possible values: <= 59 Example: 0 endMinute number required Ending minute of the working interval (0-59) Possible values: <= 59 Example: 30 ] |
| **startHour** | `number` | No |  |
| **endHour** | `number` | No |  |
| **startMinute** | `number` | No |  |
| **endMinute** | `number` | No |  |
| **timezone** | `string` | No |  |
| **isAgentAsBackupDisabled** | `boolean` | No |  |
| **translation** | `object` | Yes | Language translation settings including enablement flag and target language code. Rules: (1) translation.enabled can only be true if the agent's language is not en-US; (2) when enabled, translation.language must be either the agent's language or en-US; (3) when enabled, translation.language is required. enabled boolean required Enables language translation for agent conversations. Default: false Example: false language string Target language code for translation (e.g., "es" for Spanish, "fr" for French). Example: es |
| **enabled** | `boolean` | No |  |
| **language** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "id": "507f1f77bcf86cd799439011",
  "locationId": "LOC123456789ABCDEF",
  "agentName": "Customer Support Agent",
  "businessName": "Acme Corporation",
  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",
  "agentPrompt": "You are a helpful customer service representative.",
  "voiceId": "507f1f77bcf86cd799439011",
  "language": "en-US",
  "patienceLevel": "medium",
  "maxCallDuration": 600,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 5,
  "inboundNumber": "+1234567890",
  "numberPoolId": "pool_507f1f77bcf86cd799439011",
  "callEndWorkflowIds": [],
  "sendPostCallNotificationTo": {
    "admins": true,
    "allUsers": false,
    "contactAssignedUser": false,
    "specificUsers": [],
    "customEmails": []
  },
  "agentWorkingHours": [],
  "timezone": "America/New_York",
  "isAgentAsBackupDisabled": false,
  "translation": {
    "enabled": false,
    "language": "es"
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **id** | `str` |  |
| **locationId** | `str` |  |
| **agentName** | `str` |  |
| **businessName** | `str` |  |
| **welcomeMessage** | `str` |  |
| **agentPrompt** | `str` |  |
| **voiceId** | `str` |  |
| **language** | `str` |  |
| **patienceLevel** | `str` |  |
| **maxCallDuration** | `int` |  |
| **sendUserIdleReminders** | `bool` |  |
| **reminderAfterIdleTimeSeconds** | `int` |  |
| **inboundNumber** | `str` |  |
| **numberPoolId** | `str` |  |
| **callEndWorkflowIds** | `list` |  |
| **sendPostCallNotificationTo** | `dict` |  |
| **agentWorkingHours** | `list` |  |
| **timezone** | `str` |  |
| **isAgentAsBackupDisabled** | `bool` |  |
| **translation** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/voice-ai/agents/:agentId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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
    const response = await ghl.api.request('PATCH', 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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
  url: 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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
  'path': '/voice-ai/agents/:agentId',
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
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PATCH',
  'url': 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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

unirest('PATCH', 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/voice-ai/agents/:agentId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PATCH", url, headers=headers, data=json.dumps({
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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
$response = $client->request('PATCH', 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId', [
  'headers' => $headers,
  'body' => '{
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/voice-ai/agents/:agentId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PATCH", HttpRequest.BodyPublishers.ofString("{
  \"agentName\": \"string\",
  \"businessName\": \"string\",
  \"welcomeMessage\": \"string\",
  \"agentPrompt\": \"string\",
  \"voiceId\": \"string\",
  \"language\": \"string\",
  \"patienceLevel\": \"string\",
  \"maxCallDuration\": 123,
  \"sendUserIdleReminders\": true,
  \"reminderAfterIdleTimeSeconds\": 123,
  \"inboundNumber\": \"string\",
  \"numberPoolId\": \"string\",
  \"callEndWorkflowIds\": \"string\",
  \"sendPostCallNotificationTo\": \"string\",
  \"admins\": true,
  \"allUsers\": true,
  \"contactAssignedUser\": true,
  \"specificUsers\": \"string\",
  \"customEmails\": \"string\",
  \"agentWorkingHours\": \"string\",
  \"dayOfTheWeek\": 123,
  \"intervals\": \"string\",
  \"startHour\": 123,
  \"endHour\": 123,
  \"startMinute\": 123,
  \"endMinute\": 123,
  \"timezone\": \"string\",
  \"isAgentAsBackupDisabled\": true,
  \"translation\": \"string\",
  \"enabled\": true
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
  url := "https://services.leadconnectorhq.com/voice-ai/agents/:agentId"
  payload := strings.NewReader(`{
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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

url = URI("https://services.leadconnectorhq.com/voice-ai/agents/:agentId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Patch.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
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
  "agentName": "string",
  "businessName": "string",
  "welcomeMessage": "string",
  "agentPrompt": "string",
  "voiceId": "string",
  "language": "string",
  "patienceLevel": "string",
  "maxCallDuration": 123,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 123,
  "inboundNumber": "string",
  "numberPoolId": "string",
  "callEndWorkflowIds": "string",
  "sendPostCallNotificationTo": "string",
  "admins": true,
  "allUsers": true,
  "contactAssignedUser": true,
  "specificUsers": "string",
  "customEmails": "string",
  "agentWorkingHours": "string",
  "dayOfTheWeek": 123,
  "intervals": "string",
  "startHour": 123,
  "endHour": 123,
  "startMinute": 123,
  "endMinute": 123,
  "timezone": "string",
  "isAgentAsBackupDisabled": true,
  "translation": "string",
  "enabled": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/voice-ai/agents/:agentId' -Method 'PATCH' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
