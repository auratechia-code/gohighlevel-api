# Update Estimate

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/invoices/estimate/:estimateId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: invoices/estimate.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `estimateId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

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
</details>

<details>
<summary>Response 400</summary>

```json
{  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "_id": "67ac9a51106ee8311e911XXXX",  "liveMode": true,  "deleted": false,  "name": "Estimate Name",  "currency": "USD",  "businessDetails": {    "logoUrl": "your_image-url",    "name": "Business name",    "address": {      "addressLine1": "address line 1",      "city": "Test City",      "state": "State Name",      "countryCode": "US",      "postalCode": "12345"    },    "phoneNo": "+1 1234567890",    "website": "www.example.com",    "customValues": [      {        "name": "Test",        "fieldKey": "{{custom_values.test}}",        "id": "5DYTWoiQvWiIJZXX44XXX",        "value": "Test's Custom Value"      }    ]  },  "items": [    {      "taxes": [],      "taxInclusive": false,      "_id": "67ac9a51106ee8311e911XXXX",      "description": "<p>Futuristic anti-gravity racing</p>",      "currency": "USD",      "productId": "67ac9a51106ee8311e911XXXX",      "priceId": "67ac9a51106ee8311e911XXXX",      "amount": 9.99,      "qty": 1,      "name": "TEST",      "type": "one_time"    },    {      "taxes": [        {          "_id": "67ac9a51106ee8311e911XXXX",          "name": "TaxTwo",          "rate": 8.5,          "calculation": "exclusive"        }      ],      "taxInclusive": true,      "_id": "67ac9a51106ee8311e911XXXX",      "productId": "67ac9a51106ee8311e911XXXX",      "priceId": "67ac9a51106ee8311e911XXXX",      "currency": "USD",      "name": "TEST2",      "qty": 1,      "amount": 500,      "description": "",      "type": "recurring"    }  ],  "discount": {    "type": "percentage",    "value": 0  },  "title": "ESTIMATE",  "estimateNumberPrefix": "EST-",  "attachments": [    {      "id": "6241712be68f7a98102ba272",      "name": "Electronics.pdf",      "url": "https://example.com/digital-delivery",      "type": "string",      "size": 10000    }  ],  "updatedBy": "3HIpOF9NIc5ltriQXXXX",  "total": 1222.03,  "createdAt": "2025-02-12T13:17:47.416Z",  "updatedAt": "2025-02-12T13:17:47.416Z",  "__v": 0,  "automaticTaxesEnabled": false,  "termsNotes": "<p>All services are subject to availability.</p>",  "companyId": "COMP12345",  "contactDetails": {    "id": "jvzfKTNdE7OYXXXXXX",    "name": "Contact Name",    "phoneNo": "+911111111114",    "email": "email@test.com",    "address": {      "countryCode": "US"    }  },  "issueDate": "2023-06-15T00:00:00.000Z",  "expiryDate": "2023-07-15T00:00:00.000Z",  "sentBy": "user@example.com",  "automaticTaxesCalculated": true,  "meta": {    "key": "value"  },  "estimateActionHistory": [    {      "action": "Created",      "timestamp": "2023-06-15T10:00:00.000Z"    }  ],  "sentTo": {    "email": [      "test@example.com"    ],    "phoneNo": [      "+1 99444444444"    ]  },  "frequencySettings": {    "enabled": true,    "schedule": {      "executeAt": "string",      "rrule": {        "intervalType": "monthly",        "interval": 2,        "startDate": "2023-01-01",        "startTime": "20:45:00",        "endDate": "2029-11-01",        "endTime": "18:45:00",        "dayOfMonth": 15,        "dayOfWeek": "mo",        "numOfWeek": -1,        "monthOfYear": "jan",        "count": 10,        "daysBefore": 5,        "useStartAsPrimaryUserAccepted": true,        "endType": "by"      }    }  },  "lastVisitedAt": "2023-06-20T08:30:00.000Z",  "totalamountInUSD": 1500.75,  "autoInvoice": {    "enabled": true,    "directPayments": false  },  "traceId": "010c7a01-857f-4619-970d-xyxyxyxy"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "_id": "67ac9a51106ee8311e911XXXX",  "liveMode": true,  "deleted": false,  "name": "Estimate Name",  "currency": "USD",  "businessDetails": {    "logoUrl": "your_image-url",    "name": "Business name",    "address": {      "addressLine1": "address line 1",      "city": "Test City",      "state": "State Name",      "countryCode": "US",      "postalCode": "12345"    },    "phoneNo": "+1 1234567890",    "website": "www.example.com",    "customValues": [      {        "name": "Test",        "fieldKey": "{{custom_values.test}}",        "id": "5DYTWoiQvWiIJZXX44XXX",        "value": "Test's Custom Value"      }    ]  },  "items": [    {      "taxes": [],      "taxInclusive": false,      "_id": "67ac9a51106ee8311e911XXXX",      "description": "<p>Futuristic anti-gravity racing</p>",      "currency": "USD",      "productId": "67ac9a51106ee8311e911XXXX",      "priceId": "67ac9a51106ee8311e911XXXX",      "amount": 9.99,      "qty": 1,      "name": "TEST",      "type": "one_time"    },    {      "taxes": [        {          "_id": "67ac9a51106ee8311e911XXXX",          "name": "TaxTwo",          "rate": 8.5,          "calculation": "exclusive"        }      ],      "taxInclusive": true,      "_id": "67ac9a51106ee8311e911XXXX",      "productId": "67ac9a51106ee8311e911XXXX",      "priceId": "67ac9a51106ee8311e911XXXX",      "currency": "USD",      "name": "TEST2",      "qty": 1,      "amount": 500,      "description": "",      "type": "recurring"    }  ],  "discount": {    "type": "percentage",    "value": 0  },  "title": "ESTIMATE",  "estimateNumberPrefix": "EST-",  "attachments": [    {      "id": "6241712be68f7a98102ba272",      "name": "Electronics.pdf",      "url": "https://example.com/digital-delivery",      "type": "string",      "size": 10000    }  ],  "updatedBy": "3HIpOF9NIc5ltriQXXXX",  "total": 1222.03,  "createdAt": "2025-02-12T13:17:47.416Z",  "updatedAt": "2025-02-12T13:17:47.416Z",  "__v": 0,  "automaticTaxesEnabled": false,  "termsNotes": "<p>All services are subject to availability.</p>",  "companyId": "COMP12345",  "contactDetails": {    "id": "jvzfKTNdE7OYXXXXXX",    "name": "Contact Name",    "phoneNo": "+911111111114",    "email": "email@test.com",    "address": {      "countryCode": "US"    }  },  "issueDate": "2023-06-15T00:00:00.000Z",  "expiryDate": "2023-07-15T00:00:00.000Z",  "sentBy": "user@example.com",  "automaticTaxesCalculated": true,  "meta": {    "key": "value"  },  "estimateActionHistory": [    {      "action": "Created",      "timestamp": "2023-06-15T10:00:00.000Z"    }  ],  "sentTo": {    "email": [      "test@example.com"    ],    "phoneNo": [      "+1 99444444444"    ]  },  "frequencySettings": {    "enabled": true,    "schedule": {      "executeAt": "string",      "rrule": {        "intervalType": "monthly",        "interval": 2,        "startDate": "2023-01-01",        "startTime": "20:45:00",        "endDate": "2029-11-01",        "endTime": "18:45:00",        "dayOfMonth": 15,        "dayOfWeek": "mo",        "numOfWeek": -1,        "monthOfYear": "jan",        "count": 10,        "daysBefore": 5,        "useStartAsPrimaryUserAccepted": true,        "endType": "by"      }    }  },  "lastVisitedAt": "2023-06-20T08:30:00.000Z",  "totalamountInUSD": 1500.75,  "autoInvoice": {    "enabled": true,    "directPayments": false  },  "traceId": "010c7a01-857f-4619-970d-xyxyxyxy"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "_id": "67ac9a51106ee8311e911XXXX",  "liveMode": true,  "deleted": false,  "name": "Estimate Name",  "currency": "USD",  "businessDetails": {    "logoUrl": "your_image-url",    "name": "Business name",    "address": {      "addressLine1": "address line 1",      "city": "Test City",      "state": "State Name",      "countryCode": "US",      "postalCode": "12345"    },    "phoneNo": "+1 1234567890",    "website": "www.example.com",    "customValues": [      {        "name": "Test",        "fieldKey": "{{custom_values.test}}",        "id": "5DYTWoiQvWiIJZXX44XXX",        "value": "Test's Custom Value"      }    ]  },  "items": [    {      "taxes": [],      "taxInclusive": false,      "_id": "67ac9a51106ee8311e911XXXX",      "description": "<p>Futuristic anti-gravity racing</p>",      "currency": "USD",      "productId": "67ac9a51106ee8311e911XXXX",      "priceId": "67ac9a51106ee8311e911XXXX",      "amount": 9.99,      "qty": 1,      "name": "TEST",      "type": "one_time"    },    {      "taxes": [        {          "_id": "67ac9a51106ee8311e911XXXX",          "name": "TaxTwo",          "rate": 8.5,          "calculation": "exclusive"        }      ],      "taxInclusive": true,      "_id": "67ac9a51106ee8311e911XXXX",      "productId": "67ac9a51106ee8311e911XXXX",      "priceId": "67ac9a51106ee8311e911XXXX",      "currency": "USD",      "name": "TEST2",      "qty": 1,      "amount": 500,      "description": "",      "type": "recurring"    }  ],  "discount": {    "type": "percentage",    "value": 0  },  "title": "ESTIMATE",  "estimateNumberPrefix": "EST-",  "attachments": [    {      "id": "6241712be68f7a98102ba272",      "name": "Electronics.pdf",      "url": "https://example.com/digital-delivery",      "type": "string",      "size": 10000    }  ],  "updatedBy": "3HIpOF9NIc5ltriQXXXX",  "total": 1222.03,  "createdAt": "2025-02-12T13:17:47.416Z",  "updatedAt": "2025-02-12T13:17:47.416Z",  "__v": 0,  "automaticTaxesEnabled": false,  "termsNotes": "<p>All services are subject to availability.</p>",  "companyId": "COMP12345",  "contactDetails": {    "id": "jvzfKTNdE7OYXXXXXX",    "name": "Contact Name",    "phoneNo": "+911111111114",    "email": "email@test.com",    "address": {      "countryCode": "US"    }  },  "issueDate": "2023-06-15T00:00:00.000Z",  "expiryDate": "2023-07-15T00:00:00.000Z",  "sentBy": "user@example.com",  "automaticTaxesCalculated": true,  "meta": {    "key": "value"  },  "estimateActionHistory": [    {      "action": "Created",      "timestamp": "2023-06-15T10:00:00.000Z"    }  ],  "sentTo": {    "email": [      "test@example.com"    ],    "phoneNo": [      "+1 99444444444"    ]  },  "frequencySettings": {    "enabled": true,    "schedule": {      "executeAt": "string",      "rrule": {        "intervalType": "monthly",        "interval": 2,        "startDate": "2023-01-01",        "startTime": "20:45:00",        "endDate": "2029-11-01",        "endTime": "18:45:00",        "dayOfMonth": 15,        "dayOfWeek": "mo",        "numOfWeek": -1,        "monthOfYear": "jan",        "count": 10,        "daysBefore": 5,        "useStartAsPrimaryUserAccepted": true,        "endType": "by"      }    }  },  "lastVisitedAt": "2023-06-20T08:30:00.000Z",  "totalamountInUSD": 1500.75,  "autoInvoice": {    "enabled": true,    "directPayments": false  },  "traceId": "010c7a01-857f-4619-970d-xyxyxyxy"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	}'

