# Get Blog posts by Blog ID

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/blogs/posts/all`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: blogs/posts.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ✅ | blogId string required Example: 66f429b8afdce84227a4610d |
| `blogId` | ✅ | limit number required Example: 4 |
| `limit` | ✅ | offset number required Example: 0 |
| `offset` | ❌ | searchTerm string search for any post by name Example: ai news |
| `searchTerm` | ❌ | status string Possible values: [ ALL , PUBLISHED , SCHEDULED , ARCHIVED , DRAFT ] Example: PUBLISHED |
| `status` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "blogs": [
    {
      "categories": [
        "659ecabc4a37969a2b7cc370",
        "6683abde331c041f32c07aee"
      ],
      "tags": [
        "Apple",
        "Banana"
      ],
      "archived": false,
      "_id": "66c381b38be80858b9af62b6",
      "title": "Banana is good source of energy",
      "description": "Description",
      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",
      "status": "PUBLISHED",
      "imageAltText": "alt",
      "urlSlug": "banana-good-energy",
      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",
      "author": "659ec9634a3796e4e47cc360",
      "publishedAt": "2024-08-19T17:14:57.000Z",
      "updatedAt": "2024-08-19T17:32:36.182Z"
    }
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/blogs/posts/all' \

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

	  const response = await highLevel.blogs.getBlogPost({

	    'locationId': 've9EPM428h8vShlRW1KT',

	    'blogId': '66f429b8afdce84227a4610d',

	    'limit': 4,

	    'offset': 0,

	    'searchTerm': 'ai news',

	    'status': 'PUBLISHED'

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

	  url: 'https://services.leadconnectorhq.com/blogs/posts/all',

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

	  'path': '/blogs/posts/all',

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

	  'url': 'https://services.leadconnectorhq.com/blogs/posts/all',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/blogs/posts/all')

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

	conn.request("GET", "/blogs/posts/all", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/blogs/posts/all"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/blogs/posts/all',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/blogs/posts/all', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/blogs/posts/all');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/blogs/posts/all');

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

	  .url("https://services.leadconnectorhq.com/blogs/posts/all")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/blogs/posts/all")

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

	

	  url := "https://services.leadconnectorhq.com/blogs/posts/all"

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

	

	url = URI("https://services.leadconnectorhq.com/blogs/posts/all")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/blogs/posts/all' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

