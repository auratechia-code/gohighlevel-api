# Get messages by conversation id

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/conversations/:conversationId/messages` |
| **Scopes Required** | `conversations/message.readonly` |
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
| **conversationId** | `` | No |  |

### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **lastMessageId** | `` | No | limit number Number of messages to be fetched from the conversation. Default limit is 20 Example: 20 |
| **limit** | `` | No | type string Possible values: [ TYPE_CALL , TYPE_SMS , TYPE_EMAIL , TYPE_FACEBOOK , TYPE_GMB , TYPE_INSTAGRAM , TYPE_WHATSAPP , TYPE_ACTIVITY_APPOINTMENT , TYPE_ACTIVITY_CONTACT , TYPE_ACTIVITY_INVOICE , TYPE_ACTIVITY_PAYMENT , TYPE_ACTIVITY_OPPORTUNITY , TYPE_LIVE_CHAT , TYPE_INTERNAL_COMMENTS , TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG ] Types of message to fetched separated with comma Example: TYPE_SMS,TYPE_CALL |
| **type** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "messages": {
    "lastMessageId": "p1mRSHeLDhAms5q0LMr4",
    "nextPage": true,
    "messages": [
      {
        "id": "ve9EPM428h8vShlRW1KT",
        "altId": "msg_123456789",
        "type": 1,
        "messageType": "SMS",
        "locationId": "ve9EPM428h8vShlRW1KT",
        "contactId": "ve9EPM428h8vShlRW1KT",
        "conversationId": "ve9EPM428h8vShlRW1KT",
        "dateAdded": "2024-03-27T18:13:49.000Z",
        "body": "Hi there",
        "direction": "inbound",
        "status": "connected",
        "contentType": "text/plain",
        "attachments": [
          "string"
        ],
        "meta": {
          "callDuration": 120,
          "callStatus": "completed",
          "email": {
            "email": {
              "messageIds": [
                "ve9EPM428kjkvShlRW1KT",
                "ve9EPs1028kjkvShlRW1KT"
              ]
            }
          },
          "ig": {
            "ig": {
              "page_id": "1234567890",
              "page_name": "Instagram Page"
            }
          },
          "fb": {
            "fb": {
              "page_id": "1234567890",
              "page_name": "Facebook Page"
            }
          }
        },
        "source": "workflow",
        "userId": "ve9EPM428kjkvShlRW1KT",
        "conversationProviderId": "ve9EPM428kjkvShlRW1KT",
        "chatWidgetId": "67b0cc8cf14b19d85ace7s35",
        "from": "+14155551234",
        "to": "+14155555678",
        "error": "string"
      }
    ]
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **messages** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/conversations/:conversationId/messages \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/conversations/:conversationId/messages', {
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
  url: 'https://services.leadconnectorhq.com/conversations/:conversationId/messages',
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
  'path': '/conversations/:conversationId/messages',
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
  'url': 'https://services.leadconnectorhq.com/conversations/:conversationId/messages',
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

unirest('GET', 'https://services.leadconnectorhq.com/conversations/:conversationId/messages')
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

url = "https://services.leadconnectorhq.com/conversations/:conversationId/messages"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/conversations/:conversationId/messages', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/conversations/:conversationId/messages"))
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
  url := "https://services.leadconnectorhq.com/conversations/:conversationId/messages"
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

url = URI("https://services.leadconnectorhq.com/conversations/:conversationId/messages")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversations/:conversationId/messages' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
