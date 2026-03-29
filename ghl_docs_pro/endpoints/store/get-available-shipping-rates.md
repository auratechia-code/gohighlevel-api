# Get available shipping rates

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates`

## 🔐 Requirements
```text
N/A
```

## 📥 Parameters
## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "status": true,
  "message": "Successfully created",
  "data": [
    {
      "name": "North zone",
      "description": "Ships next day",
      "currency": "USD",
      "amount": 99.99,
      "isCarrierRate": true,
      "shippingCarrierId": "655b33a82209e60b6adb87a5",
      "percentageOfRateFee": 10.99,
      "shippingCarrierServices": [
        {
          "name": "Priority Mail Express International",
          "value": "PriorityMailExpressInternational"
        }
      ],
      "_id": "655b33a82209e60b6adb87a5",
      "shippingZoneId": "655b33a82209e60b6adb87a5"
    }
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	--data-raw '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

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

	  const response = await highLevel.store.getAvailableShippingZones({

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'country': 'US',

	    'address': {

	      'name': 'John Doe',

	      'companyName': 'ABC Company',

	      'addressLine1': '123 Main St.',

	      'country': 'US',

	      'state': 'US',

	      'city': 'New York',

	      'zip': '12345',

	      'phone': '1234567890',

	      'email': 'abu@example.com'

	    },

	    'amountAvailable': 'US',

	    'totalOrderAmount': 99.99,

	    'weightAvailable': true,

	    'totalOrderWeight': 10,

	    'source': {

	      'type': 'order',

	      'subType': 'store'

	    },

	    'products': [

	      {

	        'id': 'string',

	        'qty': 0

	      }

	    ],

	    'couponCode': 'TEST'

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

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates',

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

	  'path': '/store/shipping-zone/shipping-rates',

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

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "country": "US",

	    "address": {

	      "name": "John Doe",

	      "companyName": "ABC Company",

	      "addressLine1": "123 Main St.",

	      "country": "US",

	      "state": "US",

	      "city": "New York",

	      "zip": "12345",

	      "phone": "1234567890",

	      "email": "abu@example.com"

	    },

	    "amountAvailable": "US",

	    "totalOrderAmount": 99.99,

	    "weightAvailable": true,

	    "totalOrderWeight": 10,

	    "source": {

	      "type": "order",

	      "subType": "store"

	    },

	    "products": [

	      {

	        "id": "string",

	        "qty": 0

	      }

	    ],

	    "couponCode": "TEST"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "country": "US",

	    "address": {

	      "name": "John Doe",

	      "companyName": "ABC Company",

	      "addressLine1": "123 Main St.",

	      "country": "US",

	      "state": "US",

	      "city": "New York",

	      "zip": "12345",

	      "phone": "1234567890",

	      "email": "abu@example.com"

	    },

	    "amountAvailable": "US",

	    "totalOrderAmount": 99.99,

	    "weightAvailable": true,

	    "totalOrderWeight": 10,

	    "source": {

	      "type": "order",

	      "subType": "store"

	    },

	    "products": [

	      {

	        "id": "string",

	        "qty": 0

	      }

	    ],

	    "couponCode": "TEST"

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

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": True,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

	}

	conn.request("POST", "/store/shipping-zone/shipping-rates", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": True,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates',

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

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

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

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "country": "US",\n  "address": {\n    "name": "John Doe",\n    "companyName": "ABC Company",\n    "addressLine1": "123 Main St.",\n    "country": "US",\n    "state": "US",\n    "city": "New York",\n    "zip": "12345",\n    "phone": "1234567890",\n    "email": "abu@example.com"\n  },\n  "amountAvailable": "US",\n  "totalOrderAmount": 99.99,\n  "weightAvailable": true,\n  "totalOrderWeight": 10,\n  "source": {\n    "type": "order",\n    "subType": "store"\n  },\n  "products": [\n    {\n      "id": "string",\n      "qty": 0\n    }\n  ],\n  "couponCode": "TEST"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"country\": \"US\",\n  \"address\": {\n    \"name\": \"John Doe\",\n    \"companyName\": \"ABC Company\",\n    \"addressLine1\": \"123 Main St.\",\n    \"country\": \"US\",\n    \"state\": \"US\",\n    \"city\": \"New York\",\n    \"zip\": \"12345\",\n    \"phone\": \"1234567890\",\n    \"email\": \"abu@example.com\"\n  },\n  \"amountAvailable\": \"US\",\n  \"totalOrderAmount\": 99.99,\n  \"weightAvailable\": true,\n  \"totalOrderWeight\": 10,\n  \"source\": {\n    \"type\": \"order\",\n    \"subType\": \"store\"\n  },\n  \"products\": [\n    {\n      \"id\": \"string\",\n      \"qty\": 0\n    }\n  ],\n  \"couponCode\": \"TEST\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"country\": \"US\",\n  \"address\": {\n    \"name\": \"John Doe\",\n    \"companyName\": \"ABC Company\",\n    \"addressLine1\": \"123 Main St.\",\n    \"country\": \"US\",\n    \"state\": \"US\",\n    \"city\": \"New York\",\n    \"zip\": \"12345\",\n    \"phone\": \"1234567890\",\n    \"email\": \"abu@example.com\"\n  },\n  \"amountAvailable\": \"US\",\n  \"totalOrderAmount\": 99.99,\n  \"weightAvailable\": true,\n  \"totalOrderWeight\": 10,\n  \"source\": {\n    \"type\": \"order\",\n    \"subType\": \"store\"\n  },\n  \"products\": [\n    {\n      \"id\": \"string\",\n      \"qty\": 0\n    }\n  ],\n  \"couponCode\": \"TEST\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

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

	

	url = URI("https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "country": "US",

	  "address": {

	    "name": "John Doe",

	    "companyName": "ABC Company",

	    "addressLine1": "123 Main St.",

	    "country": "US",

	    "state": "US",

	    "city": "New York",

	    "zip": "12345",

	    "phone": "1234567890",

	    "email": "abu@example.com"

	  },

	  "amountAvailable": "US",

	  "totalOrderAmount": 99.99,

	  "weightAvailable": true,

	  "totalOrderWeight": 10,

	  "source": {

	    "type": "order",

	    "subType": "store"

	  },

	  "products": [

	    {

	      "id": "string",

	      "qty": 0

	    }

	  ],

	  "couponCode": "TEST"

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

	  `"country`": `"US`",

	  `"address`": {

	    `"name`": `"John Doe`",

	    `"companyName`": `"ABC Company`",

	    `"addressLine1`": `"123 Main St.`",

	    `"country`": `"US`",

	    `"state`": `"US`",

	    `"city`": `"New York`",

	    `"zip`": `"12345`",

	    `"phone`": `"1234567890`",

	    `"email`": `"abu@example.com`"

	  },

	  `"amountAvailable`": `"US`",

	  `"totalOrderAmount`": 99.99,

	  `"weightAvailable`": true,

	  `"totalOrderWeight`": 10,

	  `"source`": {

	    `"type`": `"order`",

	    `"subType`": `"store`"

	  },

	  `"products`": [

	    {

	      `"id`": `"string`",

	      `"qty`": 0

	    }

	  ],

	  `"couponCode`": `"TEST`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/store/shipping-zone/shipping-rates' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