```

### NODEJS
#### SDK
```nodejs
	const { HighLevel } = require('@gohighlevel/api-client');

	

	const highLevel = new HighLevel({

	  clientId: 'your_client_id_here',

	  clientSecret: 'your_client_secret_here',

	});

	

	try {

	  const response = await highLevel.invoices.updateEstimate({

	    'estimateId': '5f9d6d8b1b2d2c001f2d9e4b'

	  },

	  {

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'name': 'Home Service Estimate',

	    'businessDetails': {

	      'logoUrl': 'https://example.com/logo.png',

	      'name': 'ABC Corp.',

	      'phoneNo': '+1-214-559-6993',

	      'address': '9931 Beechwood, TX',

	      'website': 'wwww.example.com',

	      'customValues': [

	        'string'

	      ]

	    },

	    'currency': 'USD',

	    'items': [

	      {

	        'name': 'ABC Product',

	        'description': 'ABC Corp.',

	        'productId': '6578278e879ad2646715ba9c',

	        'priceId': '6578278e879ad2646715ba9c',

	        'currency': 'USD',

	        'amount': 999,

	        'qty': 1,

	        'taxes': [

	          {

	            '_id': 'string',

	            'name': 'string',

	            'rate': 0,

	            'calculation': 'exclusive',

	            'description': 'string',

	            'taxId': 'string'

	          }

	        ],

	        'automaticTaxCategoryId': '6578278e879ad2646715ba9c',

	        'isSetupFeeItem': true,

	        'type': 'one_time',

	        'taxInclusive': true,

	        'attachments': [

	          'https://example.com/file1.jpg',

	          'https://example.com/file2.png'

	        ]

	      }

	    ],

	    'liveMode': true,

	    'discount': {

	      'value': 10,

	      'type': 'percentage',

	      'validOnProductIds': '[ '6579751d56f60276e5bd4154' ]'

	    },

	    'termsNotes': '<p>This is a default terms.</p>',

	    'title': 'ESTIMATE',

	    'contactDetails': {

	      'id': '6578278e879ad2646715ba9c',

	      'name': 'Alex',

	      'phoneNo': '+1234567890',

	      'email': 'alex@example.com',

	      'additionalEmails': [

	        {

	          'email': 'alex@example.com'

	        }

	      ],

	      'companyName': 'ABC Corp.',

	      'address': {

	        'addressLine1': '9931 Beechwood',

	        'addressLine2': 'Beechwood',

	        'city': 'St. Houston',

	        'state': 'TX',

	        'countryCode': 'US',

	        'postalCode': '559-6993'

	      },

	      'customFields': [

	        'string'

	      ]

	    },

	    'estimateNumber': 1001,

	    'issueDate': '2024-08-07',

	    'expiryDate': '2024-08-10',

	    'sentTo': {

	      'email': [

	        'alex@example.com'

	      ],

	      'emailCc': [

	        'alex@example.com'

	      ],

	      'emailBcc': [

	        'alex@example.com'

	      ],

	      'phoneNo': [

	        '+1-214-559-6993'

	      ]

	    },

	    'automaticTaxesEnabled': true,

	    'meta': {

	      'key': 'value'

	    },

	    'sendEstimateDetails': {

	      'altId': '6578278e879ad2646715ba9c',

	      'altType': 'location',

	      'action': 'sms_and_email',

	      'liveMode': true,

	      'userId': '6578278e879ad2646715ba9c',

	      'sentFrom': {

	        'fromName': 'Alex',

	        'fromEmail': 'alex@example.com'

	      },

	      'estimateName': 'Estimate'

	    },

	    'frequencySettings': {

	      'enabled': true,

	      'schedule': {

	        'executeAt': 'string',

	        'rrule': {

	          'intervalType': 'monthly',

	          'interval': 2,

	          'startDate': '2023-01-01',

	          'startTime': '20:45:00',

	          'endDate': '2029-11-01',

	          'endTime': '18:45:00',

	          'dayOfMonth': 15,

	          'dayOfWeek': 'mo',

	          'numOfWeek': -1,

	          'monthOfYear': 'jan',

	          'count': 10,

	          'daysBefore': 5,

	          'useStartAsPrimaryUserAccepted': true,

	          'endType': 'by'

	        }

	      }

	    },

	    'estimateNumberPrefix': 'EST-',

	    'userId': '6578278e879ad2646715ba9c',

	    'attachments': [

	      {

	        'id': '6241712be68f7a98102ba272',

	        'name': 'Electronics.pdf',

	        'url': 'https://example.com/digital-delivery',

	        'type': 'string',

	        'size': 10000

	      }

	    ],

	    'autoInvoice': {

	      'enabled': true,

	      'directPayments': true

	    },

	    'miscellaneousCharges': {

	      'charges': [

	        [

	          null

	        ]

	      ],

	      'collectedMiscellaneousCharges': 10,

	      'paidCharges': [

	        {

	          'name': 'Processing Fee',

	          'charge': 10,

	          'amount': 10,

	          '_id': '673d01d7d547648a8dab6211'

	        }

	      ]

	    },

	    'paymentScheduleConfig': {

	      'type': 'fixed',

	      'dateConfig': {

	        'depositDateType': 'estimate_accepted',

	        'scheduleDateType': 'regular_interval'

	      },

	      'schedules': [

	        [

	          null

	        ]

	      ]

	    },

	    'estimateStatus': 'sent'

	  });

	  console.log(response);

	} catch (error) {

	  console.error('Error:', error);

	}

