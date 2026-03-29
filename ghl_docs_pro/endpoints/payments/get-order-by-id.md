# Get Order by ID

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/payments/orders/:orderId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: payments/orders.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `orderId` | ❌ |  |

### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ✅ | altId string required AltId is the unique identifier e.g: location id. Example: 3SwdhCu3svxI8AKsPJt6 |
| `altId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "_id": "653f5e0cde5a1314e62a837c",
  "altId": "3SwdhCu3svxI8AKsPJt6",
  "altType": "location",
  "contactId": "XPLSw2SVagl12LMDeTmQ",
  "currency": "USD",
  "amount": "100",
  "status": "completed",
  "liveMode": "false",
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "fulfillmentStatus": "unfulfilled",
  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",
  "amountSummary": "{ subtotal: 100, discount: 5 }",
  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",
  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",
  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",
  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",
  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",
  "meta": "{ couponSessionExpired: true }",
  "markAsTest": "false",
  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",
  "automaticTaxesCalculated": true,
  "taxCalculationProvider": "taxjar",
  "createdBy": "user123"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/payments/orders/:orderId' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>'

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

	  const response = await highLevel.payments.getOrderById({

	    'orderId': '653f5e0cde5a1314e62a837c',

	    'locationId': '3SwdhCu3svxI8AKsPJt6',

	    'altId': '3SwdhCu3svxI8AKsPJt6'

	  });

	  console.log(response);

	} catch (error) {

	  console.error('Error:', error);

	}

```

#### AXIOS
```nodejs
	const axios = require('axios');

	

	let config = {

	  method: 'get',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/payments/orders/:orderId',

	  headers: { 

	    'Accept': 'application/json', 

	    'Authorization': 'Bearer <TOKEN>'

	  }

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

	  'method': 'GET',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/payments/orders/:orderId',

	  'headers': {

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

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'GET',

	  'url': 'https://services.leadconnectorhq.com/payments/orders/:orderId',

	  'headers': {

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  }

	};

	request(options, function (error, response) {

	  if (error) throw new Error(error);

	  console.log(response.body);

	});

```

#### UNIREST
```nodejs
	var unirest = require('unirest');

	var req = unirest('GET', 'https://services.leadconnectorhq.com/payments/orders/:orderId')

	  .headers({

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .end(function (res) { 

	    if (res.error) throw new Error(res.error); 

	    console.log(res.raw_body);

	  });

```

### PYTHON
#### HTTP.CLIENT
```python
	import http.client

	

	conn = http.client.HTTPSConnection("services.leadconnectorhq.com")

	payload = ''

	headers = {

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("GET", "/payments/orders/:orderId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/payments/orders/:orderId"

	

	payload = {}

	headers = {

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("GET", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/payments/orders/:orderId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'GET',

	  CURLOPT_HTTPHEADER => array(

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

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	];

	$request = new Request('GET', 'https://services.leadconnectorhq.com/payments/orders/:orderId', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/payments/orders/:orderId');

	$request->setMethod(HTTP_Request2::METHOD_GET);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/payments/orders/:orderId');

	$request->setRequestMethod('GET');

	$request->setOptions(array());

	$request->setHeaders(array(

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

	MediaType mediaType = MediaType.parse("text/plain");

	RequestBody body = RequestBody.create(mediaType, "");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/payments/orders/:orderId")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/payments/orders/:orderId")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .asString();

```

### GO
#### NATIVE
```go
	package main

	

	import (

	  "fmt"

	  "net/http"

	  "io"

	)

	

	func main() {

	

	  url := "https://services.leadconnectorhq.com/payments/orders/:orderId"

	  method := "GET"

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, nil)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

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

	require "net/http"

	

	url = URI("https://services.leadconnectorhq.com/payments/orders/:orderId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Get.new(url)

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	

	response = https.request(request)

	puts response.read_body

```

### POWERSHELL
#### RESTMETHOD
```powershell
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"

	$headers.Add("Accept", "application/json")

	$headers.Add("Authorization", "Bearer <TOKEN>")

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/orders/:orderId' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

