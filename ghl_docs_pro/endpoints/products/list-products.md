# List Products

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/products/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: products.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `limit` | ❌ | offset number The starting index of the page, indicating the position from which the results should be retrieved. Default value: 0 Example: 0 |
| `offset` | ✅ | locationId string required LocationId is the id of the sub-account Example: 3SwdhCu3svxI8AKsPJt6 |
| `locationId` | ❌ | search string The name of the product for searching. Example: Awesome product |
| `search` | ❌ | collectionIds string Filter by product category Ids. Supports comma separated values |
| `collectionIds` | ❌ | collectionSlug string The slug value of the collection by which the collection would be searched |
| `collectionSlug` | ❌ | expand string[] Name of an entity whose data has to be fetched along with product. Possible entities are tax, stripe and paypal. If not mentioned, only ID will be returned in case of taxes |
| `expand` | ❌ | productIds string[] List of product ids to be fetched. |
| `productIds` | ❌ | storeId string fetch and project products based on the storeId Example: 3SwdhCu3svxI8AKsPJt6 |
| `storeId` | ❌ | includedInStore boolean Separate products by which are included in the store and which are not Example: |
| `includedInStore` | ❌ | availableInStore boolean If the product is included in the online store Example: |
| `availableInStore` | ❌ | sortOrder string Possible values: [ asc , desc ] The order of sort which should be applied for the date Example: desc |
| `sortOrder` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "products": [
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
  ],
  "total": [
    {
      "total": 20
    }
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/products/' \

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

	  const response = await highLevel.products.listInvoices({

	    'limit': 20,

	    'offset': 0,

	    'locationId': '3SwdhCu3svxI8AKsPJt6',

	    'search': 'Awesome product',

	    'storeId': '3SwdhCu3svxI8AKsPJt6',

	    'includedInStore': true,

	    'availableInStore': true,

	    'sortOrder': 'desc'

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

	  url: 'https://services.leadconnectorhq.com/products/',

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

	  'path': '/products/',

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

	  'url': 'https://services.leadconnectorhq.com/products/',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/products/')

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

	conn.request("GET", "/products/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/products/"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/products/',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/products/', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/products/');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/products/');

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

	  .url("https://services.leadconnectorhq.com/products/")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/products/")

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

	

	  url := "https://services.leadconnectorhq.com/products/"

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

	

	url = URI("https://services.leadconnectorhq.com/products/")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

