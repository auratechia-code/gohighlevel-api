# Update Estimate Template

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/estimate/template/:templateId` |
| **Scopes Required** | `invoices/estimate.write` |
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
| **templateId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **name** | `string` | No |  |
| **businessDetails** | `object` | No | logoUrl string Business Logo URL Example: https://example.com/logo.png name string Business Name Example: ABC Corp. phoneNo string Business Phone Number Example: +1-214-559-6993 address object Business Address addressLine1 string Address Line 1 Example: 9931 Beechwood addressLine2 string Address Line 2 Example: Beechwood city string City Example: St. Houston state string State Example: TX countryCode string Country Code Example: US postalCode string Postal Code Example: 559-6993 website string Business Website Link Example: wwww.example.com customValues string[] Custom Values |
| **logoUrl** | `string` | No |  |
| **name** | `string` | No |  |
| **phoneNo** | `string` | No |  |
| **address** | `object` | No | Business Address addressLine1 string Address Line 1 Example: 9931 Beechwood addressLine2 string Address Line 2 Example: Beechwood city string City Example: St. Houston state string State Example: TX countryCode string Country Code Example: US postalCode string Postal Code Example: 559-6993 |
| **addressLine1** | `string` | No |  |
| **addressLine2** | `string` | No |  |
| **city** | `string` | No |  |
| **state** | `string` | No |  |
| **countryCode** | `string` | No |  |
| **postalCode** | `string` | No |  |
| **website** | `string` | No |  |
| **customValues** | `string[]` | No |  |
| **currency** | `string` | No |  |
| **items** | `array[]` | No |  |
| **liveMode** | `boolean` | No |  |
| **discount** | `object` | Yes | value number Discount Value Default value: 0 Example: 10 type string required Discount type Possible values: [ percentage , fixed ] Default value: percentage Example: percentage validOnProductIds string[] Product Ids on which discount is applicable Example: [ '6579751d56f60276e5bd4154' ] |
| **value** | `number` | No |  |
| **type** | `string` | No |  |
| **validOnProductIds** | `string[]` | No |  |
| **termsNotes** | `string` | No |  |
| **title** | `string` | No |  |
| **automaticTaxesEnabled** | `boolean` | No |  |
| **meta** | `object` | No |  |
| **sendEstimateDetails** | `object` | Yes | When sending estimate directly while saving altId string required Location Id or Agency Id Example: 6578278e879ad2646715ba9c altType string required Possible values: [ location ] action string required Possible values: [ sms_and_email , send_manually , email , sms ] liveMode boolean required livemode for estimate Example: true userId string required Please ensure that the UserId corresponds to an authorized personnel, either by an employee ID or agency ID, to access this location. This account will serve as the primary channel for all future communications and updates. Example: 6578278e879ad2646715ba9c sentFrom object sender details for invoice, valid only if invoice is not sent manually fromName string Sender name to be used while sending email notification Example: Alex fromEmail string Email id to be used while sending email notification Example: alex@example.com estimateName string estimate name Example: Estimate |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **action** | `string` | No |  |
| **liveMode** | `boolean` | No |  |
| **userId** | `string` | No |  |
| **sentFrom** | `object` | No | sender details for invoice, valid only if invoice is not sent manually fromName string Sender name to be used while sending email notification Example: Alex fromEmail string Email id to be used while sending email notification Example: alex@example.com |
| **fromName** | `string` | No |  |
| **fromEmail** | `string` | No |  |
| **estimateName** | `string` | No |  |
| **estimateNumberPrefix** | `string` | No |  |
| **attachments** | `object[]` | Yes | attachments for the invoice Array [ id string required Id of the file selected Example: 6241712be68f7a98102ba272 name string required Name of the file Example: Electronics.pdf url string required URL of the file Example: https://example.com/digital-delivery type string required Type of the file size number required Size of the file Example: 10000 ] |
| **id** | `string` | No |  |
| **name** | `string` | No |  |
| **url** | `string` | No |  |
| **type** | `string` | No |  |
| **size** | `number` | No |  |
| **miscellaneousCharges** | `object` | Yes | miscellaneous charges for the estimate charges array[] required charges for the processing fee collectedMiscellaneousCharges number collected miscellaneous charges Example: 10 paidCharges object[] paid miscellaneous charges Array [ name string required name of the processing fee Example: Processing Fee charge number required charge for the processing fee Example: 10 amount number required amount of the processing fee Example: 10 _id string required id of the processing fee Example: 673d01d7d547648a8dab6211 ] |
| **charges** | `array[]` | No |  |
| **collectedMiscellaneousCharges** | `number` | No |  |
| **paidCharges** | `object[]` | Yes | paid miscellaneous charges Array [ name string required name of the processing fee Example: Processing Fee charge number required charge for the processing fee Example: 10 amount number required amount of the processing fee Example: 10 _id string required id of the processing fee Example: 673d01d7d547648a8dab6211 ] |
| **name** | `string` | No |  |
| **charge** | `number` | No |  |
| **amount** | `number` | No |  |
| **_id** | `string` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "_id": "67ac9a51106ee8311e911XXXX",
  "liveMode": true,
  "deleted": false,
  "name": "Estimate Name",
  "currency": "USD",
  "businessDetails": {
    "logoUrl": "your_image-url",
    "name": "Business name",
    "address": {
      "addressLine1": "address line 1",
      "city": "Test City",
      "state": "State Name",
      "countryCode": "US",
      "postalCode": "12345"
    },
    "phoneNo": "+1 1234567890",
    "website": "www.example.com",
    "customValues": [
      {
        "name": "Test",
        "fieldKey": "{{custom_values.test}}",
        "id": "5DYTWoiQvWiIJZXX44XXX",
        "value": "Test's Custom Value"
      }
    ]
  },
  "items": [
    {
      "taxes": [],
      "taxInclusive": false,
      "_id": "67ac9a51106ee8311e911XXXX",
      "description": "<p>Futuristic anti-gravity racing</p>",
      "currency": "USD",
      "productId": "67ac9a51106ee8311e911XXXX",
      "priceId": "67ac9a51106ee8311e911XXXX",
      "amount": 9.99,
      "qty": 1,
      "name": "TEST",
      "type": "one_time"
    },
    {
      "taxes": [
        {
          "_id": "67ac9a51106ee8311e911XXXX",
          "name": "TaxTwo",
          "rate": 8.5,
          "calculation": "exclusive"
        }
      ],
      "taxInclusive": true,
      "_id": "67ac9a51106ee8311e911XXXX",
      "productId": "67ac9a51106ee8311e911XXXX",
      "priceId": "67ac9a51106ee8311e911XXXX",
      "currency": "USD",
      "name": "TEST2",
      "qty": 1,
      "amount": 500,
      "description": "",
      "type": "recurring"
    }
  ],
  "discount": {
    "type": "percentage",
    "value": 0
  },
  "title": "ESTIMATE",
  "estimateNumberPrefix": "EST-",
  "attachments": [
    {
      "id": "6241712be68f7a98102ba272",
      "name": "Electronics.pdf",
      "url": "https://example.com/digital-delivery",
      "type": "string",
      "size": 10000
    }
  ],
  "updatedBy": "3HIpOF9NIc5ltriQXXXX",
  "total": 1222.03,
  "createdAt": "2025-02-12T13:17:47.416Z",
  "updatedAt": "2025-02-12T13:17:47.416Z",
  "__v": 0,
  "automaticTaxesEnabled": false,
  "termsNotes": "<p>All services are subject to availability.</p>"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **_id** | `str` |  |
| **liveMode** | `bool` |  |
| **deleted** | `bool` |  |
| **name** | `str` |  |
| **currency** | `str` |  |
| **businessDetails** | `dict` |  |
| **items** | `list` |  |
| **discount** | `dict` |  |
| **title** | `str` |  |
| **estimateNumberPrefix** | `str` |  |
| **attachments** | `list` |  |
| **updatedBy** | `str` |  |
| **total** | `float` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |
| **__v** | `int` |  |
| **automaticTaxesEnabled** | `bool` |  |
| **termsNotes** | `str` |  |

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
  --url https://services.leadconnectorhq.com/invoices/estimate/template/:templateId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/invoices/estimate/template/:templateId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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
  url: 'https://services.leadconnectorhq.com/invoices/estimate/template/:templateId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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
  'path': '/invoices/estimate/template/:templateId',
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
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/invoices/estimate/template/:templateId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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

unirest('PUT', 'https://services.leadconnectorhq.com/invoices/estimate/template/:templateId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/invoices/estimate/template/:templateId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/invoices/estimate/template/:templateId', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/estimate/template/:templateId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"name\": \"string\",
  \"businessDetails\": \"string\",
  \"logoUrl\": \"string\",
  \"phoneNo\": \"string\",
  \"address\": \"string\",
  \"addressLine1\": \"string\",
  \"addressLine2\": \"string\",
  \"city\": \"string\",
  \"state\": \"string\",
  \"countryCode\": \"string\",
  \"postalCode\": \"string\",
  \"website\": \"string\",
  \"customValues\": \"string\",
  \"currency\": \"string\",
  \"items\": \"string\",
  \"liveMode\": true,
  \"discount\": \"string\",
  \"value\": 123,
  \"type\": \"string\",
  \"validOnProductIds\": \"string\",
  \"termsNotes\": \"string\",
  \"title\": \"string\",
  \"automaticTaxesEnabled\": true,
  \"meta\": \"string\",
  \"sendEstimateDetails\": \"string\",
  \"action\": \"string\",
  \"userId\": \"string\",
  \"sentFrom\": \"string\",
  \"fromName\": \"string\",
  \"fromEmail\": \"string\",
  \"estimateName\": \"string\",
  \"estimateNumberPrefix\": \"string\",
  \"attachments\": \"string\",
  \"id\": \"string\",
  \"url\": \"string\",
  \"size\": 123,
  \"miscellaneousCharges\": \"string\",
  \"charges\": \"string\",
  \"collectedMiscellaneousCharges\": 123,
  \"paidCharges\": \"string\",
  \"charge\": 123,
  \"amount\": 123,
  \"_id\": \"string\"
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
  url := "https://services.leadconnectorhq.com/invoices/estimate/template/:templateId"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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

url = URI("https://services.leadconnectorhq.com/invoices/estimate/template/:templateId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
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
  "altId": "string",
  "altType": "string",
  "name": "string",
  "businessDetails": "string",
  "logoUrl": "string",
  "phoneNo": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "website": "string",
  "customValues": "string",
  "currency": "string",
  "items": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "type": "string",
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "estimateNumberPrefix": "string",
  "attachments": "string",
  "id": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "amount": 123,
  "_id": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/estimate/template/:templateId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
