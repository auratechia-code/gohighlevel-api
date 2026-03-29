# Starts OAuth For Oauth Account

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start`

## 🔐 Requirements
```text
N/A
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `platform` | ❌ |  |

### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ✅ | userId string required User Id Example: u37swmmLbA02zgqKPpxITe2 |
| `userId` | ❌ | page string Page Example: integration |
| `page` | ❌ | reconnect string Reconnect Example: true |
| `reconnect` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Authorization` | ✅ | Version string required Possible values: [ 2021-07-28 ] API Version Example: 2021-07-28 |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{  "statusCode": 400,  "message": "Bad Request"}
```
</details>

<details>
<summary>Response 400</summary>

```json
{
  "statusCode": 400,
  "message": "Bad Request"
}

```
</details>

<details>
<summary>Response 401</summary>

```json
{  "statusCode": 400,  "message": "Bad Request"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "statusCode": 400,  "message": "Bad Request"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start'

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

	  const response = await highLevel.socialPlanner.startOauth({

	    'platform': 'google',

	    'locationId': 'w37swmmLbA02zgqKPpxITe2',

	    'userId': 'u37swmmLbA02zgqKPpxITe2',

	    'page': 'integration',

	    'reconnect': 'true'

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

	  url: 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start',

	  headers: { }

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

	  'path': '/social-media-posting/oauth/:platform/start',

	  'headers': {

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

	  'url': 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start',

	  'headers': {

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start')

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

	headers = {}

	conn.request("GET", "/social-media-posting/oauth/:platform/start", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start"

	

	payload = {}

	headers = {}

	

	response = requests.request("GET", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'GET',

	));

	

	$response = curl_exec($curl);

	

	curl_close($curl);

	echo $response;

```

#### GUZZLE
```php
	<?php

	$client = new Client();

	$request = new Request('GET', 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start');

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start');

	$request->setMethod(HTTP_Request2::METHOD_GET);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start');

	$request->setRequestMethod('GET');

	$request->setOptions(array());

	

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

	  .url("https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start")

	  .method("GET", body)

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start")

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

	

	  url := "https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start"

	  method := "GET"

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, nil)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

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

	

	url = URI("https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Get.new(url)

	

	response = https.request(request)

	puts response.read_body

```

### POWERSHELL
#### RESTMETHOD
```powershell
	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/oauth/:platform/start' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

