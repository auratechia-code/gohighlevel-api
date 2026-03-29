# Get Social Media Statistics

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/social-media-posting/statistics` |
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

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `` | No |  |

### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **profileIds** | `string[]` | No |  |
| **platforms** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "results": {
    "dayRange": [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
      "Sat",
      "Sun"
    ],
    "totals": {
      "posts": 0,
      "likes": 0,
      "followers": 0,
      "impressions": 0,
      "comments": 0
    },
    "postPerformance": {
      "posts": {
        "google": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ]
      },
      "impressions": [
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "likes": [
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "comments": [
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    },
    "breakdowns": {
      "posts": {
        "total": 0,
        "totalChange": 0,
        "platforms": {
          "google": {
            "value": 0,
            "change": 0
          }
        }
      },
      "impressions": {
        "total": 0,
        "totalChange": 0,
        "platforms": {
          "google": {
            "value": 0,
            "change": 0
          }
        }
      },
      "reach": {
        "total": 0,
        "totalChange": 0,
        "platforms": {
          "google": {
            "value": 0,
            "change": 0
          }
        }
      },
      "engagement": {
        "google": {
          "likes": 0,
          "comments": 0,
          "shares": 0,
          "change": 0
        }
      }
    },
    "platformTotals": {
      "impressions": {
        "google": {
          "total": 0,
          "series": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        }
      },
      "followers": {
        "google": {
          "total": 0,
          "series": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        }
      },
      "likes": {
        "google": {
          "total": 0,
          "series": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        }
      }
    },
    "demographics": {
      "gender": {
        "totals": {
          "male": {
            "total": 0,
            "percentage": 0
          },
          "female": {
            "total": 0,
            "percentage": 0
          },
          "unknown": {
            "total": 0,
            "percentage": 0
          }
        }
      },
      "age": {
        "totals": {
          "13-17": 0,
          "18-24": 0,
          "25-34": 0,
          "35-44": 0,
          "45-54": 0,
          "55-64": 0,
          "65+": 0
        }
      }
    }
  },
  "message": "Analytics Built Successfully",
  "traceId": "42fc8dd8-d55b-475f-944f-9efb90d77564"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **results** | `dict` |  |
| **message** | `str` |  |
| **traceId** | `str` |  |

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
  --url https://services.leadconnectorhq.com/social-media-posting/statistics \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "profileIds": "string",
  "platforms": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/social-media-posting/statistics', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "profileIds": "string",
  "platforms": "string"
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
  url: 'https://services.leadconnectorhq.com/social-media-posting/statistics',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "profileIds": "string",
  "platforms": "string"
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
  'path': '/social-media-posting/statistics',
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
  "profileIds": "string",
  "platforms": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/social-media-posting/statistics',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "profileIds": "string",
  "platforms": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/social-media-posting/statistics')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "profileIds": "string",
  "platforms": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/social-media-posting/statistics"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "profileIds": "string",
  "platforms": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/social-media-posting/statistics', [
  'headers' => $headers,
  'body' => '{
  "profileIds": "string",
  "platforms": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/social-media-posting/statistics"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"profileIds\": \"string\",
  \"platforms\": \"string\"
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
  url := "https://services.leadconnectorhq.com/social-media-posting/statistics"
  payload := strings.NewReader(`{
  "profileIds": "string",
  "platforms": "string"
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

url = URI("https://services.leadconnectorhq.com/social-media-posting/statistics")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "profileIds": "string",
  "platforms": "string"
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
  "profileIds": "string",
  "platforms": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/statistics' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
