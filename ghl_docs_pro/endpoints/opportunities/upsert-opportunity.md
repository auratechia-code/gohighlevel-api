# Upsert Opportunity

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/opportunities/upsert`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: opportunities.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "opportunity": {},
  "new": true
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "opportunity": {},  "new": true}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "opportunity": {},  "new": true}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "opportunity": {},  "new": true}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/opportunities/upsert' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	  const response = await highLevel.opportunities.upsertOpportunity({

	    'id': 'yWQobCRIhRguQtD2llvk',

	    'pipelineId': 'bCkKGpDsyPP4peuKowkG',

	    'locationId': 'CLu7BaljjqrEjBGKTNNe',

	    'followers': 'LiKJ2vnRg5ETM8Z19K7',

	    'isRemoveAllFollowers': true,

	    'followersActionType': 'add',

	    'name': 'opportunity name',

	    'status': 'open',

	    'pipelineStageId': '7915dedc-8f18-44d5-8bc3-77c04e994a10',

	    'monetaryValue': 220,

	    'assignedTo': '082goXVW3lIExEQPOnd3',

	    'lostReasonId': 'CLu7BaljjqrEjBGKTNNe'

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

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/opportunities/upsert',

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

	  'path': '/opportunities/upsert',

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

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/opportunities/upsert',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "id": "yWQobCRIhRguQtD2llvk",

	    "pipelineId": "bCkKGpDsyPP4peuKowkG",

	    "locationId": "CLu7BaljjqrEjBGKTNNe",

	    "followers": "LiKJ2vnRg5ETM8Z19K7",

	    "isRemoveAllFollowers": true,

	    "followersActionType": "add",

	    "name": "opportunity name",

	    "status": "open",

	    "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	    "monetaryValue": 220,

	    "assignedTo": "082goXVW3lIExEQPOnd3",

	    "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/opportunities/upsert')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "id": "yWQobCRIhRguQtD2llvk",

	    "pipelineId": "bCkKGpDsyPP4peuKowkG",

	    "locationId": "CLu7BaljjqrEjBGKTNNe",

	    "followers": "LiKJ2vnRg5ETM8Z19K7",

	    "isRemoveAllFollowers": true,

	    "followersActionType": "add",

	    "name": "opportunity name",

	    "status": "open",

	    "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	    "monetaryValue": 220,

	    "assignedTo": "082goXVW3lIExEQPOnd3",

	    "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": True,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/opportunities/upsert", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/opportunities/upsert"

	

	payload = json.dumps({

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": True,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/opportunities/upsert',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/opportunities/upsert', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/opportunities/upsert');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "id": "yWQobCRIhRguQtD2llvk",\n  "pipelineId": "bCkKGpDsyPP4peuKowkG",\n  "locationId": "CLu7BaljjqrEjBGKTNNe",\n  "followers": "LiKJ2vnRg5ETM8Z19K7",\n  "isRemoveAllFollowers": true,\n  "followersActionType": "add",\n  "name": "opportunity name",\n  "status": "open",\n  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",\n  "monetaryValue": 220,\n  "assignedTo": "082goXVW3lIExEQPOnd3",\n  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/opportunities/upsert');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"id\": \"yWQobCRIhRguQtD2llvk\",\n  \"pipelineId\": \"bCkKGpDsyPP4peuKowkG\",\n  \"locationId\": \"CLu7BaljjqrEjBGKTNNe\",\n  \"followers\": \"LiKJ2vnRg5ETM8Z19K7\",\n  \"isRemoveAllFollowers\": true,\n  \"followersActionType\": \"add\",\n  \"name\": \"opportunity name\",\n  \"status\": \"open\",\n  \"pipelineStageId\": \"7915dedc-8f18-44d5-8bc3-77c04e994a10\",\n  \"monetaryValue\": 220,\n  \"assignedTo\": \"082goXVW3lIExEQPOnd3\",\n  \"lostReasonId\": \"CLu7BaljjqrEjBGKTNNe\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/opportunities/upsert")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/opportunities/upsert")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"id\": \"yWQobCRIhRguQtD2llvk\",\n  \"pipelineId\": \"bCkKGpDsyPP4peuKowkG\",\n  \"locationId\": \"CLu7BaljjqrEjBGKTNNe\",\n  \"followers\": \"LiKJ2vnRg5ETM8Z19K7\",\n  \"isRemoveAllFollowers\": true,\n  \"followersActionType\": \"add\",\n  \"name\": \"opportunity name\",\n  \"status\": \"open\",\n  \"pipelineStageId\": \"7915dedc-8f18-44d5-8bc3-77c04e994a10\",\n  \"monetaryValue\": 220,\n  \"assignedTo\": \"082goXVW3lIExEQPOnd3\",\n  \"lostReasonId\": \"CLu7BaljjqrEjBGKTNNe\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/opportunities/upsert"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	

	url = URI("https://services.leadconnectorhq.com/opportunities/upsert")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "id": "yWQobCRIhRguQtD2llvk",

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "locationId": "CLu7BaljjqrEjBGKTNNe",

	  "followers": "LiKJ2vnRg5ETM8Z19K7",

	  "isRemoveAllFollowers": true,

	  "followersActionType": "add",

	  "name": "opportunity name",

	  "status": "open",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "lostReasonId": "CLu7BaljjqrEjBGKTNNe"

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

	  `"id`": `"yWQobCRIhRguQtD2llvk`",

	  `"pipelineId`": `"bCkKGpDsyPP4peuKowkG`",

	  `"locationId`": `"CLu7BaljjqrEjBGKTNNe`",

	  `"followers`": `"LiKJ2vnRg5ETM8Z19K7`",

	  `"isRemoveAllFollowers`": true,

	  `"followersActionType`": `"add`",

	  `"name`": `"opportunity name`",

	  `"status`": `"open`",

	  `"pipelineStageId`": `"7915dedc-8f18-44d5-8bc3-77c04e994a10`",

	  `"monetaryValue`": 220,

	  `"assignedTo`": `"082goXVW3lIExEQPOnd3`",

	  `"lostReasonId`": `"CLu7BaljjqrEjBGKTNNe`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/opportunities/upsert' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

