# Get Transaction by ID

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/payments/transactions/:transactionId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: payments/transactions.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `transactionId` | ❌ |  |

### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ✅ | altId string required AltId is the unique identifier e.g: location id. Example: 3SwdhCu3svxI8AKsPJt6 |
| `altId` | ✅ | altType string required AltType is the type of identifier. Example: location |
| `altType` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "_id": "61dd0feac077f72010f78804",
  "altType": "location",
  "altId": "3SwdhCu3svxI8AKsPJt6",
  "contactId": "XPLSw2SVagl12LMDeTmQ",
  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",
  "currency": "USD",
  "amount": "100",
  "status": "succeeded",
  "liveMode": "false",
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "entityType": "order",
  "entityId": "61dd0fe9c077f73e67f78803",
  "entitySource": "{ type: \"funnel\", id: \"BDBMEghdIUaqMPEsK349\", subType: \"two_step_order_form\", name: \"new funnel\" }",
  "chargeId": "in_1KGcXDCScnf89tZohCsmImwE",
  "chargeSnapshot": "{ id: \"in_1KGcXDCScnf89tZohCsmImwE\", object: \"invoice\", account_country: \"US\",  account_name:  \"GHL-Testing\" }",
  "invoiceId": "in_1KGcXDCScnf89tZohCsmImwE",
  "subscriptionId": "sub_1KGcXDCScnf89tZoVkoEMCEL",
  "paymentProvider": "{ type: \"stripe\", connectedAccount: { _id: \"612ca676b484b241fef9d962\", accountId: \"acct_1Ihw53CScnf89tZo\" } }",
  "ipAddress": "107.178.194.224",
  "meta": "{ stepId: \"af7c731e-e36f-4152-bd1a-3f69a31d6d6d\", pageId: \"A8ltotc2jZxurJba4e3Y\", pageUrl: \"/v2/preview/A8ltotc2jZxurJba4e3Y\" }",
  "markAsTest": "false",
  "isParent": "false",
  "amountRefunded": "10",
  "receiptId": "6492fbea489bc07892c6defb",
  "qboSynced": "false",
  "qboResponse": "{ domain: \"QBO\", sparse: false, Id: \"180\", SyncToken: \"0\", TotalAmt: 25 }",
  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",
  "mergedFromContactId": "XPLSw2SVagl12LMDeTmQ",
  "createdBy": "user123"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "61dd0feac077f72010f78804",  "altType": "location",  "altId": "3SwdhCu3svxI8AKsPJt6",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "currency": "USD",  "amount": "100",  "status": "succeeded",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "entityType": "order",  "entityId": "61dd0fe9c077f73e67f78803",  "entitySource": "{ type: \"funnel\", id: \"BDBMEghdIUaqMPEsK349\", subType: \"two_step_order_form\", name: \"new funnel\" }",  "chargeId": "in_1KGcXDCScnf89tZohCsmImwE",  "chargeSnapshot": "{ id: \"in_1KGcXDCScnf89tZohCsmImwE\", object: \"invoice\", account_country: \"US\",  account_name:  \"GHL-Testing\" }",  "invoiceId": "in_1KGcXDCScnf89tZohCsmImwE",  "subscriptionId": "sub_1KGcXDCScnf89tZoVkoEMCEL",  "paymentProvider": "{ type: \"stripe\", connectedAccount: { _id: \"612ca676b484b241fef9d962\", accountId: \"acct_1Ihw53CScnf89tZo\" } }",  "ipAddress": "107.178.194.224",  "meta": "{ stepId: \"af7c731e-e36f-4152-bd1a-3f69a31d6d6d\", pageId: \"A8ltotc2jZxurJba4e3Y\", pageUrl: \"/v2/preview/A8ltotc2jZxurJba4e3Y\" }",  "markAsTest": "false",  "isParent": "false",  "amountRefunded": "10",  "receiptId": "6492fbea489bc07892c6defb",  "qboSynced": "false",  "qboResponse": "{ domain: \"QBO\", sparse: false, Id: \"180\", SyncToken: \"0\", TotalAmt: 25 }",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "mergedFromContactId": "XPLSw2SVagl12LMDeTmQ",  "createdBy": "user123"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "61dd0feac077f72010f78804",  "altType": "location",  "altId": "3SwdhCu3svxI8AKsPJt6",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "currency": "USD",  "amount": "100",  "status": "succeeded",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "entityType": "order",  "entityId": "61dd0fe9c077f73e67f78803",  "entitySource": "{ type: \"funnel\", id: \"BDBMEghdIUaqMPEsK349\", subType: \"two_step_order_form\", name: \"new funnel\" }",  "chargeId": "in_1KGcXDCScnf89tZohCsmImwE",  "chargeSnapshot": "{ id: \"in_1KGcXDCScnf89tZohCsmImwE\", object: \"invoice\", account_country: \"US\",  account_name:  \"GHL-Testing\" }",  "invoiceId": "in_1KGcXDCScnf89tZohCsmImwE",  "subscriptionId": "sub_1KGcXDCScnf89tZoVkoEMCEL",  "paymentProvider": "{ type: \"stripe\", connectedAccount: { _id: \"612ca676b484b241fef9d962\", accountId: \"acct_1Ihw53CScnf89tZo\" } }",  "ipAddress": "107.178.194.224",  "meta": "{ stepId: \"af7c731e-e36f-4152-bd1a-3f69a31d6d6d\", pageId: \"A8ltotc2jZxurJba4e3Y\", pageUrl: \"/v2/preview/A8ltotc2jZxurJba4e3Y\" }",  "markAsTest": "false",  "isParent": "false",  "amountRefunded": "10",  "receiptId": "6492fbea489bc07892c6defb",  "qboSynced": "false",  "qboResponse": "{ domain: \"QBO\", sparse: false, Id: \"180\", SyncToken: \"0\", TotalAmt: 25 }",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "mergedFromContactId": "XPLSw2SVagl12LMDeTmQ",  "createdBy": "user123"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "61dd0feac077f72010f78804",  "altType": "location",  "altId": "3SwdhCu3svxI8AKsPJt6",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "currency": "USD",  "amount": "100",  "status": "succeeded",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "entityType": "order",  "entityId": "61dd0fe9c077f73e67f78803",  "entitySource": "{ type: \"funnel\", id: \"BDBMEghdIUaqMPEsK349\", subType: \"two_step_order_form\", name: \"new funnel\" }",  "chargeId": "in_1KGcXDCScnf89tZohCsmImwE",  "chargeSnapshot": "{ id: \"in_1KGcXDCScnf89tZohCsmImwE\", object: \"invoice\", account_country: \"US\",  account_name:  \"GHL-Testing\" }",  "invoiceId": "in_1KGcXDCScnf89tZohCsmImwE",  "subscriptionId": "sub_1KGcXDCScnf89tZoVkoEMCEL",  "paymentProvider": "{ type: \"stripe\", connectedAccount: { _id: \"612ca676b484b241fef9d962\", accountId: \"acct_1Ihw53CScnf89tZo\" } }",  "ipAddress": "107.178.194.224",  "meta": "{ stepId: \"af7c731e-e36f-4152-bd1a-3f69a31d6d6d\", pageId: \"A8ltotc2jZxurJba4e3Y\", pageUrl: \"/v2/preview/A8ltotc2jZxurJba4e3Y\" }",  "markAsTest": "false",  "isParent": "false",  "amountRefunded": "10",  "receiptId": "6492fbea489bc07892c6defb",  "qboSynced": "false",  "qboResponse": "{ domain: \"QBO\", sparse: false, Id: \"180\", SyncToken: \"0\", TotalAmt: 25 }",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "mergedFromContactId": "XPLSw2SVagl12LMDeTmQ",  "createdBy": "user123"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/payments/transactions/:transactionId' \

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

	  const response = await highLevel.payments.getTransactionById({

	    'transactionId': '61dd0feac077f72010f78804',

	    'locationId': '3SwdhCu3svxI8AKsPJt6',

	    'altId': '3SwdhCu3svxI8AKsPJt6',

	    'altType': 'location'

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

	  url: 'https://services.leadconnectorhq.com/payments/transactions/:transactionId',

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

	  'path': '/payments/transactions/:transactionId',

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

	  'url': 'https://services.leadconnectorhq.com/payments/transactions/:transactionId',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/payments/transactions/:transactionId')

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

	conn.request("GET", "/payments/transactions/:transactionId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/payments/transactions/:transactionId"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/payments/transactions/:transactionId',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/payments/transactions/:transactionId', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/payments/transactions/:transactionId');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/payments/transactions/:transactionId');

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

	  .url("https://services.leadconnectorhq.com/payments/transactions/:transactionId")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/payments/transactions/:transactionId")

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

	

	  url := "https://services.leadconnectorhq.com/payments/transactions/:transactionId"

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

	

	url = URI("https://services.leadconnectorhq.com/payments/transactions/:transactionId")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/transactions/:transactionId' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

