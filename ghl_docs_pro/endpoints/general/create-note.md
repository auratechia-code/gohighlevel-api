# Create Note

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/contacts/:contactId/notes`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `contactId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "note": {
    "id": "HGPcayliwcdoUFzvbTok",
    "body": "lorem ipsum",
    "userId": "TUcmRxWrjqzJS8EjkxNK",
    "dateAdded": "2021-07-08T12:02:11.285Z",
    "contactId": "TUcmRxWrjqzJS8EjkxNK",
    "title": "Follow-up summary",
    "color": "#FFAA00",
    "pinned": false
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "note": {    "id": "HGPcayliwcdoUFzvbTok",    "body": "lorem ipsum",    "userId": "TUcmRxWrjqzJS8EjkxNK",    "dateAdded": "2021-07-08T12:02:11.285Z",    "contactId": "TUcmRxWrjqzJS8EjkxNK",    "title": "Follow-up summary",    "color": "#FFAA00",    "pinned": false  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "note": {    "id": "HGPcayliwcdoUFzvbTok",    "body": "lorem ipsum",    "userId": "TUcmRxWrjqzJS8EjkxNK",    "dateAdded": "2021-07-08T12:02:11.285Z",    "contactId": "TUcmRxWrjqzJS8EjkxNK",    "title": "Follow-up summary",    "color": "#FFAA00",    "pinned": false  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "note": {    "id": "HGPcayliwcdoUFzvbTok",    "body": "lorem ipsum",    "userId": "TUcmRxWrjqzJS8EjkxNK",    "dateAdded": "2021-07-08T12:02:11.285Z",    "contactId": "TUcmRxWrjqzJS8EjkxNK",    "title": "Follow-up summary",    "color": "#FFAA00",    "pinned": false  }}
```
</details>

## 💻 Code Examples

### NODEJS
#### SDK
```nodejs
	const { HighLevel } = require('@gohighlevel/api-client');

	

	const highLevel = new HighLevel({

	  clientId: 'your_client_id_here',

	  clientSecret: 'your_client_secret_here',

	});

	

	try {

	  const response = await highLevel.contacts.createNote({

	    'contactId': 'sx6wyHhbFdRXh302LLNR'

	  },

	  {

	    'userId': 'GCs5KuzPqTls7vWclkEV',

	    'body': 'lorem ipsum',

	    'title': 'Follow-up summary',

	    'color': '#FFAA00',

	    'pinned': false

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

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": false

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/contacts/:contactId/notes',

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

	  'path': '/contacts/:contactId/notes',

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

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": false

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/contacts/:contactId/notes',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "userId": "GCs5KuzPqTls7vWclkEV",

	    "body": "lorem ipsum",

	    "title": "Follow-up summary",

	    "color": "#FFAA00",

	    "pinned": false

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/contacts/:contactId/notes')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "userId": "GCs5KuzPqTls7vWclkEV",

	    "body": "lorem ipsum",

	    "title": "Follow-up summary",

	    "color": "#FFAA00",

	    "pinned": false

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

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": False

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/contacts/:contactId/notes", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/contacts/:contactId/notes"

	

	payload = json.dumps({

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": False

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/contacts/:contactId/notes',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": false

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

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": false

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/contacts/:contactId/notes', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/contacts/:contactId/notes');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "userId": "GCs5KuzPqTls7vWclkEV",\n  "body": "lorem ipsum",\n  "title": "Follow-up summary",\n  "color": "#FFAA00",\n  "pinned": false\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/contacts/:contactId/notes');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": false

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"userId\": \"GCs5KuzPqTls7vWclkEV\",\n  \"body\": \"lorem ipsum\",\n  \"title\": \"Follow-up summary\",\n  \"color\": \"#FFAA00\",\n  \"pinned\": false\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/contacts/:contactId/notes")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/contacts/:contactId/notes")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"userId\": \"GCs5KuzPqTls7vWclkEV\",\n  \"body\": \"lorem ipsum\",\n  \"title\": \"Follow-up summary\",\n  \"color\": \"#FFAA00\",\n  \"pinned\": false\n}")

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

	

	  url := "https://services.leadconnectorhq.com/contacts/:contactId/notes"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "#FFAA00",

	  "pinned": false

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

	

	url = URI("https://services.leadconnectorhq.com/contacts/:contactId/notes")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "userId": "GCs5KuzPqTls7vWclkEV",

	  "body": "lorem ipsum",

	  "title": "Follow-up summary",

	  "color": "\#FFAA00",

	  "pinned": false

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

	  `"userId`": `"GCs5KuzPqTls7vWclkEV`",

	  `"body`": `"lorem ipsum`",

	  `"title`": `"Follow-up summary`",

	  `"color`": `"#FFAA00`",

	  `"pinned`": false

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/:contactId/notes' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

