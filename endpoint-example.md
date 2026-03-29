# GET /contacts/:contactId — Full Documentation

**Source:** https://marketplace.gohighlevel.com/docs/ghl/contacts/get-contact  
**Extracted:** 2026-03-29

---

## Overview

| Field        | Value |
|---|---|
| **Method**   | `GET` |
| **Endpoint** | `https://services.leadconnectorhq.com/contacts/:contactId` |
| **Summary**  | Retrieve a single contact by its ID |

---

## Requirements

| Field | Value |
|---|---|
| **Scope(s)** | `contacts.readonly` |
| **Auth Method(s)** | OAuth Access Token, Private Integration Token |
| **Token Type(s)** | Sub-Account Token |

---

## Request

### Header Parameters

| Name | Type | Required | Possible Values | Description |
|---|---|---|---|---|
| `Version` | string | ✅ Yes | `2021-07-28` | API Version |
| `Authorization` | string | ✅ Yes | `Bearer <TOKEN>` | OAuth or Private Integration token |
| `Accept` | string | ✅ Yes | `application/json` | Response format |

### Path Parameters

| Name | Type | Required | Description | Example |
|---|---|---|---|---|
| `contactId` | string | ✅ Yes | Unique identifier of the contact | `ocQHyuzHvysMo5N5VsXc` |

---

## Responses

### 200 — Successful Response

**Content-Type:** `application/json`

#### Response Schema

```json
{
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
      "Call":     { "status": "active", "message": "string", "code": "string" },
      "Email":    { "status": "active", "message": "string", "code": "string" },
      "SMS":      { "status": "active", "message": "string", "code": "string" },
      "WhatsApp": { "status": "active", "message": "string", "code": "string" },
      "GMB":      { "status": "active", "message": "string", "code": "string" },
      "FB":       { "status": "active", "message": "string", "code": "string" }
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
    "tags": ["nisi sint commodo amet", "consequat"],
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
      { "id": "MgobCB14YMVKuE4Ka8p1", "value": "name" }
    ],
    "businessId": "641c094001436dbc2081e642",
    "attributionSource": {
      "url": "Trigger Link",
      "campaign": "string",
      "utmSource": "string",
      "utmMedium": "string",
      "utmContent": "string",
      "referrer": "https://www.google.com",
      "campaignId": "string",
      "fbclid": "string",
      "gclid": "string",
      "msclikid": "string",
      "dclid": "string",
      "fbc": "string",
      "fbp": "fb.1.1674748390986.1171287961",
      "fbEventId": "string",
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
      "referrer": "https://www.google.com",
      "campaignId": "string",
      "fbclid": "string",
      "gclid": "string",
      "msclikid": "string",
      "dclid": "string",
      "fbc": "string",
      "fbp": "fb.1.1674748390986.1171287961",
      "fbEventId": "string",
      "userAgent": "Mozilla/5.0",
      "ip": "58.111.106.198",
      "medium": "survey",
      "mediumId": "FglfHAn30PRwsZVyQlKp"
    },
    "visitorId": "ve9EPM428h8vShlRW1KT"
  }
}
```

#### Response Fields — `contact` object

| Field | Type | Description |
|---|---|---|
| `id` | string | Contact unique ID |
| `name` | string | Full name |
| `locationId` | string | Sub-account (location) ID |
| `firstName` | string | First name |
| `lastName` | string | Last name |
| `email` | string | Email address |
| `emailLowerCase` | string | Email in lowercase |
| `timezone` | string | Timezone (e.g. `Asia/Calcutta`) |
| `companyName` | string | Company name |
| `phone` | string | Phone number (E.164 format) |
| `dnd` | boolean | Do Not Disturb flag |
| `dndSettings` | object | DND config per channel |
| `dndSettings.{Channel}.status` | string | `active` or `inactive` |
| `dndSettings.{Channel}.message` | string | DND message |
| `dndSettings.{Channel}.code` | string | DND code |
| `type` | string | Contact type |
| `source` | string | Source of the contact |
| `assignedTo` | string | Assigned user ID |
| `address1` | string | Street address |
| `city` | string | City |
| `state` | string | State code |
| `country` | string | Country code (e.g. `US`) |
| `postalCode` | string | Postal/ZIP code |
| `website` | string | Website URL |
| `tags` | string[] | Array of tags |
| `dateOfBirth` | string | Date of birth (`YYYY-MM-DD`) |
| `dateAdded` | string (ISO 8601) | Creation timestamp |
| `dateUpdated` | string (ISO 8601) | Last update timestamp |
| `attachments` | string | Attachments |
| `ssn` | string | Social Security Number |
| `keyword` | string | Keyword |
| `firstNameLowerCase` | string | First name lowercase |
| `fullNameLowerCase` | string | Full name lowercase |
| `lastNameLowerCase` | string | Last name lowercase |
| `lastActivity` | string (ISO 8601) | Last activity timestamp |
| `customFields` | object[] | Custom field values |
| `customFields[].id` | string | Custom field ID |
| `customFields[].value` | any | Custom field value |
| `businessId` | string | Business ID |
| `attributionSource` | object | First attribution source data |
| `lastAttributionSource` | object | Most recent attribution source |
| `visitorId` | string | Visitor ID |

#### `attributionSource` / `lastAttributionSource` fields

