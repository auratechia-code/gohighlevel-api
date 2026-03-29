# Update Contacts Tags

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type` |
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

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **contacts** | `string[]` | No |  |
| **tags** | `string[]` | No |  |
| **locationId** | `string` | No |  |
| **removeAllTags** | `boolean` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "succeded": true,
  "errorCount": 0,
  "responses": [
    {
      "contactId": "qFSqySFkVvNzOSqgGqFi",
      "message": "Tags updated",
      "type": "success",
      "oldTags": [
        "tag-1",
        "tag-2"
      ],
      "tagsAdded": [],
      "tagsRemoved": []
    },
    {
      "contactId": "abcdef",
      "message": "contact id is not a valid firebase id",
      "type": "error"
    },
    {
      "contactId": "qFSqySFkVvNzOSqgGqFi",
      "message": "contact is deleted",
      "type": "error"
    },
    {
      "contactId": "3ualbhnV7j3n3a9r2moD",
      "message": "contact does not belong to location",
      "type": "error"
    }
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **succeded** | `bool` |  |
| **errorCount** | `int` |  |
| **responses** | `list` |  |

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
  --url https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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
  url: 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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
  'path': '/contacts/bulk/tags/update/:type',
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
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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

unirest('POST', 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type', [
  'headers' => $headers,
  'body' => '{
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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
    .uri(URI.create("https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"contacts\": \"string\",
  \"tags\": \"string\",
  \"locationId\": \"string\",
  \"removeAllTags\": true
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
  url := "https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type"
  payload := strings.NewReader(`{
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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

url = URI("https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
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
  "contacts": "string",
  "tags": "string",
  "locationId": "string",
  "removeAllTags": true
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
