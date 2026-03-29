# Create New Estimate

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/invoices/estimate` |
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

N/A
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
| **items** | `object[]` | Yes | An array of items for the estimate. Array [ name string required Invoice Item Name Example: ABC Product description string Invoice descriptions Example: ABC Corp. productId string Product Id Example: 6578278e879ad2646715ba9c priceId string Price Id Example: 6578278e879ad2646715ba9c currency string required Currency Example: USD amount number required Product amount Example: 999 qty number required Product Quantity Example: 1 taxes object[] Tax Array [ _id string required name string required rate number required calculation string Possible values: [ exclusive ] description string taxId string ] automaticTaxCategoryId string Tax category id for calculating automatic tax Example: 6578278e879ad2646715ba9c isSetupFeeItem boolean Setupfee item, only created when 1st invoice of recurring schedule is generated type string Price type of the item Possible values: [ one_time , recurring ] Example: one_time taxInclusive boolean true if item amount is tax inclusive Default value: false Example: true attachments string[] Attachments for the line item Example: ["https://example.com/file1.jpg","https://example.com/file2.png"] ] |
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
| **attachments** | `string[]` | No |  |
| **liveMode** | `boolean` | No |  |
| **discount** | `object` | Yes | value number Discount Value Default value: 0 Example: 10 type string required Discount type Possible values: [ percentage , fixed ] Default value: percentage Example: percentage validOnProductIds string[] Product Ids on which discount is applicable Example: [ '6579751d56f60276e5bd4154' ] |
| **value** | `number` | No |  |
| **type** | `string` | No |  |
| **validOnProductIds** | `string[]` | No |  |
| **termsNotes** | `string` | No |  |
| **title** | `string` | No |  |
| **contactDetails** | `object` | Yes | Contact information to send the estimate to id string required Contact ID Example: 6578278e879ad2646715ba9c name string required Contact Name Example: Alex phoneNo string required Contact Phone Number Example: +1234567890 email string required Contact Email Example: alex@example.com additionalEmails object[] Secondary email addresses for the contact to be saved Array [ email string required Example: alex@example.com ] companyName string Contact Company Name Example: ABC Corp. address object addressLine1 string Address Line 1 Example: 9931 Beechwood addressLine2 string Address Line 2 Example: Beechwood city string City Example: St. Houston state string State Example: TX countryCode string Country Code Example: US postalCode string Postal Code Example: 559-6993 customFields string[] Custom Values |
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
| **estimateNumber** | `number` | No |  |
| **issueDate** | `string` | No |  |
| **expiryDate** | `string` | No |  |
| **sentTo** | `object` | Yes | Email and sent to details for the estimate email string[] required Email Address Example: ["alex@example.com"] emailCc string[] cc to be kept in any sent out emails Example: ["alex@example.com"] emailBcc string[] bcc to be kept in any sent out emails Example: ["alex@example.com"] phoneNo string[] Contact Phone Number Example: ["+1-214-559-6993"] |
| **email** | `string[]` | No |  |
| **emailCc** | `string[]` | No |  |
| **emailBcc** | `string[]` | No |  |
| **phoneNo** | `string[]` | No |  |
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
| **frequencySettings** | `object` | Yes | frequency settings for the estimate enabled boolean required enabled for the frequency settings Example: true schedule object required schedule setting for the estimate executeAt string rrule object intervalType string required Possible values: [ yearly , monthly , weekly , daily , hourly , minutely , secondly ] Example: monthly interval number required Example: 2 startDate string required Start date in YYYY-MM-DD format Example: 2023-01-01 startTime string Start time in HH:mm:ss format Example: 20:45:00 endDate string End date in YYYY-MM-DD format Example: 2029-11-01 endTime string End time in HH:mm:ss format Example: 18:45:00 dayOfMonth number -1, 1, 2, 3, ..., 27, 28 Example: 15 dayOfWeek string Possible values: [ mo , tu , we , th , fr , sa , su ] Example: mo numOfWeek number -1, 1, 2, 3, 4 Example: -1 monthOfYear string Possible values: [ jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec ] Example: jan count number Max number of task executions Example: 10 daysBefore number Execute task number of days before Example: 5 useStartAsPrimaryUserAccepted boolean Start as primary user accepted date Example: true endType string End type like after, by, count Example: by |
| **enabled** | `boolean` | No |  |
| **schedule** | `object` | Yes | schedule setting for the estimate executeAt string rrule object intervalType string required Possible values: [ yearly , monthly , weekly , daily , hourly , minutely , secondly ] Example: monthly interval number required Example: 2 startDate string required Start date in YYYY-MM-DD format Example: 2023-01-01 startTime string Start time in HH:mm:ss format Example: 20:45:00 endDate string End date in YYYY-MM-DD format Example: 2029-11-01 endTime string End time in HH:mm:ss format Example: 18:45:00 dayOfMonth number -1, 1, 2, 3, ..., 27, 28 Example: 15 dayOfWeek string Possible values: [ mo , tu , we , th , fr , sa , su ] Example: mo numOfWeek number -1, 1, 2, 3, 4 Example: -1 monthOfYear string Possible values: [ jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec ] Example: jan count number Max number of task executions Example: 10 daysBefore number Execute task number of days before Example: 5 useStartAsPrimaryUserAccepted boolean Start as primary user accepted date Example: true endType string End type like after, by, count Example: by |
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
| **estimateNumberPrefix** | `string` | No |  |
| **userId** | `string` | No |  |
| **attachments** | `object[]` | Yes | attachments for the invoice Array [ id string required Id of the file selected Example: 6241712be68f7a98102ba272 name string required Name of the file Example: Electronics.pdf url string required URL of the file Example: https://example.com/digital-delivery type string required Type of the file size number required Size of the file Example: 10000 ] |
| **id** | `string` | No |  |
| **name** | `string` | No |  |
| **url** | `string` | No |  |
| **type** | `string` | No |  |
| **size** | `number` | No |  |
| **autoInvoice** | `object` | Yes | Auto invoice for the estimate enabled boolean required Enable Auto Invoice Example: true directPayments boolean Direct Payments Example: true |
| **enabled** | `boolean` | No |  |
| **directPayments** | `boolean` | No |  |
| **miscellaneousCharges** | `object` | Yes | miscellaneous charges for the estimate charges array[] required charges for the processing fee collectedMiscellaneousCharges number collected miscellaneous charges Example: 10 paidCharges object[] paid miscellaneous charges Array [ name string required name of the processing fee Example: Processing Fee charge number required charge for the processing fee Example: 10 amount number required amount of the processing fee Example: 10 _id string required id of the processing fee Example: 673d01d7d547648a8dab6211 ] |
| **charges** | `array[]` | No |  |
| **collectedMiscellaneousCharges** | `number` | No |  |
| **paidCharges** | `object[]` | Yes | paid miscellaneous charges Array [ name string required name of the processing fee Example: Processing Fee charge number required charge for the processing fee Example: 10 amount number required amount of the processing fee Example: 10 _id string required id of the processing fee Example: 673d01d7d547648a8dab6211 ] |
| **name** | `string` | No |  |
| **charge** | `number` | No |  |
| **amount** | `number` | No |  |
| **_id** | `string` | No |  |
| **paymentScheduleConfig** | `object` | Yes | Payment Schedule Config for the estimate type string required Payment Schedule Type Possible values: [ fixed , percentage ] Example: fixed dateConfig object required Due date type configuration depositDateType string required Deposit date type Possible values: [ estimate_accepted , custom ] Example: estimate_accepted scheduleDateType string required Payment Schedule Date Type Possible values: [ regular_interval , custom ] Example: regular_interval schedules array[] required Payment Schedule Items |
| **type** | `string` | No |  |
| **dateConfig** | `object` | Yes | Due date type configuration depositDateType string required Deposit date type Possible values: [ estimate_accepted , custom ] Example: estimate_accepted scheduleDateType string required Payment Schedule Date Type Possible values: [ regular_interval , custom ] Example: regular_interval |
| **depositDateType** | `string` | No |  |
| **scheduleDateType** | `string` | No |  |
| **schedules** | `array[]` | No |  |

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
  "termsNotes": "<p>All services are subject to availability.</p>",
  "companyId": "COMP12345",
  "contactDetails": {
    "id": "jvzfKTNdE7OYXXXXXX",
    "name": "Contact Name",
    "phoneNo": "+911111111114",
    "email": "email@test.com",
    "address": {
      "countryCode": "US"
    }
  },
  "issueDate": "2023-06-15T00:00:00.000Z",
  "expiryDate": "2023-07-15T00:00:00.000Z",
  "sentBy": "user@example.com",
  "automaticTaxesCalculated": true,
  "meta": {
    "key": "value"
  },
  "estimateActionHistory": [
    {
      "action": "Created",
      "timestamp": "2023-06-15T10:00:00.000Z"
    }
  ],
  "sentTo": {
    "email": [
      "test@example.com"
    ],
    "phoneNo": [
      "+1 99444444444"
    ]
  },
  "frequencySettings": {
    "enabled": true,
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
    }
  },
  "lastVisitedAt": "2023-06-20T08:30:00.000Z",
  "totalamountInUSD": 1500.75,
  "autoInvoice": {
    "enabled": true,
    "directPayments": false
  },
  "traceId": "010c7a01-857f-4619-970d-xyxyxyxy"
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
| **companyId** | `str` |  |
| **contactDetails** | `dict` |  |
| **issueDate** | `str` |  |
| **expiryDate** | `str` |  |
| **sentBy** | `str` |  |
| **automaticTaxesCalculated** | `bool` |  |
| **meta** | `dict` |  |
| **estimateActionHistory** | `list` |  |
| **sentTo** | `dict` |  |
| **frequencySettings** | `dict` |  |
| **lastVisitedAt** | `str` |  |
| **totalamountInUSD** | `float` |  |
| **autoInvoice** | `dict` |  |
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
  --url https://services.leadconnectorhq.com/invoices/estimate \
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/invoices/estimate', {
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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
  url: 'https://services.leadconnectorhq.com/invoices/estimate',
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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
  'path': '/invoices/estimate',
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/invoices/estimate',
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/invoices/estimate')
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/invoices/estimate"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/invoices/estimate', [
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/invoices/estimate"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
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
  \"attachments\": \"string\",
  \"liveMode\": true,
  \"discount\": \"string\",
  \"value\": 123,
  \"validOnProductIds\": \"string\",
  \"termsNotes\": \"string\",
  \"title\": \"string\",
  \"contactDetails\": \"string\",
  \"id\": \"string\",
  \"email\": \"string\",
  \"additionalEmails\": \"string\",
  \"companyName\": \"string\",
  \"customFields\": \"string\",
  \"estimateNumber\": 123,
  \"issueDate\": \"string\",
  \"expiryDate\": \"string\",
  \"sentTo\": \"string\",
  \"emailCc\": \"string\",
  \"emailBcc\": \"string\",
  \"automaticTaxesEnabled\": true,
  \"meta\": \"string\",
  \"sendEstimateDetails\": \"string\",
  \"action\": \"string\",
  \"userId\": \"string\",
  \"sentFrom\": \"string\",
  \"fromName\": \"string\",
  \"fromEmail\": \"string\",
  \"estimateName\": \"string\",
  \"frequencySettings\": \"string\",
  \"enabled\": true,
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
  \"estimateNumberPrefix\": \"string\",
  \"url\": \"string\",
  \"size\": 123,
  \"autoInvoice\": \"string\",
  \"directPayments\": true,
  \"miscellaneousCharges\": \"string\",
  \"charges\": \"string\",
  \"collectedMiscellaneousCharges\": 123,
  \"paidCharges\": \"string\",
  \"charge\": 123,
  \"paymentScheduleConfig\": \"string\",
  \"dateConfig\": \"string\",
  \"depositDateType\": \"string\",
  \"scheduleDateType\": \"string\",
  \"schedules\": \"string\"
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
  url := "https://services.leadconnectorhq.com/invoices/estimate"
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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

url = URI("https://services.leadconnectorhq.com/invoices/estimate")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
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
  "attachments": "string",
  "liveMode": true,
  "discount": "string",
  "value": 123,
  "validOnProductIds": "string",
  "termsNotes": "string",
  "title": "string",
  "contactDetails": "string",
  "id": "string",
  "email": "string",
  "additionalEmails": "string",
  "companyName": "string",
  "customFields": "string",
  "estimateNumber": 123,
  "issueDate": "string",
  "expiryDate": "string",
  "sentTo": "string",
  "emailCc": "string",
  "emailBcc": "string",
  "automaticTaxesEnabled": true,
  "meta": "string",
  "sendEstimateDetails": "string",
  "action": "string",
  "userId": "string",
  "sentFrom": "string",
  "fromName": "string",
  "fromEmail": "string",
  "estimateName": "string",
  "frequencySettings": "string",
  "enabled": true,
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
  "estimateNumberPrefix": "string",
  "url": "string",
  "size": 123,
  "autoInvoice": "string",
  "directPayments": true,
  "miscellaneousCharges": "string",
  "charges": "string",
  "collectedMiscellaneousCharges": 123,
  "paidCharges": "string",
  "charge": 123,
  "paymentScheduleConfig": "string",
  "dateConfig": "string",
  "depositDateType": "string",
  "scheduleDateType": "string",
  "schedules": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/estimate' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