```

#### AXIOS
```nodejs
	const axios = require('axios');

	let data = JSON.stringify({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId',

	  headers: { 

	    'Content-Type': 'application/json', 

	    'Accept': 'application/json', 

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  data : data

	};

	

	axios.request(config)

	.then((response) => {

	  console.log(JSON.stringify(response.data));

	})

	.catch((error) => {

	  console.log(error);

	});

```

#### NATIVE
```nodejs
	var https = require('follow-redirects').https;

	var fs = require('fs');

	

	var options = {

	  'method': 'PUT',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/invoices/estimate/:estimateId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  'maxRedirects': 20

	};

	

	var req = https.request(options, function (res) {

	  var chunks = [];

	

	  res.on("data", function (chunk) {

	    chunks.push(chunk);

	  });

	

	  res.on("end", function (chunk) {

	    var body = Buffer.concat(chunks);

	    console.log(body.toString());

	  });

	

	  res.on("error", function (error) {

	    console.error(error);

	  });

	});

	

	var postData = JSON.stringify({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "name": "Home Service Estimate",

	    "businessDetails": {

	      "logoUrl": "https://example.com/logo.png",

	      "name": "ABC Corp.",

	      "phoneNo": "+1-214-559-6993",

	      "address": "9931 Beechwood, TX",

	      "website": "wwww.example.com",

	      "customValues": [

	        "string"

	      ]

	    },

	    "currency": "USD",

	    "items": [

	      {

	        "name": "ABC Product",

	        "description": "ABC Corp.",

	        "productId": "6578278e879ad2646715ba9c",

	        "priceId": "6578278e879ad2646715ba9c",

	        "currency": "USD",

	        "amount": 999,

	        "qty": 1,

	        "taxes": [

	          {

	            "_id": "string",

	            "name": "string",

	            "rate": 0,

	            "calculation": "exclusive",

	            "description": "string",

	            "taxId": "string"

	          }

	        ],

	        "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	        "isSetupFeeItem": true,

	        "type": "one_time",

	        "taxInclusive": true,

	        "attachments": [

	          "https://example.com/file1.jpg",

	          "https://example.com/file2.png"

	        ]

	      }

	    ],

	    "liveMode": true,

	    "discount": {

	      "value": 10,

	      "type": "percentage",

	      "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	    },

	    "termsNotes": "<p>This is a default terms.</p>",

	    "title": "ESTIMATE",

	    "contactDetails": {

	      "id": "6578278e879ad2646715ba9c",

	      "name": "Alex",

	      "phoneNo": "+1234567890",

	      "email": "alex@example.com",

	      "additionalEmails": [

	        {

	          "email": "alex@example.com"

	        }

	      ],

	      "companyName": "ABC Corp.",

	      "address": {

	        "addressLine1": "9931 Beechwood",

	        "addressLine2": "Beechwood",

	        "city": "St. Houston",

	        "state": "TX",

	        "countryCode": "US",

	        "postalCode": "559-6993"

	      },

	      "customFields": [

	        "string"

	      ]

	    },

	    "estimateNumber": 1001,

	    "issueDate": "2024-08-07",

	    "expiryDate": "2024-08-10",

	    "sentTo": {

	      "email": [

	        "alex@example.com"

	      ],

	      "emailCc": [

	        "alex@example.com"

	      ],

	      "emailBcc": [

	        "alex@example.com"

	      ],

	      "phoneNo": [

	        "+1-214-559-6993"

	      ]

	    },

	    "automaticTaxesEnabled": true,

	    "meta": {

	      "key": "value"

	    },

	    "sendEstimateDetails": {

	      "altId": "6578278e879ad2646715ba9c",

	      "altType": "location",

	      "action": "sms_and_email",

	      "liveMode": true,

	      "userId": "6578278e879ad2646715ba9c",

	      "sentFrom": {

	        "fromName": "Alex",

	        "fromEmail": "alex@example.com"

	      },

	      "estimateName": "Estimate"

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

	    "estimateNumberPrefix": "EST-",

	    "userId": "6578278e879ad2646715ba9c",

	    "attachments": [

	      {

	        "id": "6241712be68f7a98102ba272",

	        "name": "Electronics.pdf",

	        "url": "https://example.com/digital-delivery",

	        "type": "string",

	        "size": 10000

	      }

	    ],

	    "autoInvoice": {

	      "enabled": true,

	      "directPayments": true

	    },

	    "miscellaneousCharges": {

	      "charges": [

	        [

	          null

	        ]

	      ],

	      "collectedMiscellaneousCharges": 10,

	      "paidCharges": [

	        {

	          "name": "Processing Fee",

	          "charge": 10,

	          "amount": 10,

	          "_id": "673d01d7d547648a8dab6211"

	        }

	      ]

	    },

	    "paymentScheduleConfig": {

	      "type": "fixed",

	      "dateConfig": {

	        "depositDateType": "estimate_accepted",

	        "scheduleDateType": "regular_interval"

	      },

	      "schedules": [

	        [

	          null

	        ]

	      ]

	    },

	    "estimateStatus": "sent"

	  })

	

	};

	request(options, function (error, response) {

	  if (error) throw new Error(error);

	  console.log(response.body);

	});

```

#### UNIREST
```nodejs
	var unirest = require('unirest');

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "name": "Home Service Estimate",

	    "businessDetails": {

	      "logoUrl": "https://example.com/logo.png",

	      "name": "ABC Corp.",

	      "phoneNo": "+1-214-559-6993",

	      "address": "9931 Beechwood, TX",

	      "website": "wwww.example.com",

	      "customValues": [

	        "string"

	      ]

	    },

	    "currency": "USD",

	    "items": [

	      {

	        "name": "ABC Product",

	        "description": "ABC Corp.",

	        "productId": "6578278e879ad2646715ba9c",

	        "priceId": "6578278e879ad2646715ba9c",

	        "currency": "USD",

	        "amount": 999,

	        "qty": 1,

	        "taxes": [

	          {

	            "_id": "string",

	            "name": "string",

	            "rate": 0,

	            "calculation": "exclusive",

	            "description": "string",

	            "taxId": "string"

	          }

	        ],

	        "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	        "isSetupFeeItem": true,

	        "type": "one_time",

	        "taxInclusive": true,

	        "attachments": [

	          "https://example.com/file1.jpg",

	          "https://example.com/file2.png"

	        ]

	      }

	    ],

	    "liveMode": true,

	    "discount": {

	      "value": 10,

	      "type": "percentage",

	      "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	    },

	    "termsNotes": "<p>This is a default terms.</p>",

	    "title": "ESTIMATE",

	    "contactDetails": {

	      "id": "6578278e879ad2646715ba9c",

	      "name": "Alex",

	      "phoneNo": "+1234567890",

	      "email": "alex@example.com",

	      "additionalEmails": [

	        {

	          "email": "alex@example.com"

	        }

	      ],

	      "companyName": "ABC Corp.",

	      "address": {

	        "addressLine1": "9931 Beechwood",

	        "addressLine2": "Beechwood",

	        "city": "St. Houston",

	        "state": "TX",

	        "countryCode": "US",

	        "postalCode": "559-6993"

	      },

	      "customFields": [

	        "string"

	      ]

	    },

	    "estimateNumber": 1001,

	    "issueDate": "2024-08-07",

	    "expiryDate": "2024-08-10",

	    "sentTo": {

	      "email": [

	        "alex@example.com"

	      ],

	      "emailCc": [

	        "alex@example.com"

	      ],

	      "emailBcc": [

	        "alex@example.com"

	      ],

	      "phoneNo": [

	        "+1-214-559-6993"

	      ]

	    },

	    "automaticTaxesEnabled": true,

	    "meta": {

	      "key": "value"

	    },

	    "sendEstimateDetails": {

	      "altId": "6578278e879ad2646715ba9c",

	      "altType": "location",

	      "action": "sms_and_email",

	      "liveMode": true,

	      "userId": "6578278e879ad2646715ba9c",

	      "sentFrom": {

	        "fromName": "Alex",

	        "fromEmail": "alex@example.com"

	      },

	      "estimateName": "Estimate"

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

	    "estimateNumberPrefix": "EST-",

	    "userId": "6578278e879ad2646715ba9c",

	    "attachments": [

	      {

	        "id": "6241712be68f7a98102ba272",

	        "name": "Electronics.pdf",

	        "url": "https://example.com/digital-delivery",

	        "type": "string",

	        "size": 10000

	      }

	    ],

	    "autoInvoice": {

	      "enabled": true,

	      "directPayments": true

	    },

	    "miscellaneousCharges": {

	      "charges": [

	        [

	          null

	        ]

	      ],

	      "collectedMiscellaneousCharges": 10,

	      "paidCharges": [

	        {

	          "name": "Processing Fee",

	          "charge": 10,

	          "amount": 10,

	          "_id": "673d01d7d547648a8dab6211"

	        }

	      ]

	    },

	    "paymentScheduleConfig": {

	      "type": "fixed",

	      "dateConfig": {

	        "depositDateType": "estimate_accepted",

	        "scheduleDateType": "regular_interval"

	      },

	      "schedules": [

	        [

	          null

	        ]

	      ]

	    },

	    "estimateStatus": "sent"

	  }))

	  .end(function (res) { 

	    if (res.error) throw new Error(res.error); 

	    console.log(res.raw_body);

	  });

```

### PYTHON
#### HTTP.CLIENT
```python
	import http.client

	import json

	

	conn = http.client.HTTPSConnection("services.leadconnectorhq.com")

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": True,

	      "type": "one_time",

	      "taxInclusive": True,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": True,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": True,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": True,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

	  },

	  "frequencySettings": {

	    "enabled": True,

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

	        "useStartAsPrimaryUserAccepted": True,

	        "endType": "by"

	      }

	    }

	  },

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": True,

	    "directPayments": True

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        None

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        None

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/invoices/estimate/:estimateId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/invoices/estimate/:estimateId"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": True,

	      "type": "one_time",

	      "taxInclusive": True,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": True,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": True,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": True,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

	  },

	  "frequencySettings": {

	    "enabled": True,

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

	        "useStartAsPrimaryUserAccepted": True,

	        "endType": "by"

	      }

	    }

	  },

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": True,

	    "directPayments": True

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        None

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        None

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("PUT", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ \'6579751d56f60276e5bd4154\' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	}',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/json',

	    'Accept: application/json',

	    'Authorization: Bearer <TOKEN>'

	  ),

	));

	

	$response = curl_exec($curl);

	

	curl_close($curl);

	echo $response;

