# Update Price by ID for a Product

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/products/:productId/price/:priceId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: products/prices.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `productId` | ✅ | priceId string required ID of the price that needs to be returned Example: 6578278e879ad2646715ba9c |
| `priceId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "_id": "655b33aa2209e60b6adb87a7",
  "membershipOffers": [
    {
      "label": "top_50",
      "value": "50",
      "_id": "655b33aa2209e60b6adb87a7"
    }
  ],
  "variantOptionIds": [
    "h4z7u0im2q8",
    "h3nst2ltsnn"
  ],
  "locationId": "3SwdhCsvxI8Au3KsPJt6",
  "product": "655b33a82209e60b6adb87a5",
  "userId": "6YAtzfzpmHAdj0e8GkKp",
  "name": "Red / S",
  "type": "one_time",
  "currency": "INR",
  "amount": 199999,
  "recurring": {
    "interval": "day",
    "intervalCount": 1
  },
  "createdAt": "2023-11-20T10:23:38.645Z",
  "updatedAt": "2024-01-23T09:57:04.852Z",
  "compareAtPrice": 2000000,
  "trackInventory": null,
  "availableQuantity": 5,
  "allowOutOfStockPurchases": true
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/products/:productId/price/:priceId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

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

	  const response = await highLevel.products.updatePriceByIdForProduct({

	    'productId': '6578278e879ad2646715ba9c',

	    'priceId': '6578278e879ad2646715ba9c'

	  },

	  {

	    'name': 'Price Name',

	    'type': 'one_time',

	    'currency': 'USD',

	    'amount': 99.99,

	    'recurring': {

	      'interval': 'day',

	      'intervalCount': 1

	    },

	    'description': 'string',

	    'membershipOffers': [

	      {

	        'label': 'top_50',

	        'value': '50',

	        '_id': '655b33aa2209e60b6adb87a7'

	      }

	    ],

	    'trialPeriod': 7,

	    'totalCycles': 12,

	    'setupFee': 10.99,

	    'variantOptionIds': [

	      'option_id_1',

	      'option_id_2'

	    ],

	    'compareAtPrice': 19.99,

	    'locationId': '6578278e879ad2646715ba9c',

	    'userId': '6578278e879ad2646715ba9c',

	    'meta': {

	      'source': 'stripe',

	      'sourceId': '123',

	      'stripePriceId': 'price_123',

	      'internalSource': 'agency_plan'

	    },

	    'trackInventory': true,

	    'availableQuantity': 5,

	    'allowOutOfStockPurchases': true,

	    'sku': 'sku_123',

	    'shippingOptions': {

	      'weight': {

	        'value': 10,

	        'unit': 'kg'

	      },

	      'dimensions': {

	        'height': 10,

	        'width': 10,

	        'length': 10,

	        'unit': 'cm'

	      }

	    },

	    'isDigitalProduct': true,

	    'digitalDelivery': [

	      'string'

	    ]

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

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/products/:productId/price/:priceId',

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

	  'path': '/products/:productId/price/:priceId',

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

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/products/:productId/price/:priceId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "name": "Price Name",

	    "type": "one_time",

	    "currency": "USD",

	    "amount": 99.99,

	    "recurring": {

	      "interval": "day",

	      "intervalCount": 1

	    },

	    "description": "string",

	    "membershipOffers": [

	      {

	        "label": "top_50",

	        "value": "50",

	        "_id": "655b33aa2209e60b6adb87a7"

	      }

	    ],

	    "trialPeriod": 7,

	    "totalCycles": 12,

	    "setupFee": 10.99,

	    "variantOptionIds": [

	      "option_id_1",

	      "option_id_2"

	    ],

	    "compareAtPrice": 19.99,

	    "locationId": "6578278e879ad2646715ba9c",

	    "userId": "6578278e879ad2646715ba9c",

	    "meta": {

	      "source": "stripe",

	      "sourceId": "123",

	      "stripePriceId": "price_123",

	      "internalSource": "agency_plan"

	    },

	    "trackInventory": true,

	    "availableQuantity": 5,

	    "allowOutOfStockPurchases": true,

	    "sku": "sku_123",

	    "shippingOptions": {

	      "weight": {

	        "value": 10,

	        "unit": "kg"

	      },

	      "dimensions": {

	        "height": 10,

	        "width": 10,

	        "length": 10,

	        "unit": "cm"

	      }

	    },

	    "isDigitalProduct": true,

	    "digitalDelivery": [

	      "string"

	    ]

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/products/:productId/price/:priceId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "name": "Price Name",

	    "type": "one_time",

	    "currency": "USD",

	    "amount": 99.99,

	    "recurring": {

	      "interval": "day",

	      "intervalCount": 1

	    },

	    "description": "string",

	    "membershipOffers": [

	      {

	        "label": "top_50",

	        "value": "50",

	        "_id": "655b33aa2209e60b6adb87a7"

	      }

	    ],

	    "trialPeriod": 7,

	    "totalCycles": 12,

	    "setupFee": 10.99,

	    "variantOptionIds": [

	      "option_id_1",

	      "option_id_2"

	    ],

	    "compareAtPrice": 19.99,

	    "locationId": "6578278e879ad2646715ba9c",

	    "userId": "6578278e879ad2646715ba9c",

	    "meta": {

	      "source": "stripe",

	      "sourceId": "123",

	      "stripePriceId": "price_123",

	      "internalSource": "agency_plan"

	    },

	    "trackInventory": true,

	    "availableQuantity": 5,

	    "allowOutOfStockPurchases": true,

	    "sku": "sku_123",

	    "shippingOptions": {

	      "weight": {

	        "value": 10,

	        "unit": "kg"

	      },

	      "dimensions": {

	        "height": 10,

	        "width": 10,

	        "length": 10,

	        "unit": "cm"

	      }

	    },

	    "isDigitalProduct": true,

	    "digitalDelivery": [

	      "string"

	    ]

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

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": True,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": True,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": True,

	  "digitalDelivery": [

	    "string"

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/products/:productId/price/:priceId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/products/:productId/price/:priceId"

	

	payload = json.dumps({

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": True,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": True,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": True,

	  "digitalDelivery": [

	    "string"

	  ]

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/products/:productId/price/:priceId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

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

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/products/:productId/price/:priceId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/products/:productId/price/:priceId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "name": "Price Name",\n  "type": "one_time",\n  "currency": "USD",\n  "amount": 99.99,\n  "recurring": {\n    "interval": "day",\n    "intervalCount": 1\n  },\n  "description": "string",\n  "membershipOffers": [\n    {\n      "label": "top_50",\n      "value": "50",\n      "_id": "655b33aa2209e60b6adb87a7"\n    }\n  ],\n  "trialPeriod": 7,\n  "totalCycles": 12,\n  "setupFee": 10.99,\n  "variantOptionIds": [\n    "option_id_1",\n    "option_id_2"\n  ],\n  "compareAtPrice": 19.99,\n  "locationId": "6578278e879ad2646715ba9c",\n  "userId": "6578278e879ad2646715ba9c",\n  "meta": {\n    "source": "stripe",\n    "sourceId": "123",\n    "stripePriceId": "price_123",\n    "internalSource": "agency_plan"\n  },\n  "trackInventory": true,\n  "availableQuantity": 5,\n  "allowOutOfStockPurchases": true,\n  "sku": "sku_123",\n  "shippingOptions": {\n    "weight": {\n      "value": 10,\n      "unit": "kg"\n    },\n    "dimensions": {\n      "height": 10,\n      "width": 10,\n      "length": 10,\n      "unit": "cm"\n    }\n  },\n  "isDigitalProduct": true,\n  "digitalDelivery": [\n    "string"\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/products/:productId/price/:priceId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Price Name\",\n  \"type\": \"one_time\",\n  \"currency\": \"USD\",\n  \"amount\": 99.99,\n  \"recurring\": {\n    \"interval\": \"day\",\n    \"intervalCount\": 1\n  },\n  \"description\": \"string\",\n  \"membershipOffers\": [\n    {\n      \"label\": \"top_50\",\n      \"value\": \"50\",\n      \"_id\": \"655b33aa2209e60b6adb87a7\"\n    }\n  ],\n  \"trialPeriod\": 7,\n  \"totalCycles\": 12,\n  \"setupFee\": 10.99,\n  \"variantOptionIds\": [\n    \"option_id_1\",\n    \"option_id_2\"\n  ],\n  \"compareAtPrice\": 19.99,\n  \"locationId\": \"6578278e879ad2646715ba9c\",\n  \"userId\": \"6578278e879ad2646715ba9c\",\n  \"meta\": {\n    \"source\": \"stripe\",\n    \"sourceId\": \"123\",\n    \"stripePriceId\": \"price_123\",\n    \"internalSource\": \"agency_plan\"\n  },\n  \"trackInventory\": true,\n  \"availableQuantity\": 5,\n  \"allowOutOfStockPurchases\": true,\n  \"sku\": \"sku_123\",\n  \"shippingOptions\": {\n    \"weight\": {\n      \"value\": 10,\n      \"unit\": \"kg\"\n    },\n    \"dimensions\": {\n      \"height\": 10,\n      \"width\": 10,\n      \"length\": 10,\n      \"unit\": \"cm\"\n    }\n  },\n  \"isDigitalProduct\": true,\n  \"digitalDelivery\": [\n    \"string\"\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/products/:productId/price/:priceId")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/products/:productId/price/:priceId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"name\": \"Price Name\",\n  \"type\": \"one_time\",\n  \"currency\": \"USD\",\n  \"amount\": 99.99,\n  \"recurring\": {\n    \"interval\": \"day\",\n    \"intervalCount\": 1\n  },\n  \"description\": \"string\",\n  \"membershipOffers\": [\n    {\n      \"label\": \"top_50\",\n      \"value\": \"50\",\n      \"_id\": \"655b33aa2209e60b6adb87a7\"\n    }\n  ],\n  \"trialPeriod\": 7,\n  \"totalCycles\": 12,\n  \"setupFee\": 10.99,\n  \"variantOptionIds\": [\n    \"option_id_1\",\n    \"option_id_2\"\n  ],\n  \"compareAtPrice\": 19.99,\n  \"locationId\": \"6578278e879ad2646715ba9c\",\n  \"userId\": \"6578278e879ad2646715ba9c\",\n  \"meta\": {\n    \"source\": \"stripe\",\n    \"sourceId\": \"123\",\n    \"stripePriceId\": \"price_123\",\n    \"internalSource\": \"agency_plan\"\n  },\n  \"trackInventory\": true,\n  \"availableQuantity\": 5,\n  \"allowOutOfStockPurchases\": true,\n  \"sku\": \"sku_123\",\n  \"shippingOptions\": {\n    \"weight\": {\n      \"value\": 10,\n      \"unit\": \"kg\"\n    },\n    \"dimensions\": {\n      \"height\": 10,\n      \"width\": 10,\n      \"length\": 10,\n      \"unit\": \"cm\"\n    }\n  },\n  \"isDigitalProduct\": true,\n  \"digitalDelivery\": [\n    \"string\"\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/products/:productId/price/:priceId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

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

	

	url = URI("https://services.leadconnectorhq.com/products/:productId/price/:priceId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "name": "Price Name",

	  "type": "one_time",

	  "currency": "USD",

	  "amount": 99.99,

	  "recurring": {

	    "interval": "day",

	    "intervalCount": 1

	  },

	  "description": "string",

	  "membershipOffers": [

	    {

	      "label": "top_50",

	      "value": "50",

	      "_id": "655b33aa2209e60b6adb87a7"

	    }

	  ],

	  "trialPeriod": 7,

	  "totalCycles": 12,

	  "setupFee": 10.99,

	  "variantOptionIds": [

	    "option_id_1",

	    "option_id_2"

	  ],

	  "compareAtPrice": 19.99,

	  "locationId": "6578278e879ad2646715ba9c",

	  "userId": "6578278e879ad2646715ba9c",

	  "meta": {

	    "source": "stripe",

	    "sourceId": "123",

	    "stripePriceId": "price_123",

	    "internalSource": "agency_plan"

	  },

	  "trackInventory": true,

	  "availableQuantity": 5,

	  "allowOutOfStockPurchases": true,

	  "sku": "sku_123",

	  "shippingOptions": {

	    "weight": {

	      "value": 10,

	      "unit": "kg"

	    },

	    "dimensions": {

	      "height": 10,

	      "width": 10,

	      "length": 10,

	      "unit": "cm"

	    }

	  },

	  "isDigitalProduct": true,

	  "digitalDelivery": [

	    "string"

	  ]

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

	  `"name`": `"Price Name`",

	  `"type`": `"one_time`",

	  `"currency`": `"USD`",

	  `"amount`": 99.99,

	  `"recurring`": {

	    `"interval`": `"day`",

	    `"intervalCount`": 1

	  },

	  `"description`": `"string`",

	  `"membershipOffers`": [

	    {

	      `"label`": `"top_50`",

	      `"value`": `"50`",

	      `"_id`": `"655b33aa2209e60b6adb87a7`"

	    }

	  ],

	  `"trialPeriod`": 7,

	  `"totalCycles`": 12,

	  `"setupFee`": 10.99,

	  `"variantOptionIds`": [

	    `"option_id_1`",

	    `"option_id_2`"

	  ],

	  `"compareAtPrice`": 19.99,

	  `"locationId`": `"6578278e879ad2646715ba9c`",

	  `"userId`": `"6578278e879ad2646715ba9c`",

	  `"meta`": {

	    `"source`": `"stripe`",

	    `"sourceId`": `"123`",

	    `"stripePriceId`": `"price_123`",

	    `"internalSource`": `"agency_plan`"

	  },

	  `"trackInventory`": true,

	  `"availableQuantity`": 5,

	  `"allowOutOfStockPurchases`": true,

	  `"sku`": `"sku_123`",

	  `"shippingOptions`": {

	    `"weight`": {

	      `"value`": 10,

	      `"unit`": `"kg`"

	    },

	    `"dimensions`": {

	      `"height`": 10,

	      `"width`": 10,

	      `"length`": 10,

	      `"unit`": `"cm`"

	    }

	  },

	  `"isDigitalProduct`": true,

	  `"digitalDelivery`": [

	    `"string`"

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/:productId/price/:priceId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

