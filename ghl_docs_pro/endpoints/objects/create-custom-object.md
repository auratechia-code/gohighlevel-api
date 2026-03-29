# Create Custom Object

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/objects/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: objects/schema.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.
```

## 📥 Parameters
### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "object": {
    "id": "661c06b4ffde146bdb469442",
    "standard": false,
    "key": "custom_objects.pet",
    "labels": {
      "singular": "Pet",
      "plural": "Pets"
    },
    "description": "These are non vaccinated pets",
    "locationId": "Q9DT3OAqEXDLYuob1G32",
    "primaryDisplayProperty": "custom_objects.pet.name",
    "dateAdded": "2024-07-29T15:51:28.071Z",
    "dateUpdated": "2024-07-29T15:51:28.071Z",
    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "object": {    "id": "661c06b4ffde146bdb469442",    "standard": false,    "key": "custom_objects.pet",    "labels": {      "singular": "Pet",      "plural": "Pets"    },    "description": "These are non vaccinated pets",    "locationId": "Q9DT3OAqEXDLYuob1G32",    "primaryDisplayProperty": "custom_objects.pet.name",    "dateAdded": "2024-07-29T15:51:28.071Z",    "dateUpdated": "2024-07-29T15:51:28.071Z",    "type": "The Object type can either USER_DEFINED or SYSTEM_DEFINED"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/objects/' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	  const response = await highLevel.objects.createCustomObjectSchema({

	    'labels': {

	      'singular': 'Pet',

	      'plural': 'Pets'

	    },

	    'key': 'custom_objects.pet',

	    'description': 'These are non vaccinated pets',

	    'locationId': 've9EPM428h8vShlRW1KT',

	    'primaryDisplayPropertyDetails': {

	      'key': 'custom_objects.pet.name',

	      'name': 'Pet name',

	      'dataType': 'TEXT'

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

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

	  }

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/objects/',

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

	  'path': '/objects/',

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

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	  'url': 'https://services.leadconnectorhq.com/objects/',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "labels": {

	      "singular": "Pet",

	      "plural": "Pets"

	    },

	    "key": "custom_objects.pet",

	    "description": "These are non vaccinated pets",

	    "locationId": "ve9EPM428h8vShlRW1KT",

	    "primaryDisplayPropertyDetails": {

	      "key": "custom_objects.pet.name",

	      "name": "Pet name",

	      "dataType": "TEXT"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/objects/')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "labels": {

	      "singular": "Pet",

	      "plural": "Pets"

	    },

	    "key": "custom_objects.pet",

	    "description": "These are non vaccinated pets",

	    "locationId": "ve9EPM428h8vShlRW1KT",

	    "primaryDisplayPropertyDetails": {

	      "key": "custom_objects.pet.name",

	      "name": "Pet name",

	      "dataType": "TEXT"

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

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/objects/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/objects/"

	

	payload = json.dumps({

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/objects/',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

	  }

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/objects/', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/objects/');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "labels": {\n    "singular": "Pet",\n    "plural": "Pets"\n  },\n  "key": "custom_objects.pet",\n  "description": "These are non vaccinated pets",\n  "locationId": "ve9EPM428h8vShlRW1KT",\n  "primaryDisplayPropertyDetails": {\n    "key": "custom_objects.pet.name",\n    "name": "Pet name",\n    "dataType": "TEXT"\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/objects/');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"labels\": {\n    \"singular\": \"Pet\",\n    \"plural\": \"Pets\"\n  },\n  \"key\": \"custom_objects.pet\",\n  \"description\": \"These are non vaccinated pets\",\n  \"locationId\": \"ve9EPM428h8vShlRW1KT\",\n  \"primaryDisplayPropertyDetails\": {\n    \"key\": \"custom_objects.pet.name\",\n    \"name\": \"Pet name\",\n    \"dataType\": \"TEXT\"\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/objects/")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/objects/")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"labels\": {\n    \"singular\": \"Pet\",\n    \"plural\": \"Pets\"\n  },\n  \"key\": \"custom_objects.pet\",\n  \"description\": \"These are non vaccinated pets\",\n  \"locationId\": \"ve9EPM428h8vShlRW1KT\",\n  \"primaryDisplayPropertyDetails\": {\n    \"key\": \"custom_objects.pet.name\",\n    \"name\": \"Pet name\",\n    \"dataType\": \"TEXT\"\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/objects/"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	

	url = URI("https://services.leadconnectorhq.com/objects/")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "labels": {

	    "singular": "Pet",

	    "plural": "Pets"

	  },

	  "key": "custom_objects.pet",

	  "description": "These are non vaccinated pets",

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "primaryDisplayPropertyDetails": {

	    "key": "custom_objects.pet.name",

	    "name": "Pet name",

	    "dataType": "TEXT"

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

	  `"labels`": {

	    `"singular`": `"Pet`",

	    `"plural`": `"Pets`"

	  },

	  `"key`": `"custom_objects.pet`",

	  `"description`": `"These are non vaccinated pets`",

	  `"locationId`": `"ve9EPM428h8vShlRW1KT`",

	  `"primaryDisplayPropertyDetails`": {

	    `"key`": `"custom_objects.pet.name`",

	    `"name`": `"Pet name`",

	    `"dataType`": `"TEXT`"

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/objects/' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

