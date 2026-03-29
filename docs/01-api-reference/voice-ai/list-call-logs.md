# List Call Logs

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs` |
| **Scopes Required** | `voice-ai-dashboard.readonly` |
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

### Path Parameters

N/A
### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `` | No | agentId string Agent identifier. When provided, returns logs for this agent only. Example: 507f1f77bcf86cd799439011 |
| **agentId** | `` | No | contactId string Contact IDs (comma-separated) to filter by. Example: contact123,contact456 |
| **contactId** | `` | No | callType string Possible values: [ LIVE , TRIAL ] Call type filter. |
| **callType** | `` | No | startDate number Start date filter (Unix timestamp). Must be less than endDate. Both startDate and endDate must be provided together. Example: 1679308800000 |
| **startDate** | `` | No | endDate number End date filter (Unix timestamp). Must be greater than startDate. Both startDate and endDate must be provided together. Example: 1679395199000 |
| **endDate** | `` | No | actionType string Possible values: [ CALL_TRANSFER , DATA_EXTRACTION , IN_CALL_DATA_EXTRACTION , WORKFLOW_TRIGGER , SMS , APPOINTMENT_BOOKING , CUSTOM_ACTION , KNOWLEDGE_BASE ] Action type filter for call logs (comma-separated ACTION_TYPE values) Example: SMS,CALL_TRANSFER,WORKFLOW_TRIGGER |
| **actionType** | `` | No | sortBy string Possible values: [ duration , createdAt ] Field to sort by. Defaults to newest if omitted. |
| **sortBy** | `` | No | sort string Possible values: [ ascend , descend ] Sort direction. Applies only when sortBy is provided. |
| **sort** | `` | No | page number Page number (1-based). Default value: 1 |
| **page** | `` | No | pageSize number Page size (max 50). Default value: 10 |
| **pageSize** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "total": 150,
  "page": 2,
  "pageSize": 10,
  "callLogs": [
    {
      "id": "507f1f77bcf86cd799439011",
      "contactId": "507f1f77bcf86cd799439012",
      "agentId": "507f1f77bcf86cd799439013",
      "isAgentDeleted": false,
      "fromNumber": "+1234567890",
      "createdAt": "2024-01-15T10:30:00.000Z",
      "duration": 180,
      "trialCall": false,
      "executedCallActions": [
        {
          "actionId": "507f1f77bcf86cd799439015",
          "actionType": "CALL_TRANSFER",
          "actionName": "Transfer to Manager",
          "actionParameters": {
            "transferToType": "number",
            "transferToValue": "+12345678901",
            "triggerMessage": "Let me transfer you to a manager right away",
            "hearWhisperMessage": true
          },
          "executedAt": "2024-01-15T10:32:00.000Z",
          "triggerReceivedAt": "2024-01-15T10:31:45.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439016",
          "actionType": "SMS",
          "actionName": "Send Confirmation SMS",
          "actionParameters": {
            "triggerPrompt": "When caller asks for booking confirmation",
            "triggerMessage": "I'll send you a confirmation text",
            "messageBody": "Your appointment is confirmed for tomorrow at 2 PM"
          },
          "executedAt": "2024-01-15T10:33:30.000Z",
          "triggerReceivedAt": "2024-01-15T10:33:15.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439017",
          "actionType": "DATA_EXTRACTION",
          "actionName": "Extract Phone Number",
          "actionParameters": {
            "contactFieldId": "507f1f77bcf86cd799439018",
            "description": "Customer's phone number",
            "examples": [
              "+1234567890",
              "+9876543210"
            ],
            "overwriteExistingValue": false
          },
          "executedAt": "2024-01-15T10:34:15.000Z",
          "triggerReceivedAt": "2024-01-15T10:34:00.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439019",
          "actionType": "WORKFLOW_TRIGGER",
          "actionName": "Start Follow-up Workflow",
          "actionParameters": {
            "triggerPrompt": "When caller requests a quote",
            "triggerMessage": "Let me start that process for you",
            "workflowId": "507f1f77bcf86cd799439020"
          },
          "executedAt": "2024-01-15T10:35:00.000Z",
          "triggerReceivedAt": "2024-01-15T10:34:45.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439021",
          "actionType": "APPOINTMENT_BOOKING",
          "actionName": "Book Consultation",
          "actionParameters": {
            "calendarId": "507f1f77bcf86cd799439022",
            "daysOfOfferingDates": 3,
            "slotsPerDay": 3,
            "hoursBetweenSlots": 1
          },
          "executedAt": "2024-01-15T10:36:45.000Z",
          "triggerReceivedAt": "2024-01-15T10:36:30.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439023",
          "actionType": "CUSTOM_ACTION",
          "actionName": "Check Order Status",
          "actionParameters": {
            "triggerPrompt": "When caller provides order number",
            "triggerMessage": "Let me check that order status",
            "apiDetails": {
              "url": "https://api.example.com/orders",
              "method": "GET",
              "authenticationRequired": true,
              "authenticationValue": "token123",
              "headers": [
                {
                  "key": "Content-Type",
                  "value": "application/json"
                }
              ],
              "parameters": [
                {
                  "name": "orderId",
                  "description": "Order ID to look up",
                  "type": "string",
                  "example": "ORD-12345"
                }
              ]
            },
            "responsePathsToExtract": [
              "data.orderId",
              "status"
            ]
          },
          "executedAt": "2024-01-15T10:37:20.000Z",
          "triggerReceivedAt": "2024-01-15T10:37:05.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439024",
          "actionType": "IN_CALL_DATA_EXTRACTION",
          "actionName": "Extract Email During Call",
          "actionParameters": {
            "contactFieldId": "507f1f77bcf86cd799439025",
            "description": "Customer's email address",
            "examples": [
              "john@example.com",
              "jane@company.com"
            ],
            "overwriteExistingValue": true
          },
          "executedAt": "2024-01-15T10:31:45.000Z",
          "triggerReceivedAt": "2024-01-15T10:31:30.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439026",
          "actionType": "KNOWLEDGE_BASE",
          "actionName": "Query Product Info",
          "actionParameters": {
            "triggerPrompt": "When caller asks about pricing",
            "triggerMessage": "Let me look that up for you",
            "knowledgeBaseId": "507f1f77bcf86cd799439027",
            "parameters": [
              {
                "name": "category",
                "description": "Product category to search",
                "type": "string",
                "example": "pricing"
              }
            ]
          },
          "executedAt": "2024-01-15T10:38:10.000Z",
          "triggerReceivedAt": "2024-01-15T10:37:55.000Z"
        }
      ],
      "summary": "Customer called to inquire about product pricing and was transferred to sales team.",
      "transcript": "bot: Hello, how can I help you today?\nhuman: I would like to know about your pricing...",
      "translation": {
        "translatedTranscript": "Translated version of the call transcript"
      },
      "extractedData": {
        "phoneNumber": "+1234567890",
        "customerName": "John Doe",
        "email": "john.doe@example.com",
        "companyName": "Acme Corp",
        "customField1": "Custom value",
        "customField2": "Another value"
      },
      "messageId": "507f1f77bcf86cd799439014"
    }
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **total** | `int` |  |
| **page** | `int` |  |
| **pageSize** | `int` |  |
| **callLogs** | `list` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{}'
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs', {
      headers: { 'Version': '2021-07-28' },
      body: {}
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
  method: 'get',
  url: 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {}
};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```

### 4. NATIVE NODE

```javascript
const https = require('follow-redirects').https;

const options = {
  'method': 'GET',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/voice-ai/dashboard/call-logs',
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

req.write(JSON.stringify({}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'GET',
  'url': 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({})
};

request(options, (error, response) => {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

### 6. UNIREST NODE

```javascript
const unirest = require('unirest');

unirest('GET', 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("GET", url, headers=headers, data=json.dumps({}))
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs', [
  'headers' => $headers,
  'body' => '{}'
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
    .uri(URI.create("https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("GET", HttpRequest.BodyPublishers.ofString("{}"))
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
  url := "https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs"
  payload := strings.NewReader(`{}`)
  req, _ := http.NewRequest("GET", url, payload)
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

url = URI("https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({})
response = http.request(request)
puts response.read_body
```

### 12. POWERSHELL

```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "2021-07-28")
$headers.Add("Content-Type", "application/json")

$body = '{}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