```

#### GUZZLE
```php
	<?php

	$client = new Client();

	$headers = [

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	];

	$body = '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/invoices/estimate/:estimateId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "name": "Home Service Estimate",\n  "businessDetails": {\n    "logoUrl": "https://example.com/logo.png",\n    "name": "ABC Corp.",\n    "phoneNo": "+1-214-559-6993",\n    "address": "9931 Beechwood, TX",\n    "website": "wwww.example.com",\n    "customValues": [\n      "string"\n    ]\n  },\n  "currency": "USD",\n  "items": [\n    {\n      "name": "ABC Product",\n      "description": "ABC Corp.",\n      "productId": "6578278e879ad2646715ba9c",\n      "priceId": "6578278e879ad2646715ba9c",\n      "currency": "USD",\n      "amount": 999,\n      "qty": 1,\n      "taxes": [\n        {\n          "_id": "string",\n          "name": "string",\n          "rate": 0,\n          "calculation": "exclusive",\n          "description": "string",\n          "taxId": "string"\n        }\n      ],\n      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",\n      "isSetupFeeItem": true,\n      "type": "one_time",\n      "taxInclusive": true,\n      "attachments": [\n        "https://example.com/file1.jpg",\n        "https://example.com/file2.png"\n      ]\n    }\n  ],\n  "liveMode": true,\n  "discount": {\n    "value": 10,\n    "type": "percentage",\n    "validOnProductIds": "[ \'6579751d56f60276e5bd4154\' ]"\n  },\n  "termsNotes": "<p>This is a default terms.</p>",\n  "title": "ESTIMATE",\n  "contactDetails": {\n    "id": "6578278e879ad2646715ba9c",\n    "name": "Alex",\n    "phoneNo": "+1234567890",\n    "email": "alex@example.com",\n    "additionalEmails": [\n      {\n        "email": "alex@example.com"\n      }\n    ],\n    "companyName": "ABC Corp.",\n    "address": {\n      "addressLine1": "9931 Beechwood",\n      "addressLine2": "Beechwood",\n      "city": "St. Houston",\n      "state": "TX",\n      "countryCode": "US",\n      "postalCode": "559-6993"\n    },\n    "customFields": [\n      "string"\n    ]\n  },\n  "estimateNumber": 1001,\n  "issueDate": "2024-08-07",\n  "expiryDate": "2024-08-10",\n  "sentTo": {\n    "email": [\n      "alex@example.com"\n    ],\n    "emailCc": [\n      "alex@example.com"\n    ],\n    "emailBcc": [\n      "alex@example.com"\n    ],\n    "phoneNo": [\n      "+1-214-559-6993"\n    ]\n  },\n  "automaticTaxesEnabled": true,\n  "meta": {\n    "key": "value"\n  },\n  "sendEstimateDetails": {\n    "altId": "6578278e879ad2646715ba9c",\n    "altType": "location",\n    "action": "sms_and_email",\n    "liveMode": true,\n    "userId": "6578278e879ad2646715ba9c",\n    "sentFrom": {\n      "fromName": "Alex",\n      "fromEmail": "alex@example.com"\n    },\n    "estimateName": "Estimate"\n  },\n  "frequencySettings": {\n    "enabled": true,\n    "schedule": {\n      "executeAt": "string",\n      "rrule": {\n        "intervalType": "monthly",\n        "interval": 2,\n        "startDate": "2023-01-01",\n        "startTime": "20:45:00",\n        "endDate": "2029-11-01",\n        "endTime": "18:45:00",\n        "dayOfMonth": 15,\n        "dayOfWeek": "mo",\n        "numOfWeek": -1,\n        "monthOfYear": "jan",\n        "count": 10,\n        "daysBefore": 5,\n        "useStartAsPrimaryUserAccepted": true,\n        "endType": "by"\n      }\n    }\n  },\n  "estimateNumberPrefix": "EST-",\n  "userId": "6578278e879ad2646715ba9c",\n  "attachments": [\n    {\n      "id": "6241712be68f7a98102ba272",\n      "name": "Electronics.pdf",\n      "url": "https://example.com/digital-delivery",\n      "type": "string",\n      "size": 10000\n    }\n  ],\n  "autoInvoice": {\n    "enabled": true,\n    "directPayments": true\n  },\n  "miscellaneousCharges": {\n    "charges": [\n      [\n        null\n      ]\n    ],\n    "collectedMiscellaneousCharges": 10,\n    "paidCharges": [\n      {\n        "name": "Processing Fee",\n        "charge": 10,\n        "amount": 10,\n        "_id": "673d01d7d547648a8dab6211"\n      }\n    ]\n  },\n  "paymentScheduleConfig": {\n    "type": "fixed",\n    "dateConfig": {\n      "depositDateType": "estimate_accepted",\n      "scheduleDateType": "regular_interval"\n    },\n    "schedules": [\n      [\n        null\n      ]\n    ]\n  },\n  "estimateStatus": "sent"\n}');

	try {

	  $response = $request->send();

	  if ($response->getStatus() == 200) {

	    echo $response->getBody();

	  }

	  else {

	    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .

	    $response->getReasonPhrase();

	  }

	}

	catch(HTTP_Request2_Exception $e) {

	  echo 'Error: ' . $e->getMessage();

	}

