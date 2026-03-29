# Create White-label Integration Provider

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: payments/integration.write
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
  "_id": "65cb47dda50f4f13ced4b870",
  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",
  "altType": "location",
  "title": "Example",
  "route": "epd",
  "provider": "nmi",
  "description": "Lorem",
  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",
  "createdAt": "2024-02-13T10:43:41.026Z",
  "updatedAt": "2024-02-13T10:43:41.026Z"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

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

	  const response = await highLevel.payments.createIntegration provider({

	    'altId': '6578278e879ad2646715ba9c',

	    'altType': 'location',

	    'uniqueName': 'easy-direct',

	    'title': 'Title',

	    'provider': {

	      'AUTHORIZE_NET': 'authorize-net',

	      'NMI': 'nmi'

	    },

	    'description': 'Description',

	    'imageUrl': 'https://example.com/image.jpg'

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

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel',

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

	  'path': '/payments/integrations/provider/whitelabel',

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

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "uniqueName": "easy-direct",

	    "title": "Title",

	    "provider": {

	      "AUTHORIZE_NET": "authorize-net",

	      "NMI": "nmi"

	    },

	    "description": "Description",

	    "imageUrl": "https://example.com/image.jpg"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "altId": "6578278e879ad2646715ba9c",

	    "altType": "location",

	    "uniqueName": "easy-direct",

	    "title": "Title",

	    "provider": {

	      "AUTHORIZE_NET": "authorize-net",

	      "NMI": "nmi"

	    },

	    "description": "Description",

	    "imageUrl": "https://example.com/image.jpg"

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

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/payments/integrations/provider/whitelabel", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel"

	

	payload = json.dumps({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

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

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "altId": "6578278e879ad2646715ba9c",\n  "altType": "location",\n  "uniqueName": "easy-direct",\n  "title": "Title",\n  "provider": {\n    "AUTHORIZE_NET": "authorize-net",\n    "NMI": "nmi"\n  },\n  "description": "Description",\n  "imageUrl": "https://example.com/image.jpg"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"uniqueName\": \"easy-direct\",\n  \"title\": \"Title\",\n  \"provider\": {\n    \"AUTHORIZE_NET\": \"authorize-net\",\n    \"NMI\": \"nmi\"\n  },\n  \"description\": \"Description\",\n  \"imageUrl\": \"https://example.com/image.jpg\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"altId\": \"6578278e879ad2646715ba9c\",\n  \"altType\": \"location\",\n  \"uniqueName\": \"easy-direct\",\n  \"title\": \"Title\",\n  \"provider\": {\n    \"AUTHORIZE_NET\": \"authorize-net\",\n    \"NMI\": \"nmi\"\n  },\n  \"description\": \"Description\",\n  \"imageUrl\": \"https://example.com/image.jpg\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

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

	

	url = URI("https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "altId": "6578278e879ad2646715ba9c",

	  "altType": "location",

	  "uniqueName": "easy-direct",

	  "title": "Title",

	  "provider": {

	    "AUTHORIZE_NET": "authorize-net",

	    "NMI": "nmi"

	  },

	  "description": "Description",

	  "imageUrl": "https://example.com/image.jpg"

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

	  `"altId`": `"6578278e879ad2646715ba9c`",

	  `"altType`": `"location`",

	  `"uniqueName`": `"easy-direct`",

	  `"title`": `"Title`",

	  `"provider`": {

	    `"AUTHORIZE_NET`": `"authorize-net`",

	    `"NMI`": `"nmi`"

	  },

	  `"description`": `"Description`",

	  `"imageUrl`": `"https://example.com/image.jpg`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/payments/integrations/provider/whitelabel' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

