# Bulk Edit Products and Prices

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/products/bulk-update/edit`

## 🔐 Requirements
```text
N/A
```

## 📥 Parameters
### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "message": "Products updated successfully",
  "status": true,
  "updatedCount": 5
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "message": "Products updated successfully",  "status": true,  "updatedCount": 5}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "message": "Products updated successfully",  "status": true,  "updatedCount": 5}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "message": "Products updated successfully",  "status": true,  "updatedCount": 5}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/products/bulk-update/edit' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-d '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

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

	  const response = await highLevel.products.bulkEdit({

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'products': [

	      {

	        '_id': '64a1b2c3d4e5f67890123456',

	        'name': 'Premium Product',

	        'description': 'A high-quality premium product with excellent features and durability',

	        'image': 'https://example.com/product-image.jpg',

	        'availableInStore': true,

	        'prices': [

	          {

	            '_id': '64a1b2c3d4e5f67890123456',

	            'name': 'Standard Plan',

	            'amount': 99.99,

	            'currency': 'USD',

	            'compareAtPrice': 129.99,

	            'availableQuantity': 100,

	            'trackInventory': true,

	            'allowOutOfStockPurchases': false,

	            'sku': 'SKU-001',

	            'trialPeriod': 7,

	            'totalCycles': 12,

	            'setupFee': 25,

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

	            'recurring': {

	              'interval': 'day',

	              'intervalCount': 1

	            }

	          }

	        ],

	        'collectionIds': [

	          '64a1b2c3d4e5f67890123458',

	          '64a1b2c3d4e5f67890123459'

	        ],

	        'isLabelEnabled': true,

	        'isTaxesEnabled': true,

	        'seo': {

	          'title': 'Best Product - Buy Now',

	          'description': 'This is the best product you can buy online with amazing features and great value'

	        },

	        'slug': 'premium-product',

	        'automaticTaxCategoryId': '64a1b2c3d4e5f67890123460',

	        'taxInclusive': false,

	        'taxes': [

	          {}

	        ],

	        'medias': [

	          {}

	        ],

	        'label': {}

	      }

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

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/products/bulk-update/edit',

	  headers: { 

	    'Content-Type': 'application/json', 

	    'Accept': 'application/json'

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

	  'path': '/products/bulk-update/edit',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

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

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/products/bulk-update/edit',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "products": [

	      {

	        "_id": "64a1b2c3d4e5f67890123456",

	        "name": "Premium Product",

	        "description": "A high-quality premium product with excellent features and durability",

	        "image": "https://example.com/product-image.jpg",

	        "availableInStore": true,

	        "prices": [

	          {

	            "_id": "64a1b2c3d4e5f67890123456",

	            "name": "Standard Plan",

	            "amount": 99.99,

	            "currency": "USD",

	            "compareAtPrice": 129.99,

	            "availableQuantity": 100,

	            "trackInventory": true,

	            "allowOutOfStockPurchases": false,

	            "sku": "SKU-001",

	            "trialPeriod": 7,

	            "totalCycles": 12,

	            "setupFee": 25,

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

	            "recurring": {

	              "interval": "day",

	              "intervalCount": 1

	            }

	          }

	        ],

	        "collectionIds": [

	          "64a1b2c3d4e5f67890123458",

	          "64a1b2c3d4e5f67890123459"

	        ],

	        "isLabelEnabled": true,

	        "isTaxesEnabled": true,

	        "seo": {

	          "title": "Best Product - Buy Now",

	          "description": "This is the best product you can buy online with amazing features and great value"

	        },

	        "slug": "premium-product",

	        "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	        "taxInclusive": false,

	        "taxes": [

	          {}

	        ],

	        "medias": [

	          {}

	        ],

	        "label": {}

	      }

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/products/bulk-update/edit')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "products": [

	      {

	        "_id": "64a1b2c3d4e5f67890123456",

	        "name": "Premium Product",

	        "description": "A high-quality premium product with excellent features and durability",

	        "image": "https://example.com/product-image.jpg",

	        "availableInStore": true,

	        "prices": [

	          {

	            "_id": "64a1b2c3d4e5f67890123456",

	            "name": "Standard Plan",

	            "amount": 99.99,

	            "currency": "USD",

	            "compareAtPrice": 129.99,

	            "availableQuantity": 100,

	            "trackInventory": true,

	            "allowOutOfStockPurchases": false,

	            "sku": "SKU-001",

	            "trialPeriod": 7,

	            "totalCycles": 12,

	            "setupFee": 25,

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

	            "recurring": {

	              "interval": "day",

	              "intervalCount": 1

	            }

	          }

	        ],

	        "collectionIds": [

	          "64a1b2c3d4e5f67890123458",

	          "64a1b2c3d4e5f67890123459"

	        ],

	        "isLabelEnabled": true,

	        "isTaxesEnabled": true,

	        "seo": {

	          "title": "Best Product - Buy Now",

	          "description": "This is the best product you can buy online with amazing features and great value"

	        },

	        "slug": "premium-product",

	        "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	        "taxInclusive": false,

	        "taxes": [

	          {}

	        ],

	        "medias": [

	          {}

	        ],

	        "label": {}

	      }

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

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": True,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": True,

	          "allowOutOfStockPurchases": False,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": True,

	      "isTaxesEnabled": True,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": False,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

	}

	conn.request("POST", "/products/bulk-update/edit", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/products/bulk-update/edit"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": True,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": True,

	          "allowOutOfStockPurchases": False,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": True,

	      "isTaxesEnabled": True,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": False,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/products/bulk-update/edit',

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

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	}',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/json',

	    'Accept: application/json'

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

	  'Accept' => 'application/json'

	];

	$body = '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/products/bulk-update/edit', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/products/bulk-update/edit');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "products": [\n    {\n      "_id": "64a1b2c3d4e5f67890123456",\n      "name": "Premium Product",\n      "description": "A high-quality premium product with excellent features and durability",\n      "image": "https://example.com/product-image.jpg",\n      "availableInStore": true,\n      "prices": [\n        {\n          "_id": "64a1b2c3d4e5f67890123456",\n          "name": "Standard Plan",\n          "amount": 99.99,\n          "currency": "USD",\n          "compareAtPrice": 129.99,\n          "availableQuantity": 100,\n          "trackInventory": true,\n          "allowOutOfStockPurchases": false,\n          "sku": "SKU-001",\n          "trialPeriod": 7,\n          "totalCycles": 12,\n          "setupFee": 25,\n          "shippingOptions": {\n            "weight": {\n              "value": 10,\n              "unit": "kg"\n            },\n            "dimensions": {\n              "height": 10,\n              "width": 10,\n              "length": 10,\n              "unit": "cm"\n            }\n          },\n          "recurring": {\n            "interval": "day",\n            "intervalCount": 1\n          }\n        }\n      ],\n      "collectionIds": [\n        "64a1b2c3d4e5f67890123458",\n        "64a1b2c3d4e5f67890123459"\n      ],\n      "isLabelEnabled": true,\n      "isTaxesEnabled": true,\n      "seo": {\n        "title": "Best Product - Buy Now",\n        "description": "This is the best product you can buy online with amazing features and great value"\n      },\n      "slug": "premium-product",\n      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",\n      "taxInclusive": false,\n      "taxes": [\n        {}\n      ],\n      "medias": [\n        {}\n      ],\n      "label": {}\n    }\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/products/bulk-update/edit');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

	  ]

	}');

	$request->setBody($body);

	$request->setOptions(array());

	$request->setHeaders(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"products\": [\n    {\n      \"_id\": \"64a1b2c3d4e5f67890123456\",\n      \"name\": \"Premium Product\",\n      \"description\": \"A high-quality premium product with excellent features and durability\",\n      \"image\": \"https://example.com/product-image.jpg\",\n      \"availableInStore\": true,\n      \"prices\": [\n        {\n          \"_id\": \"64a1b2c3d4e5f67890123456\",\n          \"name\": \"Standard Plan\",\n          \"amount\": 99.99,\n          \"currency\": \"USD\",\n          \"compareAtPrice\": 129.99,\n          \"availableQuantity\": 100,\n          \"trackInventory\": true,\n          \"allowOutOfStockPurchases\": false,\n          \"sku\": \"SKU-001\",\n          \"trialPeriod\": 7,\n          \"totalCycles\": 12,\n          \"setupFee\": 25,\n          \"shippingOptions\": {\n            \"weight\": {\n              \"value\": 10,\n              \"unit\": \"kg\"\n            },\n            \"dimensions\": {\n              \"height\": 10,\n              \"width\": 10,\n              \"length\": 10,\n              \"unit\": \"cm\"\n            }\n          },\n          \"recurring\": {\n            \"interval\": \"day\",\n            \"intervalCount\": 1\n          }\n        }\n      ],\n      \"collectionIds\": [\n        \"64a1b2c3d4e5f67890123458\",\n        \"64a1b2c3d4e5f67890123459\"\n      ],\n      \"isLabelEnabled\": true,\n      \"isTaxesEnabled\": true,\n      \"seo\": {\n        \"title\": \"Best Product - Buy Now\",\n        \"description\": \"This is the best product you can buy online with amazing features and great value\"\n      },\n      \"slug\": \"premium-product\",\n      \"automaticTaxCategoryId\": \"64a1b2c3d4e5f67890123460\",\n      \"taxInclusive\": false,\n      \"taxes\": [\n        {}\n      ],\n      \"medias\": [\n        {}\n      ],\n      \"label\": {}\n    }\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/products/bulk-update/edit")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/products/bulk-update/edit")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"products\": [\n    {\n      \"_id\": \"64a1b2c3d4e5f67890123456\",\n      \"name\": \"Premium Product\",\n      \"description\": \"A high-quality premium product with excellent features and durability\",\n      \"image\": \"https://example.com/product-image.jpg\",\n      \"availableInStore\": true,\n      \"prices\": [\n        {\n          \"_id\": \"64a1b2c3d4e5f67890123456\",\n          \"name\": \"Standard Plan\",\n          \"amount\": 99.99,\n          \"currency\": \"USD\",\n          \"compareAtPrice\": 129.99,\n          \"availableQuantity\": 100,\n          \"trackInventory\": true,\n          \"allowOutOfStockPurchases\": false,\n          \"sku\": \"SKU-001\",\n          \"trialPeriod\": 7,\n          \"totalCycles\": 12,\n          \"setupFee\": 25,\n          \"shippingOptions\": {\n            \"weight\": {\n              \"value\": 10,\n              \"unit\": \"kg\"\n            },\n            \"dimensions\": {\n              \"height\": 10,\n              \"width\": 10,\n              \"length\": 10,\n              \"unit\": \"cm\"\n            }\n          },\n          \"recurring\": {\n            \"interval\": \"day\",\n            \"intervalCount\": 1\n          }\n        }\n      ],\n      \"collectionIds\": [\n        \"64a1b2c3d4e5f67890123458\",\n        \"64a1b2c3d4e5f67890123459\"\n      ],\n      \"isLabelEnabled\": true,\n      \"isTaxesEnabled\": true,\n      \"seo\": {\n        \"title\": \"Best Product - Buy Now\",\n        \"description\": \"This is the best product you can buy online with amazing features and great value\"\n      },\n      \"slug\": \"premium-product\",\n      \"automaticTaxCategoryId\": \"64a1b2c3d4e5f67890123460\",\n      \"taxInclusive\": false,\n      \"taxes\": [\n        {}\n      ],\n      \"medias\": [\n        {}\n      ],\n      \"label\": {}\n    }\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/products/bulk-update/edit"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

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

	

	url = URI("https://services.leadconnectorhq.com/products/bulk-update/edit")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "products": [

	    {

	      "_id": "64a1b2c3d4e5f67890123456",

	      "name": "Premium Product",

	      "description": "A high-quality premium product with excellent features and durability",

	      "image": "https://example.com/product-image.jpg",

	      "availableInStore": true,

	      "prices": [

	        {

	          "_id": "64a1b2c3d4e5f67890123456",

	          "name": "Standard Plan",

	          "amount": 99.99,

	          "currency": "USD",

	          "compareAtPrice": 129.99,

	          "availableQuantity": 100,

	          "trackInventory": true,

	          "allowOutOfStockPurchases": false,

	          "sku": "SKU-001",

	          "trialPeriod": 7,

	          "totalCycles": 12,

	          "setupFee": 25,

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

	          "recurring": {

	            "interval": "day",

	            "intervalCount": 1

	          }

	        }

	      ],

	      "collectionIds": [

	        "64a1b2c3d4e5f67890123458",

	        "64a1b2c3d4e5f67890123459"

	      ],

	      "isLabelEnabled": true,

	      "isTaxesEnabled": true,

	      "seo": {

	        "title": "Best Product - Buy Now",

	        "description": "This is the best product you can buy online with amazing features and great value"

	      },

	      "slug": "premium-product",

	      "automaticTaxCategoryId": "64a1b2c3d4e5f67890123460",

	      "taxInclusive": false,

	      "taxes": [

	        {}

	      ],

	      "medias": [

	        {}

	      ],

	      "label": {}

	    }

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

	

	$body = @"

	{

	  `"altId`": `"6578278e879ad2646715ba9c`",

	  `"altType`": `"location`",

	  `"products`": [

	    {

	      `"_id`": `"64a1b2c3d4e5f67890123456`",

	      `"name`": `"Premium Product`",

	      `"description`": `"A high-quality premium product with excellent features and durability`",

	      `"image`": `"https://example.com/product-image.jpg`",

	      `"availableInStore`": true,

	      `"prices`": [

	        {

	          `"_id`": `"64a1b2c3d4e5f67890123456`",

	          `"name`": `"Standard Plan`",

	          `"amount`": 99.99,

	          `"currency`": `"USD`",

	          `"compareAtPrice`": 129.99,

	          `"availableQuantity`": 100,

	          `"trackInventory`": true,

	          `"allowOutOfStockPurchases`": false,

	          `"sku`": `"SKU-001`",

	          `"trialPeriod`": 7,

	          `"totalCycles`": 12,

	          `"setupFee`": 25,

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

	          `"recurring`": {

	            `"interval`": `"day`",

	            `"intervalCount`": 1

	          }

	        }

	      ],

	      `"collectionIds`": [

	        `"64a1b2c3d4e5f67890123458`",

	        `"64a1b2c3d4e5f67890123459`"

	      ],

	      `"isLabelEnabled`": true,

	      `"isTaxesEnabled`": true,

	      `"seo`": {

	        `"title`": `"Best Product - Buy Now`",

	        `"description`": `"This is the best product you can buy online with amazing features and great value`"

	      },

	      `"slug`": `"premium-product`",

	      `"automaticTaxCategoryId`": `"64a1b2c3d4e5f67890123460`",

	      `"taxInclusive`": false,

	      `"taxes`": [

	        {}

	      ],

	      `"medias`": [

	        {}

	      ],

	      `"label`": {}

	    }

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/bulk-update/edit' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