```

#### PECL_HTTP
```php
	<?php

	$client = new http\Client;

	$request = new http\Client\Request;

	$request->setRequestUrl('https://services.leadconnectorhq.com/invoices/estimate/:estimateId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	}');

	$request->setBody($body);

	$request->setOptions(array());

	$request->setHeaders(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$client->enqueue($request)->send();

	$response = $client->getResponse();

	echo $response->getBody();

```

### JAVA
#### OKHTTP
```java
	OkHttpClient client = new OkHttpClient().newBuilder()

	  .build();

	MediaType mediaType = MediaType.parse("application/json");

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"name\": \"Home Service Estimate\",\n  \"businessDetails\": {\n    \"logoUrl\": \"https://example.com/logo.png\",\n    \"name\": \"ABC Corp.\",\n    \"phoneNo\": \"+1-214-559-6993\",\n    \"address\": \"9931 Beechwood, TX\",\n    \"website\": \"wwww.example.com\",\n    \"customValues\": [\n      \"string\"\n    ]\n  },\n  \"currency\": \"USD\",\n  \"items\": [\n    {\n      \"name\": \"ABC Product\",\n      \"description\": \"ABC Corp.\",\n      \"productId\": \"6578278e879ad2646715ba9c\",\n      \"priceId\": \"6578278e879ad2646715ba9c\",\n      \"currency\": \"USD\",\n      \"amount\": 999,\n      \"qty\": 1,\n      \"taxes\": [\n        {\n          \"_id\": \"string\",\n          \"name\": \"string\",\n          \"rate\": 0,\n          \"calculation\": \"exclusive\",\n          \"description\": \"string\",\n          \"taxId\": \"string\"\n        }\n      ],\n      \"automaticTaxCategoryId\": \"6578278e879ad2646715ba9c\",\n      \"isSetupFeeItem\": true,\n      \"type\": \"one_time\",\n      \"taxInclusive\": true,\n      \"attachments\": [\n        \"https://example.com/file1.jpg\",\n        \"https://example.com/file2.png\"\n      ]\n    }\n  ],\n  \"liveMode\": true,\n  \"discount\": {\n    \"value\": 10,\n    \"type\": \"percentage\",\n    \"validOnProductIds\": \"[ '6579751d56f60276e5bd4154' ]\"\n  },\n  \"termsNotes\": \"<p>This is a default terms.</p>\",\n  \"title\": \"ESTIMATE\",\n  \"contactDetails\": {\n    \"id\": \"6578278e879ad2646715ba9c\",\n    \"name\": \"Alex\",\n    \"phoneNo\": \"+1234567890\",\n    \"email\": \"alex@example.com\",\n    \"additionalEmails\": [\n      {\n        \"email\": \"alex@example.com\"\n      }\n    ],\n    \"companyName\": \"ABC Corp.\",\n    \"address\": {\n      \"addressLine1\": \"9931 Beechwood\",\n      \"addressLine2\": \"Beechwood\",\n      \"city\": \"St. Houston\",\n      \"state\": \"TX\",\n      \"countryCode\": \"US\",\n      \"postalCode\": \"559-6993\"\n    },\n    \"customFields\": [\n      \"string\"\n    ]\n  },\n  \"estimateNumber\": 1001,\n  \"issueDate\": \"2024-08-07\",\n  \"expiryDate\": \"2024-08-10\",\n  \"sentTo\": {\n    \"email\": [\n      \"alex@example.com\"\n    ],\n    \"emailCc\": [\n      \"alex@example.com\"\n    ],\n    \"emailBcc\": [\n      \"alex@example.com\"\n    ],\n    \"phoneNo\": [\n      \"+1-214-559-6993\"\n    ]\n  },\n  \"automaticTaxesEnabled\": true,\n  \"meta\": {\n    \"key\": \"value\"\n  },\n  \"sendEstimateDetails\": {\n    \"altId\": \"6578278e879ad2646715ba9c\",\n    \"altType\": \"location\",\n    \"action\": \"sms_and_email\",\n    \"liveMode\": true,\n    \"userId\": \"6578278e879ad2646715ba9c\",\n    \"sentFrom\": {\n      \"fromName\": \"Alex\",\n      \"fromEmail\": \"alex@example.com\"\n    },\n    \"estimateName\": \"Estimate\"\n  },\n  \"frequencySettings\": {\n    \"enabled\": true,\n    \"schedule\": {\n      \"executeAt\": \"string\",\n      \"rrule\": {\n        \"intervalType\": \"monthly\",\n        \"interval\": 2,\n        \"startDate\": \"2023-01-01\",\n        \"startTime\": \"20:45:00\",\n        \"endDate\": \"2029-11-01\",\n        \"endTime\": \"18:45:00\",\n        \"dayOfMonth\": 15,\n        \"dayOfWeek\": \"mo\",\n        \"numOfWeek\": -1,\n        \"monthOfYear\": \"jan\",\n        \"count\": 10,\n        \"daysBefore\": 5,\n        \"useStartAsPrimaryUserAccepted\": true,\n        \"endType\": \"by\"\n      }\n    }\n  },\n  \"estimateNumberPrefix\": \"EST-\",\n  \"userId\": \"6578278e879ad2646715ba9c\",\n  \"attachments\": [\n    {\n      \"id\": \"6241712be68f7a98102ba272\",\n      \"name\": \"Electronics.pdf\",\n      \"url\": \"https://example.com/digital-delivery\",\n      \"type\": \"string\",\n      \"size\": 10000\n    }\n  ],\n  \"autoInvoice\": {\n    \"enabled\": true,\n    \"directPayments\": true\n  },\n  \"miscellaneousCharges\": {\n    \"charges\": [\n      [\n        null\n      ]\n    ],\n    \"collectedMiscellaneousCharges\": 10,\n    \"paidCharges\": [\n      {\n        \"name\": \"Processing Fee\",\n        \"charge\": 10,\n        \"amount\": 10,\n        \"_id\": \"673d01d7d547648a8dab6211\"\n      }\n    ]\n  },\n  \"paymentScheduleConfig\": {\n    \"type\": \"fixed\",\n    \"dateConfig\": {\n      \"depositDateType\": \"estimate_accepted\",\n      \"scheduleDateType\": \"regular_interval\"\n    },\n    \"schedules\": [\n      [\n        null\n      ]\n    ]\n  },\n  \"estimateStatus\": \"sent\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/invoices/estimate/:estimateId")

	  .method("PUT", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/invoices/estimate/:estimateId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"name\": \"Home Service Estimate\",\n  \"businessDetails\": {\n    \"logoUrl\": \"https://example.com/logo.png\",\n    \"name\": \"ABC Corp.\",\n    \"phoneNo\": \"+1-214-559-6993\",\n    \"address\": \"9931 Beechwood, TX\",\n    \"website\": \"wwww.example.com\",\n    \"customValues\": [\n      \"string\"\n    ]\n  },\n  \"currency\": \"USD\",\n  \"items\": [\n    {\n      \"name\": \"ABC Product\",\n      \"description\": \"ABC Corp.\",\n      \"productId\": \"6578278e879ad2646715ba9c\",\n      \"priceId\": \"6578278e879ad2646715ba9c\",\n      \"currency\": \"USD\",\n      \"amount\": 999,\n      \"qty\": 1,\n      \"taxes\": [\n        {\n          \"_id\": \"string\",\n          \"name\": \"string\",\n          \"rate\": 0,\n          \"calculation\": \"exclusive\",\n          \"description\": \"string\",\n          \"taxId\": \"string\"\n        }\n      ],\n      \"automaticTaxCategoryId\": \"6578278e879ad2646715ba9c\",\n      \"isSetupFeeItem\": true,\n      \"type\": \"one_time\",\n      \"taxInclusive\": true,\n      \"attachments\": [\n        \"https://example.com/file1.jpg\",\n        \"https://example.com/file2.png\"\n      ]\n    }\n  ],\n  \"liveMode\": true,\n  \"discount\": {\n    \"value\": 10,\n    \"type\": \"percentage\",\n    \"validOnProductIds\": \"[ '6579751d56f60276e5bd4154' ]\"\n  },\n  \"termsNotes\": \"<p>This is a default terms.</p>\",\n  \"title\": \"ESTIMATE\",\n  \"contactDetails\": {\n    \"id\": \"6578278e879ad2646715ba9c\",\n    \"name\": \"Alex\",\n    \"phoneNo\": \"+1234567890\",\n    \"email\": \"alex@example.com\",\n    \"additionalEmails\": [\n      {\n        \"email\": \"alex@example.com\"\n      }\n    ],\n    \"companyName\": \"ABC Corp.\",\n    \"address\": {\n      \"addressLine1\": \"9931 Beechwood\",\n      \"addressLine2\": \"Beechwood\",\n      \"city\": \"St. Houston\",\n      \"state\": \"TX\",\n      \"countryCode\": \"US\",\n      \"postalCode\": \"559-6993\"\n    },\n    \"customFields\": [\n      \"string\"\n    ]\n  },\n  \"estimateNumber\": 1001,\n  \"issueDate\": \"2024-08-07\",\n  \"expiryDate\": \"2024-08-10\",\n  \"sentTo\": {\n    \"email\": [\n      \"alex@example.com\"\n    ],\n    \"emailCc\": [\n      \"alex@example.com\"\n    ],\n    \"emailBcc\": [\n      \"alex@example.com\"\n    ],\n    \"phoneNo\": [\n      \"+1-214-559-6993\"\n    ]\n  },\n  \"automaticTaxesEnabled\": true,\n  \"meta\": {\n    \"key\": \"value\"\n  },\n  \"sendEstimateDetails\": {\n    \"altId\": \"6578278e879ad2646715ba9c\",\n    \"altType\": \"location\",\n    \"action\": \"sms_and_email\",\n    \"liveMode\": true,\n    \"userId\": \"6578278e879ad2646715ba9c\",\n    \"sentFrom\": {\n      \"fromName\": \"Alex\",\n      \"fromEmail\": \"alex@example.com\"\n    },\n    \"estimateName\": \"Estimate\"\n  },\n  \"frequencySettings\": {\n    \"enabled\": true,\n    \"schedule\": {\n      \"executeAt\": \"string\",\n      \"rrule\": {\n        \"intervalType\": \"monthly\",\n        \"interval\": 2,\n        \"startDate\": \"2023-01-01\",\n        \"startTime\": \"20:45:00\",\n        \"endDate\": \"2029-11-01\",\n        \"endTime\": \"18:45:00\",\n        \"dayOfMonth\": 15,\n        \"dayOfWeek\": \"mo\",\n        \"numOfWeek\": -1,\n        \"monthOfYear\": \"jan\",\n        \"count\": 10,\n        \"daysBefore\": 5,\n        \"useStartAsPrimaryUserAccepted\": true,\n        \"endType\": \"by\"\n      }\n    }\n  },\n  \"estimateNumberPrefix\": \"EST-\",\n  \"userId\": \"6578278e879ad2646715ba9c\",\n  \"attachments\": [\n    {\n      \"id\": \"6241712be68f7a98102ba272\",\n      \"name\": \"Electronics.pdf\",\n      \"url\": \"https://example.com/digital-delivery\",\n      \"type\": \"string\",\n      \"size\": 10000\n    }\n  ],\n  \"autoInvoice\": {\n    \"enabled\": true,\n    \"directPayments\": true\n  },\n  \"miscellaneousCharges\": {\n    \"charges\": [\n      [\n        null\n      ]\n    ],\n    \"collectedMiscellaneousCharges\": 10,\n    \"paidCharges\": [\n      {\n        \"name\": \"Processing Fee\",\n        \"charge\": 10,\n        \"amount\": 10,\n        \"_id\": \"673d01d7d547648a8dab6211\"\n      }\n    ]\n  },\n  \"paymentScheduleConfig\": {\n    \"type\": \"fixed\",\n    \"dateConfig\": {\n      \"depositDateType\": \"estimate_accepted\",\n      \"scheduleDateType\": \"regular_interval\"\n    },\n    \"schedules\": [\n      [\n        null\n      ]\n    ]\n  },\n  \"estimateStatus\": \"sent\"\n}")

	  .asString();

