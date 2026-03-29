# Update Contact

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/contacts/:contactId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: contacts.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `contactId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

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
      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",
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
      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",
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
</details>

<details>
<summary>Response 400</summary>

```json
{  "succeded": true,  "contact": {    "id": "seD4PfOuKoVMLkEZqohJ",    "name": "rubika deo",    "locationId": "ve9EPM428h8vShlRW1KT",    "firstName": "rubika",    "lastName": "Deo",    "email": "rubika@deos.com",    "emailLowerCase": "rubika@deos.com",    "timezone": "Asia/Calcutta",    "companyName": "DGS VolMAX",    "phone": "+18832327657",    "dnd": true,    "dndSettings": {      "Call": {        "status": "active",        "message": "string",        "code": "string"      },      "Email": {        "status": "active",        "message": "string",        "code": "string"      },      "SMS": {        "status": "active",        "message": "string",        "code": "string"      },      "WhatsApp": {        "status": "active",        "message": "string",        "code": "string"      },      "GMB": {        "status": "active",        "message": "string",        "code": "string"      },      "FB": {        "status": "active",        "message": "string",        "code": "string"      }    },    "type": "read",    "source": "public api",    "assignedTo": "ve9EPM428h8vShlRW1KT",    "address1": "3535 1st St N",    "city": "ruDolomitebika",    "state": "AL",    "country": "US",    "postalCode": "35061",    "website": "https://www.tesla.com",    "tags": [      "nisi sint commodo amet",      "consequat"    ],    "dateOfBirth": "Date format YYYY-MM-DD",    "dateAdded": "2021-07-02T05:18:26.704Z",    "dateUpdated": "2021-07-02T05:18:26.704Z",    "attachments": "string",    "ssn": "string",    "keyword": "test",    "firstNameLowerCase": "rubika",    "fullNameLowerCase": "rubika deo",    "lastNameLowerCase": "deo",    "lastActivity": "2021-07-16T11:39:30.564Z",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "value": "name"      }    ],    "businessId": "641c094001436dbc2081e642",    "attributionSource": {      "url": "Trigger Link",      "campaign": "string",      "utmSource": "string",      "utmMedium": "string",      "utmContent": "string",      "referrer": "https: //www.google.com",      "campaignId": "string",      "fbclid": "string",      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",      "msclikid": "string",      "dclid": "string",      "fbc": "string",      "fbp": "fb. 1.1674748390986.1171287961",      "fbEventId": "Mozilla/5.0",      "userAgent": "Mozilla/5.0",      "ip": "58.111.106.198",      "medium": "survey",      "mediumId": "FglfHAn30PRwsZVyQlKp"    },    "lastAttributionSource": {      "url": "Trigger Link",      "campaign": "string",      "utmSource": "string",      "utmMedium": "string",      "utmContent": "string",      "referrer": "https: //www.google.com",      "campaignId": "string",      "fbclid": "string",      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",      "msclikid": "string",      "dclid": "string",      "fbc": "string",      "fbp": "fb. 1.1674748390986.1171287961",      "fbEventId": "Mozilla/5.0",      "userAgent": "Mozilla/5.0",      "ip": "58.111.106.198",      "medium": "survey",      "mediumId": "FglfHAn30PRwsZVyQlKp"    },    "visitorId": "ve9EPM428h8vShlRW1KT"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "succeded": true,  "contact": {    "id": "seD4PfOuKoVMLkEZqohJ",    "name": "rubika deo",    "locationId": "ve9EPM428h8vShlRW1KT",    "firstName": "rubika",    "lastName": "Deo",    "email": "rubika@deos.com",    "emailLowerCase": "rubika@deos.com",    "timezone": "Asia/Calcutta",    "companyName": "DGS VolMAX",    "phone": "+18832327657",    "dnd": true,    "dndSettings": {      "Call": {        "status": "active",        "message": "string",        "code": "string"      },      "Email": {        "status": "active",        "message": "string",        "code": "string"      },      "SMS": {        "status": "active",        "message": "string",        "code": "string"      },      "WhatsApp": {        "status": "active",        "message": "string",        "code": "string"      },      "GMB": {        "status": "active",        "message": "string",        "code": "string"      },      "FB": {        "status": "active",        "message": "string",        "code": "string"      }    },    "type": "read",    "source": "public api",    "assignedTo": "ve9EPM428h8vShlRW1KT",    "address1": "3535 1st St N",    "city": "ruDolomitebika",    "state": "AL",    "country": "US",    "postalCode": "35061",    "website": "https://www.tesla.com",    "tags": [      "nisi sint commodo amet",      "consequat"    ],    "dateOfBirth": "Date format YYYY-MM-DD",    "dateAdded": "2021-07-02T05:18:26.704Z",    "dateUpdated": "2021-07-02T05:18:26.704Z",    "attachments": "string",    "ssn": "string",    "keyword": "test",    "firstNameLowerCase": "rubika",    "fullNameLowerCase": "rubika deo",    "lastNameLowerCase": "deo",    "lastActivity": "2021-07-16T11:39:30.564Z",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "value": "name"      }    ],    "businessId": "641c094001436dbc2081e642",    "attributionSource": {      "url": "Trigger Link",      "campaign": "string",      "utmSource": "string",      "utmMedium": "string",      "utmContent": "string",      "referrer": "https: //www.google.com",      "campaignId": "string",      "fbclid": "string",      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",      "msclikid": "string",      "dclid": "string",      "fbc": "string",      "fbp": "fb. 1.1674748390986.1171287961",      "fbEventId": "Mozilla/5.0",      "userAgent": "Mozilla/5.0",      "ip": "58.111.106.198",      "medium": "survey",      "mediumId": "FglfHAn30PRwsZVyQlKp"    },    "lastAttributionSource": {      "url": "Trigger Link",      "campaign": "string",      "utmSource": "string",      "utmMedium": "string",      "utmContent": "string",      "referrer": "https: //www.google.com",      "campaignId": "string",      "fbclid": "string",      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",      "msclikid": "string",      "dclid": "string",      "fbc": "string",      "fbp": "fb. 1.1674748390986.1171287961",      "fbEventId": "Mozilla/5.0",      "userAgent": "Mozilla/5.0",      "ip": "58.111.106.198",      "medium": "survey",      "mediumId": "FglfHAn30PRwsZVyQlKp"    },    "visitorId": "ve9EPM428h8vShlRW1KT"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "succeded": true,  "contact": {    "id": "seD4PfOuKoVMLkEZqohJ",    "name": "rubika deo",    "locationId": "ve9EPM428h8vShlRW1KT",    "firstName": "rubika",    "lastName": "Deo",    "email": "rubika@deos.com",    "emailLowerCase": "rubika@deos.com",    "timezone": "Asia/Calcutta",    "companyName": "DGS VolMAX",    "phone": "+18832327657",    "dnd": true,    "dndSettings": {      "Call": {        "status": "active",        "message": "string",        "code": "string"      },      "Email": {        "status": "active",        "message": "string",        "code": "string"      },      "SMS": {        "status": "active",        "message": "string",        "code": "string"      },      "WhatsApp": {        "status": "active",        "message": "string",        "code": "string"      },      "GMB": {        "status": "active",        "message": "string",        "code": "string"      },      "FB": {        "status": "active",        "message": "string",        "code": "string"      }    },    "type": "read",    "source": "public api",    "assignedTo": "ve9EPM428h8vShlRW1KT",    "address1": "3535 1st St N",    "city": "ruDolomitebika",    "state": "AL",    "country": "US",    "postalCode": "35061",    "website": "https://www.tesla.com",    "tags": [      "nisi sint commodo amet",      "consequat"    ],    "dateOfBirth": "Date format YYYY-MM-DD",    "dateAdded": "2021-07-02T05:18:26.704Z",    "dateUpdated": "2021-07-02T05:18:26.704Z",    "attachments": "string",    "ssn": "string",    "keyword": "test",    "firstNameLowerCase": "rubika",    "fullNameLowerCase": "rubika deo",    "lastNameLowerCase": "deo",    "lastActivity": "2021-07-16T11:39:30.564Z",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "value": "name"      }    ],    "businessId": "641c094001436dbc2081e642",    "attributionSource": {      "url": "Trigger Link",      "campaign": "string",      "utmSource": "string",      "utmMedium": "string",      "utmContent": "string",      "referrer": "https: //www.google.com",      "campaignId": "string",      "fbclid": "string",      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",      "msclikid": "string",      "dclid": "string",      "fbc": "string",      "fbp": "fb. 1.1674748390986.1171287961",      "fbEventId": "Mozilla/5.0",      "userAgent": "Mozilla/5.0",      "ip": "58.111.106.198",      "medium": "survey",      "mediumId": "FglfHAn30PRwsZVyQlKp"    },    "lastAttributionSource": {      "url": "Trigger Link",      "campaign": "string",      "utmSource": "string",      "utmMedium": "string",      "utmContent": "string",      "referrer": "https: //www.google.com",      "campaignId": "string",      "fbclid": "string",      "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",      "msclikid": "string",      "dclid": "string",      "fbc": "string",      "fbp": "fb. 1.1674748390986.1171287961",      "fbEventId": "Mozilla/5.0",      "userAgent": "Mozilla/5.0",      "ip": "58.111.106.198",      "medium": "survey",      "mediumId": "FglfHAn30PRwsZVyQlKp"    },    "visitorId": "ve9EPM428h8vShlRW1KT"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/contacts/:contactId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	  const response = await highLevel.contacts.updateContact({

	    'contactId': 'ocQHyuzHvysMo5N5VsXc'

	  },

	  {

	    'firstName': 'rosan',

	    'lastName': 'Deo',

	    'name': 'rosan Deo',

	    'email': 'rosan@deos.com',

	    'phone': '+1 888-888-8888',

	    'address1': '3535 1st St N',

	    'city': 'Dolomite',

	    'state': 'AL',

	    'postalCode': '35061',

	    'website': 'https://www.tesla.com',

	    'timezone': 'America/Chihuahua',

	    'dnd': true,

	    'dndSettings': {

	      'Call': {

	        'status': 'active',

	        'message': 'string',

	        'code': 'string'

	      },

	      'Email': {

	        'status': 'active',

	        'message': 'string',

	        'code': 'string'

	      },

	      'SMS': {

	        'status': 'active',

	        'message': 'string',

	        'code': 'string'

	      },

	      'WhatsApp': {

	        'status': 'active',

	        'message': 'string',

	        'code': 'string'

	      },

	      'GMB': {

	        'status': 'active',

	        'message': 'string',

	        'code': 'string'

	      },

	      'FB': {

	        'status': 'active',

	        'message': 'string',

	        'code': 'string'

	      }

	    },

	    'inboundDndSettings': {

	      'all': {

	        'status': 'active',

	        'message': 'string'

	      }

	    },

	    'tags': [

	      'nisi sint commodo amet',

	      'consequat'

	    ],

	    'customFields': [

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': 'My Text'

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': 'My Text'

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': 'My Selected Option'

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': 'My Selected Option'

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': 100

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': 100.5

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': [

	          'test',

	          'test2'

	        ]

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': [

	          'test',

	          'test2'

	        ]

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': {

	          'f31175d4-2b06-4fc6-b7bc-74cd814c68cb': {

	            'meta': {

	              'fieldname': '1HeGizb13P0odwgOgKSs',

	              'originalname': 'IMG_20231215_164412935.jpg',

	              'encoding': '7bit',

	              'mimetype': 'image/jpeg',

	              'size': 1786611,

	              'uuid': 'f31175d4-2b06-4fc6-b7bc-74cd814c68cb'

	            },

	            'url': 'https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ',

	            'documentId': 'w2M9qTZ0ZJz8rGt02jdJ'

	          }

	        }

	      }

	    ],

	    'source': 'public api',

	    'dateOfBirth': '1990-09-25',

	    'country': 'US',

	    'assignedTo': 'y0BeYjuRIlDwsDcOHOJo'

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

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/contacts/:contactId',

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

	  'path': '/contacts/:contactId',

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

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/contacts/:contactId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "firstName": "rosan",

	    "lastName": "Deo",

	    "name": "rosan Deo",

	    "email": "rosan@deos.com",

	    "phone": "+1 888-888-8888",

	    "address1": "3535 1st St N",

	    "city": "Dolomite",

	    "state": "AL",

	    "postalCode": "35061",

	    "website": "https://www.tesla.com",

	    "timezone": "America/Chihuahua",

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

	    "inboundDndSettings": {

	      "all": {

	        "status": "active",

	        "message": "string"

	      }

	    },

	    "tags": [

	      "nisi sint commodo amet",

	      "consequat"

	    ],

	    "customFields": [

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Text"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Text"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Selected Option"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Selected Option"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": 100

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": 100.5

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": [

	          "test",

	          "test2"

	        ]

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": [

	          "test",

	          "test2"

	        ]

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": {

	          "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	            "meta": {

	              "fieldname": "1HeGizb13P0odwgOgKSs",

	              "originalname": "IMG_20231215_164412935.jpg",

	              "encoding": "7bit",

	              "mimetype": "image/jpeg",

	              "size": 1786611,

	              "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	            },

	            "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	            "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	          }

	        }

	      }

	    ],

	    "source": "public api",

	    "dateOfBirth": "1990-09-25",

	    "country": "US",

	    "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/contacts/:contactId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "firstName": "rosan",

	    "lastName": "Deo",

	    "name": "rosan Deo",

	    "email": "rosan@deos.com",

	    "phone": "+1 888-888-8888",

	    "address1": "3535 1st St N",

	    "city": "Dolomite",

	    "state": "AL",

	    "postalCode": "35061",

	    "website": "https://www.tesla.com",

	    "timezone": "America/Chihuahua",

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

	    "inboundDndSettings": {

	      "all": {

	        "status": "active",

	        "message": "string"

	      }

	    },

	    "tags": [

	      "nisi sint commodo amet",

	      "consequat"

	    ],

	    "customFields": [

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Text"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Text"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Selected Option"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "My Selected Option"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": 100

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": 100.5

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": [

	          "test",

	          "test2"

	        ]

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": [

	          "test",

	          "test2"

	        ]

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": {

	          "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	            "meta": {

	              "fieldname": "1HeGizb13P0odwgOgKSs",

	              "originalname": "IMG_20231215_164412935.jpg",

	              "encoding": "7bit",

	              "mimetype": "image/jpeg",

	              "size": 1786611,

	              "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	            },

	            "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	            "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	          }

	        }

	      }

	    ],

	    "source": "public api",

	    "dateOfBirth": "1990-09-25",

	    "country": "US",

	    "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

	  "dnd": True,

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/contacts/:contactId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/contacts/:contactId"

	

	payload = json.dumps({

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

	  "dnd": True,

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/contacts/:contactId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/contacts/:contactId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/contacts/:contactId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "firstName": "rosan",\n  "lastName": "Deo",\n  "name": "rosan Deo",\n  "email": "rosan@deos.com",\n  "phone": "+1 888-888-8888",\n  "address1": "3535 1st St N",\n  "city": "Dolomite",\n  "state": "AL",\n  "postalCode": "35061",\n  "website": "https://www.tesla.com",\n  "timezone": "America/Chihuahua",\n  "dnd": true,\n  "dndSettings": {\n    "Call": {\n      "status": "active",\n      "message": "string",\n      "code": "string"\n    },\n    "Email": {\n      "status": "active",\n      "message": "string",\n      "code": "string"\n    },\n    "SMS": {\n      "status": "active",\n      "message": "string",\n      "code": "string"\n    },\n    "WhatsApp": {\n      "status": "active",\n      "message": "string",\n      "code": "string"\n    },\n    "GMB": {\n      "status": "active",\n      "message": "string",\n      "code": "string"\n    },\n    "FB": {\n      "status": "active",\n      "message": "string",\n      "code": "string"\n    }\n  },\n  "inboundDndSettings": {\n    "all": {\n      "status": "active",\n      "message": "string"\n    }\n  },\n  "tags": [\n    "nisi sint commodo amet",\n    "consequat"\n  ],\n  "customFields": [\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": "My Text"\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": "My Text"\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": "My Selected Option"\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": "My Selected Option"\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": 100\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": 100.5\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": [\n        "test",\n        "test2"\n      ]\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": [\n        "test",\n        "test2"\n      ]\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": {\n        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {\n          "meta": {\n            "fieldname": "1HeGizb13P0odwgOgKSs",\n            "originalname": "IMG_20231215_164412935.jpg",\n            "encoding": "7bit",\n            "mimetype": "image/jpeg",\n            "size": 1786611,\n            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"\n          },\n          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",\n          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"\n        }\n      }\n    }\n  ],\n  "source": "public api",\n  "dateOfBirth": "1990-09-25",\n  "country": "US",\n  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/contacts/:contactId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"firstName\": \"rosan\",\n  \"lastName\": \"Deo\",\n  \"name\": \"rosan Deo\",\n  \"email\": \"rosan@deos.com\",\n  \"phone\": \"+1 888-888-8888\",\n  \"address1\": \"3535 1st St N\",\n  \"city\": \"Dolomite\",\n  \"state\": \"AL\",\n  \"postalCode\": \"35061\",\n  \"website\": \"https://www.tesla.com\",\n  \"timezone\": \"America/Chihuahua\",\n  \"dnd\": true,\n  \"dndSettings\": {\n    \"Call\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"Email\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"SMS\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"WhatsApp\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"GMB\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"FB\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    }\n  },\n  \"inboundDndSettings\": {\n    \"all\": {\n      \"status\": \"active\",\n      \"message\": \"string\"\n    }\n  },\n  \"tags\": [\n    \"nisi sint commodo amet\",\n    \"consequat\"\n  ],\n  \"customFields\": [\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Text\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Text\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Selected Option\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Selected Option\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": 100\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": 100.5\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": [\n        \"test\",\n        \"test2\"\n      ]\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": [\n        \"test\",\n        \"test2\"\n      ]\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": {\n        \"f31175d4-2b06-4fc6-b7bc-74cd814c68cb\": {\n          \"meta\": {\n            \"fieldname\": \"1HeGizb13P0odwgOgKSs\",\n            \"originalname\": \"IMG_20231215_164412935.jpg\",\n            \"encoding\": \"7bit\",\n            \"mimetype\": \"image/jpeg\",\n            \"size\": 1786611,\n            \"uuid\": \"f31175d4-2b06-4fc6-b7bc-74cd814c68cb\"\n          },\n          \"url\": \"https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ\",\n          \"documentId\": \"w2M9qTZ0ZJz8rGt02jdJ\"\n        }\n      }\n    }\n  ],\n  \"source\": \"public api\",\n  \"dateOfBirth\": \"1990-09-25\",\n  \"country\": \"US\",\n  \"assignedTo\": \"y0BeYjuRIlDwsDcOHOJo\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/contacts/:contactId")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/contacts/:contactId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"firstName\": \"rosan\",\n  \"lastName\": \"Deo\",\n  \"name\": \"rosan Deo\",\n  \"email\": \"rosan@deos.com\",\n  \"phone\": \"+1 888-888-8888\",\n  \"address1\": \"3535 1st St N\",\n  \"city\": \"Dolomite\",\n  \"state\": \"AL\",\n  \"postalCode\": \"35061\",\n  \"website\": \"https://www.tesla.com\",\n  \"timezone\": \"America/Chihuahua\",\n  \"dnd\": true,\n  \"dndSettings\": {\n    \"Call\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"Email\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"SMS\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"WhatsApp\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"GMB\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    },\n    \"FB\": {\n      \"status\": \"active\",\n      \"message\": \"string\",\n      \"code\": \"string\"\n    }\n  },\n  \"inboundDndSettings\": {\n    \"all\": {\n      \"status\": \"active\",\n      \"message\": \"string\"\n    }\n  },\n  \"tags\": [\n    \"nisi sint commodo amet\",\n    \"consequat\"\n  ],\n  \"customFields\": [\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Text\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Text\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Selected Option\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"My Selected Option\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": 100\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": 100.5\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": [\n        \"test\",\n        \"test2\"\n      ]\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": [\n        \"test\",\n        \"test2\"\n      ]\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": {\n        \"f31175d4-2b06-4fc6-b7bc-74cd814c68cb\": {\n          \"meta\": {\n            \"fieldname\": \"1HeGizb13P0odwgOgKSs\",\n            \"originalname\": \"IMG_20231215_164412935.jpg\",\n            \"encoding\": \"7bit\",\n            \"mimetype\": \"image/jpeg\",\n            \"size\": 1786611,\n            \"uuid\": \"f31175d4-2b06-4fc6-b7bc-74cd814c68cb\"\n          },\n          \"url\": \"https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ\",\n          \"documentId\": \"w2M9qTZ0ZJz8rGt02jdJ\"\n        }\n      }\n    }\n  ],\n  \"source\": \"public api\",\n  \"dateOfBirth\": \"1990-09-25\",\n  \"country\": \"US\",\n  \"assignedTo\": \"y0BeYjuRIlDwsDcOHOJo\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/contacts/:contactId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	

	url = URI("https://services.leadconnectorhq.com/contacts/:contactId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "firstName": "rosan",

	  "lastName": "Deo",

	  "name": "rosan Deo",

	  "email": "rosan@deos.com",

	  "phone": "+1 888-888-8888",

	  "address1": "3535 1st St N",

	  "city": "Dolomite",

	  "state": "AL",

	  "postalCode": "35061",

	  "website": "https://www.tesla.com",

	  "timezone": "America/Chihuahua",

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

	  "inboundDndSettings": {

	    "all": {

	      "status": "active",

	      "message": "string"

	    }

	  },

	  "tags": [

	    "nisi sint commodo amet",

	    "consequat"

	  ],

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Text"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "My Selected Option"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": 100.5

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {

	        "f31175d4-2b06-4fc6-b7bc-74cd814c68cb": {

	          "meta": {

	            "fieldname": "1HeGizb13P0odwgOgKSs",

	            "originalname": "IMG_20231215_164412935.jpg",

	            "encoding": "7bit",

	            "mimetype": "image/jpeg",

	            "size": 1786611,

	            "uuid": "f31175d4-2b06-4fc6-b7bc-74cd814c68cb"

	          },

	          "url": "https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ",

	          "documentId": "w2M9qTZ0ZJz8rGt02jdJ"

	        }

	      }

	    }

	  ],

	  "source": "public api",

	  "dateOfBirth": "1990-09-25",

	  "country": "US",

	  "assignedTo": "y0BeYjuRIlDwsDcOHOJo"

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

	  `"firstName`": `"rosan`",

	  `"lastName`": `"Deo`",

	  `"name`": `"rosan Deo`",

	  `"email`": `"rosan@deos.com`",

	  `"phone`": `"+1 888-888-8888`",

	  `"address1`": `"3535 1st St N`",

	  `"city`": `"Dolomite`",

	  `"state`": `"AL`",

	  `"postalCode`": `"35061`",

	  `"website`": `"https://www.tesla.com`",

	  `"timezone`": `"America/Chihuahua`",

	  `"dnd`": true,

	  `"dndSettings`": {

	    `"Call`": {

	      `"status`": `"active`",

	      `"message`": `"string`",

	      `"code`": `"string`"

	    },

	    `"Email`": {

	      `"status`": `"active`",

	      `"message`": `"string`",

	      `"code`": `"string`"

	    },

	    `"SMS`": {

	      `"status`": `"active`",

	      `"message`": `"string`",

	      `"code`": `"string`"

	    },

	    `"WhatsApp`": {

	      `"status`": `"active`",

	      `"message`": `"string`",

	      `"code`": `"string`"

	    },

	    `"GMB`": {

	      `"status`": `"active`",

	      `"message`": `"string`",

	      `"code`": `"string`"

	    },

	    `"FB`": {

	      `"status`": `"active`",

	      `"message`": `"string`",

	      `"code`": `"string`"

	    }

	  },

	  `"inboundDndSettings`": {

	    `"all`": {

	      `"status`": `"active`",

	      `"message`": `"string`"

	    }

	  },

	  `"tags`": [

	    `"nisi sint commodo amet`",

	    `"consequat`"

	  ],

	  `"customFields`": [

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": `"My Text`"

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": `"My Text`"

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": `"My Selected Option`"

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": `"My Selected Option`"

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": 100

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": 100.5

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": [

	        `"test`",

	        `"test2`"

	      ]

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": [

	        `"test`",

	        `"test2`"

	      ]

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": {

	        `"f31175d4-2b06-4fc6-b7bc-74cd814c68cb`": {

	          `"meta`": {

	            `"fieldname`": `"1HeGizb13P0odwgOgKSs`",

	            `"originalname`": `"IMG_20231215_164412935.jpg`",

	            `"encoding`": `"7bit`",

	            `"mimetype`": `"image/jpeg`",

	            `"size`": 1786611,

	            `"uuid`": `"f31175d4-2b06-4fc6-b7bc-74cd814c68cb`"

	          },

	          `"url`": `"https://services.leadconnectorhq.com/documents/download/w2M9qTZ0ZJz8rGt02jdJ`",

	          `"documentId`": `"w2M9qTZ0ZJz8rGt02jdJ`"

	        }

	      }

	    }

	  ],

	  `"source`": `"public api`",

	  `"dateOfBirth`": `"1990-09-25`",

	  `"country`": `"US`",

	  `"assignedTo`": `"y0BeYjuRIlDwsDcOHOJo`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/:contactId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

