# Update schedule

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/schedule/:scheduleId` |
| **Scopes Required** | `invoices/schedule.write` |
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
| **scheduleId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **name** | `string` | No |  |
| **contactDetails** | `object` | Yes | id string required Contact ID Example: 6578278e879ad2646715ba9c name string required Contact Name Example: Alex phoneNo string required Contact Phone Number Example: +1234567890 email string required Contact Email Example: alex@example.com additionalEmails object[] Secondary email addresses for the contact to be saved Array [ email string required Example: alex@example.com ] companyName string Contact Company Name Example: ABC Corp. address object addressLine1 string Address Line 1 Example: 9931 Beechwood addressLine2 string Address Line 2 Example: Beechwood city string City Example: St. Houston state string State Example: TX countryCode string Country Code Example: US postalCode string Postal Code Example: 559-6993 customFields string[] Custom Values |
| **id** | `string` | No |  |
| **name** | `string` | No |  |
| **phoneNo** | `string` | No |  |
| **email** | `string` | No |  |
| **additionalEmails** | `object[]` | Yes | Secondary email addresses for the contact to be saved Array [ email string required Example: alex@example.com ] |
| **email** | `string` | No |  |
| **companyName** | `string` | No |  |
| **address** | `object` | No | addressLine1 string Address Line 1 Example: 9931 Beechwood addressLine2 string Address Line 2 Example: Beechwood city string City Example: St. Houston state string State Example: TX countryCode string Country Code Example: US postalCode string Postal Code Example: 559-6993 |
| **addressLine1** | `string` | No |  |
| **addressLine2** | `string` | No |  |
| **city** | `string` | No |  |
| **state** | `string` | No |  |
| **countryCode** | `string` | No |  |
| **postalCode** | `string` | No |  |
| **customFields** | `string[]` | No |  |
| **schedule** | `object` | Yes | executeAt string rrule object intervalType string required Possible values: [ yearly , monthly , weekly , daily , hourly , minutely , secondly ] Example: monthly interval number required Example: 2 startDate string required Start date in YYYY-MM-DD format Example: 2023-01-01 startTime string Start time in HH:mm:ss format Example: 20:45:00 endDate string End date in YYYY-MM-DD format Example: 2029-11-01 endTime string End time in HH:mm:ss format Example: 18:45:00 dayOfMonth number -1, 1, 2, 3, ..., 27, 28 Example: 15 dayOfWeek string Possible values: [ mo , tu , we , th , fr , sa , su ] Example: mo numOfWeek number -1, 1, 2, 3, 4 Example: -1 monthOfYear string Possible values: [ jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec ] Example: jan count number Max number of task executions Example: 10 daysBefore number Execute task number of days before Example: 5 useStartAsPrimaryUserAccepted boolean Start as primary user accepted date Example: true endType string End type like after, by, count Example: by |
| **executeAt** | `string` | No |  |
| **rrule** | `object` | Yes | intervalType string required Possible values: [ yearly , monthly , weekly , daily , hourly , minutely , secondly ] Example: monthly interval number required Example: 2 startDate string required Start date in YYYY-MM-DD format Example: 2023-01-01 startTime string Start time in HH:mm:ss format Example: 20:45:00 endDate string End date in YYYY-MM-DD format Example: 2029-11-01 endTime string End time in HH:mm:ss format Example: 18:45:00 dayOfMonth number -1, 1, 2, 3, ..., 27, 28 Example: 15 dayOfWeek string Possible values: [ mo , tu , we , th , fr , sa , su ] Example: mo numOfWeek number -1, 1, 2, 3, 4 Example: -1 monthOfYear string Possible values: [ jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec ] Example: jan count number Max number of task executions Example: 10 daysBefore number Execute task number of days before Example: 5 useStartAsPrimaryUserAccepted boolean Start as primary user accepted date Example: true endType string End type like after, by, count Example: by |
| **intervalType** | `string` | No |  |
| **interval** | `number` | No |  |
| **startDate** | `string` | No |  |
| **startTime** | `string` | No |  |
| **endDate** | `string` | No |  |
| **endTime** | `string` | No |  |
| **dayOfMonth** | `number` | No |  |
| **dayOfWeek** | `string` | No |  |
| **numOfWeek** | `number` | No |  |
| **monthOfYear** | `string` | No |  |
| **count** | `number` | No |  |
| **daysBefore** | `number` | No |  |
| **useStartAsPrimaryUserAccepted** | `boolean` | No |  |
| **endType** | `string` | No |  |
| **liveMode** | `boolean` | No |  |
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
| **discount** | `object` | Yes | value number Discount Value Default value: 0 Example: 10 type string required Discount type Possible values: [ percentage , fixed ] Default value: percentage Example: percentage validOnProductIds string[] Product Ids on which discount is applicable Example: [ '6579751d56f60276e5bd4154' ] |
| **value** | `number` | No |  |
| **type** | `string` | No |  |
| **validOnProductIds** | `string[]` | No |  |
| **termsNotes** | `string` | No |  |
| **title** | `string` | No |  |
| **attachments** | `object[]` | Yes | attachments for the invoice Array [ id string required Id of the file selected Example: 6241712be68f7a98102ba272 name string required Name of the file Example: Electronics.pdf url string required URL of the file Example: https://example.com/digital-delivery type string required Type of the file size number required Size of the file Example: 10000 ] |
| **id** | `string` | No |  |
| **name** | `string` | No |  |
| **url** | `string` | No |  |
| **type** | `string` | No |  |
| **size** | `number` | No |  |
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
  "status": "draft",
  "liveMode": false,
  "altId": "6578278e879ad2646715ba9c",
  "altType": "location",
  "name": "New Invoice",
  "schedule": {
    "executeAt": "string",
    "rrule": {
      "intervalType": "monthly",
      "interval": 2,
      "startDate": "2023-01-01",
      "startTime": "20:45:00",
      "endDate": "2029-11-01",
      "endTime": "18:45:00",
      "dayOfMonth": 15,
      "dayOfWeek": "mo",
      "numOfWeek": -1,
      "monthOfYear": "jan",
      "count": 10,
      "daysBefore": 5,
      "useStartAsPrimaryUserAccepted": true,
      "endType": "by"
    }
  },
  "invoices": [
    {
      "_id": "6578278e879ad2646715ba9c",
      "status": "draft",
      "liveMode": false,
      "amountPaid": 0,
      "altId": "6578278e879ad2646715ba9c",
      "altType": "location",
      "name": "New Invoice",
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
      "invoiceNumber": "19",
      "currency": "USD",
      "contactDetails": {
        "id": "c6tZZU0rJBf30ZXx9Gli",
        "phoneNo": "+1-214-559-6993",
        "email": "alex@example.com",
        "customFields": [],
        "name": "Alex",
        "address": {
          "countryCode": "US"
        }
      },
      "issueDate": "2023-01-01",
      "dueDate": "2023-01-01",
      "discount": {
        "type": "percentage",
        "value": 0
      },
      "invoiceItems": [
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
      "total": 999,
      "title": "INVOICE",
      "amountDue": 999,
      "createdAt": "2023-12-12T09:27:42.355Z",
      "updatedAt": "2023-12-12T09:27:42.355Z",
      "automaticTaxesEnabled": true,
      "automaticTaxesCalculated": true,
      "paymentSchedule": {}
    }
  ],
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
  "contactDetails": {
    "id": "c6tZZU0rJBf30ZXx9Gli",
    "phoneNo": "+1-214-559-6993",
    "email": "alex@example.com",
    "customFields": [],
    "name": "Alex",
    "address": {
      "countryCode": "US"
    }
  },
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
  "total": 999,
  "title": "INVOICE",
  "termsNotes": "Confidential",
  "compiledTermsNotes": "Confidential",
  "createdAt": "2023-12-12T09:27:42.355Z",
  "updatedAt": "2023-12-12T09:27:42.355Z"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **status** | `str` |  |
| **liveMode** | `bool` |  |
| **altId** | `str` |  |
| **altType** | `str` |  |
| **name** | `str` |  |
| **schedule** | `dict` |  |
| **invoices** | `list` |  |
| **businessDetails** | `dict` |  |
| **currency** | `str` |  |
| **contactDetails** | `dict` |  |
| **discount** | `dict` |  |
| **items** | `list` |  |
| **total** | `int` |  |
| **title** | `str` |  |
| **termsNotes** | `str` |  |
| **compiledTermsNotes** | `str` |  |
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
curl --request PUT \
  --url https://services.leadconnectorhq.com/invoices/schedule/:scheduleId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
  method: 'put',
  url: 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId',
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
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/invoices/schedule/:scheduleId',
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
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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

unirest('PUT', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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

url = "https://services.leadconnectorhq.com/invoices/schedule/:scheduleId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"name\": \"string\",
  \"contactDetails\": \"string\",
  \"id\": \"string\",
  \"phoneNo\": \"string\",
  \"email\": \"string\",
  \"additionalEmails\": \"string\",
  \"companyName\": \"string\",
  \"address\": \"string\",
  \"addressLine1\": \"string\",
  \"addressLine2\": \"string\",
  \"city\": \"string\",
  \"state\": \"string\",
  \"countryCode\": \"string\",
  \"postalCode\": \"string\",
  \"customFields\": \"string\",
  \"schedule\": \"string\",
  \"executeAt\": \"string\",
  \"rrule\": \"string\",
  \"intervalType\": \"string\",
  \"interval\": 123,
  \"startDate\": \"string\",
  \"startTime\": \"string\",
  \"endDate\": \"string\",
  \"endTime\": \"string\",
  \"dayOfMonth\": 123,
  \"dayOfWeek\": \"string\",
  \"numOfWeek\": 123,
  \"monthOfYear\": \"string\",
  \"count\": 123,
  \"daysBefore\": 123,
  \"useStartAsPrimaryUserAccepted\": true,
  \"endType\": \"string\",
  \"liveMode\": true,
  \"businessDetails\": \"string\",
  \"logoUrl\": \"string\",
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
  \"discount\": \"string\",
  \"value\": 123,
  \"validOnProductIds\": \"string\",
  \"termsNotes\": \"string\",
  \"title\": \"string\",
  \"attachments\": \"string\",
  \"url\": \"string\",
  \"size\": 123,
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
  url := "https://services.leadconnectorhq.com/invoices/schedule/:scheduleId"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
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

url = URI("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId")
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
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
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
  "name": "string",
  "contactDetails": "string",
  "id": "string",
  "phoneNo": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "address": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "city": "string",
  "state": "string",
  "countryCode": "string",
  "postalCode": "string",
  "customFields": "string",
  "schedule": "string",
  "executeAt": "string",
  "rrule": "string",
  "intervalType": "string",
  "interval": 123,
  "startDate": "string",
  "startTime": "string",
  "endDate": "string",
  "endTime": "string",
  "dayOfMonth": 123,
  "dayOfWeek": "string",
  "numOfWeek": 123,
  "monthOfYear": "string",
  "count": 123,
  "daysBefore": 123,
  "useStartAsPrimaryUserAccepted": true,
  "endType": "string",
  "liveMode": true,
  "businessDetails": "string",
  "logoUrl": "string",
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
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "attachments": "string",
  "url": "string",
  "size": 123,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
