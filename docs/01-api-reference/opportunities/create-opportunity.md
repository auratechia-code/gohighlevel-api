# Create Opportunity

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/opportunities/` |
| **Scopes Required** | `opportunities.write` |
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
| **pipelineId** | `string` | No |  |
| **locationId** | `string` | No |  |
| **name** | `string` | No |  |
| **pipelineStageId** | `string` | No |  |
| **status** | `string` | No |  |
| **contactId** | `string` | No |  |
| **monetaryValue** | `number` | No |  |
| **assignedTo** | `string` | No |  |
| **customFields** | `object[]` | Yes | Add custom fields to opportunities. Array [ anyOf customFieldsInputStringSchema customFieldsInputArraySchema customFieldsInputObjectSchema id string Pass either id or key of custom field Example: 6dvNaf7VhkQ9snc5vnjJ key string Pass either id or key of custom field Example: my_custom_field field_value string Example: 9039160788 id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string[] Example: ["test","test2"] id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value object Example: {} ] |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string[]` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `object` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "opportunity": {
    "id": "yWQobCRIhRguQtD2llvk",
    "name": "testing",
    "monetaryValue": 500,
    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",
    "assignedTo": "zT46WSCPbudrq4zhWMk6",
    "status": "open",
    "source": "",
    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",
    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",
    "lastActionDate": "2021-08-03T04:55:17.355Z",
    "indexVersion": 1,
    "createdAt": "2021-08-03T04:55:17.355Z",
    "updatedAt": "2021-08-03T04:55:17.355Z",
    "contactId": "zT46WSCPbudrq4zhWMk6",
    "locationId": "zT46WSCPbudrq4zhW",
    "contact": {
      "id": "byMEV0NQinDhq8ZfiOi2",
      "name": "John Deo",
      "companyName": "Tesla Inc",
      "email": "john@deo.com",
      "phone": "+1202-555-0107",
      "tags": [
        "string"
      ]
    },
    "notes": [
      [
        null
      ]
    ],
    "tasks": [
      [
        null
      ]
    ],
    "calendarEvents": [
      [
        null
      ]
    ],
    "lostReasonId": "zT46WSCPbudrq4zhWMk6",
    "customFields": [
      {
        "id": "MgobCB14YMVKuE4Ka8p1",
        "fieldValue": "string"
      }
    ],
    "followers": [
      [
        null
      ]
    ]
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **opportunity** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/opportunities/ \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/opportunities/', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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
  url: 'https://services.leadconnectorhq.com/opportunities/',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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
  'path': '/opportunities/',
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
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/opportunities/',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/opportunities/')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/opportunities/"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/opportunities/', [
  'headers' => $headers,
  'body' => '{
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/opportunities/"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"pipelineId\": \"string\",
  \"locationId\": \"string\",
  \"name\": \"string\",
  \"pipelineStageId\": \"string\",
  \"status\": \"string\",
  \"contactId\": \"string\",
  \"monetaryValue\": 123,
  \"assignedTo\": \"string\",
  \"customFields\": \"string\",
  \"id\": \"string\",
  \"key\": \"string\",
  \"field_value\": \"string\"
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
  url := "https://services.leadconnectorhq.com/opportunities/"
  payload := strings.NewReader(`{
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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

url = URI("https://services.leadconnectorhq.com/opportunities/")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
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
  "pipelineId": "string",
  "locationId": "string",
  "name": "string",
  "pipelineStageId": "string",
  "status": "string",
  "contactId": "string",
  "monetaryValue": 123,
  "assignedTo": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/opportunities/' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
