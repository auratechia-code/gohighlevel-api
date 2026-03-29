# Create a new FAQ inside knowledge base

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/knowledge-bases/faqs`

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
### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Authorization` | ✅ | Version string required Possible values: [ 2021-04-15 ] API Version |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "success": true,
  "faq": {
    "id": "3rzeElC1FOVY91veVBkp",
    "question": "What is 1+2?",
    "questionLowerCase": "what is 1+2?",
    "answer": "3",
    "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",
    "locationId": "qIyivCmsuEOSnyoFYEej",
    "trainedUrlId": "688e6b6d8a1887e6d94d1475",
    "deleted": false,
    "createdAt": "2025-08-02T19:47:57.243Z",
    "updatedAt": "2025-08-02T19:47:57.243Z"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "success": true,  "faq": {    "id": "3rzeElC1FOVY91veVBkp",    "question": "What is 1+2?",    "questionLowerCase": "what is 1+2?",    "answer": "3",    "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",    "locationId": "qIyivCmsuEOSnyoFYEej",    "trainedUrlId": "688e6b6d8a1887e6d94d1475",    "deleted": false,    "createdAt": "2025-08-02T19:47:57.243Z",    "updatedAt": "2025-08-02T19:47:57.243Z"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "success": true,  "faq": {    "id": "3rzeElC1FOVY91veVBkp",    "question": "What is 1+2?",    "questionLowerCase": "what is 1+2?",    "answer": "3",    "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",    "locationId": "qIyivCmsuEOSnyoFYEej",    "trainedUrlId": "688e6b6d8a1887e6d94d1475",    "deleted": false,    "createdAt": "2025-08-02T19:47:57.243Z",    "updatedAt": "2025-08-02T19:47:57.243Z"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "success": true,  "faq": {    "id": "3rzeElC1FOVY91veVBkp",    "question": "What is 1+2?",    "questionLowerCase": "what is 1+2?",    "answer": "3",    "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",    "locationId": "qIyivCmsuEOSnyoFYEej",    "trainedUrlId": "688e6b6d8a1887e6d94d1475",    "deleted": false,    "createdAt": "2025-08-02T19:47:57.243Z",    "updatedAt": "2025-08-02T19:47:57.243Z"  }}
```
</details>

<details>
<summary>Response 500</summary>

```json
{  "success": true,  "faq": {    "id": "3rzeElC1FOVY91veVBkp",    "question": "What is 1+2?",    "questionLowerCase": "what is 1+2?",    "answer": "3",    "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",    "locationId": "qIyivCmsuEOSnyoFYEej",    "trainedUrlId": "688e6b6d8a1887e6d94d1475",    "deleted": false,    "createdAt": "2025-08-02T19:47:57.243Z",    "updatedAt": "2025-08-02T19:47:57.243Z"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/knowledge-bases/faqs' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	  const response = await highLevel.knowledgeBase.create({

	    'locationId': 'HqDZpF8GH3qvgJTmKCoL',

	    'question': 'What is the capital of France?',

	    'answer': 'The capital of France is Paris.',

	    'knowledgeBaseId': '710KoEzy793Fxubft0bc'

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

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/knowledge-bases/faqs',

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

	  'path': '/knowledge-bases/faqs',

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

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/knowledge-bases/faqs',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "HqDZpF8GH3qvgJTmKCoL",

	    "question": "What is the capital of France?",

	    "answer": "The capital of France is Paris.",

	    "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/knowledge-bases/faqs')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "HqDZpF8GH3qvgJTmKCoL",

	    "question": "What is the capital of France?",

	    "answer": "The capital of France is Paris.",

	    "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/knowledge-bases/faqs", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/knowledge-bases/faqs"

	

	payload = json.dumps({

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/knowledge-bases/faqs',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/knowledge-bases/faqs', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/knowledge-bases/faqs');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "HqDZpF8GH3qvgJTmKCoL",\n  "question": "What is the capital of France?",\n  "answer": "The capital of France is Paris.",\n  "knowledgeBaseId": "710KoEzy793Fxubft0bc"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/knowledge-bases/faqs');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"HqDZpF8GH3qvgJTmKCoL\",\n  \"question\": \"What is the capital of France?\",\n  \"answer\": \"The capital of France is Paris.\",\n  \"knowledgeBaseId\": \"710KoEzy793Fxubft0bc\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/knowledge-bases/faqs")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/knowledge-bases/faqs")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"HqDZpF8GH3qvgJTmKCoL\",\n  \"question\": \"What is the capital of France?\",\n  \"answer\": \"The capital of France is Paris.\",\n  \"knowledgeBaseId\": \"710KoEzy793Fxubft0bc\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/knowledge-bases/faqs"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	

	url = URI("https://services.leadconnectorhq.com/knowledge-bases/faqs")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "HqDZpF8GH3qvgJTmKCoL",

	  "question": "What is the capital of France?",

	  "answer": "The capital of France is Paris.",

	  "knowledgeBaseId": "710KoEzy793Fxubft0bc"

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

	  `"locationId`": `"HqDZpF8GH3qvgJTmKCoL`",

	  `"question`": `"What is the capital of France?`",

	  `"answer`": `"The capital of France is Paris.`",

	  `"knowledgeBaseId`": `"710KoEzy793Fxubft0bc`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/knowledge-bases/faqs' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

