# Get Subscription by ID

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: payments/subscriptions.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `subscriptionId` | ❌ |  |

### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `altId` | ✅ | altType string required Possible values: [ location ] AltType is the type of identifier. Example: location |
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
  "_id": "64bf78af39118e4011926cba",
  "altType": "location",
  "altId": "3SwdhCu3svxI8AKsPJt6",
  "contactId": "XPLSw2SVagl12LMDeTmQ",
  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",
  "coupon": "{ _id: \"6374c6926d119a393fe1e556\", usageCount: 5260, altId: \"jVFIxsMY19D94nOSIOEO\", altType: \"location\", name: \"FREE-100%\", code: \"FREE100\", discountType: \"percentage\", discountValue: 100 }",
  "currency": "USD",
  "amount": "100",
  "status": "active",
  "liveMode": "false",
  "entityType": "order",
  "entityId": "62f4db0f3059ecee61379012",
  "entitySource": "{ type: \"funnel\", id: \"lx6ROqruHGVQD2PZwFxK\", subType: \"upsell\", name: \"test funnel\" }",
  "subscriptionId": "I-0UE609H8E43P",
  "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",
  "paymentProvider": "{ type: \"paypal\", connectedAccount: { _id: \"64410debdc8f3b0503523abb\", merchantClientId: \"AeXtjrxdgsJiCPwQt5jML5pH-0mwmLs-tH7ub4Uo3IrDKvRl34FvJy8niI6E1wmS_pryIRdNllyVl58b\" } }",
  "ipAddress": "103.100.16.82",
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "meta": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",
  "markAsTest": "false",
  "schedule": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",
  "autoPayment": "{ customerId: \"908879612\", paymentMethodId: \"908646635\" }",
  "recurringProduct": "{ locationId: \"Z4Bxl8J4SaPEPLq9IQ8g\", funnel: \"bQHJWKcyjiKjk4BHv91g\", step: \"2281a993-8a75-4b48-9912-571f29c99a74\", name: \"Sofa Set\" }",
  "canceledAt": "2023-11-20T10:23:36.515Z",
  "canceledBy": "qUuXUiB2AiA2DIthEicP",
  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a",
  "createdBy": "user123"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "64bf78af39118e4011926cba",  "altType": "location",  "altId": "3SwdhCu3svxI8AKsPJt6",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "coupon": "{ _id: \"6374c6926d119a393fe1e556\", usageCount: 5260, altId: \"jVFIxsMY19D94nOSIOEO\", altType: \"location\", name: \"FREE-100%\", code: \"FREE100\", discountType: \"percentage\", discountValue: 100 }",  "currency": "USD",  "amount": "100",  "status": "active",  "liveMode": "false",  "entityType": "order",  "entityId": "62f4db0f3059ecee61379012",  "entitySource": "{ type: \"funnel\", id: \"lx6ROqruHGVQD2PZwFxK\", subType: \"upsell\", name: \"test funnel\" }",  "subscriptionId": "I-0UE609H8E43P",  "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",  "paymentProvider": "{ type: \"paypal\", connectedAccount: { _id: \"64410debdc8f3b0503523abb\", merchantClientId: \"AeXtjrxdgsJiCPwQt5jML5pH-0mwmLs-tH7ub4Uo3IrDKvRl34FvJy8niI6E1wmS_pryIRdNllyVl58b\" } }",  "ipAddress": "103.100.16.82",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "meta": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",  "markAsTest": "false",  "schedule": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",  "autoPayment": "{ customerId: \"908879612\", paymentMethodId: \"908646635\" }",  "recurringProduct": "{ locationId: \"Z4Bxl8J4SaPEPLq9IQ8g\", funnel: \"bQHJWKcyjiKjk4BHv91g\", step: \"2281a993-8a75-4b48-9912-571f29c99a74\", name: \"Sofa Set\" }",  "canceledAt": "2023-11-20T10:23:36.515Z",  "canceledBy": "qUuXUiB2AiA2DIthEicP",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a",  "createdBy": "user123"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "64bf78af39118e4011926cba",  "altType": "location",  "altId": "3SwdhCu3svxI8AKsPJt6",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "coupon": "{ _id: \"6374c6926d119a393fe1e556\", usageCount: 5260, altId: \"jVFIxsMY19D94nOSIOEO\", altType: \"location\", name: \"FREE-100%\", code: \"FREE100\", discountType: \"percentage\", discountValue: 100 }",  "currency": "USD",  "amount": "100",  "status": "active",  "liveMode": "false",  "entityType": "order",  "entityId": "62f4db0f3059ecee61379012",  "entitySource": "{ type: \"funnel\", id: \"lx6ROqruHGVQD2PZwFxK\", subType: \"upsell\", name: \"test funnel\" }",  "subscriptionId": "I-0UE609H8E43P",  "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",  "paymentProvider": "{ type: \"paypal\", connectedAccount: { _id: \"64410debdc8f3b0503523abb\", merchantClientId: \"AeXtjrxdgsJiCPwQt5jML5pH-0mwmLs-tH7ub4Uo3IrDKvRl34FvJy8niI6E1wmS_pryIRdNllyVl58b\" } }",  "ipAddress": "103.100.16.82",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "meta": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",  "markAsTest": "false",  "schedule": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",  "autoPayment": "{ customerId: \"908879612\", paymentMethodId: \"908646635\" }",  "recurringProduct": "{ locationId: \"Z4Bxl8J4SaPEPLq9IQ8g\", funnel: \"bQHJWKcyjiKjk4BHv91g\", step: \"2281a993-8a75-4b48-9912-571f29c99a74\", name: \"Sofa Set\" }",  "canceledAt": "2023-11-20T10:23:36.515Z",  "canceledBy": "qUuXUiB2AiA2DIthEicP",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a",  "createdBy": "user123"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "64bf78af39118e4011926cba",  "altType": "location",  "altId": "3SwdhCu3svxI8AKsPJt6",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "coupon": "{ _id: \"6374c6926d119a393fe1e556\", usageCount: 5260, altId: \"jVFIxsMY19D94nOSIOEO\", altType: \"location\", name: \"FREE-100%\", code: \"FREE100\", discountType: \"percentage\", discountValue: 100 }",  "currency": "USD",  "amount": "100",  "status": "active",  "liveMode": "false",  "entityType": "order",  "entityId": "62f4db0f3059ecee61379012",  "entitySource": "{ type: \"funnel\", id: \"lx6ROqruHGVQD2PZwFxK\", subType: \"upsell\", name: \"test funnel\" }",  "subscriptionId": "I-0UE609H8E43P",  "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",  "paymentProvider": "{ type: \"paypal\", connectedAccount: { _id: \"64410debdc8f3b0503523abb\", merchantClientId: \"AeXtjrxdgsJiCPwQt5jML5pH-0mwmLs-tH7ub4Uo3IrDKvRl34FvJy8niI6E1wmS_pryIRdNllyVl58b\" } }",  "ipAddress": "103.100.16.82",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "meta": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",  "markAsTest": "false",  "schedule": "{ collection: \"transactionsv2\", id: \"6320652f0f664b6632006920\" }",  "autoPayment": "{ customerId: \"908879612\", paymentMethodId: \"908646635\" }",  "recurringProduct": "{ locationId: \"Z4Bxl8J4SaPEPLq9IQ8g\", funnel: \"bQHJWKcyjiKjk4BHv91g\", step: \"2281a993-8a75-4b48-9912-571f29c99a74\", name: \"Sofa Set\" }",  "canceledAt": "2023-11-20T10:23:36.515Z",  "canceledBy": "qUuXUiB2AiA2DIthEicP",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a",  "createdBy": "user123"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId' \

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

	  const response = await highLevel.payments.getSubscriptionById({

	    'subscriptionId': '6322e9c9e39fc14ab3ed7042',

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

	  url: 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId',

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

	  'path': '/payments/subscriptions/:subscriptionId',

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

	  'url': 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId')

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

	conn.request("GET", "/payments/subscriptions/:subscriptionId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId');

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

	  .url("https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId")

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

	

	  url := "https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId"

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

	

	url = URI("https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/subscriptions/:subscriptionId' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

