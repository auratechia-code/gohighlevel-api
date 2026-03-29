# Search Opportunity

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/opportunities/search` |
| **Scopes Required** | `opportunities.readonly` |
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
| **q** | `` | Yes | location_id string required Location Id Example: i2SpAtBVHSVea1sL6oah |
| **location_id** | `` | No | pipeline_id string Pipeline Id Example: bCkKGpDsyPP4peuKowkG |
| **pipeline_id** | `` | No | pipeline_stage_id string stage Id Example: 7915dedc-8f18-44d5-8bc3-77c04e994a10 |
| **pipeline_stage_id** | `` | No | contact_id string Contact Id Example: WFwVrSSjZ2CNHbZThQX2 |
| **contact_id** | `` | No | status string Possible values: [ open , won , lost , abandoned , all ] |
| **status** | `` | No | assigned_to string Example: 082goXVW3lIExEQPOnd3 |
| **assigned_to** | `` | No | campaignId string Campaign Id Example: Y2I9XM7aO1hncuSOlc9L |
| **campaignId** | `` | No | id string Opportunity Id Example: 123akv4LFn6C9frZoy3e |
| **id** | `` | No | order string Example: added_asc |
| **order** | `` | No | endDate string End date Example: mm-dd-yyyy |
| **endDate** | `` | No | startAfter string Start After Example: 1628008053263 |
| **startAfter** | `` | No | startAfterId string Start After Id Example: UIaE1WjAwWKdlyD7osQI |
| **startAfterId** | `` | No | date string Start date Example: mm-dd-yyyy |
| **date** | `` | No | country string Example: US |
| **country** | `` | No | page number Default value: 1 |
| **page** | `` | No | limit number Limit Per Page records count. will allow maximum up to 100 and default will be 20 Default value: 20 |
| **limit** | `` | No | getTasks boolean get Tasks in contact |
| **getTasks** | `` | No | getNotes boolean get Notes in contact |
| **getNotes** | `` | No | getCalendarEvents boolean get Calender event in contact |
| **getCalendarEvents** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "opportunities": [
    {
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
  ],
  "meta": {
    "total": 1,
    "nextPageUrl": "http://localhost:5066/opportunities/search?q=&location_id=ve9EPM428h8vShlRW1KT&pipeline_id=&pipeline_stage_id=&status=&assigned_to+=&campaignId=&id=&order=&endDate=&startAfter=1625203104328&startAfterId=yWQobCRIhRguQtD2llvk&date=&limit=1&country=&page=1",
    "startAfterId": "yWQobCRIhRguQtD2llvk",
    "startAfter": 1625203104328,
    "currentPage": 2,
    "nextPage": 3,
    "prevPage": 1
  },
  "aggregations": {}
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **opportunities** | `list` |  |
| **meta** | `dict` |  |
| **aggregations** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/opportunities/search \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/opportunities/search', {
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
  url: 'https://services.leadconnectorhq.com/opportunities/search',
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
  'path': '/opportunities/search',
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
  'url': 'https://services.leadconnectorhq.com/opportunities/search',
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

unirest('GET', 'https://services.leadconnectorhq.com/opportunities/search')
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

url = "https://services.leadconnectorhq.com/opportunities/search"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/opportunities/search', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/opportunities/search"))
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
  url := "https://services.leadconnectorhq.com/opportunities/search"
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

url = URI("https://services.leadconnectorhq.com/opportunities/search")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/opportunities/search' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
