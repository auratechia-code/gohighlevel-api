# Filter Users by Email

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/users/search/filter-by-email`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: users.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.
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
  "users": [
    {
      "id": "0IHuJvc2ofPAAA8GzTRi",
      "name": "John Deo",
      "firstName": "John",
      "lastName": "Deo",
      "email": "john@deo.com",
      "phone": "+1 808-868-8888",
      "extension": "",
      "permissions": {
        "campaignsEnabled": true,
        "campaignsReadOnly": false,
        "contactsEnabled": true,
        "workflowsEnabled": true,
        "workflowsReadOnly": true,
        "triggersEnabled": true,
        "funnelsEnabled": true,
        "websitesEnabled": false,
        "opportunitiesEnabled": true,
        "dashboardStatsEnabled": true,
        "bulkRequestsEnabled": true,
        "appointmentsEnabled": true,
        "reviewsEnabled": true,
        "onlineListingsEnabled": true,
        "phoneCallEnabled": true,
        "conversationsEnabled": true,
        "assignedDataOnly": false,
        "adwordsReportingEnabled": false,
        "membershipEnabled": false,
        "facebookAdsReportingEnabled": false,
        "attributionsReportingEnabled": false,
        "settingsEnabled": true,
        "tagsEnabled": true,
        "leadValueEnabled": true,
        "marketingEnabled": true,
        "agentReportingEnabled": true,
        "botService": false,
        "socialPlanner": true,
        "bloggingEnabled": true,
        "invoiceEnabled": true,
        "affiliateManagerEnabled": true,
        "contentAiEnabled": true,
        "refundsEnabled": true,
        "recordPaymentEnabled": true,
        "cancelSubscriptionEnabled": true,
        "paymentsEnabled": true,
        "communitiesEnabled": true,
        "exportPaymentsEnabled": true
      },
      "scopes": "campaigns.readonly",
      "roles": {
        "type": "account",
        "role": "admin",
        "locationIds": [
          "ve9EPM428h8vShlRW1KT"
        ],
        "restrictSubAccount": true
      },
      "deleted": false,
      "lcPhone": {
        "locationId": "+1234556677"
      },
      "platformLanguage": "en_US"
    }
  ],
  "count": 1231
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "users": [    {      "id": "0IHuJvc2ofPAAA8GzTRi",      "name": "John Deo",      "firstName": "John",      "lastName": "Deo",      "email": "john@deo.com",      "phone": "+1 808-868-8888",      "extension": "",      "permissions": {        "campaignsEnabled": true,        "campaignsReadOnly": false,        "contactsEnabled": true,        "workflowsEnabled": true,        "workflowsReadOnly": true,        "triggersEnabled": true,        "funnelsEnabled": true,        "websitesEnabled": false,        "opportunitiesEnabled": true,        "dashboardStatsEnabled": true,        "bulkRequestsEnabled": true,        "appointmentsEnabled": true,        "reviewsEnabled": true,        "onlineListingsEnabled": true,        "phoneCallEnabled": true,        "conversationsEnabled": true,        "assignedDataOnly": false,        "adwordsReportingEnabled": false,        "membershipEnabled": false,        "facebookAdsReportingEnabled": false,        "attributionsReportingEnabled": false,        "settingsEnabled": true,        "tagsEnabled": true,        "leadValueEnabled": true,        "marketingEnabled": true,        "agentReportingEnabled": true,        "botService": false,        "socialPlanner": true,        "bloggingEnabled": true,        "invoiceEnabled": true,        "affiliateManagerEnabled": true,        "contentAiEnabled": true,        "refundsEnabled": true,        "recordPaymentEnabled": true,        "cancelSubscriptionEnabled": true,        "paymentsEnabled": true,        "communitiesEnabled": true,        "exportPaymentsEnabled": true      },      "scopes": "campaigns.readonly",      "roles": {        "type": "account",        "role": "admin",        "locationIds": [          "ve9EPM428h8vShlRW1KT"        ],        "restrictSubAccount": true      },      "deleted": false,      "lcPhone": {        "locationId": "+1234556677"      },      "platformLanguage": "en_US"    }  ],  "count": 1231}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "users": [    {      "id": "0IHuJvc2ofPAAA8GzTRi",      "name": "John Deo",      "firstName": "John",      "lastName": "Deo",      "email": "john@deo.com",      "phone": "+1 808-868-8888",      "extension": "",      "permissions": {        "campaignsEnabled": true,        "campaignsReadOnly": false,        "contactsEnabled": true,        "workflowsEnabled": true,        "workflowsReadOnly": true,        "triggersEnabled": true,        "funnelsEnabled": true,        "websitesEnabled": false,        "opportunitiesEnabled": true,        "dashboardStatsEnabled": true,        "bulkRequestsEnabled": true,        "appointmentsEnabled": true,        "reviewsEnabled": true,        "onlineListingsEnabled": true,        "phoneCallEnabled": true,        "conversationsEnabled": true,        "assignedDataOnly": false,        "adwordsReportingEnabled": false,        "membershipEnabled": false,        "facebookAdsReportingEnabled": false,        "attributionsReportingEnabled": false,        "settingsEnabled": true,        "tagsEnabled": true,        "leadValueEnabled": true,        "marketingEnabled": true,        "agentReportingEnabled": true,        "botService": false,        "socialPlanner": true,        "bloggingEnabled": true,        "invoiceEnabled": true,        "affiliateManagerEnabled": true,        "contentAiEnabled": true,        "refundsEnabled": true,        "recordPaymentEnabled": true,        "cancelSubscriptionEnabled": true,        "paymentsEnabled": true,        "communitiesEnabled": true,        "exportPaymentsEnabled": true      },      "scopes": "campaigns.readonly",      "roles": {        "type": "account",        "role": "admin",        "locationIds": [          "ve9EPM428h8vShlRW1KT"        ],        "restrictSubAccount": true      },      "deleted": false,      "lcPhone": {        "locationId": "+1234556677"      },      "platformLanguage": "en_US"    }  ],  "count": 1231}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "users": [    {      "id": "0IHuJvc2ofPAAA8GzTRi",      "name": "John Deo",      "firstName": "John",      "lastName": "Deo",      "email": "john@deo.com",      "phone": "+1 808-868-8888",      "extension": "",      "permissions": {        "campaignsEnabled": true,        "campaignsReadOnly": false,        "contactsEnabled": true,        "workflowsEnabled": true,        "workflowsReadOnly": true,        "triggersEnabled": true,        "funnelsEnabled": true,        "websitesEnabled": false,        "opportunitiesEnabled": true,        "dashboardStatsEnabled": true,        "bulkRequestsEnabled": true,        "appointmentsEnabled": true,        "reviewsEnabled": true,        "onlineListingsEnabled": true,        "phoneCallEnabled": true,        "conversationsEnabled": true,        "assignedDataOnly": false,        "adwordsReportingEnabled": false,        "membershipEnabled": false,        "facebookAdsReportingEnabled": false,        "attributionsReportingEnabled": false,        "settingsEnabled": true,        "tagsEnabled": true,        "leadValueEnabled": true,        "marketingEnabled": true,        "agentReportingEnabled": true,        "botService": false,        "socialPlanner": true,        "bloggingEnabled": true,        "invoiceEnabled": true,        "affiliateManagerEnabled": true,        "contentAiEnabled": true,        "refundsEnabled": true,        "recordPaymentEnabled": true,        "cancelSubscriptionEnabled": true,        "paymentsEnabled": true,        "communitiesEnabled": true,        "exportPaymentsEnabled": true      },      "scopes": "campaigns.readonly",      "roles": {        "type": "account",        "role": "admin",        "locationIds": [          "ve9EPM428h8vShlRW1KT"        ],        "restrictSubAccount": true      },      "deleted": false,      "lcPhone": {        "locationId": "+1234556677"      },      "platformLanguage": "en_US"    }  ],  "count": 1231}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/users/search/filter-by-email' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

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

	  const response = await highLevel.users.filterUsersByEmail({

	    'companyId': '5DP41231LkQsiKESj6rh',

	    'emails': 'user1@example.com,user2@example.com',

	    'deleted': false,

	    'skip': '1',

	    'limit': '10',

	    'projection': 'all'

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

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/users/search/filter-by-email',

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

	  'path': '/users/search/filter-by-email',

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

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/users/search/filter-by-email',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "companyId": "5DP41231LkQsiKESj6rh",

	    "emails": "user1@example.com,user2@example.com",

	    "deleted": false,

	    "skip": "1",

	    "limit": "10",

	    "projection": "all"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/users/search/filter-by-email')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "companyId": "5DP41231LkQsiKESj6rh",

	    "emails": "user1@example.com,user2@example.com",

	    "deleted": false,

	    "skip": "1",

	    "limit": "10",

	    "projection": "all"

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

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": False,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/users/search/filter-by-email", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/users/search/filter-by-email"

	

	payload = json.dumps({

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": False,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/users/search/filter-by-email',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

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

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/users/search/filter-by-email', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/users/search/filter-by-email');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "companyId": "5DP41231LkQsiKESj6rh",\n  "emails": "user1@example.com,user2@example.com",\n  "deleted": false,\n  "skip": "1",\n  "limit": "10",\n  "projection": "all"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/users/search/filter-by-email');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"companyId\": \"5DP41231LkQsiKESj6rh\",\n  \"emails\": \"user1@example.com,user2@example.com\",\n  \"deleted\": false,\n  \"skip\": \"1\",\n  \"limit\": \"10\",\n  \"projection\": \"all\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/users/search/filter-by-email")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/users/search/filter-by-email")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"companyId\": \"5DP41231LkQsiKESj6rh\",\n  \"emails\": \"user1@example.com,user2@example.com\",\n  \"deleted\": false,\n  \"skip\": \"1\",\n  \"limit\": \"10\",\n  \"projection\": \"all\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/users/search/filter-by-email"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

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

	

	url = URI("https://services.leadconnectorhq.com/users/search/filter-by-email")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "companyId": "5DP41231LkQsiKESj6rh",

	  "emails": "user1@example.com,user2@example.com",

	  "deleted": false,

	  "skip": "1",

	  "limit": "10",

	  "projection": "all"

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

	  `"companyId`": `"5DP41231LkQsiKESj6rh`",

	  `"emails`": `"user1@example.com,user2@example.com`",

	  `"deleted`": false,

	  `"skip`": `"1`",

	  `"limit`": `"10`",

	  `"projection`": `"all`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/users/search/filter-by-email' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

