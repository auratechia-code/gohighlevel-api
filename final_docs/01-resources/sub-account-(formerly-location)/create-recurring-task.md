# Create Recurring Task

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks` |
| **Scopes Required** | `N/A` |
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
| **locationId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **title** | `string` | No |  |
| **description** | `string` | No |  |
| **contactIds** | `string[]` | No |  |
| **owners** | `string[]` | No |  |
| **rruleOptions** | `object` | Yes | Recurring rules intervalType string required Possible values: [ yearly , monthly , weekly , daily , hourly ] Example: monthly interval number required Example: 2 startDate string required Start Date Example: 2021-09-30T00:00:00.000Z endDate string End Date Example: 2021-09-30T00:00:00.000Z dayOfMonth number 1, 2, 3, ..., 27, 31 Example: 15 dayOfWeek string Possible values: [ MO , TU , WE , TH , FR , SA , SU ] Example: MO monthOfYear number 1, 2, ....., 11, 12 Example: 1 count number Max number of task executions Example: 10 createTaskIfOverDue boolean Create Task If Over Due Example: true dueAfterSeconds number required Due after seconds Example: 23404000 |
| **intervalType** | `string` | No |  |
| **interval** | `number` | No |  |
| **startDate** | `string` | No |  |
| **endDate** | `string` | No |  |
| **dayOfMonth** | `number` | No |  |
| **dayOfWeek** | `string` | No |  |
| **monthOfYear** | `number` | No |  |
| **count** | `number` | No |  |
| **createTaskIfOverDue** | `boolean` | No |  |
| **dueAfterSeconds** | `number` | No |  |
| **ignoreTaskCreation** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "recurringTask": {
    "id": "sx6wyHhbFdRXh302Lunr",
    "title": "Task Name",
    "description": "Task Description",
    "locationId": "sx6wyHhbFdRXh302Lunr",
    "updatedAt": "2021-04-15T10:00:00.000Z",
    "createdAt": "2021-04-15T10:00:00.000Z",
    "rruleOptions": {
      "createTaskIfOverDue": false,
      "interval": 1,
      "intervalType": "hourly",
      "startDate": "2024-10-29T12:34:03.000Z",
      "dueAfterSeconds": 600,
      "count": 550
    },
    "totalOccurrence": 10,
    "deleted": false,
    "assignedTo": "sx6wyHhbFdRXh302Lunr",
    "contactId": "v5cEPM428h8vShlRW1KT"
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **recurringTask** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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
  url: 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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
  'path': '/locations/:locationId/recurring-tasks',
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
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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

unirest('POST', 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks', [
  'headers' => $headers,
  'body' => '{
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"title\": \"string\",
  \"description\": \"string\",
  \"contactIds\": \"string\",
  \"owners\": \"string\",
  \"rruleOptions\": \"string\",
  \"intervalType\": \"string\",
  \"interval\": 123,
  \"startDate\": \"string\",
  \"endDate\": \"string\",
  \"dayOfMonth\": 123,
  \"dayOfWeek\": \"string\",
  \"monthOfYear\": 123,
  \"count\": 123,
  \"createTaskIfOverDue\": true,
  \"dueAfterSeconds\": 123,
  \"ignoreTaskCreation\": true
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
  url := "https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks"
  payload := strings.NewReader(`{
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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

url = URI("https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
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
  "title": "string",
  "description": "string",
  "contactIds": "string",
  "owners": "string",
  "rruleOptions": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "endDate": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "monthOfYear": 123,
  "count": 123,
  "createTaskIfOverDue": true,
  "dueAfterSeconds": 123,
  "ignoreTaskCreation": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
