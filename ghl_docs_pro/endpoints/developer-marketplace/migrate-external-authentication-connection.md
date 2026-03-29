# Migrate external authentication connection

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/marketplace/external-auth/migration`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: marketplace-external-auth-migration.write
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
<summary>Response 201</summary>

```json
{
  "success": true,
  "identifier": "migration_12345",
  "message": "Connection migrated successfully"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "success": true,  "identifier": "migration_12345",  "message": "Connection migrated successfully"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "success": true,  "identifier": "migration_12345",  "message": "Connection migrated successfully"}
```
</details>

<details>
<summary>Response 404</summary>

```json
{  "success": true,  "identifier": "migration_12345",  "message": "Connection migrated successfully"}
```
</details>

<details>
<summary>Response 500</summary>

```json
{  "success": true,  "identifier": "migration_12345",  "message": "Connection migrated successfully"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/marketplace/external-auth/migration' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

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

	  const response = await highLevel.marketplace.migrateConnection({

	    'type': 'oauth2',

	    'locationId': 'location_12345',

	    'appId': '507f1f77bcf86cd799439011',

	    'appVersionId': '507f1f77bcf86cd799439012',

	    'accountId': 'my-connection-identifier',

	    'apiKey': 'sk_test_1234567890',

	    'basicCredentials': {

	      'email': 'user@example.com',

	      'password': 'p@ssw0rd'

	    },

	    'accessToken': 'ya29.a0AfH6SMBx...',

	    'refreshToken': '1//0gHq5F...',

	    'expiryIn': 3600000,

	    'expiryAt': 1735689600000,

	    'scopes': [

	      'contacts.readonly',

	      'contacts.write'

	    ],

	    'displayName': 'My Connection Display Name',

	    'isDefault': false

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

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/marketplace/external-auth/migration',

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

	  'path': '/marketplace/external-auth/migration',

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

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/marketplace/external-auth/migration',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "type": "oauth2",

	    "locationId": "location_12345",

	    "appId": "507f1f77bcf86cd799439011",

	    "appVersionId": "507f1f77bcf86cd799439012",

	    "accountId": "my-connection-identifier",

	    "apiKey": "sk_test_1234567890",

	    "basicCredentials": {

	      "email": "user@example.com",

	      "password": "p@ssw0rd"

	    },

	    "accessToken": "ya29.a0AfH6SMBx...",

	    "refreshToken": "1//0gHq5F...",

	    "expiryIn": 3600000,

	    "expiryAt": 1735689600000,

	    "scopes": [

	      "contacts.readonly",

	      "contacts.write"

	    ],

	    "displayName": "My Connection Display Name",

	    "isDefault": false

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/marketplace/external-auth/migration')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "type": "oauth2",

	    "locationId": "location_12345",

	    "appId": "507f1f77bcf86cd799439011",

	    "appVersionId": "507f1f77bcf86cd799439012",

	    "accountId": "my-connection-identifier",

	    "apiKey": "sk_test_1234567890",

	    "basicCredentials": {

	      "email": "user@example.com",

	      "password": "p@ssw0rd"

	    },

	    "accessToken": "ya29.a0AfH6SMBx...",

	    "refreshToken": "1//0gHq5F...",

	    "expiryIn": 3600000,

	    "expiryAt": 1735689600000,

	    "scopes": [

	      "contacts.readonly",

	      "contacts.write"

	    ],

	    "displayName": "My Connection Display Name",

	    "isDefault": false

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

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": False

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/marketplace/external-auth/migration", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/marketplace/external-auth/migration"

	

	payload = json.dumps({

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": False

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/marketplace/external-auth/migration',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

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

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/marketplace/external-auth/migration', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/marketplace/external-auth/migration');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "type": "oauth2",\n  "locationId": "location_12345",\n  "appId": "507f1f77bcf86cd799439011",\n  "appVersionId": "507f1f77bcf86cd799439012",\n  "accountId": "my-connection-identifier",\n  "apiKey": "sk_test_1234567890",\n  "basicCredentials": {\n    "email": "user@example.com",\n    "password": "p@ssw0rd"\n  },\n  "accessToken": "ya29.a0AfH6SMBx...",\n  "refreshToken": "1//0gHq5F...",\n  "expiryIn": 3600000,\n  "expiryAt": 1735689600000,\n  "scopes": [\n    "contacts.readonly",\n    "contacts.write"\n  ],\n  "displayName": "My Connection Display Name",\n  "isDefault": false\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/marketplace/external-auth/migration');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"type\": \"oauth2\",\n  \"locationId\": \"location_12345\",\n  \"appId\": \"507f1f77bcf86cd799439011\",\n  \"appVersionId\": \"507f1f77bcf86cd799439012\",\n  \"accountId\": \"my-connection-identifier\",\n  \"apiKey\": \"sk_test_1234567890\",\n  \"basicCredentials\": {\n    \"email\": \"user@example.com\",\n    \"password\": \"p@ssw0rd\"\n  },\n  \"accessToken\": \"ya29.a0AfH6SMBx...\",\n  \"refreshToken\": \"1//0gHq5F...\",\n  \"expiryIn\": 3600000,\n  \"expiryAt\": 1735689600000,\n  \"scopes\": [\n    \"contacts.readonly\",\n    \"contacts.write\"\n  ],\n  \"displayName\": \"My Connection Display Name\",\n  \"isDefault\": false\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/marketplace/external-auth/migration")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/marketplace/external-auth/migration")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"type\": \"oauth2\",\n  \"locationId\": \"location_12345\",\n  \"appId\": \"507f1f77bcf86cd799439011\",\n  \"appVersionId\": \"507f1f77bcf86cd799439012\",\n  \"accountId\": \"my-connection-identifier\",\n  \"apiKey\": \"sk_test_1234567890\",\n  \"basicCredentials\": {\n    \"email\": \"user@example.com\",\n    \"password\": \"p@ssw0rd\"\n  },\n  \"accessToken\": \"ya29.a0AfH6SMBx...\",\n  \"refreshToken\": \"1//0gHq5F...\",\n  \"expiryIn\": 3600000,\n  \"expiryAt\": 1735689600000,\n  \"scopes\": [\n    \"contacts.readonly\",\n    \"contacts.write\"\n  ],\n  \"displayName\": \"My Connection Display Name\",\n  \"isDefault\": false\n}")

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

	

	  url := "https://services.leadconnectorhq.com/marketplace/external-auth/migration"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

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

	

	url = URI("https://services.leadconnectorhq.com/marketplace/external-auth/migration")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "type": "oauth2",

	  "locationId": "location_12345",

	  "appId": "507f1f77bcf86cd799439011",

	  "appVersionId": "507f1f77bcf86cd799439012",

	  "accountId": "my-connection-identifier",

	  "apiKey": "sk_test_1234567890",

	  "basicCredentials": {

	    "email": "user@example.com",

	    "password": "p@ssw0rd"

	  },

	  "accessToken": "ya29.a0AfH6SMBx...",

	  "refreshToken": "1//0gHq5F...",

	  "expiryIn": 3600000,

	  "expiryAt": 1735689600000,

	  "scopes": [

	    "contacts.readonly",

	    "contacts.write"

	  ],

	  "displayName": "My Connection Display Name",

	  "isDefault": false

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

	  `"type`": `"oauth2`",

	  `"locationId`": `"location_12345`",

	  `"appId`": `"507f1f77bcf86cd799439011`",

	  `"appVersionId`": `"507f1f77bcf86cd799439012`",

	  `"accountId`": `"my-connection-identifier`",

	  `"apiKey`": `"sk_test_1234567890`",

	  `"basicCredentials`": {

	    `"email`": `"user@example.com`",

	    `"password`": `"p@ssw0rd`"

	  },

	  `"accessToken`": `"ya29.a0AfH6SMBx...`",

	  `"refreshToken`": `"1//0gHq5F...`",

	  `"expiryIn`": 3600000,

	  `"expiryAt`": 1735689600000,

	  `"scopes`": [

	    `"contacts.readonly`",

	    `"contacts.write`"

	  ],

	  `"displayName`": `"My Connection Display Name`",

	  `"isDefault`": false

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/marketplace/external-auth/migration' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

