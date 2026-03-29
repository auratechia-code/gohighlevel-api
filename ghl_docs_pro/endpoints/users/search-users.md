# Search Users

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/users/search`

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
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `companyId` | ❌ | query string The search term for the user is matched based on the user full name, email or phone Example: John |
| `query` | ❌ | skip string No of results to be skipped before returning the result Default value: 0 Example: 1 |
| `skip` | ❌ | limit string No of results to be limited before returning the result Default value: 25 Example: 10 |
| `limit` | ❌ | locationId string Location ID in which the search needs to be performed Example: 5DP41231LkQsiKESj6rh |
| `locationId` | ❌ | type string Type of the users to be filtered in the search Example: agency |
| `type` | ❌ | role string Role of the users to be filtered in the search Example: admin |
| `role` | ❌ | ids string List of User IDs to be filtered in the search Example: 5DP4iH6HLkQsiKESj6rh,5DP4iH6HLkQsiKESj34h |
| `ids` | ❌ | sort string The field on which sort is applied in which the results need to be sorted. Default is based on the first and last name Example: dateAdded |
| `sort` | ❌ | sortDirection string The direction in which the results need to be sorted Example: asc |
| `sortDirection` | ❌ | enabled2waySync boolean |
| `enabled2waySync` | ❌ |  |

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
	curl -L 'https://services.leadconnectorhq.com/users/search' \

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

	  const response = await highLevel.users.searchUsers({

	    'companyId': '5DP41231LkQsiKESj6rh',

	    'query': 'John',

	    'skip': '1',

	    'limit': '10',

	    'locationId': '5DP41231LkQsiKESj6rh',

	    'type': 'agency',

	    'role': 'admin',

	    'ids': '5DP4iH6HLkQsiKESj6rh,5DP4iH6HLkQsiKESj34h',

	    'sort': 'dateAdded',

	    'sortDirection': 'asc'

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

	  url: 'https://services.leadconnectorhq.com/users/search',

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

	  'path': '/users/search',

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

	  'url': 'https://services.leadconnectorhq.com/users/search',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/users/search')

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

	conn.request("GET", "/users/search", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/users/search"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/users/search',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/users/search', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/users/search');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/users/search');

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

	  .url("https://services.leadconnectorhq.com/users/search")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/users/search")

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

	

	  url := "https://services.leadconnectorhq.com/users/search"

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

	

	url = URI("https://services.leadconnectorhq.com/users/search")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/users/search' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

