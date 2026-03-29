# Create Coupon

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/payments/coupon`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: payments/coupons.write
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
<summary>Response 201</summary>

```json
{
  "_id": "67f6c132d9485f9dacd5f123",
  "usageCount": 12,
  "limitPerCustomer": 5,
  "altId": "79t07PzK8Tvf73d12312",
  "altType": "location",
  "name": "NEWT6",
  "code": "NEWT6",
  "discountType": "percentage",
  "discountValue": 25,
  "status": "scheduled",
  "startDate": "2025-04-30T18:30:00.000Z",
  "endDate": "2025-05-30T18:30:00.000Z",
  "applyToFuturePayments": true,
  "applyToFuturePaymentsConfig": {
    "type": "fixed",
    "duration": 3,
    "durationType": "months"
  },
  "userId": "q0m15dTLGeiGOXG123123",
  "createdAt": "2025-04-09T18:49:22.026Z",
  "updatedAt": "2025-04-09T18:49:22.026Z",
  "traceId": "c667b18d-8f5e-44cf-a914"
}

```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/payments/coupon' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

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

	  const response = await highLevel.payments.createCoupon({

	    'altId': 'BQdAwxa0ky1iK2sstLGJ',

	    'altType': 'location',

	    'name': 'New Year Sale',

	    'code': 'LEVELUPDAY2022',

	    'discountType': 'amount',

	    'discountValue': 10,

	    'startDate': '2023-01-01T22:45:00.000Z',

	    'endDate': '2023-01-31T22:45:00.000Z',

	    'usageLimit': 10,

	    'productIds': [

	      '6241712be68f7a98102ba272'

	    ],

	    'priceIds': [

	      '6241712be68f7a98102ba272'

	    ],

	    'variantIds': [

	      '6241712be68f7a98102ba272'

	    ],

	    'applyToFuturePayments': true,

	    'applyToFuturePaymentsConfig': [

	      {

	        'type': 'fixed',

	        'duration': 5,

	        'durationType': 'months'

	      },

	      {

	        'type': 'forever'

	      }

	    ],

	    'limitPerCustomer': true

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

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/payments/coupon',

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

	  'path': '/payments/coupon',

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

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/payments/coupon',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "BQdAwxa0ky1iK2sstLGJ",

	    "altType": "location",

	    "name": "New Year Sale",

	    "code": "LEVELUPDAY2022",

	    "discountType": "amount",

	    "discountValue": 10,

	    "startDate": "2023-01-01T22:45:00.000Z",

	    "endDate": "2023-01-31T22:45:00.000Z",

	    "usageLimit": 10,

	    "productIds": [

	      "6241712be68f7a98102ba272"

	    ],

	    "priceIds": [

	      "6241712be68f7a98102ba272"

	    ],

	    "variantIds": [

	      "6241712be68f7a98102ba272"

	    ],

	    "applyToFuturePayments": true,

	    "applyToFuturePaymentsConfig": [

	      {

	        "type": "fixed",

	        "duration": 5,

	        "durationType": "months"

	      },

	      {

	        "type": "forever"

	      }

	    ],

	    "limitPerCustomer": true

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/payments/coupon')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "BQdAwxa0ky1iK2sstLGJ",

	    "altType": "location",

	    "name": "New Year Sale",

	    "code": "LEVELUPDAY2022",

	    "discountType": "amount",

	    "discountValue": 10,

	    "startDate": "2023-01-01T22:45:00.000Z",

	    "endDate": "2023-01-31T22:45:00.000Z",

	    "usageLimit": 10,

	    "productIds": [

	      "6241712be68f7a98102ba272"

	    ],

	    "priceIds": [

	      "6241712be68f7a98102ba272"

	    ],

	    "variantIds": [

	      "6241712be68f7a98102ba272"

	    ],

	    "applyToFuturePayments": true,

	    "applyToFuturePaymentsConfig": [

	      {

	        "type": "fixed",

	        "duration": 5,

	        "durationType": "months"

	      },

	      {

	        "type": "forever"

	      }

	    ],

	    "limitPerCustomer": true

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

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": True,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": True

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/payments/coupon", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/payments/coupon"

	

	payload = json.dumps({

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": True,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": True

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/payments/coupon',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

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

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/payments/coupon', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/payments/coupon');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "BQdAwxa0ky1iK2sstLGJ",\n  "altType": "location",\n  "name": "New Year Sale",\n  "code": "LEVELUPDAY2022",\n  "discountType": "amount",\n  "discountValue": 10,\n  "startDate": "2023-01-01T22:45:00.000Z",\n  "endDate": "2023-01-31T22:45:00.000Z",\n  "usageLimit": 10,\n  "productIds": [\n    "6241712be68f7a98102ba272"\n  ],\n  "priceIds": [\n    "6241712be68f7a98102ba272"\n  ],\n  "variantIds": [\n    "6241712be68f7a98102ba272"\n  ],\n  "applyToFuturePayments": true,\n  "applyToFuturePaymentsConfig": [\n    {\n      "type": "fixed",\n      "duration": 5,\n      "durationType": "months"\n    },\n    {\n      "type": "forever"\n    }\n  ],\n  "limitPerCustomer": true\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/payments/coupon');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"BQdAwxa0ky1iK2sstLGJ\",\n  \"altType\": \"location\",\n  \"name\": \"New Year Sale\",\n  \"code\": \"LEVELUPDAY2022\",\n  \"discountType\": \"amount\",\n  \"discountValue\": 10,\n  \"startDate\": \"2023-01-01T22:45:00.000Z\",\n  \"endDate\": \"2023-01-31T22:45:00.000Z\",\n  \"usageLimit\": 10,\n  \"productIds\": [\n    \"6241712be68f7a98102ba272\"\n  ],\n  \"priceIds\": [\n    \"6241712be68f7a98102ba272\"\n  ],\n  \"variantIds\": [\n    \"6241712be68f7a98102ba272\"\n  ],\n  \"applyToFuturePayments\": true,\n  \"applyToFuturePaymentsConfig\": [\n    {\n      \"type\": \"fixed\",\n      \"duration\": 5,\n      \"durationType\": \"months\"\n    },\n    {\n      \"type\": \"forever\"\n    }\n  ],\n  \"limitPerCustomer\": true\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/payments/coupon")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/payments/coupon")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"BQdAwxa0ky1iK2sstLGJ\",\n  \"altType\": \"location\",\n  \"name\": \"New Year Sale\",\n  \"code\": \"LEVELUPDAY2022\",\n  \"discountType\": \"amount\",\n  \"discountValue\": 10,\n  \"startDate\": \"2023-01-01T22:45:00.000Z\",\n  \"endDate\": \"2023-01-31T22:45:00.000Z\",\n  \"usageLimit\": 10,\n  \"productIds\": [\n    \"6241712be68f7a98102ba272\"\n  ],\n  \"priceIds\": [\n    \"6241712be68f7a98102ba272\"\n  ],\n  \"variantIds\": [\n    \"6241712be68f7a98102ba272\"\n  ],\n  \"applyToFuturePayments\": true,\n  \"applyToFuturePaymentsConfig\": [\n    {\n      \"type\": \"fixed\",\n      \"duration\": 5,\n      \"durationType\": \"months\"\n    },\n    {\n      \"type\": \"forever\"\n    }\n  ],\n  \"limitPerCustomer\": true\n}")

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

	

	  url := "https://services.leadconnectorhq.com/payments/coupon"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

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

	

	url = URI("https://services.leadconnectorhq.com/payments/coupon")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "BQdAwxa0ky1iK2sstLGJ",

	  "altType": "location",

	  "name": "New Year Sale",

	  "code": "LEVELUPDAY2022",

	  "discountType": "amount",

	  "discountValue": 10,

	  "startDate": "2023-01-01T22:45:00.000Z",

	  "endDate": "2023-01-31T22:45:00.000Z",

	  "usageLimit": 10,

	  "productIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "priceIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "variantIds": [

	    "6241712be68f7a98102ba272"

	  ],

	  "applyToFuturePayments": true,

	  "applyToFuturePaymentsConfig": [

	    {

	      "type": "fixed",

	      "duration": 5,

	      "durationType": "months"

	    },

	    {

	      "type": "forever"

	    }

	  ],

	  "limitPerCustomer": true

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

	  `"altId`": `"BQdAwxa0ky1iK2sstLGJ`",

	  `"altType`": `"location`",

	  `"name`": `"New Year Sale`",

	  `"code`": `"LEVELUPDAY2022`",

	  `"discountType`": `"amount`",

	  `"discountValue`": 10,

	  `"startDate`": `"2023-01-01T22:45:00.000Z`",

	  `"endDate`": `"2023-01-31T22:45:00.000Z`",

	  `"usageLimit`": 10,

	  `"productIds`": [

	    `"6241712be68f7a98102ba272`"

	  ],

	  `"priceIds`": [

	    `"6241712be68f7a98102ba272`"

	  ],

	  `"variantIds`": [

	    `"6241712be68f7a98102ba272`"

	  ],

	  `"applyToFuturePayments`": true,

	  `"applyToFuturePaymentsConfig`": [

	    {

	      `"type`": `"fixed`",

	      `"duration`": 5,

	      `"durationType`": `"months`"

	    },

	    {

	      `"type`": `"forever`"

	    }

	  ],

	  `"limitPerCustomer`": true

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/coupon' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

