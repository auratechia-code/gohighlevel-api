# Export messages by location ID

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/conversations/messages/export` |
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

N/A
### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `` | No | channel string Possible values: [ Call , SMS , Email , WhatsApp , Instagram , Facebook ] Filter by message channel. Optional - when not provided, all non-email message types will be returned including activity messages (opportunity updates, appointments, etc.). To fetch email messages, you must explicitly set channel=Email. |
| **channel** | `` | No | limit number Possible values: >= 10 and <= 500 Number of messages to return per page Default value: 100 |
| **limit** | `` | No | cursor string Cursor for pagination. Pass the nextCursor from previous response to get next page. Example: a748514c-f49e-4fa8-9954-b53afc78d81d |
| **cursor** | `` | No | sortBy string Possible values: [ createdAt , updatedAt ] Field to sort by Default value: createdAt |
| **sortBy** | `` | No | sortOrder string Possible values: [ asc , desc ] Sort order Default value: desc |
| **sortOrder** | `` | No | conversationId string Filter messages by conversation ID |
| **conversationId** | `` | No | contactId string Filter messages by contact ID |
| **contactId** | `` | No | startDate string Start date to filter messages by |
| **startDate** | `` | No | endDate string End date to filter messages by |
| **endDate** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
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
  ],
  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",
  "total": 1234
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **messages** | `list` |  |
| **nextCursor** | `str` |  |
| **total** | `int` |  |

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
  --url https://services.leadconnectorhq.com/conversations/messages/export \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/conversations/messages/export', {
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
  url: 'https://services.leadconnectorhq.com/conversations/messages/export',
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
  'path': '/conversations/messages/export',
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
  'url': 'https://services.leadconnectorhq.com/conversations/messages/export',
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

unirest('GET', 'https://services.leadconnectorhq.com/conversations/messages/export')
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

url = "https://services.leadconnectorhq.com/conversations/messages/export"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/conversations/messages/export', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/conversations/messages/export"))
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
  url := "https://services.leadconnectorhq.com/conversations/messages/export"
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

url = URI("https://services.leadconnectorhq.com/conversations/messages/export")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversations/messages/export' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
