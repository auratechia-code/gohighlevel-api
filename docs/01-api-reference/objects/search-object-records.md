# Search Object Records

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/objects/:schemaKey/records/search` |
| **Scopes Required** | `objects/record.readonly` |
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
| **schemaKey** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **page** | `number` | No |  |
| **pageLimit** | `number` | No |  |
| **query** | `string` | No |  |
| **searchAfter** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "records": [
    {
      "id": "661c06b4ffde146bdb469442",
      "owner": [
        "sx6wyHhbFdRXh302Lunr"
      ],
      "followers": [
        "sx6wyHhbFdRXh302Lunr",
        "v5cEPM428h8vShlRW1KT"
      ],
      "properties": {
        "customer_number": 1424,
        "ticket_name": "Customer not able login",
        "phone_number": "+917000000000",
        "money": {
          "currency": "default",
          "value": 100
        },
        "type_of_ticket": "doubt",
        "section_of_app": [
          "contacts",
          "smartlist"
        ],
        "recieved_on": "2024-07-11",
        "my_files": [
          {
            "url": "---url_of_file---"
          }
        ],
        "my_textbox_list.option_a": "Value 1",
        "my_textbox_list.option_b": "Value 2"
      },
      "createdAt": "2024-07-29T15:51:28.071Z",
      "updatedAt": "2024-07-29T15:51:28.071Z",
      "locationId": "ve9EPM428h8vShlRW1KT",
      "objectId": "6d6f6e676f5f6576656e7473",
      "objectKey": "custom_objects.pet",
      "createdBy": {
        "channel": "WEB_USER",
        "createdAt": "2025-01-02T09:35:39.032Z",
        "source": "PUBLIC_API",
        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"
      },
      "lastUpdatedBy": {
        "channel": "WEB_USER",
        "createdAt": "2025-01-02T09:35:39.032Z",
        "source": "PUBLIC_API",
        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"
      },
      "searchAfter": [
        1738683828372,
        "67a235b49b289431bcf657f8"
      ]
    }
  ],
  "total": 20
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **records** | `list` |  |
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
curl --request POST \
  --url https://services.leadconnectorhq.com/objects/:schemaKey/records/search \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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
  url: 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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
  'path': '/objects/:schemaKey/records/search',
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
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/objects/:schemaKey/records/search"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/objects/:schemaKey/records/search"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"page\": 123,
  \"pageLimit\": 123,
  \"query\": \"string\",
  \"searchAfter\": \"string\"
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
  url := "https://services.leadconnectorhq.com/objects/:schemaKey/records/search"
  payload := strings.NewReader(`{
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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

url = URI("https://services.leadconnectorhq.com/objects/:schemaKey/records/search")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
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
  "page": 123,
  "pageLimit": 123,
  "query": "string",
  "searchAfter": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
