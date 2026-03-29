# Create Invoice

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/invoices/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: invoices.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
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

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "6578278e879ad2646715ba9c",  "status": "draft",  "liveMode": false,  "amountPaid": 0,  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Invoice",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "invoiceNumber": "19",  "currency": "USD",  "contactDetails": {    "id": "c6tZZU0rJBf30ZXx9Gli",    "phoneNo": "+1-214-559-6993",    "email": "alex@example.com",    "customFields": [],    "name": "Alex",    "address": {      "countryCode": "US"    }  },  "issueDate": "2023-01-01",  "dueDate": "2023-01-01",  "discount": {    "type": "percentage",    "value": 0  },  "invoiceItems": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "total": 999,  "title": "INVOICE",  "amountDue": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z",  "automaticTaxesEnabled": true,  "automaticTaxesCalculated": true,  "paymentSchedule": {}}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "6578278e879ad2646715ba9c",  "status": "draft",  "liveMode": false,  "amountPaid": 0,  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Invoice",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "invoiceNumber": "19",  "currency": "USD",  "contactDetails": {    "id": "c6tZZU0rJBf30ZXx9Gli",    "phoneNo": "+1-214-559-6993",    "email": "alex@example.com",    "customFields": [],    "name": "Alex",    "address": {      "countryCode": "US"    }  },  "issueDate": "2023-01-01",  "dueDate": "2023-01-01",  "discount": {    "type": "percentage",    "value": 0  },  "invoiceItems": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "total": 999,  "title": "INVOICE",  "amountDue": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z",  "automaticTaxesEnabled": true,  "automaticTaxesCalculated": true,  "paymentSchedule": {}}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "6578278e879ad2646715ba9c",  "status": "draft",  "liveMode": false,  "amountPaid": 0,  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Invoice",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "invoiceNumber": "19",  "currency": "USD",  "contactDetails": {    "id": "c6tZZU0rJBf30ZXx9Gli",    "phoneNo": "+1-214-559-6993",    "email": "alex@example.com",    "customFields": [],    "name": "Alex",    "address": {      "countryCode": "US"    }  },  "issueDate": "2023-01-01",  "dueDate": "2023-01-01",  "discount": {    "type": "percentage",    "value": 0  },  "invoiceItems": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "total": 999,  "title": "INVOICE",  "amountDue": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z",  "automaticTaxesEnabled": true,  "automaticTaxesCalculated": true,  "paymentSchedule": {}}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/invoices/' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '\''6579751d56f60276e5bd4154'\'' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  const response = await highLevel.invoices.createInvoice({

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'name': 'New Invoice',

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

	        'taxInclusive': true

	      }

	    ],

	    'discount': {

	      'value': 10,

	      'type': 'percentage',

	      'validOnProductIds': '[ '6579751d56f60276e5bd4154' ]'

	    },

	    'termsNotes': '<p>This is a default terms.</p>',

	    'title': 'INVOICE',

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

	    'invoiceNumber': '1001',

	    'issueDate': '2023-01-01',

	    'dueDate': '2023-01-14',

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

	    'liveMode': true,

	    'automaticTaxesEnabled': true,

	    'paymentSchedule': {

	      'type': 'percentage',

	      'schedules': [

	        'string'

	      ]

	    },

	    'lateFeesConfiguration': {

	      'enable': true,

	      'value': 10,

	      'type': 'fixed',

	      'frequency': {

	        'intervalCount': 10,

	        'interval': 'day'

	      },

	      'grace': {

	        'intervalCount': 10,

	        'interval': 'day'

	      },

	      'maxLateFees': {

	        'type': 'fixed',

	        'value': '10'

	      }

	    },

	    'tipsConfiguration': {

	      'tipsPercentage': [

	        5,

	        10,

	        15

	      ],

	      'tipsEnabled': true

	    },

	    'invoiceNumberPrefix': 'INV-',

	    'paymentMethods': {

	      'stripe': {

	        'enableBankDebitOnly': false

	      }

	    },

	    'attachments': [

	      {

	        'id': '6241712be68f7a98102ba272',

	        'name': 'Electronics.pdf',

	        'url': 'https://example.com/digital-delivery',

	        'type': 'string',

	        'size': 10000

	      }

	    ],

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

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  }

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/invoices/',

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

	  'path': '/invoices/',

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

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  'url': 'https://services.leadconnectorhq.com/invoices/',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "name": "New Invoice",

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

	        "taxInclusive": true

	      }

	    ],

	    "discount": {

	      "value": 10,

	      "type": "percentage",

	      "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	    },

	    "termsNotes": "<p>This is a default terms.</p>",

	    "title": "INVOICE",

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

	    "invoiceNumber": "1001",

	    "issueDate": "2023-01-01",

	    "dueDate": "2023-01-14",

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

	    "liveMode": true,

	    "automaticTaxesEnabled": true,

	    "paymentSchedule": {

	      "type": "percentage",

	      "schedules": [

	        "string"

	      ]

	    },

	    "lateFeesConfiguration": {

	      "enable": true,

	      "value": 10,

	      "type": "fixed",

	      "frequency": {

	        "intervalCount": 10,

	        "interval": "day"

	      },

	      "grace": {

	        "intervalCount": 10,

	        "interval": "day"

	      },

	      "maxLateFees": {

	        "type": "fixed",

	        "value": "10"

	      }

	    },

	    "tipsConfiguration": {

	      "tipsPercentage": [

	        5,

	        10,

	        15

	      ],

	      "tipsEnabled": true

	    },

	    "invoiceNumberPrefix": "INV-",

	    "paymentMethods": {

	      "stripe": {

	        "enableBankDebitOnly": false

	      }

	    },

	    "attachments": [

	      {

	        "id": "6241712be68f7a98102ba272",

	        "name": "Electronics.pdf",

	        "url": "https://example.com/digital-delivery",

	        "type": "string",

	        "size": 10000

	      }

	    ],

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/invoices/')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "name": "New Invoice",

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

	        "taxInclusive": true

	      }

	    ],

	    "discount": {

	      "value": 10,

	      "type": "percentage",

	      "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	    },

	    "termsNotes": "<p>This is a default terms.</p>",

	    "title": "INVOICE",

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

	    "invoiceNumber": "1001",

	    "issueDate": "2023-01-01",

	    "dueDate": "2023-01-14",

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

	    "liveMode": true,

	    "automaticTaxesEnabled": true,

	    "paymentSchedule": {

	      "type": "percentage",

	      "schedules": [

	        "string"

	      ]

	    },

	    "lateFeesConfiguration": {

	      "enable": true,

	      "value": 10,

	      "type": "fixed",

	      "frequency": {

	        "intervalCount": 10,

	        "interval": "day"

	      },

	      "grace": {

	        "intervalCount": 10,

	        "interval": "day"

	      },

	      "maxLateFees": {

	        "type": "fixed",

	        "value": "10"

	      }

	    },

	    "tipsConfiguration": {

	      "tipsPercentage": [

	        5,

	        10,

	        15

	      ],

	      "tipsEnabled": true

	    },

	    "invoiceNumberPrefix": "INV-",

	    "paymentMethods": {

	      "stripe": {

	        "enableBankDebitOnly": false

	      }

	    },

	    "attachments": [

	      {

	        "id": "6241712be68f7a98102ba272",

	        "name": "Electronics.pdf",

	        "url": "https://example.com/digital-delivery",

	        "type": "string",

	        "size": 10000

	      }

	    ],

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

	  "name": "New Invoice",

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

	      "taxInclusive": True

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": True,

	  "automaticTaxesEnabled": True,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": True,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": True

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": False

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/invoices/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/invoices/"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "New Invoice",

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

	      "taxInclusive": True

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": True,

	  "automaticTaxesEnabled": True,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": True,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": True

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": False

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/invoices/',

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

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ \'6579751d56f60276e5bd4154\' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  }

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/invoices/', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/invoices/');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "name": "New Invoice",\n  "businessDetails": {\n    "logoUrl": "https://example.com/logo.png",\n    "name": "ABC Corp.",\n    "phoneNo": "+1-214-559-6993",\n    "address": "9931 Beechwood, TX",\n    "website": "wwww.example.com",\n    "customValues": [\n      "string"\n    ]\n  },\n  "currency": "USD",\n  "items": [\n    {\n      "name": "ABC Product",\n      "description": "ABC Corp.",\n      "productId": "6578278e879ad2646715ba9c",\n      "priceId": "6578278e879ad2646715ba9c",\n      "currency": "USD",\n      "amount": 999,\n      "qty": 1,\n      "taxes": [\n        {\n          "_id": "string",\n          "name": "string",\n          "rate": 0,\n          "calculation": "exclusive",\n          "description": "string",\n          "taxId": "string"\n        }\n      ],\n      "automaticTaxCategoryId": "6578278e879ad2646715ba9c",\n      "isSetupFeeItem": true,\n      "type": "one_time",\n      "taxInclusive": true\n    }\n  ],\n  "discount": {\n    "value": 10,\n    "type": "percentage",\n    "validOnProductIds": "[ \'6579751d56f60276e5bd4154\' ]"\n  },\n  "termsNotes": "<p>This is a default terms.</p>",\n  "title": "INVOICE",\n  "contactDetails": {\n    "id": "6578278e879ad2646715ba9c",\n    "name": "Alex",\n    "phoneNo": "+1234567890",\n    "email": "alex@example.com",\n    "additionalEmails": [\n      {\n        "email": "alex@example.com"\n      }\n    ],\n    "companyName": "ABC Corp.",\n    "address": {\n      "addressLine1": "9931 Beechwood",\n      "addressLine2": "Beechwood",\n      "city": "St. Houston",\n      "state": "TX",\n      "countryCode": "US",\n      "postalCode": "559-6993"\n    },\n    "customFields": [\n      "string"\n    ]\n  },\n  "invoiceNumber": "1001",\n  "issueDate": "2023-01-01",\n  "dueDate": "2023-01-14",\n  "sentTo": {\n    "email": [\n      "alex@example.com"\n    ],\n    "emailCc": [\n      "alex@example.com"\n    ],\n    "emailBcc": [\n      "alex@example.com"\n    ],\n    "phoneNo": [\n      "+1-214-559-6993"\n    ]\n  },\n  "liveMode": true,\n  "automaticTaxesEnabled": true,\n  "paymentSchedule": {\n    "type": "percentage",\n    "schedules": [\n      "string"\n    ]\n  },\n  "lateFeesConfiguration": {\n    "enable": true,\n    "value": 10,\n    "type": "fixed",\n    "frequency": {\n      "intervalCount": 10,\n      "interval": "day"\n    },\n    "grace": {\n      "intervalCount": 10,\n      "interval": "day"\n    },\n    "maxLateFees": {\n      "type": "fixed",\n      "value": "10"\n    }\n  },\n  "tipsConfiguration": {\n    "tipsPercentage": [\n      5,\n      10,\n      15\n    ],\n    "tipsEnabled": true\n  },\n  "invoiceNumberPrefix": "INV-",\n  "paymentMethods": {\n    "stripe": {\n      "enableBankDebitOnly": false\n    }\n  },\n  "attachments": [\n    {\n      "id": "6241712be68f7a98102ba272",\n      "name": "Electronics.pdf",\n      "url": "https://example.com/digital-delivery",\n      "type": "string",\n      "size": 10000\n    }\n  ],\n  "miscellaneousCharges": {\n    "charges": [\n      [\n        null\n      ]\n    ],\n    "collectedMiscellaneousCharges": 10,\n    "paidCharges": [\n      {\n        "name": "Processing Fee",\n        "charge": 10,\n        "amount": 10,\n        "_id": "673d01d7d547648a8dab6211"\n      }\n    ]\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/invoices/');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"name\": \"New Invoice\",\n  \"businessDetails\": {\n    \"logoUrl\": \"https://example.com/logo.png\",\n    \"name\": \"ABC Corp.\",\n    \"phoneNo\": \"+1-214-559-6993\",\n    \"address\": \"9931 Beechwood, TX\",\n    \"website\": \"wwww.example.com\",\n    \"customValues\": [\n      \"string\"\n    ]\n  },\n  \"currency\": \"USD\",\n  \"items\": [\n    {\n      \"name\": \"ABC Product\",\n      \"description\": \"ABC Corp.\",\n      \"productId\": \"6578278e879ad2646715ba9c\",\n      \"priceId\": \"6578278e879ad2646715ba9c\",\n      \"currency\": \"USD\",\n      \"amount\": 999,\n      \"qty\": 1,\n      \"taxes\": [\n        {\n          \"_id\": \"string\",\n          \"name\": \"string\",\n          \"rate\": 0,\n          \"calculation\": \"exclusive\",\n          \"description\": \"string\",\n          \"taxId\": \"string\"\n        }\n      ],\n      \"automaticTaxCategoryId\": \"6578278e879ad2646715ba9c\",\n      \"isSetupFeeItem\": true,\n      \"type\": \"one_time\",\n      \"taxInclusive\": true\n    }\n  ],\n  \"discount\": {\n    \"value\": 10,\n    \"type\": \"percentage\",\n    \"validOnProductIds\": \"[ '6579751d56f60276e5bd4154' ]\"\n  },\n  \"termsNotes\": \"<p>This is a default terms.</p>\",\n  \"title\": \"INVOICE\",\n  \"contactDetails\": {\n    \"id\": \"6578278e879ad2646715ba9c\",\n    \"name\": \"Alex\",\n    \"phoneNo\": \"+1234567890\",\n    \"email\": \"alex@example.com\",\n    \"additionalEmails\": [\n      {\n        \"email\": \"alex@example.com\"\n      }\n    ],\n    \"companyName\": \"ABC Corp.\",\n    \"address\": {\n      \"addressLine1\": \"9931 Beechwood\",\n      \"addressLine2\": \"Beechwood\",\n      \"city\": \"St. Houston\",\n      \"state\": \"TX\",\n      \"countryCode\": \"US\",\n      \"postalCode\": \"559-6993\"\n    },\n    \"customFields\": [\n      \"string\"\n    ]\n  },\n  \"invoiceNumber\": \"1001\",\n  \"issueDate\": \"2023-01-01\",\n  \"dueDate\": \"2023-01-14\",\n  \"sentTo\": {\n    \"email\": [\n      \"alex@example.com\"\n    ],\n    \"emailCc\": [\n      \"alex@example.com\"\n    ],\n    \"emailBcc\": [\n      \"alex@example.com\"\n    ],\n    \"phoneNo\": [\n      \"+1-214-559-6993\"\n    ]\n  },\n  \"liveMode\": true,\n  \"automaticTaxesEnabled\": true,\n  \"paymentSchedule\": {\n    \"type\": \"percentage\",\n    \"schedules\": [\n      \"string\"\n    ]\n  },\n  \"lateFeesConfiguration\": {\n    \"enable\": true,\n    \"value\": 10,\n    \"type\": \"fixed\",\n    \"frequency\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"grace\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"maxLateFees\": {\n      \"type\": \"fixed\",\n      \"value\": \"10\"\n    }\n  },\n  \"tipsConfiguration\": {\n    \"tipsPercentage\": [\n      5,\n      10,\n      15\n    ],\n    \"tipsEnabled\": true\n  },\n  \"invoiceNumberPrefix\": \"INV-\",\n  \"paymentMethods\": {\n    \"stripe\": {\n      \"enableBankDebitOnly\": false\n    }\n  },\n  \"attachments\": [\n    {\n      \"id\": \"6241712be68f7a98102ba272\",\n      \"name\": \"Electronics.pdf\",\n      \"url\": \"https://example.com/digital-delivery\",\n      \"type\": \"string\",\n      \"size\": 10000\n    }\n  ],\n  \"miscellaneousCharges\": {\n    \"charges\": [\n      [\n        null\n      ]\n    ],\n    \"collectedMiscellaneousCharges\": 10,\n    \"paidCharges\": [\n      {\n        \"name\": \"Processing Fee\",\n        \"charge\": 10,\n        \"amount\": 10,\n        \"_id\": \"673d01d7d547648a8dab6211\"\n      }\n    ]\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/invoices/")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/invoices/")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"name\": \"New Invoice\",\n  \"businessDetails\": {\n    \"logoUrl\": \"https://example.com/logo.png\",\n    \"name\": \"ABC Corp.\",\n    \"phoneNo\": \"+1-214-559-6993\",\n    \"address\": \"9931 Beechwood, TX\",\n    \"website\": \"wwww.example.com\",\n    \"customValues\": [\n      \"string\"\n    ]\n  },\n  \"currency\": \"USD\",\n  \"items\": [\n    {\n      \"name\": \"ABC Product\",\n      \"description\": \"ABC Corp.\",\n      \"productId\": \"6578278e879ad2646715ba9c\",\n      \"priceId\": \"6578278e879ad2646715ba9c\",\n      \"currency\": \"USD\",\n      \"amount\": 999,\n      \"qty\": 1,\n      \"taxes\": [\n        {\n          \"_id\": \"string\",\n          \"name\": \"string\",\n          \"rate\": 0,\n          \"calculation\": \"exclusive\",\n          \"description\": \"string\",\n          \"taxId\": \"string\"\n        }\n      ],\n      \"automaticTaxCategoryId\": \"6578278e879ad2646715ba9c\",\n      \"isSetupFeeItem\": true,\n      \"type\": \"one_time\",\n      \"taxInclusive\": true\n    }\n  ],\n  \"discount\": {\n    \"value\": 10,\n    \"type\": \"percentage\",\n    \"validOnProductIds\": \"[ '6579751d56f60276e5bd4154' ]\"\n  },\n  \"termsNotes\": \"<p>This is a default terms.</p>\",\n  \"title\": \"INVOICE\",\n  \"contactDetails\": {\n    \"id\": \"6578278e879ad2646715ba9c\",\n    \"name\": \"Alex\",\n    \"phoneNo\": \"+1234567890\",\n    \"email\": \"alex@example.com\",\n    \"additionalEmails\": [\n      {\n        \"email\": \"alex@example.com\"\n      }\n    ],\n    \"companyName\": \"ABC Corp.\",\n    \"address\": {\n      \"addressLine1\": \"9931 Beechwood\",\n      \"addressLine2\": \"Beechwood\",\n      \"city\": \"St. Houston\",\n      \"state\": \"TX\",\n      \"countryCode\": \"US\",\n      \"postalCode\": \"559-6993\"\n    },\n    \"customFields\": [\n      \"string\"\n    ]\n  },\n  \"invoiceNumber\": \"1001\",\n  \"issueDate\": \"2023-01-01\",\n  \"dueDate\": \"2023-01-14\",\n  \"sentTo\": {\n    \"email\": [\n      \"alex@example.com\"\n    ],\n    \"emailCc\": [\n      \"alex@example.com\"\n    ],\n    \"emailBcc\": [\n      \"alex@example.com\"\n    ],\n    \"phoneNo\": [\n      \"+1-214-559-6993\"\n    ]\n  },\n  \"liveMode\": true,\n  \"automaticTaxesEnabled\": true,\n  \"paymentSchedule\": {\n    \"type\": \"percentage\",\n    \"schedules\": [\n      \"string\"\n    ]\n  },\n  \"lateFeesConfiguration\": {\n    \"enable\": true,\n    \"value\": 10,\n    \"type\": \"fixed\",\n    \"frequency\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"grace\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"maxLateFees\": {\n      \"type\": \"fixed\",\n      \"value\": \"10\"\n    }\n  },\n  \"tipsConfiguration\": {\n    \"tipsPercentage\": [\n      5,\n      10,\n      15\n    ],\n    \"tipsEnabled\": true\n  },\n  \"invoiceNumberPrefix\": \"INV-\",\n  \"paymentMethods\": {\n    \"stripe\": {\n      \"enableBankDebitOnly\": false\n    }\n  },\n  \"attachments\": [\n    {\n      \"id\": \"6241712be68f7a98102ba272\",\n      \"name\": \"Electronics.pdf\",\n      \"url\": \"https://example.com/digital-delivery\",\n      \"type\": \"string\",\n      \"size\": 10000\n    }\n  ],\n  \"miscellaneousCharges\": {\n    \"charges\": [\n      [\n        null\n      ]\n    ],\n    \"collectedMiscellaneousCharges\": 10,\n    \"paidCharges\": [\n      {\n        \"name\": \"Processing Fee\",\n        \"charge\": 10,\n        \"amount\": 10,\n        \"_id\": \"673d01d7d547648a8dab6211\"\n      }\n    ]\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/invoices/"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	

	url = URI("https://services.leadconnectorhq.com/invoices/")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "name": "New Invoice",

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

	      "taxInclusive": true

	    }

	  ],

	  "discount": {

	    "value": 10,

	    "type": "percentage",

	    "validOnProductIds": "[ '6579751d56f60276e5bd4154' ]"

	  },

	  "termsNotes": "<p>This is a default terms.</p>",

	  "title": "INVOICE",

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

	  "invoiceNumber": "1001",

	  "issueDate": "2023-01-01",

	  "dueDate": "2023-01-14",

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

	  "liveMode": true,

	  "automaticTaxesEnabled": true,

	  "paymentSchedule": {

	    "type": "percentage",

	    "schedules": [

	      "string"

	    ]

	  },

	  "lateFeesConfiguration": {

	    "enable": true,

	    "value": 10,

	    "type": "fixed",

	    "frequency": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "grace": {

	      "intervalCount": 10,

	      "interval": "day"

	    },

	    "maxLateFees": {

	      "type": "fixed",

	      "value": "10"

	    }

	  },

	  "tipsConfiguration": {

	    "tipsPercentage": [

	      5,

	      10,

	      15

	    ],

	    "tipsEnabled": true

	  },

	  "invoiceNumberPrefix": "INV-",

	  "paymentMethods": {

	    "stripe": {

	      "enableBankDebitOnly": false

	    }

	  },

	  "attachments": [

	    {

	      "id": "6241712be68f7a98102ba272",

	      "name": "Electronics.pdf",

	      "url": "https://example.com/digital-delivery",

	      "type": "string",

	      "size": 10000

	    }

	  ],

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

	  `"name`": `"New Invoice`",

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

	      `"taxInclusive`": true

	    }

	  ],

	  `"discount`": {

	    `"value`": 10,

	    `"type`": `"percentage`",

	    `"validOnProductIds`": `"[ '6579751d56f60276e5bd4154' ]`"

	  },

	  `"termsNotes`": `"<p>This is a default terms.</p>`",

	  `"title`": `"INVOICE`",

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

	  `"invoiceNumber`": `"1001`",

	  `"issueDate`": `"2023-01-01`",

	  `"dueDate`": `"2023-01-14`",

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

	  `"liveMode`": true,

	  `"automaticTaxesEnabled`": true,

	  `"paymentSchedule`": {

	    `"type`": `"percentage`",

	    `"schedules`": [

	      `"string`"

	    ]

	  },

	  `"lateFeesConfiguration`": {

	    `"enable`": true,

	    `"value`": 10,

	    `"type`": `"fixed`",

	    `"frequency`": {

	      `"intervalCount`": 10,

	      `"interval`": `"day`"

	    },

	    `"grace`": {

	      `"intervalCount`": 10,

	      `"interval`": `"day`"

	    },

	    `"maxLateFees`": {

	      `"type`": `"fixed`",

	      `"value`": `"10`"

	    }

	  },

	  `"tipsConfiguration`": {

	    `"tipsPercentage`": [

	      5,

	      10,

	      15

	    ],

	    `"tipsEnabled`": true

	  },

	  `"invoiceNumberPrefix`": `"INV-`",

	  `"paymentMethods`": {

	    `"stripe`": {

	      `"enableBankDebitOnly`": false

	    }

	  },

	  `"attachments`": [

	    {

	      `"id`": `"6241712be68f7a98102ba272`",

	      `"name`": `"Electronics.pdf`",

	      `"url`": `"https://example.com/digital-delivery`",

	      `"type`": `"string`",

	      `"size`": 10000

	    }

	  ],

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

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

