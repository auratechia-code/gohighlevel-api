# Update Contact

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/contacts/:contactId` |
| **Scopes Required** | `contacts.write` |
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
| **contactId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **firstName** | `string` | No |  |
| **lastName** | `string` | No |  |
| **name** | `string` | No |  |
| **email** | `string` | No |  |
| **phone** | `string` | No |  |
| **address1** | `string` | No |  |
| **city** | `string` | No |  |
| **state** | `string` | No |  |
| **postalCode** | `string` | No |  |
| **website** | `string` | No |  |
| **timezone** | `string` | No |  |
| **dnd** | `boolean` | No |  |
| **dndSettings** | `object` | Yes | Call object status string required Possible values: [ active , inactive , permanent ] message string code string Email object status string required Possible values: [ active , inactive , permanent ] message string code string SMS object status string required Possible values: [ active , inactive , permanent ] message string code string WhatsApp object status string required Possible values: [ active , inactive , permanent ] message string code string GMB object status string required Possible values: [ active , inactive , permanent ] message string code string FB object status string required Possible values: [ active , inactive , permanent ] message string code string |
| **Call** | `object` | Yes | status string required Possible values: [ active , inactive , permanent ] message string code string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **code** | `string` | No |  |
| **Email** | `object` | Yes | status string required Possible values: [ active , inactive , permanent ] message string code string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **code** | `string` | No |  |
| **SMS** | `object` | Yes | status string required Possible values: [ active , inactive , permanent ] message string code string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **code** | `string` | No |  |
| **WhatsApp** | `object` | Yes | status string required Possible values: [ active , inactive , permanent ] message string code string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **code** | `string` | No |  |
| **GMB** | `object` | Yes | status string required Possible values: [ active , inactive , permanent ] message string code string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **code** | `string` | No |  |
| **FB** | `object` | Yes | status string required Possible values: [ active , inactive , permanent ] message string code string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **code** | `string` | No |  |
| **inboundDndSettings** | `object` | Yes | all object status string required Possible values: [ active , inactive ] message string |
| **all** | `object` | Yes | status string required Possible values: [ active , inactive ] message string |
| **status** | `string` | No |  |
| **message** | `string` | No |  |
| **tags** | `string[]` | No |  |
| **customFields** | `object[]` | Yes | Array [ anyOf TextField LargeTextField SingleSelectField RadioField NumericField MonetoryField CheckboxField MultiSelectField FileField id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string Example: My Text id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string Example: My Text id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string Example: My Selected Option id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string Example: My Selected Option id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value object Example: 100 id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value object Example: 100.5 id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string[] Example: ["test","test2"] id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value string[] Example: ["test","test2"] id string required Example: 6dvNaf7VhkQ9snc5vnjJ key string Example: my_custom_field field_value object Example: {"f31175d4-2b06-4fc6-b7bc-74cd814c68cb":{"meta":{"fieldname":"1HeGizb13P0odwgOgKSs","originalname":"IMG_20231215_164412935.jpg","encoding":"7bit","mimetype":"image/jpeg","size":1786611,"uuid":"f31175d4-2b06-4fc6-b7bc-74cd814c68cb"},"url":"https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ","documentId":"w2M9qTZ0ZJz8rGt02jdJ"}} ] |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `object` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `object` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string[]` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `string[]` | No |  |
| **id** | `string` | No |  |
| **key** | `string` | No |  |
| **field_value** | `object` | No |  |
| **source** | `string` | No |  |
| **dateOfBirth** | `object` | No |  |
| **country** | `string` | No |  |
| **assignedTo** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "succeded": true,
  "contact": {
    "id": "seD4PfOuKoVMLkEZqohJ",
    "name": "rubika deo",
    "locationId": "ve9EPM428h8vShlRW1KT",
    "firstName": "rubika",
    "lastName": "Deo",
    "email": "rubika@deos.com",
    "emailLowerCase": "rubika@deos.com",
    "timezone": "Asia/Calcutta",
    "companyName": "DGS VolMAX",
    "phone": "+18832327657",
    "dnd": true,
    "dndSettings": {
      "Call": {
        "status": "active",
        "message": "string",
        "code": "string"
      },
      "Email": {
        "status": "active",
        "message": "string",
        "code": "string"
      },
      "SMS": {
        "status": "active",
        "message": "string",
        "code": "string"
      },
      "WhatsApp": {
        "status": "active",
        "message": "string",
        "code": "string"
      },
      "GMB": {
        "status": "active",
        "message": "string",
        "code": "string"
      },
      "FB": {
        "status": "active",
        "message": "string",
        "code": "string"
      }
    },
    "type": "read",
    "source": "public api",
    "assignedTo": "ve9EPM428h8vShlRW1KT",
    "address1": "3535 1st St N",
    "city": "ruDolomitebika",
    "state": "AL",
    "country": "US",
    "postalCode": "35061",
    "website": "https://www.tesla.com",
    "tags": [
      "nisi sint commodo amet",
      "consequat"
    ],
    "dateOfBirth": "Date format YYYY-MM-DD",
    "dateAdded": "2021-07-02T05:18:26.704Z",
    "dateUpdated": "2021-07-02T05:18:26.704Z",
    "attachments": "string",
    "ssn": "string",
    "keyword": "test",
    "firstNameLowerCase": "rubika",
    "fullNameLowerCase": "rubika deo",
    "lastNameLowerCase": "deo",
    "lastActivity": "2021-07-16T11:39:30.564Z",
    "customFields": [
      {
        "id": "MgobCB14YMVKuE4Ka8p1",
        "value": "name"
      }
    ],
    "businessId": "641c094001436dbc2081e642",
    "attributionSource": {
      "url": "Trigger Link",
      "campaign": "string",
      "utmSource": "string",
      "utmMedium": "string",
      "utmContent": "string",
      "referrer": "https: //www.google.com",
      "campaignId": "string",
      "fbclid": "string",
      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY\u00a31-MAIWmEaAo2VEALW_WCB",
      "msclikid": "string",
      "dclid": "string",
      "fbc": "string",
      "fbp": "fb. 1.1674748390986.1171287961",
      "fbEventId": "Mozilla/5.0",
      "userAgent": "Mozilla/5.0",
      "ip": "58.111.106.198",
      "medium": "survey",
      "mediumId": "FglfHAn30PRwsZVyQlKp"
    },
    "lastAttributionSource": {
      "url": "Trigger Link",
      "campaign": "string",
      "utmSource": "string",
      "utmMedium": "string",
      "utmContent": "string",
      "referrer": "https: //www.google.com",
      "campaignId": "string",
      "fbclid": "string",
      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY\u00a31-MAIWmEaAo2VEALW_WCB",
      "msclikid": "string",
      "dclid": "string",
      "fbc": "string",
      "fbp": "fb. 1.1674748390986.1171287961",
      "fbEventId": "Mozilla/5.0",
      "userAgent": "Mozilla/5.0",
      "ip": "58.111.106.198",
      "medium": "survey",
      "mediumId": "FglfHAn30PRwsZVyQlKp"
    },
    "visitorId": "ve9EPM428h8vShlRW1KT"
  }
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **succeded** | `bool` |  |
| **contact** | `dict` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/contacts/:contactId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/contacts/:contactId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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
  method: 'put',
  url: 'https://services.leadconnectorhq.com/contacts/:contactId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/contacts/:contactId',
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
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/contacts/:contactId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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

