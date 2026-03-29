# Create notification

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/:calendarId/notifications` |
| **Scopes Required** | `calendars/events.write` |
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
| **calendarId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **receiverType** | `string` | No |  |
| **channel** | `string` | No |  |
| **notificationType** | `string` | No |  |
| **isActive** | `boolean` | No |  |
| **templateId** | `string` | No |  |
| **body** | `string` | No |  |
| **subject** | `string` | No |  |
| **afterTime** | `object[]` | Yes | Specifies the time after which the follow-up notification should be sent. This is not required for other notification types. Array [ timeOffset number unit string ] |
| **timeOffset** | `number` | No |  |
| **unit** | `string` | No |  |
| **beforeTime** | `object[]` | Yes | Specifies the time before which the reminder notification should be sent. This is not required for other notification types. Array [ timeOffset number unit string ] |
| **timeOffset** | `number` | No |  |
| **unit** | `string` | No |  |
| **additionalEmailIds** | `string[]` | No |  |
| **additionalPhoneNumbers** | `string[]` | No |  |
| **selectedUsers** | `string[]` | No |  |
| **fromAddress** | `string` | No |  |
| **fromName** | `string` | No |  |
| **fromNumber** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
[
  {
    "_id": "string",
    "receiverType": "contact",
    "additionalEmailIds": [
      "example1@email.com",
      "example2@email.com"
    ],
    "additionalPhoneNumbers": [
      "+919876744444",
      "+919876744445"
    ],
    "channel": "email",
    "notificationType": "confirmation",
    "isActive": true,
    "additionalWhatsappNumbers": [
      "+919876744444",
      "+919876744445"
    ],
    "templateId": "0as9d8as0d",
    "body": "This is a test notification",
    "subject": "Test Notification",
    "afterTime": [
      {
        "timeOffset": 1,
        "unit": "hours"
      }
    ],
    "beforeTime": [
      {
        "timeOffset": 1,
        "unit": "hours"
      }
    ],
    "selectedUsers": [
      "user1",
      "user2"
    ],
    "deleted": false
  }
]
```

### Response Field Table

N/A
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
  --url https://services.leadconnectorhq.com/calendars/:calendarId/notifications \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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
  url: 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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
  'path': '/calendars/:calendarId/notifications',
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
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/:calendarId/notifications"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications', [
  'headers' => $headers,
  'body' => '{
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/:calendarId/notifications"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"receiverType\": \"string\",
  \"channel\": \"string\",
  \"notificationType\": \"string\",
  \"isActive\": true,
  \"templateId\": \"string\",
  \"body\": \"string\",
  \"subject\": \"string\",
  \"afterTime\": \"string\",
  \"timeOffset\": 123,
  \"unit\": \"string\",
  \"beforeTime\": \"string\",
  \"additionalEmailIds\": \"string\",
  \"additionalPhoneNumbers\": \"string\",
  \"selectedUsers\": \"string\",
  \"fromAddress\": \"string\",
  \"fromName\": \"string\",
  \"fromNumber\": \"string\"
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
  url := "https://services.leadconnectorhq.com/calendars/:calendarId/notifications"
  payload := strings.NewReader(`{
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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

url = URI("https://services.leadconnectorhq.com/calendars/:calendarId/notifications")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
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
  "receiverType": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "fromAddress": "string",
  "fromName": "string",
  "fromNumber": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
