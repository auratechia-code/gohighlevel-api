# Update Conversation

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/conversations/:conversationId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: conversations.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `conversationId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "success": true,
  "conversation": {
    "id": "tDtDnQdgm2LXpyiqYvZ6",
    "locationId": "tDtDnQdgm2LXpyiqYvZ6",
    "contactId": "tDtDnQdgm2LXpyiqYvZ6",
    "assignedTo": "tDtDnQdgm2LXpyiqYvZ6",
    "userId": "tDtDnQdgm2LXpyiqYvZ6",
    "lastMessageBody": "Hello, this is the message body",
    "lastMessageDate": "1628008053263",
    "lastMessageType": "TYPE_CALL",
    "unreadCount": 1,
    "inbox": true,
    "starred": true,
    "deleted": false
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "success": true,  "conversation": {    "id": "tDtDnQdgm2LXpyiqYvZ6",    "locationId": "tDtDnQdgm2LXpyiqYvZ6",    "contactId": "tDtDnQdgm2LXpyiqYvZ6",    "assignedTo": "tDtDnQdgm2LXpyiqYvZ6",    "userId": "tDtDnQdgm2LXpyiqYvZ6",    "lastMessageBody": "Hello, this is the message body",    "lastMessageDate": "1628008053263",    "lastMessageType": "TYPE_CALL",    "unreadCount": 1,    "inbox": true,    "starred": true,    "deleted": false  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "success": true,  "conversation": {    "id": "tDtDnQdgm2LXpyiqYvZ6",    "locationId": "tDtDnQdgm2LXpyiqYvZ6",    "contactId": "tDtDnQdgm2LXpyiqYvZ6",    "assignedTo": "tDtDnQdgm2LXpyiqYvZ6",    "userId": "tDtDnQdgm2LXpyiqYvZ6",    "lastMessageBody": "Hello, this is the message body",    "lastMessageDate": "1628008053263",    "lastMessageType": "TYPE_CALL",    "unreadCount": 1,    "inbox": true,    "starred": true,    "deleted": false  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/conversations/:conversationId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

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

	  const response = await highLevel.conversations.updateConversation({

	    'conversationId': 'tDtDnQdgm2LXpyiqYvZ6'

	  },

	  {

	    'locationId': 'tDtDnQdgm2LXpyiqYvZ6',

	    'unreadCount': 1,

	    'starred': true,

	    'feedback': {}

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

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/conversations/:conversationId',

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

	  'method': 'PUT',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/conversations/:conversationId',

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

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/conversations/:conversationId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	    "unreadCount": 1,

	    "starred": true,

	    "feedback": {}

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/conversations/:conversationId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	    "unreadCount": 1,

	    "starred": true,

	    "feedback": {}

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

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": True,

	  "feedback": {}

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/conversations/:conversationId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/conversations/:conversationId"

	

	payload = json.dumps({

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": True,

	  "feedback": {}

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("PUT", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/conversations/:conversationId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

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

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/conversations/:conversationId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/conversations/:conversationId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "tDtDnQdgm2LXpyiqYvZ6",\n  "unreadCount": 1,\n  "starred": true,\n  "feedback": {}\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/conversations/:conversationId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"tDtDnQdgm2LXpyiqYvZ6\",\n  \"unreadCount\": 1,\n  \"starred\": true,\n  \"feedback\": {}\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/conversations/:conversationId")

	  .method("PUT", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/conversations/:conversationId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"tDtDnQdgm2LXpyiqYvZ6\",\n  \"unreadCount\": 1,\n  \"starred\": true,\n  \"feedback\": {}\n}")

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

	

	  url := "https://services.leadconnectorhq.com/conversations/:conversationId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

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

	

	url = URI("https://services.leadconnectorhq.com/conversations/:conversationId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "tDtDnQdgm2LXpyiqYvZ6",

	  "unreadCount": 1,

	  "starred": true,

	  "feedback": {}

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

	  `"locationId`": `"tDtDnQdgm2LXpyiqYvZ6`",

	  `"unreadCount`": 1,

	  `"starred`": true,

	  `"feedback`": {}

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversations/:conversationId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

