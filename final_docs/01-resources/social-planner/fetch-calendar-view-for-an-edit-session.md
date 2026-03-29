# Fetch calendar view for an edit session

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar` |
| **Scopes Required** | `socialplanner/category.readonly` |
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
| **queueId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **locationId** | `string` | No |  |
| **sessionId** | `string` | No |  |
| **startDate** | `string` | No |  |
| **endDate** | `string` | No |  |
| **accountIds** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "success": true,
  "statusCode": 201,
  "results": {
    "message": "Edit session calendar fetched successfully",
    "scheduledPosts": [
      {
        "scheduledDateTime": "2023-10-15T10:00:00.000Z",
        "post": {
          "_id": "61bb16833b3f2791f9715be2",
          "source": "composer",
          "locationId": "ve9EPM428h8vShlRW1KT",
          "platform": "google",
          "displayDate": "2023-08-02T00:00:00.000Z",
          "createdAt": "2023-08-02T00:00:00.000Z",
          "updatedAt": "2023-08-02T00:00:00.000Z",
          "accountId": "w37swmmLbA02zgqKPpxITe",
          "error": "Failed due to auth token",
          "postId": "323534534435",
          "publishedAt": "2021-06-22T05:32:49.463Z",
          "accountIds": [
            "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
          ],
          "summary": "Sample Summary",
          "media": [
            {
              "url": "https://example.com/image.jpg",
              "type": "image/jpeg",
              "caption": "Sample caption"
            }
          ],
          "status": "published",
          "createdBy": "Lx1EI6YIgQYMQi0ytFXv",
          "type": "post",
          "tags": [
            "aF3KhyL8JIuBwzK3m7Ly_iVrVJ2uoXNF0wzcBzgl5_12554616564525983496"
          ],
          "ogTagsDetails": {
            "metaImage": "https://example.com/image.jpg",
            "metaLink": "https://www.yahoo.com/",
            "ogTitle": "Page Title",
            "ogDescription": "Page Description"
          },
          "postApprovalDetails": {
            "approver": "iVrVJ2uoXNF0wzcBzgl5",
            "approvalStatus": "approved"
          },
          "tiktokPostDetails": {
            "privacyLevel": "PUBLIC_TO_EVERYONE",
            "enableComment": true
          },
          "gmbPostDetails": {
            "gmbEventType": "STANDARD",
            "actionType": "BOOK"
          },
          "blueskyPostDetails": {
            "shortenedLinks": [
              "string"
            ],
            "replyTo": "at://did:plc:abc123def456/app.bsky.feed.post/xyz789",
            "quotePost": "at://did:plc:abc123def456/app.bsky.feed.post/xyz789",
            "language": "en",
            "externalLink": "https://yoursite.com/article",
            "externalLinkTitle": "10 Tips for Better Social Media Marketing",
            "externalLinkDescription": "Learn how to improve your social media presence with these proven strategies."
          },
          "user": {
            "id": "6284c43d519161e96cc09c13",
            "firstName": "Harry",
            "lastName": "Spencer",
            "email": "abc@xyc.com"
          },
          "linkedinPostDetails": {
            "pdfTitle": "Q4 Marketing Strategy Presentation",
            "postAsPdf": true
          },
          "pinterestPostDetails": {
            "title": "10 Easy Home Decor Ideas for 2024",
            "link": "https://yoursite.com/blog/home-decor-ideas",
            "boardIds": {
              "6887d6de1d8175813d50dab8": "987654321098765432",
              "682c7d1710a2fe3d805a3513": "123456789012345678"
            },
            "shortenedLinks": [
              "string"
            ]
          },
          "facebookPostDetails": {
            "type": "post"
          },
          "instagramPostDetails": {
            "type": "post",
            "collaborators": {
              "accountId1": [
                "username1",
                "username2"
              ],
              "accountId2": [
                "username3",
                "username4"
              ]
            },
            "showOnFeed": true,
            "publishViaPushNotification": true,
            "publisherNote": "When publishing, add swipe up link to the landing page so that we can direct them to the sales page"
          },
          "youtubePostDetails": {
            "title": "How to Build a Successful Marketing Strategy in 2024",
            "privacyLevel": "public",
            "type": "video"
          },
          "communityPostDetails": {
            "title": "Welcome to Our New Community Feature!",
            "notifyAllGroupMembers": true,
            "postAsUser": {
              "xMQswA02zgqKPpxITe": {
                "avatar": "https://lh3.googleusercontent.com/a/user-avatar.jpg",
                "id": "snCr14eeYkSppD04rkNW",
                "name": "John Smith"
              }
            }
          },
          "mediaOptimization": true
        },
        "queueItemId": "60af88475f1b2c001f5d5f4b",
        "queueId": "60af88475f1b2c001f5d5f4a",
        "order": 1000,
        "variations": [
          {
            "_id": "60af88475f1b2c001f5d5f4c",
            "content": "Check out our latest blog post! #marketing #socialmedia",
            "mentions": [
              {
                "platform": "instagram",
                "username": "example_user",
                "offset": 10,
                "length": 12
              }
            ],
            "ogTags": {
              "metaLink": "https://example.com",
              "metaImage": "https://example.com/image.png",
              "ogTitle": "Example Title"
            }
          }
        ],
        "primaryImage": "https://example.com/images/post-image.png",
        "errors": [
          "INVALID_USER_ID",
          "PIXABAY_MEDIA"
        ],
        "category": {
          "_id": "6756f381be2553245b08d30c",
          "name": "Category Name",
          "primaryColor": "#FFFFFF",
          "secondaryColor": "#000000",
          "deleted": false,
          "locationId": "fvg1TXIiVxGcdOaL0riG",
          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",
          "createdAt": "2024-12-09T13:41:21.385Z",
          "updatedAt": "2024-12-09T13:41:21.385Z"
        },
        "currentVariation": 0,
        "timezone": "America/New_York",
        "isDraft": true,
        "originalItemId": "60af88475f1b2c001f5d5f4b"
      }
    ],
    "total": 0,
    "timezone": "string"
  },
  "traceId": "string"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **success** | `bool` |  |
| **statusCode** | `int` |  |
| **results** | `dict` |  |
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
  --url https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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
  url: 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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
  'path': '/social-media-posting/category/queues/:queueId/edit/calendar',
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
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"sessionId\": \"string\",
  \"startDate\": \"string\",
  \"endDate\": \"string\",
  \"accountIds\": \"string\"
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
  url := "https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar"
  payload := strings.NewReader(`{
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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

url = URI("https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
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
  "sessionId": "string",
  "startDate": "string",
  "endDate": "string",
  "accountIds": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/category/queues/:queueId/edit/calendar' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
