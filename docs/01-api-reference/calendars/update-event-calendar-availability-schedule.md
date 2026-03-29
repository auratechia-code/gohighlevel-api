# Update event calendar availability schedule

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId` |
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

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **calendarId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **rules** | `object[]` | Yes | Updated schedule rules defining when the schedule is active Array [ type string required Type of schedule rule - weekday (recurring) or date (specific date) Possible values: [ wday , date ] Example: wday intervals object[] required Time intervals for the rule (e.g., 9 AM to 5 PM) Array [ from string required Start time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 09:00 to string required End time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 17:00 ] date string Specific date in YYYY-MM-DD format (only for date-type rules) Possible values: Value must match regular expression ^\d{4}-\d{2}-\d{2}$ Example: 2023-04-15 day string Day of week (only for weekday-type rules) Possible values: [ sunday , monday , tuesday , wednesday , thursday , friday , saturday ] Example: monday ] |
| **type** | `string` | No |  |
| **intervals** | `object[]` | Yes | Time intervals for the rule (e.g., 9 AM to 5 PM) Array [ from string required Start time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 09:00 to string required End time in HH:MM format (24-hour format) Possible values: Value must match regular expression ^([01]?[0-9]|2[0-3]):[0-5][0-9]$ Example: 17:00 ] |
| **from** | `string` | No |  |
| **to** | `string` | No |  |
| **date** | `string` | No |  |
| **day** | `string` | No |  |
| **timezone** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "schedule": {
    "timezone": "America/New_York",
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
    "calendarId": "WvVX9LpvlBO6K506xLbp",
    "dateAdded": "string",
    "dateUpdated": "string"
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
curl --request PUT \
  --url https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId \
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
  "timezone": "string"
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string"
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
  url: 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId',
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
  "timezone": "string"
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
  'path': '/calendars/schedules/event-calendar/:calendarId',
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
  "timezone": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId',
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
  "timezone": "string"
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

unirest('PUT', 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId')
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
  "timezone": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string"
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId', [
  'headers' => $headers,
  'body' => '{
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"rules\": \"string\",
  \"type\": \"string\",
  \"intervals\": \"string\",
  \"from\": \"string\",
  \"to\": \"string\",
  \"date\": \"string\",
  \"day\": \"string\",
  \"timezone\": \"string\"
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
  url := "https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId"
  payload := strings.NewReader(`{
  "rules": "string",
  "type": "string",
  "intervals": "string",
  "from": "string",
  "to": "string",
  "date": "string",
  "day": "string",
  "timezone": "string"
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

url = URI("https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
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
  "timezone": "string"
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
  "timezone": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/schedules/event-calendar/:calendarId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
