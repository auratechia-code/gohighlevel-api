# Create/Update Store Settings

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/store/store-setting`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "status": true,
  "message": "Successfully created",
  "data": {
    "altId": "6578278e879ad2646715ba9c",
    "altType": "location",
    "shippingOrigin": {
      "name": "ABC Store",
      "country": "US",
      "state": "VA",
      "city": "Tokyo",
      "street1": "Street 1",
      "street2": "Street 2",
      "zip": "674561",
      "phone": "+1-214-559-6993",
      "email": "john@deo.com"
    },
    "storeOrderNotification": {
      "enabled": true,
      "subject": "Your order is placed !",
      "emailTemplateId": "6788d542f0462ffd6bc29bb9",
      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"
    },
    "storeOrderFulfillmentNotification": {
      "enabled": true,
      "subject": "Order fulfilled",
      "emailTemplateId": "6788d542f0462ffd6bc29bb9",
      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"
    },
    "_id": "655b33a82209e60b6adb87a5",
    "createdAt": "2023-12-12T09:27:42.355Z",
    "updatedAt": "2023-12-12T09:27:42.355Z"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/store/store-setting' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	  const response = await highLevel.store.createStoreSetting({

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'shippingOrigin': {

	      'name': 'ABC Store',

	      'country': 'US',

	      'state': 'VA',

	      'city': 'Tokyo',

	      'street1': 'Street 1',

	      'street2': 'Street 2',

	      'zip': '674561',

	      'phone': '+1-214-559-6993',

	      'email': 'john@deo.com'

	    },

	    'storeOrderNotification': {

	      'enabled': true,

	      'subject': 'Your order is placed !',

	      'emailTemplateId': '6788d542f0462ffd6bc29bb9',

	      'defaultEmailTemplateId': '6788d542f0462ffd6bc29bb9'

	    },

	    'storeOrderFulfillmentNotification': {

	      'enabled': true,

	      'subject': 'Order fulfilled',

	      'emailTemplateId': '6788d542f0462ffd6bc29bb9',

	      'defaultEmailTemplateId': '6788d542f0462ffd6bc29bb9'

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

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  }

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/store/store-setting',

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

	  'path': '/store/store-setting',

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

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	  'url': 'https://services.leadconnectorhq.com/store/store-setting',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "shippingOrigin": {

	      "name": "ABC Store",

	      "country": "US",

	      "state": "VA",

	      "city": "Tokyo",

	      "street1": "Street 1",

	      "street2": "Street 2",

	      "zip": "674561",

	      "phone": "+1-214-559-6993",

	      "email": "john@deo.com"

	    },

	    "storeOrderNotification": {

	      "enabled": true,

	      "subject": "Your order is placed !",

	      "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	    },

	    "storeOrderFulfillmentNotification": {

	      "enabled": true,

	      "subject": "Order fulfilled",

	      "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/store/store-setting')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "shippingOrigin": {

	      "name": "ABC Store",

	      "country": "US",

	      "state": "VA",

	      "city": "Tokyo",

	      "street1": "Street 1",

	      "street2": "Street 2",

	      "zip": "674561",

	      "phone": "+1-214-559-6993",

	      "email": "john@deo.com"

	    },

	    "storeOrderNotification": {

	      "enabled": true,

	      "subject": "Your order is placed !",

	      "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	    },

	    "storeOrderFulfillmentNotification": {

	      "enabled": true,

	      "subject": "Order fulfilled",

	      "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": True,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": True,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/store/store-setting", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/store/store-setting"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": True,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": True,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/store/store-setting',

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

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  }

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/store/store-setting', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/store/store-setting');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "shippingOrigin": {\n    "name": "ABC Store",\n    "country": "US",\n    "state": "VA",\n    "city": "Tokyo",\n    "street1": "Street 1",\n    "street2": "Street 2",\n    "zip": "674561",\n    "phone": "+1-214-559-6993",\n    "email": "john@deo.com"\n  },\n  "storeOrderNotification": {\n    "enabled": true,\n    "subject": "Your order is placed !",\n    "emailTemplateId": "6788d542f0462ffd6bc29bb9",\n    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"\n  },\n  "storeOrderFulfillmentNotification": {\n    "enabled": true,\n    "subject": "Order fulfilled",\n    "emailTemplateId": "6788d542f0462ffd6bc29bb9",\n    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/store/store-setting');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"shippingOrigin\": {\n    \"name\": \"ABC Store\",\n    \"country\": \"US\",\n    \"state\": \"VA\",\n    \"city\": \"Tokyo\",\n    \"street1\": \"Street 1\",\n    \"street2\": \"Street 2\",\n    \"zip\": \"674561\",\n    \"phone\": \"+1-214-559-6993\",\n    \"email\": \"john@deo.com\"\n  },\n  \"storeOrderNotification\": {\n    \"enabled\": true,\n    \"subject\": \"Your order is placed !\",\n    \"emailTemplateId\": \"6788d542f0462ffd6bc29bb9\",\n    \"defaultEmailTemplateId\": \"6788d542f0462ffd6bc29bb9\"\n  },\n  \"storeOrderFulfillmentNotification\": {\n    \"enabled\": true,\n    \"subject\": \"Order fulfilled\",\n    \"emailTemplateId\": \"6788d542f0462ffd6bc29bb9\",\n    \"defaultEmailTemplateId\": \"6788d542f0462ffd6bc29bb9\"\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/store/store-setting")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/store/store-setting")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"shippingOrigin\": {\n    \"name\": \"ABC Store\",\n    \"country\": \"US\",\n    \"state\": \"VA\",\n    \"city\": \"Tokyo\",\n    \"street1\": \"Street 1\",\n    \"street2\": \"Street 2\",\n    \"zip\": \"674561\",\n    \"phone\": \"+1-214-559-6993\",\n    \"email\": \"john@deo.com\"\n  },\n  \"storeOrderNotification\": {\n    \"enabled\": true,\n    \"subject\": \"Your order is placed !\",\n    \"emailTemplateId\": \"6788d542f0462ffd6bc29bb9\",\n    \"defaultEmailTemplateId\": \"6788d542f0462ffd6bc29bb9\"\n  },\n  \"storeOrderFulfillmentNotification\": {\n    \"enabled\": true,\n    \"subject\": \"Order fulfilled\",\n    \"emailTemplateId\": \"6788d542f0462ffd6bc29bb9\",\n    \"defaultEmailTemplateId\": \"6788d542f0462ffd6bc29bb9\"\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/store/store-setting"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed !",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	

	url = URI("https://services.leadconnectorhq.com/store/store-setting")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "shippingOrigin": {

	    "name": "ABC Store",

	    "country": "US",

	    "state": "VA",

	    "city": "Tokyo",

	    "street1": "Street 1",

	    "street2": "Street 2",

	    "zip": "674561",

	    "phone": "+1-214-559-6993",

	    "email": "john@deo.com"

	  },

	  "storeOrderNotification": {

	    "enabled": true,

	    "subject": "Your order is placed \!",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

	  },

	  "storeOrderFulfillmentNotification": {

	    "enabled": true,

	    "subject": "Order fulfilled",

	    "emailTemplateId": "6788d542f0462ffd6bc29bb9",

	    "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"

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

	  `"shippingOrigin`": {

	    `"name`": `"ABC Store`",

	    `"country`": `"US`",

	    `"state`": `"VA`",

	    `"city`": `"Tokyo`",

	    `"street1`": `"Street 1`",

	    `"street2`": `"Street 2`",

	    `"zip`": `"674561`",

	    `"phone`": `"+1-214-559-6993`",

	    `"email`": `"john@deo.com`"

	  },

	  `"storeOrderNotification`": {

	    `"enabled`": true,

	    `"subject`": `"Your order is placed !`",

	    `"emailTemplateId`": `"6788d542f0462ffd6bc29bb9`",

	    `"defaultEmailTemplateId`": `"6788d542f0462ffd6bc29bb9`"

	  },

	  `"storeOrderFulfillmentNotification`": {

	    `"enabled`": true,

	    `"subject`": `"Order fulfilled`",

	    `"emailTemplateId`": `"6788d542f0462ffd6bc29bb9`",

	    `"defaultEmailTemplateId`": `"6788d542f0462ffd6bc29bb9`"

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/store/store-setting' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