| Field | Type | Description |
|---|---|---|
| `url` | string | Source URL |
| `campaign` | string | Campaign name |
| `utmSource` | string | UTM source |
| `utmMedium` | string | UTM medium |
| `utmContent` | string | UTM content |
| `referrer` | string | Referrer URL |
| `campaignId` | string | Campaign ID |
| `fbclid` | string | Facebook click ID |
| `gclid` | string | Google click ID |
| `msclikid` | string | Microsoft click ID |
| `dclid` | string | Display click ID |
| `fbc` | string | Facebook cookie |
| `fbp` | string | Facebook pixel |
| `fbEventId` | string | Facebook event ID |
| `userAgent` | string | User agent string |
| `ip` | string | IP address |
| `medium` | string | Medium (e.g. `survey`) |
| `mediumId` | string | Medium ID |

### 400 — Bad Request
Invalid parameters or malformed request.

### 401 — Unauthorized
Missing or invalid authentication token.

### 422 — Unprocessable Entity
Validation error on the provided data.

---

## Code Examples

### cURL

```bash
curl -L 'https://services.leadconnectorhq.com/contacts/:contactId' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <TOKEN>' \
  -H 'Version: 2021-07-28'
```

---

### Node.js — SDK (Official @gohighlevel/api-client)

```javascript
const { HighLevel } = require('@gohighlevel/api-client');

const highLevel = new HighLevel({
  clientId: 'your_client_id_here',
  clientSecret: 'your_client_secret_here',
});

try {
  const response = await highLevel.contacts.getContact({
    contactId: 'ocQHyuzHvysMo5N5VsXc'
  });
  console.log(response);
} catch (error) {
  console.error('Error:', error);
}
```

---

### Node.js — Axios

```javascript
const axios = require('axios');

const config = {
  method: 'get',
  maxBodyLength: Infinity,
  url: 'https://services.leadconnectorhq.com/contacts/:contactId',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(config)
  .then((response) => {
    console.log(JSON.stringify(response.data));
  })
  .catch((error) => {
    console.log(error);
  });
```

---

### Node.js — Native HTTPS

```javascript
var https = require('follow-redirects').https;

var options = {
  method: 'GET',
  hostname: 'services.leadconnectorhq.com',
  path: '/contacts/:contactId',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  },
  maxRedirects: 20
};

var req = https.request(options, function (res) {
  var chunks = [];
  res.on('data', function (chunk) { chunks.push(chunk); });
  res.on('end', function () {
    var body = Buffer.concat(chunks);
    console.log(body.toString());
  });
  res.on('error', function (error) { console.error(error); });
});

req.end();
```

---

### Node.js — Request

```javascript
var request = require('request');

var options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/contacts/:contactId',
  headers: {
    'Accept': 'application/json',
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

---

### Node.js — Unirest

```javascript
var unirest = require('unirest');

unirest
  .get('https://services.leadconnectorhq.com/contacts/:contactId')
  .headers({
    'Accept': 'application/json',
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  })
  .end(function (res) {
    if (res.error) throw new Error(res.error);
    console.log(res.body);
  });
```

---

### Python — Requests

```python
import requests

url = "https://services.leadconnectorhq.com/contacts/:contactId"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.get(url, headers=headers)
print(response.json())
```

---

### PHP

```php
<?php

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://services.leadconnectorhq.com/contacts/:contactId', [
  'headers' => [
    'Accept' => 'application/json',
    'Authorization' => 'Bearer <TOKEN>',
    'Version' => '2021-07-28',
  ],
]);

echo $response->getBody();
```

---

### Java

```java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://services.leadconnectorhq.com/contacts/:contactId"))
    .header("Accept", "application/json")
    .header("Authorization", "Bearer <TOKEN>")
    .header("Version", "2021-07-28")
    .method("GET", HttpRequest.BodyPublishers.noBody())
    .build();

HttpResponse<String> response = HttpClient.newHttpClient()
    .send(request, HttpResponse.BodyHandlers.ofString());

System.out.println(response.body());
```

---

### Go

```go
package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
)

func main() {
    url := "https://services.leadconnectorhq.com/contacts/:contactId"

    req, _ := http.NewRequest("GET", url, nil)
    req.Header.Add("Accept", "application/json")
    req.Header.Add("Authorization", "Bearer <TOKEN>")
    req.Header.Add("Version", "2021-07-28")

    res, _ := http.DefaultClient.Do(req)
    defer res.Body.Close()
    body, _ := ioutil.ReadAll(res.Body)

    fmt.Println(string(body))
}
```

---

### Ruby

```ruby
require 'uri'
require 'net/http'

url = URI("https://services.leadconnectorhq.com/contacts/:contactId")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Accept"] = "application/json"
request["Authorization"] = "Bearer <TOKEN>"
request["Version"] = "2021-07-28"

response = http.request(request)
puts response.read_body
```

---

### PowerShell

```powershell
$headers = @{
    "Accept"        = "application/json"
    "Authorization" = "Bearer <TOKEN>"
    "Version"       = "2021-07-28"
}

$response = Invoke-RestMethod `
    -Uri "https://services.leadconnectorhq.com/contacts/:contactId" `
    -Method GET `
    -Headers $headers

$response | ConvertTo-Json
```

---

## Navigation

- **Previous:** [Contacts](/docs/ghl/contacts/contacts)
- **Next:** [Update Contact](/docs/ghl/contacts/update-contact)
