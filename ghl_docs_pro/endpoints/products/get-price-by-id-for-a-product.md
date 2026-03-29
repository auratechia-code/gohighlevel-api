# Get Price by ID for a Product

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/products/:productId/price/:priceId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: products/prices.readonly
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
	curl -L 'https://services.leadconnectorhq.com/products/:productId/price/:priceId' \

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

	  const response = await highLevel.products.getPriceByIdForProduct({

	    'productId': '6578278e879ad2646715ba9c',

	    'priceId': '6578278e879ad2646715ba9c',

	    'locationId': '6578278e879ad2646715ba9c'

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

	  url: 'https://services.leadconnectorhq.com/products/:productId/price/:priceId',

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

	  'path': '/products/:productId/price/:priceId',

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

	  'url': 'https://services.leadconnectorhq.com/products/:productId/price/:priceId',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/products/:productId/price/:priceId')

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

	conn.request("GET", "/products/:productId/price/:priceId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/products/:productId/price/:priceId"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/products/:productId/price/:priceId',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/products/:productId/price/:priceId', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/products/:productId/price/:priceId');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/products/:productId/price/:priceId');

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

	  .url("https://services.leadconnectorhq.com/products/:productId/price/:priceId")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/products/:productId/price/:priceId")

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

	

	  url := "https://services.leadconnectorhq.com/products/:productId/price/:priceId"

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

	

	url = URI("https://services.leadconnectorhq.com/products/:productId/price/:priceId")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/:productId/price/:priceId' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