unirest('PUT', 'https://services.leadconnectorhq.com/contacts/:contactId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/contacts/:contactId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/contacts/:contactId', [
  'headers' => $headers,
  'body' => '{
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/contacts/:contactId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"firstName\": \"string\",
  \"lastName\": \"string\",
  \"name\": \"string\",
  \"email\": \"string\",
  \"phone\": \"string\",
  \"address1\": \"string\",
  \"city\": \"string\",
  \"state\": \"string\",
  \"postalCode\": \"string\",
  \"website\": \"string\",
  \"timezone\": \"string\",
  \"dnd\": true,
  \"dndSettings\": \"string\",
  \"Call\": \"string\",
  \"status\": \"string\",
  \"message\": \"string\",
  \"code\": \"string\",
  \"Email\": \"string\",
  \"SMS\": \"string\",
  \"WhatsApp\": \"string\",
  \"GMB\": \"string\",
  \"FB\": \"string\",
  \"inboundDndSettings\": \"string\",
  \"all\": \"string\",
  \"tags\": \"string\",
  \"customFields\": \"string\",
  \"id\": \"string\",
  \"key\": \"string\",
  \"field_value\": \"string\",
  \"source\": \"string\",
  \"dateOfBirth\": \"string\",
  \"country\": \"string\",
  \"assignedTo\": \"string\"
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
  url := "https://services.leadconnectorhq.com/contacts/:contactId"
  payload := strings.NewReader(`{
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
}`)
  req, _ := http.NewRequest("PUT", url, payload)
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

url = URI("https://services.leadconnectorhq.com/contacts/:contactId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
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
  "firstName": "string",
  "lastName": "string",
  "name": "string",
  "email": "string",
  "phone": "string",
  "address1": "string",
  "city": "string",
  "state": "string",
  "postalCode": "string",
  "website": "string",
  "timezone": "string",
  "dnd": true,
  "dndSettings": "string",
  "Call": "string",
  "status": "string",
  "message": "string",
  "code": "string",
  "Email": "string",
  "SMS": "string",
  "WhatsApp": "string",
  "GMB": "string",
  "FB": "string",
  "inboundDndSettings": "string",
  "all": "string",
  "tags": "string",
  "customFields": "string",
  "id": "string",
  "key": "string",
  "field_value": "string",
  "source": "string",
  "dateOfBirth": "string",
  "country": "string",
  "assignedTo": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/:contactId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
