# Create Sub-Account (Formerly Location)

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/locations/` |
| **Scopes Required** | `locations.write` |
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
| **name** | `string` | No |  |
| **phone** | `string` | No |  |
| **companyId** | `string` | No |  |
| **address** | `string` | No |  |
| **city** | `string` | No |  |
| **state** | `string` | No |  |
| **country** | `string` | No |  |
| **postalCode** | `string` | No |  |
| **website** | `string` | No |  |
| **timezone** | `string` | No |  |
| **prospectInfo** | `object` | Yes | firstName string required First name of the prospect Example: John lastName string required Last name of the prospect Example: Doe email string required Email of the prospect Example: john.doe@mail.com |
| **firstName** | `string` | No |  |
| **lastName** | `string` | No |  |
| **email** | `string` | No |  |
| **settings** | `object` | No | The default settings for location allowDuplicateContact boolean Example: false allowDuplicateOpportunity boolean Example: false allowFacebookNameMerge boolean Example: false disableContactTimezone boolean Example: false |
| **allowDuplicateContact** | `boolean` | No |  |
| **allowDuplicateOpportunity** | `boolean` | No |  |
| **allowFacebookNameMerge** | `boolean` | No |  |
| **disableContactTimezone** | `boolean` | No |  |
| **social** | `object` | No | The social media links for location facebookUrl string Facebook URL Example: https://www.facebook.com/ googlePlus string Googleplus URL Example: https://www.googleplus.com/ linkedIn string LinkedIn URL Example: https://www.linkedIn.com/ foursquare string Foursquare URL Example: https://www.foursquare.com/ twitter string Twitter URL Example: https://www.foutwitterrsquare.com/ yelp string Yelp URL Example: https://www.yelp.com/ instagram string Instagram URL Example: https://www.instagram.com/ youtube string Instagram URL Example: https://www.youtube.com/ pinterest string Instagram URL Example: https://www.pinterest.com/ blogRss string Instagram URL Example: https://www.blogRss.com/ googlePlacesId string Google Business Places ID Example: ChIJJGPdVbQTrjsRGUkefteUeFk |
| **facebookUrl** | `string` | No |  |
| **googlePlus** | `string` | No |  |
| **linkedIn** | `string` | No |  |
| **foursquare** | `string` | No |  |
| **twitter** | `string` | No |  |
| **yelp** | `string` | No |  |
| **instagram** | `string` | No |  |
| **youtube** | `string` | No |  |
| **pinterest** | `string` | No |  |
| **blogRss** | `string` | No |  |
| **googlePlacesId** | `string` | No |  |
| **twilio** | `object` | Yes | (DEPRECATED) The twilio credentials for location sid string required SID provided by Twilio Example: AC_XXXXXXXXXXX authToken string required Auth token provided by Twilio Example: 77_XXXXXXXXXXX |
| **sid** | `string` | No |  |
| **authToken** | `string` | No |  |
| **mailgun** | `object` | Yes | The mailgun credentials for location apiKey string required API key provided by Mailgun Example: key-XXXXXXXXXXX domain string required Domain connected with Mailgun Example: replies.yourdomain.com |
| **apiKey** | `string` | No |  |
| **domain** | `string` | No |  |
| **snapshotId** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "id": "ve9EPM428h8vShlRW1KT",
  "companyId": "UAXssdawIWAWD",
  "name": "Mark Shoes",
  "phone": "+1410039940",
  "email": "john.doe@mail.com",
  "address": "4th fleet street",
  "city": "New York",
  "state": "Illinois",
  "domain": "test.msgsndr.com",
  "country": "US",
  "postalCode": "567654",
  "website": "https://yourwebsite.com",
  "timezone": "US/Central",
  "settings": {
    "allowDuplicateContact": false,
    "allowDuplicateOpportunity": false,
    "allowFacebookNameMerge": false,
    "disableContactTimezone": false
  },
  "social": {
    "facebookUrl": "https://www.facebook.com/",
    "googlePlus": "https://www.googleplus.com/",
    "linkedIn": "https://www.linkedIn.com/",
    "foursquare": "https://www.foursquare.com/",
    "twitter": "https://www.foutwitterrsquare.com/",
    "yelp": "https://www.yelp.com/",
    "instagram": "https://www.instagram.com/",
    "youtube": "https://www.youtube.com/",
    "pinterest": "https://www.pinterest.com/",
    "blogRss": "https://www.blogRss.com/",
    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **id** | `str` |  |
| **companyId** | `str` |  |
| **name** | `str` |  |
| **phone** | `str` |  |
| **email** | `str` |  |
| **address** | `str` |  |
| **city** | `str` |  |
| **state** | `str` |  |
| **domain** | `str` |  |
| **country** | `str` |  |
| **postalCode** | `str` |  |
| **website** | `str` |  |
| **timezone** | `str` |  |
| **settings** | `dict` |  |
| **social** | `dict` |  |

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
  --url https://services.leadconnectorhq.com/locations/ \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/locations/', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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
  url: 'https://services.leadconnectorhq.com/locations/',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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
  'path': '/locations/',
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
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/locations/',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/locations/')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/locations/"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/locations/', [
  'headers' => $headers,
  'body' => '{
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/locations/"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"name\": \"string\",
  \"phone\": \"string\",
  \"companyId\": \"string\",
  \"address\": \"string\",
  \"city\": \"string\",
  \"state\": \"string\",
  \"country\": \"string\",
  \"postalCode\": \"string\",
  \"website\": \"string\",
  \"timezone\": \"string\",
  \"prospectInfo\": \"string\",
  \"firstName\": \"string\",
  \"lastName\": \"string\",
  \"email\": \"string\",
  \"settings\": \"string\",
  \"allowDuplicateContact\": true,
  \"allowDuplicateOpportunity\": true,
  \"allowFacebookNameMerge\": true,
  \"disableContactTimezone\": true,
  \"social\": \"string\",
  \"facebookUrl\": \"string\",
  \"googlePlus\": \"string\",
  \"linkedIn\": \"string\",
  \"foursquare\": \"string\",
  \"twitter\": \"string\",
  \"yelp\": \"string\",
  \"instagram\": \"string\",
  \"youtube\": \"string\",
  \"pinterest\": \"string\",
  \"blogRss\": \"string\",
  \"googlePlacesId\": \"string\",
  \"twilio\": \"string\",
  \"sid\": \"string\",
  \"authToken\": \"string\",
  \"mailgun\": \"string\",
  \"apiKey\": \"string\",
  \"domain\": \"string\",
  \"snapshotId\": \"string\"
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
  url := "https://services.leadconnectorhq.com/locations/"
  payload := strings.NewReader(`{
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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

url = URI("https://services.leadconnectorhq.com/locations/")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
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
  "name": "string",
  "phone": "string",
  "companyId": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "country": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "prospectInfo": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "settings": "string",
  "allowDuplicateContact": true,
  "allowDuplicateOpportunity": true,
  "allowFacebookNameMerge": true,
  "disableContactTimezone": true,
  "social": "string",
  "facebookUrl": "string",
  "googlePlus": "string",
  "linkedIn": "string",
  "foursquare": "string",
  "twitter": "string",
  "yelp": "string",
  "instagram": "string",
  "youtube": "string",
  "pinterest": "string",
  "blogRss": "string",
  "googlePlacesId": "string",
  "twilio": "string",
  "sid": "string",
  "authToken": "string",
  "mailgun": "string",
  "apiKey": "string",
  "domain": "string",
  "snapshotId": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/locations/' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
