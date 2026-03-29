# Update notification

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId` |
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
| **calendarId** | `` | Yes | notificationId string required |
| **notificationId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **receiverType** | `string` | No |  |
| **additionalEmailIds** | `string[]` | No |  |
| **additionalPhoneNumbers** | `string[]` | No |  |
| **selectedUsers** | `string[]` | No |  |
| **channel** | `string` | No |  |
| **notificationType** | `string` | No |  |
| **isActive** | `boolean` | No |  |
| **deleted** | `boolean` | No |  |
| **templateId** | `string` | No |  |
| **body** | `string` | No |  |
| **subject** | `string` | No |  |
| **afterTime** | `object[]` | Yes | Specifies the time after which the follow-up notification should be sent. This is not required for other notification types. Array [ timeOffset number unit string ] |
| **timeOffset** | `number` | No |  |
| **unit** | `string` | No |  |
| **beforeTime** | `object[]` | Yes | Specifies the time before which the reminder notification should be sent. This is not required for other notification types. Array [ timeOffset number unit string ] |
| **timeOffset** | `number` | No |  |
| **unit** | `string` | No |  |
| **fromAddress** | `string` | No |  |
| **fromNumber** | `string` | No |  |
| **fromName** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "message": "string"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **message** | `str` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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
  method: 'put',
  url: 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/calendars/:calendarId/notifications/:notificationId',
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
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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

unirest('PUT', 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId', [
  'headers' => $headers,
  'body' => '{
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"receiverType\": \"string\",
  \"additionalEmailIds\": \"string\",
  \"additionalPhoneNumbers\": \"string\",
  \"selectedUsers\": \"string\",
  \"channel\": \"string\",
  \"notificationType\": \"string\",
  \"isActive\": true,
  \"deleted\": true,
  \"templateId\": \"string\",
  \"body\": \"string\",
  \"subject\": \"string\",
  \"afterTime\": \"string\",
  \"timeOffset\": 123,
  \"unit\": \"string\",
  \"beforeTime\": \"string\",
  \"fromAddress\": \"string\",
  \"fromNumber\": \"string\",
  \"fromName\": \"string\"
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
  url := "https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId"
  payload := strings.NewReader(`{
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
}`)
  req, _ := http.NewRequest("PUT", url, payload)
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

url = URI("https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "receiverType": "string",
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
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
  "additionalEmailIds": "string",
  "additionalPhoneNumbers": "string",
  "selectedUsers": "string",
  "channel": "string",
  "notificationType": "string",
  "isActive": true,
  "deleted": true,
  "templateId": "string",
  "body": "string",
  "subject": "string",
  "afterTime": "string",
  "timeOffset": 123,
  "unit": "string",
  "beforeTime": "string",
  "fromAddress": "string",
  "fromNumber": "string",
  "fromName": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/:calendarId/notifications/:notificationId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
