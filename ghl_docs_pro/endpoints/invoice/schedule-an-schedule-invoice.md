# Schedule an schedule invoice

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: invoices/schedule.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `scheduleId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

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
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "6578278e879ad2646715ba9c",  "status": "draft",  "liveMode": false,  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Invoice",  "schedule": {    "executeAt": "string",    "rrule": {      "intervalType": "monthly",      "interval": 2,      "startDate": "2023-01-01",      "startTime": "20:45:00",      "endDate": "2029-11-01",      "endTime": "18:45:00",      "dayOfMonth": 15,      "dayOfWeek": "mo",      "numOfWeek": -1,      "monthOfYear": "jan",      "count": 10,      "daysBefore": 5,      "useStartAsPrimaryUserAccepted": true,      "endType": "by"    }  },  "invoices": [    {      "_id": "6578278e879ad2646715ba9c",      "status": "draft",      "liveMode": false,      "amountPaid": 0,      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "New Invoice",      "businessDetails": {        "name": "Alex",        "address": {          "addressLine1": "9931 Beechwood",          "city": "St. Houston",          "state": "TX",          "countryCode": "USA",          "postalCode": "559-6993"        },        "phoneNo": "+1-214-559-6993",        "website": "www.example.com"      },      "invoiceNumber": "19",      "currency": "USD",      "contactDetails": {        "id": "c6tZZU0rJBf30ZXx9Gli",        "phoneNo": "+1-214-559-6993",        "email": "alex@example.com",        "customFields": [],        "name": "Alex",        "address": {          "countryCode": "US"        }      },      "issueDate": "2023-01-01",      "dueDate": "2023-01-01",      "discount": {        "type": "percentage",        "value": 0      },      "invoiceItems": [        {          "taxes": [],          "_id": "c6tZZU0rJBf30ZXx9Gli",          "productId": "c6tZZU0rJBf30ZXx9Gli",          "priceId": "c6tZZU0rJBf30ZXx9Gli",          "currency": "USD",          "name": "Macbook Pro",          "qty": 1,          "amount": 999        }      ],      "total": 999,      "title": "INVOICE",      "amountDue": 999,      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z",      "automaticTaxesEnabled": true,      "automaticTaxesCalculated": true,      "paymentSchedule": {}    }  ],  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "contactDetails": {    "id": "c6tZZU0rJBf30ZXx9Gli",    "phoneNo": "+1-214-559-6993",    "email": "alex@example.com",    "customFields": [],    "name": "Alex",    "address": {      "countryCode": "US"    }  },  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "total": 999,  "title": "INVOICE",  "termsNotes": "Confidential",  "compiledTermsNotes": "Confidential",  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "6578278e879ad2646715ba9c",  "status": "draft",  "liveMode": false,  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Invoice",  "schedule": {    "executeAt": "string",    "rrule": {      "intervalType": "monthly",      "interval": 2,      "startDate": "2023-01-01",      "startTime": "20:45:00",      "endDate": "2029-11-01",      "endTime": "18:45:00",      "dayOfMonth": 15,      "dayOfWeek": "mo",      "numOfWeek": -1,      "monthOfYear": "jan",      "count": 10,      "daysBefore": 5,      "useStartAsPrimaryUserAccepted": true,      "endType": "by"    }  },  "invoices": [    {      "_id": "6578278e879ad2646715ba9c",      "status": "draft",      "liveMode": false,      "amountPaid": 0,      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "New Invoice",      "businessDetails": {        "name": "Alex",        "address": {          "addressLine1": "9931 Beechwood",          "city": "St. Houston",          "state": "TX",          "countryCode": "USA",          "postalCode": "559-6993"        },        "phoneNo": "+1-214-559-6993",        "website": "www.example.com"      },      "invoiceNumber": "19",      "currency": "USD",      "contactDetails": {        "id": "c6tZZU0rJBf30ZXx9Gli",        "phoneNo": "+1-214-559-6993",        "email": "alex@example.com",        "customFields": [],        "name": "Alex",        "address": {          "countryCode": "US"        }      },      "issueDate": "2023-01-01",      "dueDate": "2023-01-01",      "discount": {        "type": "percentage",        "value": 0      },      "invoiceItems": [        {          "taxes": [],          "_id": "c6tZZU0rJBf30ZXx9Gli",          "productId": "c6tZZU0rJBf30ZXx9Gli",          "priceId": "c6tZZU0rJBf30ZXx9Gli",          "currency": "USD",          "name": "Macbook Pro",          "qty": 1,          "amount": 999        }      ],      "total": 999,      "title": "INVOICE",      "amountDue": 999,      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z",      "automaticTaxesEnabled": true,      "automaticTaxesCalculated": true,      "paymentSchedule": {}    }  ],  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "contactDetails": {    "id": "c6tZZU0rJBf30ZXx9Gli",    "phoneNo": "+1-214-559-6993",    "email": "alex@example.com",    "customFields": [],    "name": "Alex",    "address": {      "countryCode": "US"    }  },  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "total": 999,  "title": "INVOICE",  "termsNotes": "Confidential",  "compiledTermsNotes": "Confidential",  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "6578278e879ad2646715ba9c",  "status": "draft",  "liveMode": false,  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Invoice",  "schedule": {    "executeAt": "string",    "rrule": {      "intervalType": "monthly",      "interval": 2,      "startDate": "2023-01-01",      "startTime": "20:45:00",      "endDate": "2029-11-01",      "endTime": "18:45:00",      "dayOfMonth": 15,      "dayOfWeek": "mo",      "numOfWeek": -1,      "monthOfYear": "jan",      "count": 10,      "daysBefore": 5,      "useStartAsPrimaryUserAccepted": true,      "endType": "by"    }  },  "invoices": [    {      "_id": "6578278e879ad2646715ba9c",      "status": "draft",      "liveMode": false,      "amountPaid": 0,      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "New Invoice",      "businessDetails": {        "name": "Alex",        "address": {          "addressLine1": "9931 Beechwood",          "city": "St. Houston",          "state": "TX",          "countryCode": "USA",          "postalCode": "559-6993"        },        "phoneNo": "+1-214-559-6993",        "website": "www.example.com"      },      "invoiceNumber": "19",      "currency": "USD",      "contactDetails": {        "id": "c6tZZU0rJBf30ZXx9Gli",        "phoneNo": "+1-214-559-6993",        "email": "alex@example.com",        "customFields": [],        "name": "Alex",        "address": {          "countryCode": "US"        }      },      "issueDate": "2023-01-01",      "dueDate": "2023-01-01",      "discount": {        "type": "percentage",        "value": 0      },      "invoiceItems": [        {          "taxes": [],          "_id": "c6tZZU0rJBf30ZXx9Gli",          "productId": "c6tZZU0rJBf30ZXx9Gli",          "priceId": "c6tZZU0rJBf30ZXx9Gli",          "currency": "USD",          "name": "Macbook Pro",          "qty": 1,          "amount": 999        }      ],      "total": 999,      "title": "INVOICE",      "amountDue": 999,      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z",      "automaticTaxesEnabled": true,      "automaticTaxesCalculated": true,      "paymentSchedule": {}    }  ],  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "contactDetails": {    "id": "c6tZZU0rJBf30ZXx9Gli",    "phoneNo": "+1-214-559-6993",    "email": "alex@example.com",    "customFields": [],    "name": "Alex",    "address": {      "countryCode": "US"    }  },  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "total": 999,  "title": "INVOICE",  "termsNotes": "Confidential",  "compiledTermsNotes": "Confidential",  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

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

	  const response = await highLevel.invoices.scheduleInvoiceSchedule({

	    'scheduleId': '6578278e879ad2646715ba9c'

	  },

	  {

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'liveMode': true,

	    'autoPayment': {

	      'enable': true,

	      'type': 'string',

	      'paymentMethodId': 'string',

	      'customerId': 'string',

	      'card': {

	        'brand': 'string',

	        'last4': 'string'

	      },

	      'usBankAccount': {

	        'bank_name': 'string',

	        'last4': 'string'

	      },

	      'sepaDirectDebit': {

	        'bank_code': 'string',

	        'last4': 'string',

	        'branch_code': 'string'

	      },

	      'bacsDirectDebit': {

	        'sort_code': 'string',

	        'last4': 'string'

	      },

	      'becsDirectDebit': {

	        'bsb_number': 'string',

	        'last4': 'string'

	      },

	      'cardId': 'string',

	      'provider': {}

	    }

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

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule',

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

	  'method': 'POST',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/invoices/schedule/:scheduleId/schedule',

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

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "liveMode": true,

	    "autoPayment": {

	      "enable": true,

	      "type": "string",

	      "paymentMethodId": "string",

	      "customerId": "string",

	      "card": {

	        "brand": "string",

	        "last4": "string"

	      },

	      "usBankAccount": {

	        "bank_name": "string",

	        "last4": "string"

	      },

	      "sepaDirectDebit": {

	        "bank_code": "string",

	        "last4": "string",

	        "branch_code": "string"

	      },

	      "bacsDirectDebit": {

	        "sort_code": "string",

	        "last4": "string"

	      },

	      "becsDirectDebit": {

	        "bsb_number": "string",

	        "last4": "string"

	      },

	      "cardId": "string",

	      "provider": {}

	    }

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "liveMode": true,

	    "autoPayment": {

	      "enable": true,

	      "type": "string",

	      "paymentMethodId": "string",

	      "customerId": "string",

	      "card": {

	        "brand": "string",

	        "last4": "string"

	      },

	      "usBankAccount": {

	        "bank_name": "string",

	        "last4": "string"

	      },

	      "sepaDirectDebit": {

	        "bank_code": "string",

	        "last4": "string",

	        "branch_code": "string"

	      },

	      "bacsDirectDebit": {

	        "sort_code": "string",

	        "last4": "string"

	      },

	      "becsDirectDebit": {

	        "bsb_number": "string",

	        "last4": "string"

	      },

	      "cardId": "string",

	      "provider": {}

	    }

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

	  "liveMode": True,

	  "autoPayment": {

	    "enable": True,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/invoices/schedule/:scheduleId/schedule", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "liveMode": True,

	  "autoPayment": {

	    "enable": True,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("POST", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

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

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "liveMode": true,\n  "autoPayment": {\n    "enable": true,\n    "type": "string",\n    "paymentMethodId": "string",\n    "customerId": "string",\n    "card": {\n      "brand": "string",\n      "last4": "string"\n    },\n    "usBankAccount": {\n      "bank_name": "string",\n      "last4": "string"\n    },\n    "sepaDirectDebit": {\n      "bank_code": "string",\n      "last4": "string",\n      "branch_code": "string"\n    },\n    "bacsDirectDebit": {\n      "sort_code": "string",\n      "last4": "string"\n    },\n    "becsDirectDebit": {\n      "bsb_number": "string",\n      "last4": "string"\n    },\n    "cardId": "string",\n    "provider": {}\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"liveMode\": true,\n  \"autoPayment\": {\n    \"enable\": true,\n    \"type\": \"string\",\n    \"paymentMethodId\": \"string\",\n    \"customerId\": \"string\",\n    \"card\": {\n      \"brand\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"usBankAccount\": {\n      \"bank_name\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"sepaDirectDebit\": {\n      \"bank_code\": \"string\",\n      \"last4\": \"string\",\n      \"branch_code\": \"string\"\n    },\n    \"bacsDirectDebit\": {\n      \"sort_code\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"becsDirectDebit\": {\n      \"bsb_number\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"cardId\": \"string\",\n    \"provider\": {}\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"liveMode\": true,\n  \"autoPayment\": {\n    \"enable\": true,\n    \"type\": \"string\",\n    \"paymentMethodId\": \"string\",\n    \"customerId\": \"string\",\n    \"card\": {\n      \"brand\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"usBankAccount\": {\n      \"bank_name\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"sepaDirectDebit\": {\n      \"bank_code\": \"string\",\n      \"last4\": \"string\",\n      \"branch_code\": \"string\"\n    },\n    \"bacsDirectDebit\": {\n      \"sort_code\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"becsDirectDebit\": {\n      \"bsb_number\": \"string\",\n      \"last4\": \"string\"\n    },\n    \"cardId\": \"string\",\n    \"provider\": {}\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

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

	

	url = URI("https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "liveMode": true,

	  "autoPayment": {

	    "enable": true,

	    "type": "string",

	    "paymentMethodId": "string",

	    "customerId": "string",

	    "card": {

	      "brand": "string",

	      "last4": "string"

	    },

	    "usBankAccount": {

	      "bank_name": "string",

	      "last4": "string"

	    },

	    "sepaDirectDebit": {

	      "bank_code": "string",

	      "last4": "string",

	      "branch_code": "string"

	    },

	    "bacsDirectDebit": {

	      "sort_code": "string",

	      "last4": "string"

	    },

	    "becsDirectDebit": {

	      "bsb_number": "string",

	      "last4": "string"

	    },

	    "cardId": "string",

	    "provider": {}

	  }

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

	  `"liveMode`": true,

	  `"autoPayment`": {

	    `"enable`": true,

	    `"type`": `"string`",

	    `"paymentMethodId`": `"string`",

	    `"customerId`": `"string`",

	    `"card`": {

	      `"brand`": `"string`",

	      `"last4`": `"string`"

	    },

	    `"usBankAccount`": {

	      `"bank_name`": `"string`",

	      `"last4`": `"string`"

	    },

	    `"sepaDirectDebit`": {

	      `"bank_code`": `"string`",

	      `"last4`": `"string`",

	      `"branch_code`": `"string`"

	    },

	    `"bacsDirectDebit`": {

	      `"sort_code`": `"string`",

	      `"last4`": `"string`"

	    },

	    `"becsDirectDebit`": {

	      `"bsb_number`": `"string`",

	      `"last4`": `"string`"

	    },

	    `"cardId`": `"string`",

	    `"provider`": {}

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/schedule/:scheduleId/schedule' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

