# List Subscriptions

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | GET |
| **Endpoint URL** | `https://services.leadconnectorhq.com/payments/subscriptions` |
| **Scopes Required** | `payments/subscriptions.readonly` |
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
| **altId** | `` | Yes | altType string required Possible values: [ location ] AltType is the type of identifier. Example: location |
| **altType** | `` | No | entityId string Entity id for filtering of subscriptions. Example: 61dd0fe9c077f73e67f78803 |
| **entityId** | `` | No | paymentMode string Mode of payment. Example: live |
| **paymentMode** | `` | No | startAt string Starting interval of subscriptions. Example: 2024-02-01 |
| **startAt** | `` | No | endAt string Closing interval of subscriptions. Example: 2024-02-13 |
| **endAt** | `` | No | entitySourceType string Source of the subscriptions. Example: funnel |
| **entitySourceType** | `` | No | search string The name of the subscription for searching. Example: Awesome subscription |
| **search** | `` | No | contactId string Contact ID for the subscription Example: AmuzcoPBpgKeccNsFlib |
| **contactId** | `` | No | id string Subscription id for filtering of subscriptions. Example: 64bf78af39118e4011926cba |
| **id** | `` | No | limit number The maximum number of items to be included in a single page of results Default value: 10 Example: 20 |
| **limit** | `` | No | offset number The starting index of the page, indicating the position from which the results should be retrieved. Default value: 0 Example: 0 |
| **offset** | `` | No | getPaymentsCollectedCount boolean Get the total payments collected for the subscription. Example: true |
| **getPaymentsCollectedCount** | `` | No |  |

### Body Parameters

N/A
---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "data": [
    {
      "_id": "64bf78af39118e4011926cba",
      "altId": "3SwdhCu3svxI8AKsPJt6",
      "altType": "location",
      "contactId": "XPLSw2SVagl12LMDeTmQ",
      "contactName": "James Bond",
      "contactEmail": "james.bond@gohighlevel.com",
      "currency": "USD",
      "amount": "100",
      "status": "active",
      "liveMode": "false",
      "entityType": "order",
      "entityId": "62f4db0f3059ecee61379012",
      "entitySourceType": "funnel",
      "entitySourceName": "Attribution Funnel",
      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",
      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",
      "subscriptionId": "I-0UE609H8E43P",
      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",
      "paymentProviderType": "stripe",
      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",
      "ipAddress": "103.100.16.82",
      "createdAt": "2023-11-20T10:23:36.515Z",
      "updatedAt": "2023-11-20T10:23:36.515Z",
      "createdBy": "user123"
    }
  ],
  "totalCount": 0
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **data** | `list` |  |
| **totalCount** | `int` |  |

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
  --url https://services.leadconnectorhq.com/payments/subscriptions \
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
    const response = await ghl.api.request('GET', 'https://services.leadconnectorhq.com/payments/subscriptions', {
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
  url: 'https://services.leadconnectorhq.com/payments/subscriptions',
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
  'path': '/payments/subscriptions',
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
  'url': 'https://services.leadconnectorhq.com/payments/subscriptions',
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

unirest('GET', 'https://services.leadconnectorhq.com/payments/subscriptions')
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

url = "https://services.leadconnectorhq.com/payments/subscriptions"
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
$response = $client->request('GET', 'https://services.leadconnectorhq.com/payments/subscriptions', [
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
    .uri(URI.create("https://services.leadconnectorhq.com/payments/subscriptions"))
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
  url := "https://services.leadconnectorhq.com/payments/subscriptions"
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

url = URI("https://services.leadconnectorhq.com/payments/subscriptions")
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

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/subscriptions' -Method 'GET' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
