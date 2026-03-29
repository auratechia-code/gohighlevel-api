# Update Product by ID

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/products/:productId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: products.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `productId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "_id": "655b33a82209e60b6adb87a5",
  "description": "This is a really awesome product",
  "variants": [
    {
      "id": "38s63qmxfr4",
      "name": "Size",
      "options": [
        {
          "id": "h4z7u0im2q8",
          "name": "XL"
        }
      ]
    }
  ],
  "locationId": "3SwdhCsvxI8Au3KsPJt6",
  "name": "Awesome Product",
  "productType": "PHYSICAL",
  "availableInStore": true,
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "statementDescriptor": "abcde",
  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",
  "collectionIds": [
    "65d71377c326ea78e1c47df5",
    "65d71377c326ea78e1c47d34"
  ],
  "isTaxesEnabled": true,
  "taxes": [
    "654492a4e6bef380114de15a"
  ],
  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",
  "label": {
    "title": "Featured",
    "startDate": "2024-06-26T05:43:35.000Z",
    "endDate": "2024-06-30T05:43:39.000Z"
  },
  "slug": "washing-machine"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/products/:productId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

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

	  const response = await highLevel.products.updateProductById({

	    'productId': '6578278e879ad2646715ba9c'

	  },

	  {

	    'name': 'Awesome Product',

	    'locationId': '3SwdhCsvxI8Au3KsPJt6',

	    'description': 'Product description goes here.',

	    'productType': 'DIGITAL',

	    'image': 'https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png',

	    'statementDescriptor': 'abcde',

	    'availableInStore': true,

	    'medias': [

	      {

	        'id': 'fzrgusiuu0m',

	        'title': '1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png',

	        'url': 'https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png',

	        'type': 'image',

	        'isFeatured': true,

	        'priceIds': '6578278e879ad2646715ba9c'

	      }

	    ],

	    'variants': [

	      {

	        'id': '38s63qmxfr4',

	        'name': 'Size',

	        'options': [

	          {

	            'id': 'h4z7u0im2q8',

	            'name': 'XL'

	          }

	        ]

	      }

	    ],

	    'collectionIds': [

	      '65d71377c326ea78e1c47df5',

	      '65d71377c326ea78e1c47d34'

	    ],

	    'isTaxesEnabled': true,

	    'taxes': [

	      '654492a4e6bef380114de15a'

	    ],

	    'automaticTaxCategoryId': '65d71377c326ea78e1c47df5',

	    'isLabelEnabled': true,

	    'label': {

	      'title': 'Featured',

	      'startDate': '2024-06-26T05:43:35.000Z',

	      'endDate': '2024-06-30T05:43:39.000Z'

	    },

	    'slug': 'awesome-product',

	    'seo': {

	      'title': 'Best Product - Buy Now',

	      'description': 'This is the best product you can buy online with amazing features and great value'

	    },

	    'taxInclusive': true,

	    'prices': [

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

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

	    "string"

	  ]

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/products/:productId',

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

	  'path': '/products/:productId',

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

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

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

	  'url': 'https://services.leadconnectorhq.com/products/:productId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "name": "Awesome Product",

	    "locationId": "3SwdhCsvxI8Au3KsPJt6",

	    "description": "Product description goes here.",

	    "productType": "DIGITAL",

	    "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	    "statementDescriptor": "abcde",

	    "availableInStore": true,

	    "medias": [

	      {

	        "id": "fzrgusiuu0m",

	        "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	        "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	        "type": "image",

	        "isFeatured": true,

	        "priceIds": "6578278e879ad2646715ba9c"

	      }

	    ],

	    "variants": [

	      {

	        "id": "38s63qmxfr4",

	        "name": "Size",

	        "options": [

	          {

	            "id": "h4z7u0im2q8",

	            "name": "XL"

	          }

	        ]

	      }

	    ],

	    "collectionIds": [

	      "65d71377c326ea78e1c47df5",

	      "65d71377c326ea78e1c47d34"

	    ],

	    "isTaxesEnabled": true,

	    "taxes": [

	      "654492a4e6bef380114de15a"

	    ],

	    "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	    "isLabelEnabled": true,

	    "label": {

	      "title": "Featured",

	      "startDate": "2024-06-26T05:43:35.000Z",

	      "endDate": "2024-06-30T05:43:39.000Z"

	    },

	    "slug": "awesome-product",

	    "seo": {

	      "title": "Best Product - Buy Now",

	      "description": "This is the best product you can buy online with amazing features and great value"

	    },

	    "taxInclusive": true,

	    "prices": [

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/products/:productId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "name": "Awesome Product",

	    "locationId": "3SwdhCsvxI8Au3KsPJt6",

	    "description": "Product description goes here.",

	    "productType": "DIGITAL",

	    "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	    "statementDescriptor": "abcde",

	    "availableInStore": true,

	    "medias": [

	      {

	        "id": "fzrgusiuu0m",

	        "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	        "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	        "type": "image",

	        "isFeatured": true,

	        "priceIds": "6578278e879ad2646715ba9c"

	      }

	    ],

	    "variants": [

	      {

	        "id": "38s63qmxfr4",

	        "name": "Size",

	        "options": [

	          {

	            "id": "h4z7u0im2q8",

	            "name": "XL"

	          }

	        ]

	      }

	    ],

	    "collectionIds": [

	      "65d71377c326ea78e1c47df5",

	      "65d71377c326ea78e1c47d34"

	    ],

	    "isTaxesEnabled": true,

	    "taxes": [

	      "654492a4e6bef380114de15a"

	    ],

	    "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	    "isLabelEnabled": true,

	    "label": {

	      "title": "Featured",

	      "startDate": "2024-06-26T05:43:35.000Z",

	      "endDate": "2024-06-30T05:43:39.000Z"

	    },

	    "slug": "awesome-product",

	    "seo": {

	      "title": "Best Product - Buy Now",

	      "description": "This is the best product you can buy online with amazing features and great value"

	    },

	    "taxInclusive": true,

	    "prices": [

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

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": True,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": True,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": True,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": True,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": True,

	  "prices": [

	    "string"

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/products/:productId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/products/:productId"

	

	payload = json.dumps({

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": True,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": True,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": True,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": True,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": True,

	  "prices": [

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/products/:productId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

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

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

	    "string"

	  ]

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/products/:productId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/products/:productId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "name": "Awesome Product",\n  "locationId": "3SwdhCsvxI8Au3KsPJt6",\n  "description": "Product description goes here.",\n  "productType": "DIGITAL",\n  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",\n  "statementDescriptor": "abcde",\n  "availableInStore": true,\n  "medias": [\n    {\n      "id": "fzrgusiuu0m",\n      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",\n      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",\n      "type": "image",\n      "isFeatured": true,\n      "priceIds": "6578278e879ad2646715ba9c"\n    }\n  ],\n  "variants": [\n    {\n      "id": "38s63qmxfr4",\n      "name": "Size",\n      "options": [\n        {\n          "id": "h4z7u0im2q8",\n          "name": "XL"\n        }\n      ]\n    }\n  ],\n  "collectionIds": [\n    "65d71377c326ea78e1c47df5",\n    "65d71377c326ea78e1c47d34"\n  ],\n  "isTaxesEnabled": true,\n  "taxes": [\n    "654492a4e6bef380114de15a"\n  ],\n  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",\n  "isLabelEnabled": true,\n  "label": {\n    "title": "Featured",\n    "startDate": "2024-06-26T05:43:35.000Z",\n    "endDate": "2024-06-30T05:43:39.000Z"\n  },\n  "slug": "awesome-product",\n  "seo": {\n    "title": "Best Product - Buy Now",\n    "description": "This is the best product you can buy online with amazing features and great value"\n  },\n  "taxInclusive": true,\n  "prices": [\n    "string"\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/products/:productId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Awesome Product\",\n  \"locationId\": \"3SwdhCsvxI8Au3KsPJt6\",\n  \"description\": \"Product description goes here.\",\n  \"productType\": \"DIGITAL\",\n  \"image\": \"https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png\",\n  \"statementDescriptor\": \"abcde\",\n  \"availableInStore\": true,\n  \"medias\": [\n    {\n      \"id\": \"fzrgusiuu0m\",\n      \"title\": \"1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png\",\n      \"url\": \"https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png\",\n      \"type\": \"image\",\n      \"isFeatured\": true,\n      \"priceIds\": \"6578278e879ad2646715ba9c\"\n    }\n  ],\n  \"variants\": [\n    {\n      \"id\": \"38s63qmxfr4\",\n      \"name\": \"Size\",\n      \"options\": [\n        {\n          \"id\": \"h4z7u0im2q8\",\n          \"name\": \"XL\"\n        }\n      ]\n    }\n  ],\n  \"collectionIds\": [\n    \"65d71377c326ea78e1c47df5\",\n    \"65d71377c326ea78e1c47d34\"\n  ],\n  \"isTaxesEnabled\": true,\n  \"taxes\": [\n    \"654492a4e6bef380114de15a\"\n  ],\n  \"automaticTaxCategoryId\": \"65d71377c326ea78e1c47df5\",\n  \"isLabelEnabled\": true,\n  \"label\": {\n    \"title\": \"Featured\",\n    \"startDate\": \"2024-06-26T05:43:35.000Z\",\n    \"endDate\": \"2024-06-30T05:43:39.000Z\"\n  },\n  \"slug\": \"awesome-product\",\n  \"seo\": {\n    \"title\": \"Best Product - Buy Now\",\n    \"description\": \"This is the best product you can buy online with amazing features and great value\"\n  },\n  \"taxInclusive\": true,\n  \"prices\": [\n    \"string\"\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/products/:productId")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/products/:productId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"name\": \"Awesome Product\",\n  \"locationId\": \"3SwdhCsvxI8Au3KsPJt6\",\n  \"description\": \"Product description goes here.\",\n  \"productType\": \"DIGITAL\",\n  \"image\": \"https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png\",\n  \"statementDescriptor\": \"abcde\",\n  \"availableInStore\": true,\n  \"medias\": [\n    {\n      \"id\": \"fzrgusiuu0m\",\n      \"title\": \"1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png\",\n      \"url\": \"https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png\",\n      \"type\": \"image\",\n      \"isFeatured\": true,\n      \"priceIds\": \"6578278e879ad2646715ba9c\"\n    }\n  ],\n  \"variants\": [\n    {\n      \"id\": \"38s63qmxfr4\",\n      \"name\": \"Size\",\n      \"options\": [\n        {\n          \"id\": \"h4z7u0im2q8\",\n          \"name\": \"XL\"\n        }\n      ]\n    }\n  ],\n  \"collectionIds\": [\n    \"65d71377c326ea78e1c47df5\",\n    \"65d71377c326ea78e1c47d34\"\n  ],\n  \"isTaxesEnabled\": true,\n  \"taxes\": [\n    \"654492a4e6bef380114de15a\"\n  ],\n  \"automaticTaxCategoryId\": \"65d71377c326ea78e1c47df5\",\n  \"isLabelEnabled\": true,\n  \"label\": {\n    \"title\": \"Featured\",\n    \"startDate\": \"2024-06-26T05:43:35.000Z\",\n    \"endDate\": \"2024-06-30T05:43:39.000Z\"\n  },\n  \"slug\": \"awesome-product\",\n  \"seo\": {\n    \"title\": \"Best Product - Buy Now\",\n    \"description\": \"This is the best product you can buy online with amazing features and great value\"\n  },\n  \"taxInclusive\": true,\n  \"prices\": [\n    \"string\"\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/products/:productId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

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

	

	url = URI("https://services.leadconnectorhq.com/products/:productId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "name": "Awesome Product",

	  "locationId": "3SwdhCsvxI8Au3KsPJt6",

	  "description": "Product description goes here.",

	  "productType": "DIGITAL",

	  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",

	  "statementDescriptor": "abcde",

	  "availableInStore": true,

	  "medias": [

	    {

	      "id": "fzrgusiuu0m",

	      "title": "1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png",

	      "url": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png",

	      "type": "image",

	      "isFeatured": true,

	      "priceIds": "6578278e879ad2646715ba9c"

	    }

	  ],

	  "variants": [

	    {

	      "id": "38s63qmxfr4",

	      "name": "Size",

	      "options": [

	        {

	          "id": "h4z7u0im2q8",

	          "name": "XL"

	        }

	      ]

	    }

	  ],

	  "collectionIds": [

	    "65d71377c326ea78e1c47df5",

	    "65d71377c326ea78e1c47d34"

	  ],

	  "isTaxesEnabled": true,

	  "taxes": [

	    "654492a4e6bef380114de15a"

	  ],

	  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",

	  "isLabelEnabled": true,

	  "label": {

	    "title": "Featured",

	    "startDate": "2024-06-26T05:43:35.000Z",

	    "endDate": "2024-06-30T05:43:39.000Z"

	  },

	  "slug": "awesome-product",

	  "seo": {

	    "title": "Best Product - Buy Now",

	    "description": "This is the best product you can buy online with amazing features and great value"

	  },

	  "taxInclusive": true,

	  "prices": [

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

	  `"name`": `"Awesome Product`",

	  `"locationId`": `"3SwdhCsvxI8Au3KsPJt6`",

	  `"description`": `"Product description goes here.`",

	  `"productType`": `"DIGITAL`",

	  `"image`": `"https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png`",

	  `"statementDescriptor`": `"abcde`",

	  `"availableInStore`": true,

	  `"medias`": [

	    {

	      `"id`": `"fzrgusiuu0m`",

	      `"title`": `"1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png`",

	      `"url`": `"https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png`",

	      `"type`": `"image`",

	      `"isFeatured`": true,

	      `"priceIds`": `"6578278e879ad2646715ba9c`"

	    }

	  ],

	  `"variants`": [

	    {

	      `"id`": `"38s63qmxfr4`",

	      `"name`": `"Size`",

	      `"options`": [

	        {

	          `"id`": `"h4z7u0im2q8`",

	          `"name`": `"XL`"

	        }

	      ]

	    }

	  ],

	  `"collectionIds`": [

	    `"65d71377c326ea78e1c47df5`",

	    `"65d71377c326ea78e1c47d34`"

	  ],

	  `"isTaxesEnabled`": true,

	  `"taxes`": [

	    `"654492a4e6bef380114de15a`"

	  ],

	  `"automaticTaxCategoryId`": `"65d71377c326ea78e1c47df5`",

	  `"isLabelEnabled`": true,

	  `"label`": {

	    `"title`": `"Featured`",

	    `"startDate`": `"2024-06-26T05:43:35.000Z`",

	    `"endDate`": `"2024-06-30T05:43:39.000Z`"

	  },

	  `"slug`": `"awesome-product`",

	  `"seo`": {

	    `"title`": `"Best Product - Buy Now`",

	    `"description`": `"This is the best product you can buy online with amazing features and great value`"

	  },

	  `"taxInclusive`": true,

	  `"prices`": [

	    `"string`"

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/:productId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