```

### GO
#### NATIVE
```go
	package main

	

	import (

	  "fmt"

	  "strings"

	  "net/http"

	  "io"

	)

	

	func main() {

	

	  url := "https://services.leadconnectorhq.com/invoices/estimate/:estimateId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        null

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        null

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	}`)

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, payload)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  req.Header.Add("Content-Type", "application/json")

	  req.Header.Add("Accept", "application/json")

	  req.Header.Add("Authorization", "Bearer <TOKEN>")

	

	  res, err := client.Do(req)

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  defer res.Body.Close()

	

	  body, err := io.ReadAll(res.Body)

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  fmt.Println(string(body))

	}

```

### RUBY
#### NET::HTTP
```ruby
	require "uri"

	require "json"

	require "net/http"

	

	url = URI("https://services.leadconnectorhq.com/invoices/estimate/:estimateId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "Home Service Estimate",

	  "businessDetails": {

	    "logoUrl": "https://example.com/logo.png",

	    "name": "ABC Corp.",

	    "phoneNo": "+1-214-559-6993",

	    "address": "9931 Beechwood, TX",

	    "website": "wwww.example.com",

	    "customValues": [

	      "string"

	    ]

	  },

	  "currency": "USD",

	  "items": [

	    {

	      "name": "ABC Product",

	      "description": "ABC Corp.",

	      "productId": "6578278e879ad2646715ba9c",

	      "priceId": "6578278e879ad2646715ba9c",

	      "currency": "USD",

	      "amount": 999,

	      "qty": 1,

	      "taxes": [

	        {

	          "_id": "string",

	          "name": "string",

	          "rate": 0,

	          "calculation": "exclusive",

	          "description": "string",

	          "taxId": "string"

	        }

	      ],

	      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",

	      "isSetupFeeItem": true,

	      "type": "one_time",

	      "taxInclusive": true,

	      "attachments": [

	        "https://example.com/file1.jpg",

	        "https://example.com/file2.png"

	      ]

	    }

	  ],

	  "liveMode": true,

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "ESTIMATE",

	  "contactDetails": {

	    "id": "6578278e879ad2646715ba9c",

	    "name": "Alex",

	    "phoneNo": "+1234567890",

	    "email": "alex@example.com",

	    "additionalEmails": [

	      {

	        "email": "alex@example.com"

	      }

	    ],

	    "companyName": "ABC Corp.",

	    "address": {

	      "addressLine1": "9931 Beechwood",

	      "addressLine2": "Beechwood",

	      "city": "St. Houston",

	      "state": "TX",

	      "countryCode": "US",

	      "postalCode": "559-6993"

	    },

	    "customFields": [

	      "string"

	    ]

	  },

	  "estimateNumber": 1001,

	  "issueDate": "2024-08-07",

	  "expiryDate": "2024-08-10",

	  "sentTo": {

	    "email": [

	      "alex@example.com"

	    ],

	    "emailCc": [

	      "alex@example.com"

	    ],

	    "emailBcc": [

	      "alex@example.com"

	    ],

	    "phoneNo": [

	      "+1-214-559-6993"

	    ]

	  },

	  "automaticTaxesEnabled": true,

	  "meta": {

	    "key": "value"

	  },

	  "sendEstimateDetails": {

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "action": "sms_and_email",

	    "liveMode": true,

	    "userId": "6578278e879ad2646715ba9c",

	    "sentFrom": {

	      "fromName": "Alex",

	      "fromEmail": "alex@example.com"

	    },

	    "estimateName": "Estimate"

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

	  "estimateNumberPrefix": "EST-",

	  "userId": "6578278e879ad2646715ba9c",

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

	  "autoInvoice": {

	    "enabled": true,

	    "directPayments": true

	  },

	  "miscellaneousCharges": {

	    "charges": [

	      [

	        "__RUBY\#%0NULL__"

	      ]

	    ],

	    "collectedMiscellaneousCharges": 10,

	    "paidCharges": [

	      {

	        "name": "Processing Fee",

	        "charge": 10,

	        "amount": 10,

	        "_id": "673d01d7d547648a8dab6211"

	      }

	    ]

	  },

	  "paymentScheduleConfig": {

	    "type": "fixed",

	    "dateConfig": {

	      "depositDateType": "estimate_accepted",

	      "scheduleDateType": "regular_interval"

	    },

	    "schedules": [

	      [

	        "__RUBY\#%0NULL__"

	      ]

	    ]

	  },

	  "estimateStatus": "sent"

	})

	

	response = https.request(request)

	puts response.read_body

```

