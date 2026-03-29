# Update invoice late fees configuration

**Method:** `PATCH` | **URL:** `https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration`

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
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `invoiceId` | ❌ |  |

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
	curl -L -X PATCH 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

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

	  const response = await highLevel.invoices.updateInvoiceLateFeesConfiguration({

	    'invoiceId': '6578278e879ad2646715ba9c'

	  },

	  {

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

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

	  }

	});

	

	let config = {

	  method: 'patch',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration',

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

	  'method': 'PATCH',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/invoices/:invoiceId/late-fees-configuration',

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

	  }

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PATCH',

	  'url': 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

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

	var req = unirest('PATCH', 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

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

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PATCH", "/invoices/:invoiceId/late-fees-configuration", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

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

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("PATCH", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PATCH',

	  CURLOPT_POSTFIELDS =>'{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

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

	  }

	}';

	$request = new Request('PATCH', 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration');

	$request->setMethod('PATCH');

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "lateFeesConfiguration": {\n    "enable": true,\n    "value": 10,\n    "type": "fixed",\n    "frequency": {\n      "intervalCount": 10,\n      "interval": "day"\n    },\n    "grace": {\n      "intervalCount": 10,\n      "interval": "day"\n    },\n    "maxLateFees": {\n      "type": "fixed",\n      "value": "10"\n    }\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration');

	$request->setRequestMethod('PATCH');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"lateFeesConfiguration\": {\n    \"enable\": true,\n    \"value\": 10,\n    \"type\": \"fixed\",\n    \"frequency\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"grace\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"maxLateFees\": {\n      \"type\": \"fixed\",\n      \"value\": \"10\"\n    }\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration")

	  .method("PATCH", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.patch("https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"lateFeesConfiguration\": {\n    \"enable\": true,\n    \"value\": 10,\n    \"type\": \"fixed\",\n    \"frequency\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"grace\": {\n      \"intervalCount\": 10,\n      \"interval\": \"day\"\n    },\n    \"maxLateFees\": {\n      \"type\": \"fixed\",\n      \"value\": \"10\"\n    }\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration"

	  method := "PATCH"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

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

	

	url = URI("https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Patch.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

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

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/:invoiceId/late-fees-configuration' -Method 'PATCH' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

