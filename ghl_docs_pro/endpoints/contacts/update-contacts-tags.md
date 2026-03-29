# Update Contacts Tags

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type`

## 🔐 Requirements
```text
N/A
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
  "succeded": true,
  "errorCount": 0,
  "responses": [
    {
      "contactId": "qFSqySFkVvNzOSqgGqFi",
      "message": "Tags updated",
      "type": "success",
      "oldTags": [
        "tag-1",
        "tag-2"
      ],
      "tagsAdded": [],
      "tagsRemoved": []
    },
    {
      "contactId": "abcdef",
      "message": "contact id is not a valid firebase id",
      "type": "error"
    },
    {
      "contactId": "qFSqySFkVvNzOSqgGqFi",
      "message": "contact is deleted",
      "type": "error"
    },
    {
      "contactId": "3ualbhnV7j3n3a9r2moD",
      "message": "contact does not belong to location",
      "type": "error"
    }
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-d '{

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

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

	  const response = await highLevel.contacts.createAssociation({

	    'contacts': [

	      'qFSqySFkVvNzOSqgGqFi',

	      'abcdef',

	      'qFSqySFkVvNzOSqgGqFi',

	      '3ualbhnV7j3n3a9r2moD'

	    ],

	    'tags': [

	      'tag-1',

	      'tag-2'

	    ],

	    'locationId': 'asdrwHvLUxlfw5SqKVCN',

	    'removeAllTags': 'false'

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

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type',

	  headers: { 

	    'Content-Type': 'application/json', 

	    'Accept': 'application/json'

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

	  'path': '/contacts/bulk/tags/update/:type',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

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

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  },

	  body: JSON.stringify({

	    "contacts": [

	      "qFSqySFkVvNzOSqgGqFi",

	      "abcdef",

	      "qFSqySFkVvNzOSqgGqFi",

	      "3ualbhnV7j3n3a9r2moD"

	    ],

	    "tags": [

	      "tag-1",

	      "tag-2"

	    ],

	    "locationId": "asdrwHvLUxlfw5SqKVCN",

	    "removeAllTags": "false"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  })

	  .send(JSON.stringify({

	    "contacts": [

	      "qFSqySFkVvNzOSqgGqFi",

	      "abcdef",

	      "qFSqySFkVvNzOSqgGqFi",

	      "3ualbhnV7j3n3a9r2moD"

	    ],

	    "tags": [

	      "tag-1",

	      "tag-2"

	    ],

	    "locationId": "asdrwHvLUxlfw5SqKVCN",

	    "removeAllTags": "false"

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

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

	}

	conn.request("POST", "/contacts/bulk/tags/update/:type", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type"

	

	payload = json.dumps({

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	}',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/json',

	    'Accept: application/json'

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

	  'Accept' => 'application/json'

	];

	$body = '{

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

	));

	$request->setBody('{\n  "contacts": [\n    "qFSqySFkVvNzOSqgGqFi",\n    "abcdef",\n    "qFSqySFkVvNzOSqgGqFi",\n    "3ualbhnV7j3n3a9r2moD"\n  ],\n  "tags": [\n    "tag-1",\n    "tag-2"\n  ],\n  "locationId": "asdrwHvLUxlfw5SqKVCN",\n  "removeAllTags": "false"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

	}');

	$request->setBody($body);

	$request->setOptions(array());

	$request->setHeaders(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"contacts\": [\n    \"qFSqySFkVvNzOSqgGqFi\",\n    \"abcdef\",\n    \"qFSqySFkVvNzOSqgGqFi\",\n    \"3ualbhnV7j3n3a9r2moD\"\n  ],\n  \"tags\": [\n    \"tag-1\",\n    \"tag-2\"\n  ],\n  \"locationId\": \"asdrwHvLUxlfw5SqKVCN\",\n  \"removeAllTags\": \"false\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .body("{\n  \"contacts\": [\n    \"qFSqySFkVvNzOSqgGqFi\",\n    \"abcdef\",\n    \"qFSqySFkVvNzOSqgGqFi\",\n    \"3ualbhnV7j3n3a9r2moD\"\n  ],\n  \"tags\": [\n    \"tag-1\",\n    \"tag-2\"\n  ],\n  \"locationId\": \"asdrwHvLUxlfw5SqKVCN\",\n  \"removeAllTags\": \"false\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

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

	

	url = URI("https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request.body = JSON.dump({

	  "contacts": [

	    "qFSqySFkVvNzOSqgGqFi",

	    "abcdef",

	    "qFSqySFkVvNzOSqgGqFi",

	    "3ualbhnV7j3n3a9r2moD"

	  ],

	  "tags": [

	    "tag-1",

	    "tag-2"

	  ],

	  "locationId": "asdrwHvLUxlfw5SqKVCN",

	  "removeAllTags": "false"

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

	

	$body = @"

	{

	  `"contacts`": [

	    `"qFSqySFkVvNzOSqgGqFi`",

	    `"abcdef`",

	    `"qFSqySFkVvNzOSqgGqFi`",

	    `"3ualbhnV7j3n3a9r2moD`"

	  ],

	  `"tags`": [

	    `"tag-1`",

	    `"tag-2`"

	  ],

	  `"locationId`": `"asdrwHvLUxlfw5SqKVCN`",

	  `"removeAllTags`": `"false`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/bulk/tags/update/:type' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

