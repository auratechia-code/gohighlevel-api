# Get Access Token

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/oauth/token`

## 🔐 Requirements
```text
N/A
```

## 📥 Parameters
## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",
  "token_type": "Bearer",
  "expires_in": 86399,
  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",
  "scope": "conversations/message.readonly conversations/message.write",
  "userType": "Location",
  "locationId": "l1C08ntBrFjLS0elLIYU",
  "companyId": "l1C08ntBrFjLS0elLIYU",
  "approvedLocations": [
    "l1C08ntBrFjLS0elLIYU"
  ],
  "userId": "l1C08ntBrFjLS0elLIYU",
  "planId": "l1C08ntBrFjLS0elLIYU",
  "isBulkInstallation": "Bearer",
  "installToFutureLocations": true,
  "approveAllLocations": true
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X POST 'https://services.leadconnectorhq.com/oauth/token' \

	-H 'Content-Type: application/x-www-form-urlencoded' \

	-H 'Accept: application/json'

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

	  const response = await highLevel.oauth.getAccessToken({

	    'client_id': 'client_id_value',

	    'client_secret': 'client_secret_value',

	    'grant_type': 'grant_type_value',

	    'code': 'code_value',

	    'refresh_token': 'refresh_token_value',

	    'user_type': 'Location',

	    'redirect_uri': 'https://myapp.com/oauth/callback/gohighlevel'

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

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/oauth/token',

	  headers: { 

	    'Content-Type': 'application/x-www-form-urlencoded', 

	    'Accept': 'application/json'

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

	  'method': 'POST',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/oauth/token',

	  'headers': {

	    'Content-Type': 'application/x-www-form-urlencoded',

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

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/oauth/token',

	  'headers': {

	    'Content-Type': 'application/x-www-form-urlencoded',

	    'Accept': 'application/json'

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/oauth/token')

	  .headers({

	    'Content-Type': 'application/x-www-form-urlencoded',

	    'Accept': 'application/json'

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

	  'Content-Type': 'application/x-www-form-urlencoded',

	  'Accept': 'application/json'

	}

	conn.request("POST", "/oauth/token", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/oauth/token"

	

	payload = {}

	headers = {

	  'Content-Type': 'application/x-www-form-urlencoded',

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/oauth/token',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/x-www-form-urlencoded',

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

	  'Content-Type' => 'application/x-www-form-urlencoded',

	  'Accept' => 'application/json'

	];

	$request = new Request('POST', 'https://services.leadconnectorhq.com/oauth/token', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/oauth/token');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/x-www-form-urlencoded',

	  'Accept' => 'application/json'

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/oauth/token');

	$request->setRequestMethod('POST');

	$request->setOptions(array());

	$request->setHeaders(array(

	  'Content-Type' => 'application/x-www-form-urlencoded',

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

	MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");

	RequestBody body = RequestBody.create(mediaType, "");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/oauth/token")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/x-www-form-urlencoded")

	  .addHeader("Accept", "application/json")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/oauth/token")

	  .header("Content-Type", "application/x-www-form-urlencoded")

	  .header("Accept", "application/json")

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

	

	  url := "https://services.leadconnectorhq.com/oauth/token"

	  method := "POST"

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, nil)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

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

	require "net/http"

	

	url = URI("https://services.leadconnectorhq.com/oauth/token")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/x-www-form-urlencoded"

	request["Accept"] = "application/json"

	

	response = https.request(request)

	puts response.read_body

```

### POWERSHELL
#### RESTMETHOD
```powershell
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"

	$headers.Add("Content-Type", "application/x-www-form-urlencoded")

	$headers.Add("Accept", "application/json")

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/oauth/token' -Method 'POST' -Headers $headers

	$response | ConvertTo-Json

```

