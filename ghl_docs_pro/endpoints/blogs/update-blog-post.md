# Update Blog Post

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/blogs/posts/:postId`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: blogs/post-update.write
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
  "updatedBlogPost": {
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
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "updatedBlogPost": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "updatedBlogPost": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "updatedBlogPost": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/blogs/posts/:postId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

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

	  const response = await highLevel.blogs.updateBlogPost({

	    'title': 'Your blog title',

	    'locationId': 'Location ID',

	    'blogId': 'Blog ID',

	    'imageUrl': 'Image URl',

	    'description': 'A short description',

	    'rawHTML': '<h1>Your blog content</h1>',

	    'status': 'PUBLISHED',

	    'imageAltText': 'Alt text for your blog image',

	    'categories': [

	      '9c48df2694a849b6089f9d0d3513efe',

	      '6683abde331c041f32c07aee'

	    ],

	    'tags': [

	      'blog',

	      'seo'

	    ],

	    'author': '6683abde331c041f32c07aea',

	    'urlSlug': 'any-blog-post-url',

	    'wordCount': 100,

	    'canonicalLink': 'https://tryghl.blog/post/testing-unsplash',

	    'publishedAt': '2025-02-05T18:30:47.000Z'

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

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/blogs/posts/:postId',

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

	  'path': '/blogs/posts/:postId',

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

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/blogs/posts/:postId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "title": "Your blog title",

	    "locationId": "Location ID",

	    "blogId": "Blog ID",

	    "imageUrl": "Image URl",

	    "description": "A short description",

	    "rawHTML": "<h1>Your blog content</h1>",

	    "status": "PUBLISHED",

	    "imageAltText": "Alt text for your blog image",

	    "categories": [

	      "9c48df2694a849b6089f9d0d3513efe",

	      "6683abde331c041f32c07aee"

	    ],

	    "tags": [

	      "blog",

	      "seo"

	    ],

	    "author": "6683abde331c041f32c07aea",

	    "urlSlug": "any-blog-post-url",

	    "wordCount": 100,

	    "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	    "publishedAt": "2025-02-05T18:30:47.000Z"

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/blogs/posts/:postId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "title": "Your blog title",

	    "locationId": "Location ID",

	    "blogId": "Blog ID",

	    "imageUrl": "Image URl",

	    "description": "A short description",

	    "rawHTML": "<h1>Your blog content</h1>",

	    "status": "PUBLISHED",

	    "imageAltText": "Alt text for your blog image",

	    "categories": [

	      "9c48df2694a849b6089f9d0d3513efe",

	      "6683abde331c041f32c07aee"

	    ],

	    "tags": [

	      "blog",

	      "seo"

	    ],

	    "author": "6683abde331c041f32c07aea",

	    "urlSlug": "any-blog-post-url",

	    "wordCount": 100,

	    "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	    "publishedAt": "2025-02-05T18:30:47.000Z"

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

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/blogs/posts/:postId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/blogs/posts/:postId"

	

	payload = json.dumps({

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/blogs/posts/:postId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

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

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/blogs/posts/:postId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/blogs/posts/:postId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "title": "Your blog title",\n  "locationId": "Location ID",\n  "blogId": "Blog ID",\n  "imageUrl": "Image URl",\n  "description": "A short description",\n  "rawHTML": "<h1>Your blog content</h1>",\n  "status": "PUBLISHED",\n  "imageAltText": "Alt text for your blog image",\n  "categories": [\n    "9c48df2694a849b6089f9d0d3513efe",\n    "6683abde331c041f32c07aee"\n  ],\n  "tags": [\n    "blog",\n    "seo"\n  ],\n  "author": "6683abde331c041f32c07aea",\n  "urlSlug": "any-blog-post-url",\n  "wordCount": 100,\n  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",\n  "publishedAt": "2025-02-05T18:30:47.000Z"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/blogs/posts/:postId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"title\": \"Your blog title\",\n  \"locationId\": \"Location ID\",\n  \"blogId\": \"Blog ID\",\n  \"imageUrl\": \"Image URl\",\n  \"description\": \"A short description\",\n  \"rawHTML\": \"<h1>Your blog content</h1>\",\n  \"status\": \"PUBLISHED\",\n  \"imageAltText\": \"Alt text for your blog image\",\n  \"categories\": [\n    \"9c48df2694a849b6089f9d0d3513efe\",\n    \"6683abde331c041f32c07aee\"\n  ],\n  \"tags\": [\n    \"blog\",\n    \"seo\"\n  ],\n  \"author\": \"6683abde331c041f32c07aea\",\n  \"urlSlug\": \"any-blog-post-url\",\n  \"wordCount\": 100,\n  \"canonicalLink\": \"https://tryghl.blog/post/testing-unsplash\",\n  \"publishedAt\": \"2025-02-05T18:30:47.000Z\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/blogs/posts/:postId")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/blogs/posts/:postId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"title\": \"Your blog title\",\n  \"locationId\": \"Location ID\",\n  \"blogId\": \"Blog ID\",\n  \"imageUrl\": \"Image URl\",\n  \"description\": \"A short description\",\n  \"rawHTML\": \"<h1>Your blog content</h1>\",\n  \"status\": \"PUBLISHED\",\n  \"imageAltText\": \"Alt text for your blog image\",\n  \"categories\": [\n    \"9c48df2694a849b6089f9d0d3513efe\",\n    \"6683abde331c041f32c07aee\"\n  ],\n  \"tags\": [\n    \"blog\",\n    \"seo\"\n  ],\n  \"author\": \"6683abde331c041f32c07aea\",\n  \"urlSlug\": \"any-blog-post-url\",\n  \"wordCount\": 100,\n  \"canonicalLink\": \"https://tryghl.blog/post/testing-unsplash\",\n  \"publishedAt\": \"2025-02-05T18:30:47.000Z\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/blogs/posts/:postId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

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

	

	url = URI("https://services.leadconnectorhq.com/blogs/posts/:postId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "title": "Your blog title",

	  "locationId": "Location ID",

	  "blogId": "Blog ID",

	  "imageUrl": "Image URl",

	  "description": "A short description",

	  "rawHTML": "<h1>Your blog content</h1>",

	  "status": "PUBLISHED",

	  "imageAltText": "Alt text for your blog image",

	  "categories": [

	    "9c48df2694a849b6089f9d0d3513efe",

	    "6683abde331c041f32c07aee"

	  ],

	  "tags": [

	    "blog",

	    "seo"

	  ],

	  "author": "6683abde331c041f32c07aea",

	  "urlSlug": "any-blog-post-url",

	  "wordCount": 100,

	  "canonicalLink": "https://tryghl.blog/post/testing-unsplash",

	  "publishedAt": "2025-02-05T18:30:47.000Z"

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

	  `"title`": `"Your blog title`",

	  `"locationId`": `"Location ID`",

	  `"blogId`": `"Blog ID`",

	  `"imageUrl`": `"Image URl`",

	  `"description`": `"A short description`",

	  `"rawHTML`": `"<h1>Your blog content</h1>`",

	  `"status`": `"PUBLISHED`",

	  `"imageAltText`": `"Alt text for your blog image`",

	  `"categories`": [

	    `"9c48df2694a849b6089f9d0d3513efe`",

	    `"6683abde331c041f32c07aee`"

	  ],

	  `"tags`": [

	    `"blog`",

	    `"seo`"

	  ],

	  `"author`": `"6683abde331c041f32c07aea`",

	  `"urlSlug`": `"any-blog-post-url`",

	  `"wordCount`": 100,

	  `"canonicalLink`": `"https://tryghl.blog/post/testing-unsplash`",

	  `"publishedAt`": `"2025-02-05T18:30:47.000Z`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/blogs/posts/:postId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

