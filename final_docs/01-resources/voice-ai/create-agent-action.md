# Create Agent Action

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/voice-ai/actions` |
| **Scopes Required** | `voice-ai-agent-goals.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |
| **headers** | `object[]` | Yes | HTTP headers to include Array [ key string required HTTP header name Example: id value string required HTTP header value Example: 1234567890 ] |
| **key** | `string` | No |  |
| **value** | `string` | No |  |
| **headers** | `object[]` | Yes | HTTP headers to include Array [ key string required HTTP header name Example: id value string required HTTP header value Example: 1234567890 ] |
| **key** | `string` | No |  |
| **value** | `string` | No |  |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **agentId** | `string` | No |  |
| **locationId** | `string` | No |  |
| **actionType** | `string` | No |  |
| **name** | `string` | No |  |
| **actionParameters** | `object` | Yes | Action parameters - structure varies by actionType oneOf CallTransferActionParameters DataExtractionActionParameters InCallDataExtractionActionParameters WorkflowTriggerParameters SMSParameters AppointmentBookingActionParameters CustomActionParameters KnowledgeBaseParameters triggerPrompt string required When to trigger this action during the call Example: When the caller asks to speak to a manager transferToType string required Type of transfer destination (currently only "number" is supported) Possible values: [ number ] Example: number transferToValue string required Phone number to transfer to. Must start with +, include country code, contain only numbers, and be 11-16 characters long (e.g., +12345678901). Example: +12345678901 triggerMessage string required Message to tell the caller before transferring Example: Let me transfer you to a manager right away hearWhisperMessage boolean Whether to play whisper message to the receiving party Example: true contactFieldId string required ID of the contact field to be updated with the extracted data Example: 507f1f77bcf86cd799439011 description string required Description of what data to extract Example: Caller's phone number examples string[] required Example values to help Agent understand the expected format. At least one example is required, maximum 5 examples allowed. Example: ["+1234567890","+9876543210"] overwriteExistingValue boolean Whether to overwrite existing field value if already set, default is false Default value: false Example: false contactFieldId string required ID of the contact field to be updated with the extracted data Example: 507f1f77bcf86cd799439011 description string required Description of what data to extract Example: Caller's phone number examples string[] required Example values to help Agent understand the expected format. At least one example is required, maximum 5 examples allowed. Example: ["+1234567890","+9876543210"] overwriteExistingValue boolean Whether to overwrite existing field value if already set, default is false Default value: false Example: false triggerPrompt string required When to trigger this workflow Example: When caller requests a quote triggerMessage string required Message to tell the caller Example: Let me start that process for you workflowId string required Workflow ID to trigger Example: 507f1f77bcf86cd799439011 triggerPrompt string required When to send the SMS Example: When caller asks for booking confirmation triggerMessage string required Message to tell the caller Example: I'll send you a confirmation text messageBody string required SMS message content to send Example: Your appointment is confirmed for tomorrow at 2 PM calendarId string required Calendar ID to book appointments in Example: 507f1f77bcf86cd799439011 daysOfOfferingDates number required Number of days ahead to offer booking dates Example: 3 slotsPerDay number required Number of available slots per day Example: 3 hoursBetweenSlots number required Hours between available slots Example: 1 triggerPrompt string required When to call the custom API Example: When caller provides order number triggerMessage string required Message to tell the caller Example: Let me check that order status apiDetails object API endpoint configuration url string required API endpoint URL Example: https://api.example.com/orders method string required HTTP method Possible values: [ POST , GET ] Example: GET authenticationRequired boolean Whether authentication is required Example: true authenticationValue string Authentication token or API key (required if authenticationRequired is true) Example: token123 headers object[] HTTP headers to include Array [ key string required HTTP header name Example: id value string required HTTP header value Example: 1234567890 ] parameters object[] API parameters to send Array [ name string required Parameter name Example: orderId description string Parameter description Example: Order ID to look up type string Parameter type Example: string example string Example parameter value Example: ORD-12345 ] selectedPaths string[] Selected response paths to extract from API response. Required: at least 1 value if the method is GET. Should be empty if the method is POST. Example: ["data.orderId","status"] triggerPrompt string required When to query the knowledge base Example: When caller asks about pricing knowledgeBaseId string required Knowledge base ID to query Example: 507f1f77bcf86cd799439011 |
| **triggerPrompt** | `string` | No |  |
| **transferToType** | `string` | No |  |
| **transferToValue** | `string` | No |  |
| **triggerMessage** | `string` | No |  |
| **hearWhisperMessage** | `boolean` | No |  |
| **contactFieldId** | `string` | No |  |
| **description** | `string` | No |  |
| **examples** | `string[]` | No |  |
| **overwriteExistingValue** | `boolean` | No |  |
| **contactFieldId** | `string` | No |  |
| **description** | `string` | No |  |
| **examples** | `string[]` | No |  |
| **overwriteExistingValue** | `boolean` | No |  |
| **triggerPrompt** | `string` | No |  |
| **triggerMessage** | `string` | No |  |
| **workflowId** | `string` | No |  |
| **triggerPrompt** | `string` | No |  |
| **triggerMessage** | `string` | No |  |
| **messageBody** | `string` | No |  |
| **calendarId** | `string` | No |  |
| **daysOfOfferingDates** | `number` | No |  |
| **slotsPerDay** | `number` | No |  |
| **hoursBetweenSlots** | `number` | No |  |
| **triggerPrompt** | `string` | No |  |
| **triggerMessage** | `string` | No |  |
| **apiDetails** | `object` | Yes | API endpoint configuration url string required API endpoint URL Example: https://api.example.com/orders method string required HTTP method Possible values: [ POST , GET ] Example: GET authenticationRequired boolean Whether authentication is required Example: true authenticationValue string Authentication token or API key (required if authenticationRequired is true) Example: token123 headers object[] HTTP headers to include Array [ key string required HTTP header name Example: id value string required HTTP header value Example: 1234567890 ] parameters object[] API parameters to send Array [ name string required Parameter name Example: orderId description string Parameter description Example: Order ID to look up type string Parameter type Example: string example string Example parameter value Example: ORD-12345 ] |
| **url** | `string` | No |  |
| **method** | `string` | No |  |
| **authenticationRequired** | `boolean` | Yes |  |
| **authenticationValue** | `string` | No |  |
| **headers** | `object[]` | Yes | HTTP headers to include Array [ key string required HTTP header name Example: id value string required HTTP header value Example: 1234567890 ] |
| **key** | `string` | No |  |
| **value** | `string` | No |  |
| **parameters** | `object[]` | Yes | API parameters to send Array [ name string required Parameter name Example: orderId description string Parameter description Example: Order ID to look up type string Parameter type Example: string example string Example parameter value Example: ORD-12345 ] |
| **name** | `string` | No |  |
| **description** | `string` | No |  |
| **type** | `string` | No |  |
| **example** | `string` | No |  |
| **selectedPaths** | `string[]` | No |  |
| **triggerPrompt** | `string` | No |  |
| **knowledgeBaseId** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "id": "507f1f77bcf86cd799439011",
  "actionType": "CALL_TRANSFER",
  "name": "Transfer to Manager",
  "actionParameters": {
    "triggerPrompt": "When the caller asks to speak to a manager",
    "transferToType": "number",
    "transferToValue": "+12345678901",
    "triggerMessage": "Let me transfer you to a manager right away",
    "hearWhisperMessage": true
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **id** | `str` |  |
| **actionType** | `str` |  |
| **name** | `str` |  |
| **actionParameters** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/voice-ai/actions \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/voice-ai/actions', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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
  url: 'https://services.leadconnectorhq.com/voice-ai/actions',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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
  'path': '/voice-ai/actions',
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
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/voice-ai/actions',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/voice-ai/actions')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/voice-ai/actions"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/voice-ai/actions', [
  'headers' => $headers,
  'body' => '{
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/voice-ai/actions"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"agentId\": \"string\",
  \"locationId\": \"string\",
  \"actionType\": \"string\",
  \"name\": \"string\",
  \"actionParameters\": \"string\",
  \"triggerPrompt\": \"string\",
  \"transferToType\": \"string\",
  \"transferToValue\": \"string\",
  \"triggerMessage\": \"string\",
  \"hearWhisperMessage\": true,
  \"contactFieldId\": \"string\",
  \"description\": \"string\",
  \"examples\": \"string\",
  \"overwriteExistingValue\": true,
  \"workflowId\": \"string\",
  \"messageBody\": \"string\",
  \"calendarId\": \"string\",
  \"daysOfOfferingDates\": 123,
  \"slotsPerDay\": 123,
  \"hoursBetweenSlots\": 123,
  \"apiDetails\": \"string\",
  \"url\": \"string\",
  \"method\": \"string\",
  \"authenticationRequired\": true,
  \"authenticationValue\": \"string\",
  \"headers\": \"string\",
  \"key\": \"string\",
  \"value\": \"string\",
  \"parameters\": \"string\",
  \"type\": \"string\",
  \"example\": \"string\",
  \"selectedPaths\": \"string\",
  \"knowledgeBaseId\": \"string\"
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
  url := "https://services.leadconnectorhq.com/voice-ai/actions"
  payload := strings.NewReader(`{
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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

url = URI("https://services.leadconnectorhq.com/voice-ai/actions")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
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
  "agentId": "string",
  "locationId": "string",
  "actionType": "string",
  "name": "string",
  "actionParameters": "string",
  "triggerPrompt": "string",
  "transferToType": "string",
  "transferToValue": "string",
  "triggerMessage": "string",
  "hearWhisperMessage": true,
  "contactFieldId": "string",
  "description": "string",
  "examples": "string",
  "overwriteExistingValue": true,
  "workflowId": "string",
  "messageBody": "string",
  "calendarId": "string",
  "daysOfOfferingDates": 123,
  "slotsPerDay": 123,
  "hoursBetweenSlots": 123,
  "apiDetails": "string",
  "url": "string",
  "method": "string",
  "authenticationRequired": true,
  "authenticationValue": "string",
  "headers": "string",
  "key": "string",
  "value": "string",
  "parameters": "string",
  "type": "string",
  "example": "string",
  "selectedPaths": "string",
  "knowledgeBaseId": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/voice-ai/actions' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
