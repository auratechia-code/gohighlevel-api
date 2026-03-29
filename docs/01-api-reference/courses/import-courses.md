# Import Courses

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/courses/courses-exporter/public/import` |
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
| **locationId** | `string` | No |  |
| **userId** | `string` | No |  |
| **products** | `object[]` | Yes | Array [ title string required description string required imageUrl string categories object[] required Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string posts object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] subCategories object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string posts object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] ] ] instructorDetails object name string required description string required ] |
| **title** | `string` | No |  |
| **description** | `string` | No |  |
| **imageUrl** | `string` | No |  |
| **categories** | `object[]` | Yes | Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string posts object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] subCategories object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string posts object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] ] ] |
| **title** | `string` | No |  |
| **visibility** | `visibility (string)` | No |  |
| **thumbnailUrl** | `string` | No |  |
| **posts** | `object[]` | Yes | Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] |
| **title** | `string` | No |  |
| **visibility** | `visibility (string)` | No |  |
| **thumbnailUrl** | `string` | No |  |
| **contentType** | `contentType (string)` | No |  |
| **description** | `string` | No |  |
| **bucketVideoUrl** | `string` | No |  |
| **postMaterials** | `object[]` | Yes | Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] |
| **title** | `string` | No |  |
| **type** | `type (string)` | No |  |
| **url** | `string` | No |  |
| **subCategories** | `object[]` | Yes | Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string posts object[] Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] ] |
| **title** | `string` | No |  |
| **visibility** | `visibility (string)` | No |  |
| **thumbnailUrl** | `string` | No |  |
| **posts** | `object[]` | Yes | Array [ title string required visibility visibility (string) required Possible values: [ published , draft ] thumbnailUrl string contentType contentType (string) required Possible values: [ video , assignment , quiz ] description string required bucketVideoUrl string postMaterials object[] Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] ] |
| **title** | `string` | No |  |
| **visibility** | `visibility (string)` | No |  |
| **thumbnailUrl** | `string` | No |  |
| **contentType** | `contentType (string)` | No |  |
| **description** | `string` | No |  |
| **bucketVideoUrl** | `string` | No |  |
| **postMaterials** | `object[]` | Yes | Array [ title string required type type (string) required Possible values: [ pdf , image , docx , pptx , xlsx , html , dotx , epub , webp , gdoc , mp3 , doc , txt , zip , ppt , key , htm , xls , odp , odt , rtf , m4a , ods , mp4 , ai , avi , mov , wmv , mkv , wav , flac , ogg , png , jpeg , jpg , gif , bmp , tiff , svg , odg , sxw , sxc , sxi , rar , 7z , json , xml , csv , md , obj , stl , woff , ttf ] url string required ] |
| **title** | `string` | No |  |
| **type** | `type (string)` | No |  |
| **url** | `string` | No |  |
| **instructorDetails** | `object` | Yes | name string required description string required |
| **name** | `string` | No |  |
| **description** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "locationId": "string",
  "userId": "string",
  "products": [
    {
      "title": "string",
      "description": "string",
      "imageUrl": "string",
      "categories": [
        {
          "title": "string",
          "visibility": "published",
          "thumbnailUrl": "string",
          "posts": [
            {
              "title": "string",
              "visibility": "published",
              "thumbnailUrl": "string",
              "contentType": "video",
              "description": "string",
              "bucketVideoUrl": "string",
              "postMaterials": [
                {
                  "title": "string",
                  "type": "pdf",
                  "url": "string"
                }
              ]
            }
          ],
          "subCategories": [
            {
              "title": "string",
              "visibility": "published",
              "thumbnailUrl": "string",
              "posts": [
                {
                  "title": "string",
                  "visibility": "published",
                  "thumbnailUrl": "string",
                  "contentType": "video",
                  "description": "string",
                  "bucketVideoUrl": "string",
                  "postMaterials": [
                    {
                      "title": "string",
                      "type": "pdf",
                      "url": "string"
                    }
                  ]
                }
              ]
            }
          ]
        }
      ],
      "instructorDetails": {
        "name": "string",
        "description": "string"
      }
    }
  ]
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **locationId** | `str` |  |
| **userId** | `str` |  |
| **products** | `list` |  |

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
  --url https://services.leadconnectorhq.com/courses/courses-exporter/public/import \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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
  url: 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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
  'path': '/courses/courses-exporter/public/import',
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
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/courses/courses-exporter/public/import"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import', [
  'headers' => $headers,
  'body' => '{
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/courses/courses-exporter/public/import"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"locationId\": \"string\",
  \"userId\": \"string\",
  \"products\": \"string\",
  \"title\": \"string\",
  \"description\": \"string\",
  \"imageUrl\": \"string\",
  \"categories\": \"string\",
  \"visibility\": \"string\",
  \"thumbnailUrl\": \"string\",
  \"posts\": \"string\",
  \"contentType\": \"string\",
  \"bucketVideoUrl\": \"string\",
  \"postMaterials\": \"string\",
  \"type\": \"string\",
  \"url\": \"string\",
  \"subCategories\": \"string\",
  \"instructorDetails\": \"string\",
  \"name\": \"string\"
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
  url := "https://services.leadconnectorhq.com/courses/courses-exporter/public/import"
  payload := strings.NewReader(`{
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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

url = URI("https://services.leadconnectorhq.com/courses/courses-exporter/public/import")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "locationId": "string",
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
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
  "userId": "string",
  "products": "string",
  "title": "string",
  "description": "string",
  "imageUrl": "string",
  "categories": "string",
  "visibility": "string",
  "thumbnailUrl": "string",
  "posts": "string",
  "contentType": "string",
  "bucketVideoUrl": "string",
  "postMaterials": "string",
  "type": "string",
  "url": "string",
  "subCategories": "string",
  "instructorDetails": "string",
  "name": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/courses/courses-exporter/public/import' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
