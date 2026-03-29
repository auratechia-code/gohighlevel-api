# List invoices

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/invoices/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: invoices.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `altId` | ✅ | altType string required Possible values: [ location ] Alt Type Example: location |
| `altType` | ❌ | status string status to be filtered |
| `status` | ❌ | startAt string startAt in YYYY-MM-DD format Example: 2023-01-01 |
| `startAt` | ❌ | endAt string endAt in YYYY-MM-DD format Example: 2023-01-01 |
| `endAt` | ❌ | search string To search for an invoice by id / name / email / phoneNo Example: Alex |
| `search` | ❌ | paymentMode string Possible values: [ default , live , test ] payment mode Example: live |
| `paymentMode` | ❌ | contactId string Contact ID for the invoice Example: AmuzcoPBpgKeccNsFlib |
| `contactId` | ✅ | limit string required Limit the number of items to return Example: 10 |
| `limit` | ✅ | offset string required Number of items to skip Example: 10 |
| `offset` | ❌ | sortField string Possible values: [ issueDate ] The field on which sorting should be applied Example: issueDate |
| `sortField` | ❌ | sortOrder string Possible values: [ ascend , descend ] The order of sort which should be applied for the sortField Example: descend |
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
  "invoices": [
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
      "paymentSchedule": {},
      "totalSummary": {
        "subTotal": 999,
        "discount": 0,
        "tax": 0
      },
      "remindersConfiguration": {
        "reminderExecutionDetailsList": {},
        "reminderSettings": {
          "defaultEmailTemplateId": "dhwjqi2899012990w2u",
          "reminders": [
            {
              "enabled": true,
              "emailTemplate": "default",
              "smsTemplate": "default",
              "emailSubject": "Reminder",
              "reminderId": "9333e45f-a27d-4659-90e5-76c5ef06d094",
              "reminderName": "Special Reminder",
              "reminderTime": "before",
              "intervalType": "daily",
              "maxReminders": 3,
              "reminderInvoiceCondition": "invoice_sent",
              "reminderNumber": 10,
              "startTime": "9:00 AM",
              "endTime": "5:00 PM",
              "timezone": "businessTZ"
            }
          ]
        }
      }
    }
  ],
  "total": 100
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "invoices": [    {      "_id": "6578278e879ad2646715ba9c",      "status": "draft",      "liveMode": false,      "amountPaid": 0,      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "New Invoice",      "businessDetails": {        "name": "Alex",        "address": {          "addressLine1": "9931 Beechwood",          "city": "St. Houston",          "state": "TX",          "countryCode": "USA",          "postalCode": "559-6993"        },        "phoneNo": "+1-214-559-6993",        "website": "www.example.com"      },      "invoiceNumber": "19",      "currency": "USD",      "contactDetails": {        "id": "c6tZZU0rJBf30ZXx9Gli",        "phoneNo": "+1-214-559-6993",        "email": "alex@example.com",        "customFields": [],        "name": "Alex",        "address": {          "countryCode": "US"        }      },      "issueDate": "2023-01-01",      "dueDate": "2023-01-01",      "discount": {        "type": "percentage",        "value": 0      },      "invoiceItems": [        {          "taxes": [],          "_id": "c6tZZU0rJBf30ZXx9Gli",          "productId": "c6tZZU0rJBf30ZXx9Gli",          "priceId": "c6tZZU0rJBf30ZXx9Gli",          "currency": "USD",          "name": "Macbook Pro",          "qty": 1,          "amount": 999        }      ],      "total": 999,      "title": "INVOICE",      "amountDue": 999,      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z",      "automaticTaxesEnabled": true,      "automaticTaxesCalculated": true,      "paymentSchedule": {},      "totalSummary": {        "subTotal": 999,        "discount": 0,        "tax": 0      },      "remindersConfiguration": {        "reminderExecutionDetailsList": {},        "reminderSettings": {          "defaultEmailTemplateId": "dhwjqi2899012990w2u",          "reminders": [            {              "enabled": true,              "emailTemplate": "default",              "smsTemplate": "default",              "emailSubject": "Reminder",              "reminderId": "9333e45f-a27d-4659-90e5-76c5ef06d094",              "reminderName": "Special Reminder",              "reminderTime": "before",              "intervalType": "daily",              "maxReminders": 3,              "reminderInvoiceCondition": "invoice_sent",              "reminderNumber": 10,              "startTime": "9:00 AM",              "endTime": "5:00 PM",              "timezone": "businessTZ"            }          ]        }      }    }  ],  "total": 100}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "invoices": [    {      "_id": "6578278e879ad2646715ba9c",      "status": "draft",      "liveMode": false,      "amountPaid": 0,      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "New Invoice",      "businessDetails": {        "name": "Alex",        "address": {          "addressLine1": "9931 Beechwood",          "city": "St. Houston",          "state": "TX",          "countryCode": "USA",          "postalCode": "559-6993"        },        "phoneNo": "+1-214-559-6993",        "website": "www.example.com"      },      "invoiceNumber": "19",      "currency": "USD",      "contactDetails": {        "id": "c6tZZU0rJBf30ZXx9Gli",        "phoneNo": "+1-214-559-6993",        "email": "alex@example.com",        "customFields": [],        "name": "Alex",        "address": {          "countryCode": "US"        }      },      "issueDate": "2023-01-01",      "dueDate": "2023-01-01",      "discount": {        "type": "percentage",        "value": 0      },      "invoiceItems": [        {          "taxes": [],          "_id": "c6tZZU0rJBf30ZXx9Gli",          "productId": "c6tZZU0rJBf30ZXx9Gli",          "priceId": "c6tZZU0rJBf30ZXx9Gli",          "currency": "USD",          "name": "Macbook Pro",          "qty": 1,          "amount": 999        }      ],      "total": 999,      "title": "INVOICE",      "amountDue": 999,      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z",      "automaticTaxesEnabled": true,      "automaticTaxesCalculated": true,      "paymentSchedule": {},      "totalSummary": {        "subTotal": 999,        "discount": 0,        "tax": 0      },      "remindersConfiguration": {        "reminderExecutionDetailsList": {},        "reminderSettings": {          "defaultEmailTemplateId": "dhwjqi2899012990w2u",          "reminders": [            {              "enabled": true,              "emailTemplate": "default",              "smsTemplate": "default",              "emailSubject": "Reminder",              "reminderId": "9333e45f-a27d-4659-90e5-76c5ef06d094",              "reminderName": "Special Reminder",              "reminderTime": "before",              "intervalType": "daily",              "maxReminders": 3,              "reminderInvoiceCondition": "invoice_sent",              "reminderNumber": 10,              "startTime": "9:00 AM",              "endTime": "5:00 PM",              "timezone": "businessTZ"            }          ]        }      }    }  ],  "total": 100}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "invoices": [    {      "_id": "6578278e879ad2646715ba9c",      "status": "draft",      "liveMode": false,      "amountPaid": 0,      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "New Invoice",      "businessDetails": {        "name": "Alex",        "address": {          "addressLine1": "9931 Beechwood",          "city": "St. Houston",          "state": "TX",          "countryCode": "USA",          "postalCode": "559-6993"        },        "phoneNo": "+1-214-559-6993",        "website": "www.example.com"      },      "invoiceNumber": "19",      "currency": "USD",      "contactDetails": {        "id": "c6tZZU0rJBf30ZXx9Gli",        "phoneNo": "+1-214-559-6993",        "email": "alex@example.com",        "customFields": [],        "name": "Alex",        "address": {          "countryCode": "US"        }      },      "issueDate": "2023-01-01",      "dueDate": "2023-01-01",      "discount": {        "type": "percentage",        "value": 0      },      "invoiceItems": [        {          "taxes": [],          "_id": "c6tZZU0rJBf30ZXx9Gli",          "productId": "c6tZZU0rJBf30ZXx9Gli",          "priceId": "c6tZZU0rJBf30ZXx9Gli",          "currency": "USD",          "name": "Macbook Pro",          "qty": 1,          "amount": 999        }      ],      "total": 999,      "title": "INVOICE",      "amountDue": 999,      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z",      "automaticTaxesEnabled": true,      "automaticTaxesCalculated": true,      "paymentSchedule": {},      "totalSummary": {        "subTotal": 999,        "discount": 0,        "tax": 0      },      "remindersConfiguration": {        "reminderExecutionDetailsList": {},        "reminderSettings": {          "defaultEmailTemplateId": "dhwjqi2899012990w2u",          "reminders": [            {              "enabled": true,              "emailTemplate": "default",              "smsTemplate": "default",              "emailSubject": "Reminder",              "reminderId": "9333e45f-a27d-4659-90e5-76c5ef06d094",              "reminderName": "Special Reminder",              "reminderTime": "before",              "intervalType": "daily",              "maxReminders": 3,              "reminderInvoiceCondition": "invoice_sent",              "reminderNumber": 10,              "startTime": "9:00 AM",              "endTime": "5:00 PM",              "timezone": "businessTZ"            }          ]        }      }    }  ],  "total": 100}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/invoices/' \

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

	  const response = await highLevel.invoices.listInvoices({

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'startAt': '2023-01-01',

	    'endAt': '2023-01-01',

	    'search': 'Alex',

	    'paymentMode': 'live',

	    'contactId': 'AmuzcoPBpgKeccNsFlib',

	    'limit': 10,

	    'offset': 10,

	    'sortField': 'issueDate',

	    'sortOrder': 'descend'

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

	  url: 'https://services.leadconnectorhq.com/invoices/',

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

	  'path': '/invoices/',

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

	  'url': 'https://services.leadconnectorhq.com/invoices/',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/invoices/')

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

	conn.request("GET", "/invoices/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/invoices/"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/invoices/',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/invoices/', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/invoices/');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/invoices/');

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

	  .url("https://services.leadconnectorhq.com/invoices/")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/invoices/")

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

	

	  url := "https://services.leadconnectorhq.com/invoices/"

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

	

	url = URI("https://services.leadconnectorhq.com/invoices/")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/invoices/' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