### POWERSHELL
#### RESTMETHOD
```powershell
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"

	$headers.Add("Content-Type", "application/json")

	$headers.Add("Accept", "application/json")

	$headers.Add("Authorization", "Bearer <TOKEN>")

	

	$body = @"

	{

	  `"altId`": `"6578278e879ad2646715ba9c`",

	  `"altType`": `"location`",

	  `"name`": `"Home Service Estimate`",

	  `"businessDetails`": {

	    `"logoUrl`": `"https://example.com/logo.png`",

	    `"name`": `"ABC Corp.`",

	    `"phoneNo`": `"+1-214-559-6993`",

	    `"address`": `"9931 Beechwood, TX`",

	    `"website`": `"wwww.example.com`",

	    `"customValues`": [

	      `"string`"

	    ]

	  },

	  `"currency`": `"USD`",

	  `"items`": [

	    {

	      `"name`": `"ABC Product`",

	      `"description`": `"ABC Corp.`",

	      `"productId`": `"6578278e879ad2646715ba9c`",

	      `"priceId`": `"6578278e879ad2646715ba9c`",

	      `"currency`": `"USD`",

	      `"amount`": 999,

	      `"qty`": 1,

	      `"taxes`": [

	        {

	          `"_id`": `"string`",

	          `"name`": `"string`",

	          `"rate`": 0,

	          `"calculation`": `"exclusive`",

	          `"description`": `"string`",

	          `"taxId`": `"string`"

	        }

	      ],

	      `"automaticTaxCategoryId`": `"6578278e879ad2646715ba9c`",

	      `"isSetupFeeItem`": true,

	      `"type`": `"one_time`",

	      `"taxInclusive`": true,

	      `"attachments`": [

	        `"https://example.com/file1.jpg`",

	        `"https://example.com/file2.png`"

	      ]

	    }

	  ],

	  `"liveMode`": true,

	  `"discount`": {

	    `"value`": 10,

	    `"type`": `"percentage`",

	    `"validOnProductIds`": `"[ '6579751d56f60276e5bd4154' ]`"

	  },

	  `"termsNotes`": `"<p>This is a default terms.</p>`",

	  `"title`": `"ESTIMATE`",

	  `"contactDetails`": {

	    `"id`": `"6578278e879ad2646715ba9c`",

	    `"name`": `"Alex`",

	    `"phoneNo`": `"+1234567890`",

	    `"email`": `"alex@example.com`",

	    `"additionalEmails`": [

	      {

	        `"email`": `"alex@example.com`"

	      }

	    ],

	    `"companyName`": `"ABC Corp.`",

	    `"address`": {

	      `"addressLine1`": `"9931 Beechwood`",

	      `"addressLine2`": `"Beechwood`",

	      `"city`": `"St. Houston`",

	      `"state`": `"TX`",

	      `"countryCode`": `"US`",

	      `"postalCode`": `"559-6993`"

	    },

	    `"customFields`": [

	      `"string`"

	    ]

	  },

	  `"estimateNumber`": 1001,

	  `"issueDate`": `"2024-08-07`",

	  `"expiryDate`": `"2024-08-10`",

	  `"sentTo`": {

	    `"email`": [

	      `"alex@example.com`"

	    ],

	    `"emailCc`": [

	      `"alex@example.com`"

	    ],

	    `"emailBcc`": [

	      `"alex@example.com`"

	    ],

	    `"phoneNo`": [

	      `"+1-214-559-6993`"

	    ]

	  },

	  `"automaticTaxesEnabled`": true,

	  `"meta`": {

	    `"key`": `"value`"

	  },

	  `"sendEstimateDetails`": {

	    `"altId`": `"6578278e879ad2646715ba9c`",

	    `"altType`": `"location`",

	    `"action`": `"sms_and_email`",

	    `"liveMode`": true,

	    `"userId`": `"6578278e879ad2646715ba9c`",

	    `"sentFrom`": {

	      `"fromName`": `"Alex`",

	      `"fromEmail`": `"alex@example.com`"

	    },

	    `"estimateName`": `"Estimate`"

	  },

	  `"frequencySettings`": {

	    `"enabled`": true,

	    `"schedule`": {

	      `"executeAt`": `"string`",

	      `"rrule`": {

	        `"intervalType`": `"monthly`",

	        `"interval`": 2,

	        `"startDate`": `"2023-01-01`",

	        `"startTime`": `"20:45:00`",

	        `"endDate`": `"2029-11-01`",

	        `"endTime`": `"18:45:00`",

	        `"dayOfMonth`": 15,

	        `"dayOfWeek`": `"mo`",

	        `"numOfWeek`": -1,

	        `"monthOfYear`": `"jan`",

	        `"count`": 10,

	        `"daysBefore`": 5,

	        `"useStartAsPrimaryUserAccepted`": true,

	        `"endType`": `"by`"

	      }

	    }

	  },

	  `"estimateNumberPrefix`": `"EST-`",

	  `"userId`": `"6578278e879ad2646715ba9c`",

	  `"attachments`": [

	    {

	      `"id`": `"6241712be68f7a98102ba272`",

	      `"name`": `"Electronics.pdf`",

	      `"url`": `"https://example.com/digital-delivery`",

	      `"type`": `"string`",

	      `"size`": 10000

	    }

	  ],

	  `"autoInvoice`": {

	    `"enabled`": true,

	    `"directPayments`": true

	  },

	  `"miscellaneousCharges`": {

	    `"charges`": [

	      [

	        null

	      ]

	    ],

	    `"collectedMiscellaneousCharges`": 10,

	    `"paidCharges`": [

	      {

	        `"name`": `"Processing Fee`",

	        `"charge`": 10,

	        `"amount`": 10,

	        `"_id`": `"673d01d7d547648a8dab6211`"

	      }

	    ]

	  },

	  `"paymentScheduleConfig`": {

	    `"type`": `"fixed`",

	    `"dateConfig`": {

	      `"depositDateType`": `"estimate_accepted`",

	      `"scheduleDateType`": `"regular_interval`"

	    },

	    `"schedules`": [

	      [

	        null

	      ]

	    ]

	  },

	  `"estimateStatus`": `"sent`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/estimate/:estimateId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

