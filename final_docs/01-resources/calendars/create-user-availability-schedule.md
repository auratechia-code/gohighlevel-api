# Create user availability schedule

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/schedules` |
| **Scopes Required** | `calendars.write` |
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
| **rules** | `object[]` | Yes | Schedule rules defining when the schedule is active Array [ type string required Type of schedule rule - weekday (recurring) or date (specific date) Possible values: [ wday , date ] Example: wday intervals object[] required Time intervals for the rule (e.g., 9 AM to 5 PM) Array [ from string required Start time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 09:00 to string required End time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 17:00 ] date string Specific date in YYYY-MM-DD format (only for date-type rules) Possible values: Value must match regular expression ^\d{4}-\d{2}-\d{2}$ Example: 2023-04-15 day string Day of week (only for weekday-type rules) Possible values: [ sunday , monday , tuesday , wednesday , thursday , friday , saturday ] Example: monday ] |
| **type** | `string` | No |  |
| **intervals** | `object[]` | Yes | Time intervals for the rule (e.g., 9 AM to 5 PM) Array [ from string required Start time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 09:00 to string required End time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 17:00 ] |
| **from** | `string` | No |  |
| **to** | `string` | No |  |
| **date** | `string` | No |  |
| **day** | `string` | No |  |
| **timezone** | `string` | No |  |
| **locationId** | `string` | No |  |
| **name** | `string` | No |  |
| **userId** | `string` | No |  |
| **calendarIds** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "schedule": {
    "id": "IkqiJlXJ7o9h61tCHHod",
    "name": "Business Hours Schedule",
    "locationId": "IkqiJlXJ7o9h61tCHHod",
    "rules": [
      {
        "type": "wday",
        "intervals": [
          {
            "from": "09:00",
            "to": "17:00"
          }
        ],
        "date": "2023-04-15",
        "day": "monday"
      }
    ],
    "timezone": "America/New_York",
    "dateAdded": "2023-01-15T10:30:00.000Z",
    "dateUpdated": "2023-01-20T14:45:00.000Z",
    "userId": "IkqiJlXJ7o9h61tCHHod",
    "calendarIds": [
      "string"
    ],
    "deleted": false
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **schedule** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/calendars/schedules \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/calendars/schedules', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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
  url: 'https://services.leadconnectorhq.com/calendars/schedules',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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
  'path': '/calendars/schedules',
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
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/calendars/schedules',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/calendars/schedules')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/schedules"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/calendars/schedules', [
  'headers' => $headers,
  'body' => '{
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/schedules"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"rules\": \"string\",
  \"type\": \"string\",
  \"intervals\": \"string\",
  \"from\": \"string\",
  \"to\": \"string\",
  \"date\": \"string\",
  \"day\": \"string\",
  \"timezone\": \"string\",
  \"locationId\": \"string\",
  \"name\": \"string\",
  \"userId\": \"string\",
  \"calendarIds\": \"string\"
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
  url := "https://services.leadconnectorhq.com/calendars/schedules"
  payload := strings.NewReader(`{
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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

url = URI("https://services.leadconnectorhq.com/calendars/schedules")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
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
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string",
  "locationId": "string",
  "name": "string",
  "userId": "string",
  "calendarIds": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/schedules' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
