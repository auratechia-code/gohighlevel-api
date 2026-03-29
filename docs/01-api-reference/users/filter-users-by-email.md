# Filter Users by Email

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/users/search/filter-by-email` |
| **Scopes Required** | `users.readonly` |
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
| **companyId** | `string` | No |  |
| **emails** | `string` | No |  |
| **deleted** | `boolean` | No |  |
| **skip** | `string` | No |  |
| **limit** | `string` | No |  |
| **projection** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "users": [
    {
      "id": "0IHuJvc2ofPAAA8GzTRi",
      "name": "John Deo",
      "firstName": "John",
      "lastName": "Deo",
      "email": "john@deo.com",
      "phone": "+1 808-868-8888",
      "extension": "",
      "permissions": {
        "campaignsEnabled": true,
        "campaignsReadOnly": false,
        "contactsEnabled": true,
        "workflowsEnabled": true,
        "workflowsReadOnly": true,
        "triggersEnabled": true,
        "funnelsEnabled": true,
        "websitesEnabled": false,
        "opportunitiesEnabled": true,
        "dashboardStatsEnabled": true,
        "bulkRequestsEnabled": true,
        "appointmentsEnabled": true,
        "reviewsEnabled": true,
        "onlineListingsEnabled": true,
        "phoneCallEnabled": true,
        "conversationsEnabled": true,
        "assignedDataOnly": false,
        "adwordsReportingEnabled": false,
        "membershipEnabled": false,
        "facebookAdsReportingEnabled": false,
        "attributionsReportingEnabled": false,
        "settingsEnabled": true,
        "tagsEnabled": true,
        "leadValueEnabled": true,
        "marketingEnabled": true,
        "agentReportingEnabled": true,
        "botService": false,
        "socialPlanner": true,
        "bloggingEnabled": true,
        "invoiceEnabled": true,
        "affiliateManagerEnabled": true,
        "contentAiEnabled": true,
        "refundsEnabled": true,
        "recordPaymentEnabled": true,
        "cancelSubscriptionEnabled": true,
        "paymentsEnabled": true,
        "communitiesEnabled": true,
        "exportPaymentsEnabled": true
      },
      "scopes": "campaigns.readonly",
      "roles": {
        "type": "account",
        "role": "admin",
        "locationIds": [
          "ve9EPM428h8vShlRW1KT"
        ],
        "restrictSubAccount": true
      },
      "deleted": false,
      "lcPhone": {
        "locationId": "+1234556677"
      },
      "platformLanguage": "en_US"
    }
  ],
  "count": 1231
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **users** | `list` |  |
| **count** | `int` |  |

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
  --url https://services.leadconnectorhq.com/users/search/filter-by-email \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/users/search/filter-by-email', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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
  url: 'https://services.leadconnectorhq.com/users/search/filter-by-email',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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
  'path': '/users/search/filter-by-email',
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
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/users/search/filter-by-email',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/users/search/filter-by-email')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/users/search/filter-by-email"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/users/search/filter-by-email', [
  'headers' => $headers,
  'body' => '{
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/users/search/filter-by-email"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"companyId\": \"string\",
  \"emails\": \"string\",
  \"deleted\": true,
  \"skip\": \"string\",
  \"limit\": \"string\",
  \"projection\": \"string\"
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
  url := "https://services.leadconnectorhq.com/users/search/filter-by-email"
  payload := strings.NewReader(`{
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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

url = URI("https://services.leadconnectorhq.com/users/search/filter-by-email")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
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
  "companyId": "string",
  "emails": "string",
  "deleted": true,
  "skip": "string",
  "limit": "string",
  "projection": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/users/search/filter-by-email' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
