# Search Conversations

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/conversations/search` |
| **Scopes Required** | `conversations.readonly` |
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
| **locationId** | `` | No | contactId string Contact Id Example: 9VEmS0si86GW6gXWU89b |
| **contactId** | `` | No | assignedTo string User IDs that conversations are assigned to. Multiple IDs can be provided as comma-separated values. Use "unassigned" to fetch conversations not assigned to any user. Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik |
| **assignedTo** | `` | No | followers string User IDs of followers to filter conversations by. Multiple IDs can be provided as comma-separated values. Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik |
| **followers** | `` | No | mentions string User Id of the mention. Multiple values are comma separated. Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik |
| **mentions** | `` | No | query string Search paramater as a string Example: Search string |
| **query** | `` | No | sort string Possible values: [ asc , desc ] Sort paramater - asc or desc Example: asc |
| **sort** | `` | No | startAfterDate any Search to begin after the specified date - should contain the sort value of the last document Example: 1600854 |
| **startAfterDate** | `` | No | id string Id of the conversation Example: ABCHkzuJQ8ZMd4Te84GK |
| **id** | `` | No | limit number Limit of conversations - Default is 20 Example: 20 |
| **limit** | `` | No | lastMessageType string Possible values: [ TYPE_CALL , TYPE_SMS , TYPE_EMAIL , TYPE_SMS_REVIEW_REQUEST , TYPE_WEBCHAT , TYPE_SMS_NO_SHOW_REQUEST , TYPE_CAMPAIGN_SMS , TYPE_CAMPAIGN_CALL , TYPE_CAMPAIGN_EMAIL , TYPE_CAMPAIGN_VOICEMAIL , TYPE_FACEBOOK , TYPE_CAMPAIGN_FACEBOOK , TYPE_CAMPAIGN_MANUAL_CALL , TYPE_CAMPAIGN_MANUAL_SMS , TYPE_GMB , TYPE_CAMPAIGN_GMB , TYPE_REVIEW , TYPE_INSTAGRAM , TYPE_WHATSAPP , TYPE_CUSTOM_SMS , TYPE_CUSTOM_EMAIL , TYPE_CUSTOM_PROVIDER_SMS , TYPE_CUSTOM_PROVIDER_EMAIL , TYPE_IVR_CALL , TYPE_ACTIVITY_CONTACT , TYPE_ACTIVITY_INVOICE , TYPE_ACTIVITY_PAYMENT , TYPE_ACTIVITY_OPPORTUNITY , TYPE_LIVE_CHAT , TYPE_LIVE_CHAT_INFO_MESSAGE , TYPE_ACTIVITY_APPOINTMENT , TYPE_FACEBOOK_COMMENT , TYPE_INSTAGRAM_COMMENT , TYPE_CUSTOM_CALL , TYPE_INTERNAL_COMMENT , TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG ] Type of the last message in the conversation as a string Example: TYPE_SMS |
| **lastMessageType** | `` | No | lastMessageAction string Possible values: [ automated , manual ] Action of the last outbound message in the conversation as string. Example: manual |
| **lastMessageAction** | `` | No | lastMessageDirection string Possible values: [ inbound , outbound ] Direction of the last message in the conversation as string. Example: inbound |
| **lastMessageDirection** | `` | No | status string Possible values: [ all , read , unread , starred , recents ] The status of the conversation to be filtered - all, read, unread, starred Example: all |
| **status** | `` | No | sortBy string Possible values: [ last_manual_message_date , last_message_date , score_profile ] The sorting of the conversation to be filtered as - manual messages or all messages Example: last_message_date |
| **sortBy** | `` | No | sortScoreProfile string Id of score profile on which sortBy.ScoreProfile should sort on Example: ABCHkzuJQ8ZMd4Te84GK |
| **sortScoreProfile** | `` | No | scoreProfile string Id of score profile on which conversations should get filtered out, works with scoreProfileMin & scoreProfileMax Example: ABCHkzuJQ8ZMd4Te84GK |
| **scoreProfile** | `` | No | scoreProfileMin number Minimum value for score Example: ABCHkzuJQ8ZMd4Te84GK |
| **scoreProfileMin** | `` | No | scoreProfileMax number Maximum value for score Example: ABCHkzuJQ8ZMd4Te84GK |
| **scoreProfileMax** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "conversations": [
    {
      "id": "ABCHkzuJQ8ZMd4Te84GK",
      "contactId": "ABCHkzuJQ8ZMd4Te84GK",
      "locationId": "ABCHkzuJQ8ZMd4Te84GK",
      "lastMessageBody": "This is a sample message body",
      "lastMessageType": "TYPE_SMS",
      "type": "TYPE_PHONE",
      "unreadCount": 1,
      "fullName": "John Doe",
      "contactName": "John Doe Company",
      "email": "johndoe@mailingdomain.com",
      "phone": "+15550001234"
    }
  ],
  "total": 100
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **conversations** | `list` |  |
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
  --url https://services.leadconnectorhq.com/conversations/search \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/conversations/search', {
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
  url: 'https://services.leadconnectorhq.com/conversations/search',
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
  'path': '/conversations/search',
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
  'url': 'https://services.leadconnectorhq.com/conversations/search',
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

unirest('GET', 'https://services.leadconnectorhq.com/conversations/search')
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

url = "https://services.leadconnectorhq.com/conversations/search"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/conversations/search', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/conversations/search"))
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
  url := "https://services.leadconnectorhq.com/conversations/search"
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

url = URI("https://services.leadconnectorhq.com/conversations/search")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversations/search' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
