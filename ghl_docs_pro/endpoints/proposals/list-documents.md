# List documents

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/proposals/document`

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
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ | status string Possible values: [ draft , sent , viewed , completed , accepted ] Document status, pass as comma separated values Example: draft |
| `status` | ❌ | paymentStatus string Possible values: [ waiting_for_payment , paid , no_payment ] Payment status, pass as comma separated values Example: paid |
| `paymentStatus` | ❌ | limit number Limit to fetch number of records Example: 10 |
| `limit` | ❌ | skip number Skip number of records Example: 0 |
| `skip` | ❌ | query string Search string Example: document |
| `query` | ❌ | dateFrom string Date start from (ISO 8601), dateFrom & DateTo must be provided together Example: 2025-02-03T18:30:00.000Z |
| `dateFrom` | ❌ | dateTo string Date to (ISO 8601), dateFrom & DateTo must be provided together Example: 2025-02-14T18:29:59.999Z |
| `dateTo` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "documents": [
    {
      "locationId": "hTlkh7t8gujsahgg93",
      "documentId": "hTlkh7t8gujsahgg93",
      "_id": "67ac9a51106ee8311e911XXXX",
      "name": "Document Name",
      "type": "proposal",
      "deleted": false,
      "isExpired": false,
      "documentRevision": 1,
      "fillableFields": [
        {
          "fieldId": "text_field_1",
          "isRequired": true,
          "hasCompleted": true,
          "recipient": "John Doe",
          "entityType": "contacts",
          "id": "2d0a6fe1-d519-4198-8785-3da1d7cab925",
          "type": "TextField",
          "value": "John Doe"
        }
      ],
      "grandTotal": {
        "amount": 100,
        "currency": "USD",
        "discountPercentage": 15,
        "discounts": [
          {
            "id": "123456",
            "value": 10,
            "type": "percentage"
          }
        ]
      },
      "locale": "en-US",
      "status": "draft",
      "paymentStatus": "paid",
      "recipients": [
        {
          "id": "u240JcS0E5qE0ziHnwMm",
          "email": "jim@gmail.com",
          "imageUrl": "",
          "contactName": "Jim Anton",
          "firstName": "Jim",
          "lastName": "Anton",
          "role": "signer",
          "hasCompleted": true,
          "signingOrder": 1,
          "imgUrl": "base64 image url",
          "ip": "123.123.123.123"
        }
      ],
      "links": [
        {
          "referenceId": "550e8400-e29b-41d4-a716-446655440000",
          "documentId": "c1e87a91-93b2-4b78-821f-85cf0e1f925b",
          "recipientId": "u240JcS0E5qE0ziHnwMm",
          "entityName": "contacts",
          "recipientCategory": "recipient",
          "documentRevision": 1,
          "createdBy": "b6d8fa28-1112-4dc7-b9d2-f22b75a477ea",
          "deleted": false
        }
      ],
      "updatedAt": "2025-02-03T18:30:00.000Z",
      "createdAt": "2025-02-14T18:29:59.999Z"
    }
  ],
  "total": 10,
  "whiteLabelBaseUrl": "https://example.com",
  "whiteLabelBaseUrlForInvoice": "https://example.com"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "documents": [    {      "locationId": "hTlkh7t8gujsahgg93",      "documentId": "hTlkh7t8gujsahgg93",      "_id": "67ac9a51106ee8311e911XXXX",      "name": "Document Name",      "type": "proposal",      "deleted": false,      "isExpired": false,      "documentRevision": 1,      "fillableFields": [        {          "fieldId": "text_field_1",          "isRequired": true,          "hasCompleted": true,          "recipient": "John Doe",          "entityType": "contacts",          "id": "2d0a6fe1-d519-4198-8785-3da1d7cab925",          "type": "TextField",          "value": "John Doe"        }      ],      "grandTotal": {        "amount": 100,        "currency": "USD",        "discountPercentage": 15,        "discounts": [          {            "id": "123456",            "value": 10,            "type": "percentage"          }        ]      },      "locale": "en-US",      "status": "draft",      "paymentStatus": "paid",      "recipients": [        {          "id": "u240JcS0E5qE0ziHnwMm",          "email": "jim@gmail.com",          "imageUrl": "",          "contactName": "Jim Anton",          "firstName": "Jim",          "lastName": "Anton",          "role": "signer",          "hasCompleted": true,          "signingOrder": 1,          "imgUrl": "base64 image url",          "ip": "123.123.123.123"        }      ],      "links": [        {          "referenceId": "550e8400-e29b-41d4-a716-446655440000",          "documentId": "c1e87a91-93b2-4b78-821f-85cf0e1f925b",          "recipientId": "u240JcS0E5qE0ziHnwMm",          "entityName": "contacts",          "recipientCategory": "recipient",          "documentRevision": 1,          "createdBy": "b6d8fa28-1112-4dc7-b9d2-f22b75a477ea",          "deleted": false        }      ],      "updatedAt": "2025-02-03T18:30:00.000Z",      "createdAt": "2025-02-14T18:29:59.999Z"    }  ],  "total": 10,  "whiteLabelBaseUrl": "https://example.com",  "whiteLabelBaseUrlForInvoice": "https://example.com"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/proposals/document' \

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

	  const response = await highLevel.proposals.listDocumentsContracts({

	    'locationId': 'hTlkh7t8gujsahgg93',

	    'status': 'draft',

	    'paymentStatus': 'paid',

	    'limit': 10,

	    'skip': 0,

	    'query': 'document',

	    'dateFrom': '2025-02-03T18:30:00.000Z',

	    'dateTo': '2025-02-14T18:29:59.999Z'

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

	  url: 'https://services.leadconnectorhq.com/proposals/document',

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

	  'path': '/proposals/document',

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

	  'url': 'https://services.leadconnectorhq.com/proposals/document',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/proposals/document')

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

	conn.request("GET", "/proposals/document", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/proposals/document"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/proposals/document',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/proposals/document', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/proposals/document');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/proposals/document');

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

	  .url("https://services.leadconnectorhq.com/proposals/document")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/proposals/document")

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

	

	  url := "https://services.leadconnectorhq.com/proposals/document"

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

	

	url = URI("https://services.leadconnectorhq.com/proposals/document")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/proposals/document' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

