# Create template

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/template` |
| **Scopes Required** | `invoices/template.write` |
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
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **internal** | `boolean` | No |  |
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
| **items** | `object[]` | Yes | Array [ name string required Invoice Item Name Example: ABC Product description string Invoice descriptions Example: ABC Corp. productId string Product Id Example: 6578278e879ad2646715ba9c priceId string Price Id Example: 6578278e879ad2646715ba9c currency string required Currency Example: USD amount number required Product amount Example: 999 qty number required Product Quantity Example: 1 taxes object[] Tax Array [ _id string required name string required rate number required calculation string Possible values: [ exclusive ] description string taxId string ] automaticTaxCategoryId string Tax category id for calculating automatic tax Example: 6578278e879ad2646715ba9c isSetupFeeItem boolean Setupfee item, only created when 1st invoice of recurring schedule is generated type string Price type of the item Possible values: [ one_time , recurring ] Example: one_time taxInclusive boolean true if item amount is tax inclusive Default value: false Example: true ] |
| **name** | `string` | No |  |
| **description** | `string` | No |  |
| **productId** | `string` | No |  |
| **priceId** | `string` | No |  |
| **currency** | `string` | No |  |
| **amount** | `number` | No |  |
| **qty** | `number` | No |  |
| **taxes** | `object[]` | Yes | Tax Array [ _id string required name string required rate number required calculation string Possible values: [ exclusive ] description string taxId string ] |
| **_id** | `string` | No |  |
| **name** | `string` | No |  |
| **rate** | `number` | No |  |
| **calculation** | `string` | No |  |
| **description** | `string` | No |  |
| **taxId** | `string` | No |  |
| **automaticTaxCategoryId** | `string` | No |  |
| **isSetupFeeItem** | `boolean` | No |  |
| **type** | `string` | No |  |
| **taxInclusive** | `boolean` | No |  |
| **automaticTaxesEnabled** | `boolean` | No |  |
| **discount** | `object` | Yes | value number Discount Value Default value: 0 Example: 10 type string required Discount type Possible values: [ percentage , fixed ] Default value: percentage Example: percentage validOnProductIds string[] Product Ids on which discount is applicable Example: [ '6579751d56f60276e5bd4154' ] |
| **value** | `number` | No |  |
| **type** | `string` | No |  |
| **validOnProductIds** | `string[]` | No |  |
| **termsNotes** | `string` | No |  |
| **title** | `string` | No |  |
| **tipsConfiguration** | `object` | Yes | Configuration for tips on invoices tipsPercentage string[] required Percentage of tips allowed Example: [5,10,15] tipsEnabled boolean required Tips enabled status Example: true |
| **tipsPercentage** | `string[]` | No |  |
| **tipsEnabled** | `boolean` | No |  |
| **lateFeesConfiguration** | `object` | Yes | Late fees configuration for the invoices enable boolean required Enable late fees Example: true value number required Late Fees Value Example: 10 type string required Late Fees Type Possible values: [ fixed , percentage ] Example: fixed frequency object required Late Fees Frequency intervalCount number required Late fees interval count Example: 10 interval string required Late fees interval Possible values: [ minute , hour , day , week , month , one_time ] Example: day grace object Late Fees Grace intervalCount number required Late fees grace interval count Example: 10 interval string required Late fees grace interval Possible values: [ day ] Example: day maxLateFees object Max late fees payable type string required Possible values: [ fixed ] Example: fixed value number required Max late fees to pay Example: 10 |
| **enable** | `boolean` | No |  |
| **value** | `number` | No |  |
| **type** | `string` | No |  |
| **frequency** | `object` | Yes | Late Fees Frequency intervalCount number required Late fees interval count Example: 10 interval string required Late fees interval Possible values: [ minute , hour , day , week , month , one_time ] Example: day |
| **intervalCount** | `number` | No |  |
| **interval** | `string` | No |  |
| **grace** | `object` | Yes | Late Fees Grace intervalCount number required Late fees grace interval count Example: 10 interval string required Late fees grace interval Possible values: [ day ] Example: day |
| **intervalCount** | `number` | No |  |
| **interval** | `string` | No |  |
| **maxLateFees** | `object` | Yes | Max late fees payable type string required Possible values: [ fixed ] Example: fixed value number required Max late fees to pay Example: 10 |
| **type** | `string` | No |  |
| **value** | `number` | No |  |
| **invoiceNumberPrefix** | `string` | No |  |
| **paymentMethods** | `object` | Yes | Payment Methods for Invoices stripe object required Payment Method enableBankDebitOnly boolean required Enable Bank Debit Only Example: false |
| **stripe** | `object` | Yes | Payment Method enableBankDebitOnly boolean required Enable Bank Debit Only Example: false |
| **enableBankDebitOnly** | `boolean` | No |  |
| **attachments** | `string[]` | No |  |
| **miscellaneousCharges** | `object` | Yes | miscellaneous charges for the invoice charges array[] required charges for the processing fee collectedMiscellaneousCharges number collected miscellaneous charges Example: 10 paidCharges object[] paid miscellaneous charges Array [ name string required name of the processing fee Example: Processing Fee charge number required charge for the processing fee Example: 10 amount number required amount of the processing fee Example: 10 _id string required id of the processing fee Example: 673d01d7d547648a8dab6211 ] |
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
  "_id": "6578278e879ad2646715ba9c",
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "New Template",
  "businessDetails": {
    "name": "Alex",
    "address": {
      "addressLine1": "9931 Beechwood",
      "city": "St. Houston",
      "state": "TX",
      "countryCode": "USA",
      "postalCode": "559-6993"
    },
    "phoneNo": "+1-214-559-6993",
    "website": "www.example.com"
  },
  "currency": "USD",
  "discount": {
    "type": "percentage",
    "value": 0
  },
  "items": [
    {
      "taxes": [],
      "_id": "c6tZZU0rJBf30ZXx9Gli",
      "productId": "c6tZZU0rJBf30ZXx9Gli",
      "priceId": "c6tZZU0rJBf30ZXx9Gli",
      "currency": "USD",
      "name": "Macbook Pro",
      "qty": 1,
      "amount": 999
    }
  ],
  "invoiceNumberPrefix": "INV-",
  "total": 999,
  "createdAt": "2023-12-12T09:27:42.355Z",
  "updatedAt": "2023-12-12T09:27:42.355Z"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **name** | `str` |  |
| **businessDetails** | `dict` |  |
| **currency** | `str` |  |
| **discount** | `dict` |  |
| **items** | `list` |  |
| **invoiceNumberPrefix** | `str` |  |
| **total** | `int` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |

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
  --url https://services.leadconnectorhq.com/invoices/template \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/invoices/template', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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
  url: 'https://services.leadconnectorhq.com/invoices/template',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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
  'path': '/invoices/template',
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
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/invoices/template',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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

unirest('POST', 'https://services.leadconnectorhq.com/invoices/template')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/invoices/template"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/invoices/template', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/template"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"internal\": true,
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
  \"description\": \"string\",
  \"productId\": \"string\",
  \"priceId\": \"string\",
  \"amount\": 123,
  \"qty\": 123,
  \"taxes\": \"string\",
  \"_id\": \"string\",
  \"rate\": 123,
  \"calculation\": \"string\",
  \"taxId\": \"string\",
  \"automaticTaxCategoryId\": \"string\",
  \"isSetupFeeItem\": true,
  \"type\": \"string\",
  \"taxInclusive\": true,
  \"automaticTaxesEnabled\": true,
  \"discount\": \"string\",
  \"value\": 123,
  \"validOnProductIds\": \"string\",
  \"termsNotes\": \"string\",
  \"title\": \"string\",
  \"tipsConfiguration\": \"string\",
  \"tipsPercentage\": \"string\",
  \"tipsEnabled\": true,
  \"lateFeesConfiguration\": \"string\",
  \"enable\": true,
  \"frequency\": \"string\",
  \"intervalCount\": 123,
  \"interval\": \"string\",
  \"grace\": \"string\",
  \"maxLateFees\": \"string\",
  \"invoiceNumberPrefix\": \"string\",
  \"paymentMethods\": \"string\",
  \"stripe\": \"string\",
  \"enableBankDebitOnly\": true,
  \"attachments\": \"string\",
  \"miscellaneousCharges\": \"string\",
  \"charges\": \"string\",
  \"collectedMiscellaneousCharges\": 123,
  \"paidCharges\": \"string\",
  \"charge\": 123
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
  url := "https://services.leadconnectorhq.com/invoices/template"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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

url = URI("https://services.leadconnectorhq.com/invoices/template")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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
  "internal": true,
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
  "description": "string",
  "productId": "string",
  "priceId": "string",
  "amount": 123,
  "qty": 123,
  "taxes": "string",
  "_id": "string",
  "rate": 123,
  "calculation": "string",
  "taxId": "string",
  "automaticTaxCategoryId": "string",
  "isSetupFeeItem": true,
  "type": "string",
  "taxInclusive": true,
  "automaticTaxesEnabled": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "tipsConfiguration": "string",
  "tipsPercentage": "string",
  "tipsEnabled": true,
  "lateFeesConfiguration": "string",
  "enable": true,
  "frequency": "string",
  "intervalCount": 123,
  "interval": "string",
  "grace": "string",
  "maxLateFees": "string",
  "invoiceNumberPrefix": "string",
  "paymentMethods": "string",
  "stripe": "string",
  "enableBankDebitOnly": true,
  "attachments": "string",
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/template' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
