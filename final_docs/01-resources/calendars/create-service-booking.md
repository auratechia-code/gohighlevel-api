# Create Service Booking

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/calendars/services/bookings` |
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

N/A
### Query Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **overrideAvailability** | `` | No | skipSchedulingNotice boolean If set to true, the minimum scheduling notice and date range would be ignored Default value: false |
| **skipSchedulingNotice** | `` | No |  |

### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **contactId** | `string` | No |  |
| **startTime** | `string` | No |  |
| **endTime** | `string` | No |  |
| **timezone** | `string` | No |  |
| **services** | `object[]` | Yes | Services Array [ id string required Service ID Example: a3b4c5d6e7f8901234567890 staffId string Staff ID Example: 8MkU36Wps2w5bRbuGtw3 position number Position Example: 0 addOns object[] Add-ons Array [ id string required Add-on ID Example: 6985f6dfacf123513228d384 quantity number Add-on quantity Example: 2 duration number Add-on duration (in minutes) Example: 30 ] ] |
| **id** | `string` | No |  |
| **staffId** | `string` | No |  |
| **position** | `number` | No |  |
| **addOns** | `object[]` | Yes | Add-ons Array [ id string required Add-on ID Example: 6985f6dfacf123513228d384 quantity number Add-on quantity Example: 2 duration number Add-on duration (in minutes) Example: 30 ] |
| **id** | `string` | No |  |
| **quantity** | `number` | No |  |
| **duration** | `number` | No |  |
| **serviceLocationId** | `string` | No |  |
| **meetingLocation** | `string` | No |  |
| **title** | `string` | No |  |
| **status** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "bookingId": "7NkT25Vor1v4aQatFsv2",
  "locationId": "0007BWpSzSwfiuSl0tR2",
  "serviceLocationId": "65e5f6dfacf123513228d384",
  "startTime": "2023-09-25T16:00:00+05:30",
  "endTime": "2023-09-25T16:30:00+05:30",
  "services": [
    {
      "id": "68e5f6dfacf123513228d384",
      "serviceCategoryId": "3c4d5e6f7890123456789abc",
      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",
      "serviceStartTime": "2023-09-25T16:00:00+05:30",
      "serviceEndTime": "2023-09-25T16:30:00+05:30",
      "serviceResources": [
        {
          "id": "6985f6dfacf123513228d384"
        }
      ],
      "serviceAddOns": [
        {
          "id": "6985f6dfacf123513228d384",
          "quantity": 2
        }
      ]
    }
  ],
  "timezone": "America/New_York",
  "status": "confirmed",
  "meetingLocation": "123 Main St, Anytown, USA",
  "messages": [
    "Meeting location is not supported for the selected service location and has been ignored."
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **bookingId** | `str` |  |
| **locationId** | `str` |  |
| **serviceLocationId** | `str` |  |
| **startTime** | `str` |  |
| **endTime** | `str` |  |
| **services** | `list` |  |
| **timezone** | `str` |  |
| **status** | `str` |  |
| **meetingLocation** | `str` |  |
| **messages** | `list` |  |

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
  --url https://services.leadconnectorhq.com/calendars/services/bookings \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/calendars/services/bookings', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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
  url: 'https://services.leadconnectorhq.com/calendars/services/bookings',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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
  'path': '/calendars/services/bookings',
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
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/calendars/services/bookings',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/calendars/services/bookings')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/calendars/services/bookings"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/calendars/services/bookings', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/calendars/services/bookings"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"contactId\": \"string\",
  \"startTime\": \"string\",
  \"endTime\": \"string\",
  \"timezone\": \"string\",
  \"services\": \"string\",
  \"id\": \"string\",
  \"staffId\": \"string\",
  \"position\": 123,
  \"addOns\": \"string\",
  \"quantity\": 123,
  \"duration\": 123,
  \"serviceLocationId\": \"string\",
  \"meetingLocation\": \"string\",
  \"title\": \"string\",
  \"status\": \"string\"
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
  url := "https://services.leadconnectorhq.com/calendars/services/bookings"
  payload := strings.NewReader(`{
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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

url = URI("https://services.leadconnectorhq.com/calendars/services/bookings")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
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
  "locationId": "string",
  "contactId": "string",
  "startTime": "string",
  "endTime": "string",
  "timezone": "string",
  "services": "string",
  "id": "string",
  "staffId": "string",
  "position": 123,
  "addOns": "string",
  "quantity": 123,
  "duration": 123,
  "serviceLocationId": "string",
  "meetingLocation": "string",
  "title": "string",
  "status": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/services/bookings' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
