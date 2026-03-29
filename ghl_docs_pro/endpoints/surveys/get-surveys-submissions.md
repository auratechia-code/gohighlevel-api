# Get Surveys Submissions

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/surveys/submissions`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: surveys.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ | page number Page No. By default it will be 1 Default value: 1 Example: 1 |
| `page` | ❌ | limit number Limit Per Page records count. will allow maximum up to 100 and default will be 20 Default value: 20 Example: 20 |
| `limit` | ❌ | surveyId string Filter submission by survey id Example: jjusM6EOngDExnbo2DbU |
| `surveyId` | ❌ | q string Filter by contactId, name, email or phone no. Example: john@deo.com |
| `q` | ❌ | startAt string Get submission by starting of this date. By default it will be same date of last month(YYYY-MM-DD). Example: 2020-11-14 |
| `startAt` | ❌ | endAt string Get submission by ending of this date. By default it will be current date(YYYY-MM-DD). Example: 2020-12-14 |
| `endAt` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "submissions": [
    {
      "id": "be759b9a-c3ec-4b29-ba07-fc3c89c77673",
      "contactId": "9NkT25Vor1v4aQatFsv2",
      "createdAt": "2020-11-01T18:02:21.000Z",
      "surveyId": "jjusM6EOngDExnbo2DbU",
      "name": "test",
      "email": "test@test.com",
      "others": {
        "__submissions_other_field__": "john@deo.com",
        "__custom_field_id__": "20",
        "eventData": {
          "fbc": "fb.1.123456789.987654321",
          "fbp": "fbp.1.987654321.123456789",
          "page": {
            "url": "https://example.com",
            "title": "Example Page"
          },
          "type": "page-visit",
          "domain": "example.com",
          "medium": "survey",
          "source": "Direct traffic",
          "version": "v3",
          "adSource": "example-ad-source",
          "mediumId": "medium-id-123",
          "parentId": "parent-id-456",
          "referrer": "https://staging.gohighlevel.com",
          "fbEventId": "event-id-789",
          "timestamp": 1234567890,
          "parentName": "Parent Survey",
          "fingerprint": "example-fingerprint",
          "pageVisitType": "survey",
          "contactSessionIds": {
            "ids": [
              "session1",
              "session2"
            ]
          }
        },
        "fieldsOriSequance": [
          "full_name",
          "first_name",
          "last_name",
          "phone",
          "email"
        ]
      }
    }
  ],
  "meta": {
    "total": 1,
    "currentPage": 1,
    "nextPage": null,
    "prevPage": null
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "submissions": [    {      "id": "be759b9a-c3ec-4b29-ba07-fc3c89c77673",      "contactId": "9NkT25Vor1v4aQatFsv2",      "createdAt": "2020-11-01T18:02:21.000Z",      "surveyId": "jjusM6EOngDExnbo2DbU",      "name": "test",      "email": "test@test.com",      "others": {        "__submissions_other_field__": "john@deo.com",        "__custom_field_id__": "20",        "eventData": {          "fbc": "fb.1.123456789.987654321",          "fbp": "fbp.1.987654321.123456789",          "page": {            "url": "https://example.com",            "title": "Example Page"          },          "type": "page-visit",          "domain": "example.com",          "medium": "survey",          "source": "Direct traffic",          "version": "v3",          "adSource": "example-ad-source",          "mediumId": "medium-id-123",          "parentId": "parent-id-456",          "referrer": "https://staging.gohighlevel.com",          "fbEventId": "event-id-789",          "timestamp": 1234567890,          "parentName": "Parent Survey",          "fingerprint": "example-fingerprint",          "pageVisitType": "survey",          "contactSessionIds": {            "ids": [              "session1",              "session2"            ]          }        },        "fieldsOriSequance": [          "full_name",          "first_name",          "last_name",          "phone",          "email"        ]      }    }  ],  "meta": {    "total": 1,    "currentPage": 1,    "nextPage": null,    "prevPage": null  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "submissions": [    {      "id": "be759b9a-c3ec-4b29-ba07-fc3c89c77673",      "contactId": "9NkT25Vor1v4aQatFsv2",      "createdAt": "2020-11-01T18:02:21.000Z",      "surveyId": "jjusM6EOngDExnbo2DbU",      "name": "test",      "email": "test@test.com",      "others": {        "__submissions_other_field__": "john@deo.com",        "__custom_field_id__": "20",        "eventData": {          "fbc": "fb.1.123456789.987654321",          "fbp": "fbp.1.987654321.123456789",          "page": {            "url": "https://example.com",            "title": "Example Page"          },          "type": "page-visit",          "domain": "example.com",          "medium": "survey",          "source": "Direct traffic",          "version": "v3",          "adSource": "example-ad-source",          "mediumId": "medium-id-123",          "parentId": "parent-id-456",          "referrer": "https://staging.gohighlevel.com",          "fbEventId": "event-id-789",          "timestamp": 1234567890,          "parentName": "Parent Survey",          "fingerprint": "example-fingerprint",          "pageVisitType": "survey",          "contactSessionIds": {            "ids": [              "session1",              "session2"            ]          }        },        "fieldsOriSequance": [          "full_name",          "first_name",          "last_name",          "phone",          "email"        ]      }    }  ],  "meta": {    "total": 1,    "currentPage": 1,    "nextPage": null,    "prevPage": null  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "submissions": [    {      "id": "be759b9a-c3ec-4b29-ba07-fc3c89c77673",      "contactId": "9NkT25Vor1v4aQatFsv2",      "createdAt": "2020-11-01T18:02:21.000Z",      "surveyId": "jjusM6EOngDExnbo2DbU",      "name": "test",      "email": "test@test.com",      "others": {        "__submissions_other_field__": "john@deo.com",        "__custom_field_id__": "20",        "eventData": {          "fbc": "fb.1.123456789.987654321",          "fbp": "fbp.1.987654321.123456789",          "page": {            "url": "https://example.com",            "title": "Example Page"          },          "type": "page-visit",          "domain": "example.com",          "medium": "survey",          "source": "Direct traffic",          "version": "v3",          "adSource": "example-ad-source",          "mediumId": "medium-id-123",          "parentId": "parent-id-456",          "referrer": "https://staging.gohighlevel.com",          "fbEventId": "event-id-789",          "timestamp": 1234567890,          "parentName": "Parent Survey",          "fingerprint": "example-fingerprint",          "pageVisitType": "survey",          "contactSessionIds": {            "ids": [              "session1",              "session2"            ]          }        },        "fieldsOriSequance": [          "full_name",          "first_name",          "last_name",          "phone",          "email"        ]      }    }  ],  "meta": {    "total": 1,    "currentPage": 1,    "nextPage": null,    "prevPage": null  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/surveys/submissions' \

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

	  const response = await highLevel.surveys.getSurveysSubmissions({

	    'locationId': 've9EPM428h8vShlRW1KT',

	    'page': 1,

	    'limit': 20,

	    'surveyId': 'jjusM6EOngDExnbo2DbU',

	    'q': 'john@deo.com',

	    'startAt': '2020-11-14',

	    'endAt': '2020-12-14'

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

	  url: 'https://services.leadconnectorhq.com/surveys/submissions',

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

	  'path': '/surveys/submissions',

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

	  'url': 'https://services.leadconnectorhq.com/surveys/submissions',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/surveys/submissions')

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

	conn.request("GET", "/surveys/submissions", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/surveys/submissions"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/surveys/submissions',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/surveys/submissions', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/surveys/submissions');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/surveys/submissions');

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

	  .url("https://services.leadconnectorhq.com/surveys/submissions")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/surveys/submissions")

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

	

	  url := "https://services.leadconnectorhq.com/surveys/submissions"

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

	

	url = URI("https://services.leadconnectorhq.com/surveys/submissions")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/surveys/submissions' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

