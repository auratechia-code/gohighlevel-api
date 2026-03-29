# Create Calendar Resource

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/calendars/resources/:resourceType`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: calendars/resources.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `resourceType` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "locationId": "string",
  "name": "yoga room",
  "resourceType": "equipments",
  "isActive": true,
  "description": "string",
  "quantity": 0,
  "outOfService": 0,
  "capacity": 85,
  "calendarIds": [
    "Jsj0xnlDDjw0SuvX1J13",
    "oCM5feFC86FAAbcO7lJK"
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "locationId": "string",  "name": "yoga room",  "resourceType": "equipments",  "isActive": true,  "description": "string",  "quantity": 0,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "locationId": "string",  "name": "yoga room",  "resourceType": "equipments",  "isActive": true,  "description": "string",  "quantity": 0,  "outOfService": 0,  "capacity": 85,  "calendarIds": [    "Jsj0xnlDDjw0SuvX1J13",    "oCM5feFC86FAAbcO7lJK"  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/calendars/resources/:resourceType' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

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

	  const response = await highLevel.calendars.createCalendarResource({

	    'resourceType': 'resourceType_value'

	  },

	  {

	    'locationId': 'string',

	    'name': 'string',

	    'description': 'string',

	    'quantity': 0,

	    'outOfService': 0,

	    'capacity': 0,

	    'calendarIds': [

	      'string'

	    ]

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

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/calendars/resources/:resourceType',

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

	  'path': '/calendars/resources/:resourceType',

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

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/calendars/resources/:resourceType',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "string",

	    "name": "string",

	    "description": "string",

	    "quantity": 0,

	    "outOfService": 0,

	    "capacity": 0,

	    "calendarIds": [

	      "string"

	    ]

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/calendars/resources/:resourceType')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "string",

	    "name": "string",

	    "description": "string",

	    "quantity": 0,

	    "outOfService": 0,

	    "capacity": 0,

	    "calendarIds": [

	      "string"

	    ]

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

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/calendars/resources/:resourceType", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/calendars/resources/:resourceType"

	

	payload = json.dumps({

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/calendars/resources/:resourceType',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

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

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/calendars/resources/:resourceType', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/calendars/resources/:resourceType');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "string",\n  "name": "string",\n  "description": "string",\n  "quantity": 0,\n  "outOfService": 0,\n  "capacity": 0,\n  "calendarIds": [\n    "string"\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/calendars/resources/:resourceType');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"string\",\n  \"name\": \"string\",\n  \"description\": \"string\",\n  \"quantity\": 0,\n  \"outOfService\": 0,\n  \"capacity\": 0,\n  \"calendarIds\": [\n    \"string\"\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/calendars/resources/:resourceType")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/calendars/resources/:resourceType")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"string\",\n  \"name\": \"string\",\n  \"description\": \"string\",\n  \"quantity\": 0,\n  \"outOfService\": 0,\n  \"capacity\": 0,\n  \"calendarIds\": [\n    \"string\"\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/calendars/resources/:resourceType"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

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

	

	url = URI("https://services.leadconnectorhq.com/calendars/resources/:resourceType")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "string",

	  "name": "string",

	  "description": "string",

	  "quantity": 0,

	  "outOfService": 0,

	  "capacity": 0,

	  "calendarIds": [

	    "string"

	  ]

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

	  `"locationId`": `"string`",

	  `"name`": `"string`",

	  `"description`": `"string`",

	  `"quantity`": 0,

	  `"outOfService`": 0,

	  `"capacity`": 0,

	  `"calendarIds`": [

	    `"string`"

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/resources/:resourceType' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

