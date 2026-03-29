# Create new provider config

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/payments/custom-provider/connect`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: payments/custom-provider.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "name": "Company Paypal Integration",
  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",
  "paymentsUrl": "https://testpayment.paypal.com",
  "queryUrl": "https://testsubscription.paypal.com",
  "imageUrl": "https://testsubscription.paypal.com",
  "_id": "662a44ad19a2a44d3cd9d749",
  "locationId": "Lk3nlfk4lxlelVEwcW",
  "marketplaceAppId": "65f0b217a05c774da7f1efa5",
  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",
  "deleted": true,
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/payments/custom-provider/connect' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	  const response = await highLevel.payments.createConfig({

	    'locationId': 'Lk3nlfk4lxlelVEwcW'

	  },

	  {

	    'live': {

	      'apiKey': 'y5ZQxryRFXZHvUJZdLeXXXXX',

	      'publishableKey': 'rzp_test_zPRoVMLOa0XXXX'

	    },

	    'test': {

	      'apiKey': 'y5ZQxryRFXZHvUJZdLeXXXXX',

	      'publishableKey': 'rzp_test_zPRoVMLOa0XXXX'

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

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  }

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/payments/custom-provider/connect',

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

	  'path': '/payments/custom-provider/connect',

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

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	  'url': 'https://services.leadconnectorhq.com/payments/custom-provider/connect',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "live": {

	      "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	      "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	    },

	    "test": {

	      "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	      "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/payments/custom-provider/connect')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "live": {

	      "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	      "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	    },

	    "test": {

	      "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	      "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/payments/custom-provider/connect", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/payments/custom-provider/connect"

	

	payload = json.dumps({

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/payments/custom-provider/connect',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  }

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/payments/custom-provider/connect', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/payments/custom-provider/connect');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "live": {\n    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",\n    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"\n  },\n  "test": {\n    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",\n    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/payments/custom-provider/connect');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"live\": {\n    \"apiKey\": \"y5ZQxryRFXZHvUJZdLeXXXXX\",\n    \"publishableKey\": \"rzp_test_zPRoVMLOa0XXXX\"\n  },\n  \"test\": {\n    \"apiKey\": \"y5ZQxryRFXZHvUJZdLeXXXXX\",\n    \"publishableKey\": \"rzp_test_zPRoVMLOa0XXXX\"\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/payments/custom-provider/connect")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/payments/custom-provider/connect")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"live\": {\n    \"apiKey\": \"y5ZQxryRFXZHvUJZdLeXXXXX\",\n    \"publishableKey\": \"rzp_test_zPRoVMLOa0XXXX\"\n  },\n  \"test\": {\n    \"apiKey\": \"y5ZQxryRFXZHvUJZdLeXXXXX\",\n    \"publishableKey\": \"rzp_test_zPRoVMLOa0XXXX\"\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/payments/custom-provider/connect"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	

	url = URI("https://services.leadconnectorhq.com/payments/custom-provider/connect")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "live": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

	  },

	  "test": {

	    "apiKey": "y5ZQxryRFXZHvUJZdLeXXXXX",

	    "publishableKey": "rzp_test_zPRoVMLOa0XXXX"

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

	  `"live`": {

	    `"apiKey`": `"y5ZQxryRFXZHvUJZdLeXXXXX`",

	    `"publishableKey`": `"rzp_test_zPRoVMLOa0XXXX`"

	  },

	  `"test`": {

	    `"apiKey`": `"y5ZQxryRFXZHvUJZdLeXXXXX`",

	    `"publishableKey`": `"rzp_test_zPRoVMLOa0XXXX`"

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/custom-provider/connect' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

