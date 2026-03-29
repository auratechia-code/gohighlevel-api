# Search Opportunity

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/opportunities/search`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: opportunities.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `q` | ✅ | location_id string required Location Id Example: i2SpAtBVHSVea1sL6oah |
| `location_id` | ❌ | pipeline_id string Pipeline Id Example: bCkKGpDsyPP4peuKowkG |
| `pipeline_id` | ❌ | pipeline_stage_id string stage Id Example: 7915dedc-8f18-44d5-8bc3-77c04e994a10 |
| `pipeline_stage_id` | ❌ | contact_id string Contact Id Example: WFwVrSSjZ2CNHbZThQX2 |
| `contact_id` | ❌ | status string Possible values: [ open , won , lost , abandoned , all ] |
| `status` | ❌ | assigned_to string Example: 082goXVW3lIExEQPOnd3 |
| `assigned_to` | ❌ | campaignId string Campaign Id Example: Y2I9XM7aO1hncuSOlc9L |
| `campaignId` | ❌ | id string Opportunity Id Example: 123akv4LFn6C9frZoy3e |
| `id` | ❌ | order string Example: added_asc |
| `order` | ❌ | endDate string End date Example: mm-dd-yyyy |
| `endDate` | ❌ | startAfter string Start After Example: 1628008053263 |
| `startAfter` | ❌ | startAfterId string Start After Id Example: UIaE1WjAwWKdlyD7osQI |
| `startAfterId` | ❌ | date string Start date Example: mm-dd-yyyy |
| `date` | ❌ | country string Example: US |
| `country` | ❌ | page number Default value: 1 |
| `page` | ❌ | limit number Limit Per Page records count. will allow maximum up to 100 and default will be 20 Default value: 20 |
| `limit` | ❌ | getTasks boolean get Tasks in contact |
| `getTasks` | ❌ | getNotes boolean get Notes in contact |
| `getNotes` | ❌ | getCalendarEvents boolean get Calender event in contact |
| `getCalendarEvents` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "opportunities": [
    {
      "id": "yWQobCRIhRguQtD2llvk",
      "name": "testing",
      "monetaryValue": 500,
      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",
      "assignedTo": "zT46WSCPbudrq4zhWMk6",
      "status": "open",
      "source": "",
      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",
      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",
      "lastActionDate": "2021-08-03T04:55:17.355Z",
      "indexVersion": 1,
      "createdAt": "2021-08-03T04:55:17.355Z",
      "updatedAt": "2021-08-03T04:55:17.355Z",
      "contactId": "zT46WSCPbudrq4zhWMk6",
      "locationId": "zT46WSCPbudrq4zhW",
      "contact": {
        "id": "byMEV0NQinDhq8ZfiOi2",
        "name": "John Deo",
        "companyName": "Tesla Inc",
        "email": "john@deo.com",
        "phone": "+1202-555-0107",
        "tags": [
          "string"
        ]
      },
      "notes": [
        [
          null
        ]
      ],
      "tasks": [
        [
          null
        ]
      ],
      "calendarEvents": [
        [
          null
        ]
      ],
      "lostReasonId": "zT46WSCPbudrq4zhWMk6",
      "customFields": [
        {
          "id": "MgobCB14YMVKuE4Ka8p1",
          "fieldValue": "string"
        }
      ],
      "followers": [
        [
          null
        ]
      ]
    }
  ],
  "meta": {
    "total": 1,
    "nextPageUrl": "http://localhost:5066/opportunities/search?q=&location_id=ve9EPM428h8vShlRW1KT&pipeline_id=&pipeline_stage_id=&status=&assigned_to+=&campaignId=&id=&order=&endDate=&startAfter=1625203104328&startAfterId=yWQobCRIhRguQtD2llvk&date=&limit=1&country=&page=1",
    "startAfterId": "yWQobCRIhRguQtD2llvk",
    "startAfter": 1625203104328,
    "currentPage": 2,
    "nextPage": 3,
    "prevPage": 1
  },
  "aggregations": {}
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "meta": {    "total": 1,    "nextPageUrl": "http://localhost:5066/opportunities/search?q=&location_id=ve9EPM428h8vShlRW1KT&pipeline_id=&pipeline_stage_id=&status=&assigned_to+=&campaignId=&id=&order=&endDate=&startAfter=1625203104328&startAfterId=yWQobCRIhRguQtD2llvk&date=&limit=1&country=&page=1",    "startAfterId": "yWQobCRIhRguQtD2llvk",    "startAfter": 1625203104328,    "currentPage": 2,    "nextPage": 3,    "prevPage": 1  },  "aggregations": {}}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "meta": {    "total": 1,    "nextPageUrl": "http://localhost:5066/opportunities/search?q=&location_id=ve9EPM428h8vShlRW1KT&pipeline_id=&pipeline_stage_id=&status=&assigned_to+=&campaignId=&id=&order=&endDate=&startAfter=1625203104328&startAfterId=yWQobCRIhRguQtD2llvk&date=&limit=1&country=&page=1",    "startAfterId": "yWQobCRIhRguQtD2llvk",    "startAfter": 1625203104328,    "currentPage": 2,    "nextPage": 3,    "prevPage": 1  },  "aggregations": {}}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "meta": {    "total": 1,    "nextPageUrl": "http://localhost:5066/opportunities/search?q=&location_id=ve9EPM428h8vShlRW1KT&pipeline_id=&pipeline_stage_id=&status=&assigned_to+=&campaignId=&id=&order=&endDate=&startAfter=1625203104328&startAfterId=yWQobCRIhRguQtD2llvk&date=&limit=1&country=&page=1",    "startAfterId": "yWQobCRIhRguQtD2llvk",    "startAfter": 1625203104328,    "currentPage": 2,    "nextPage": 3,    "prevPage": 1  },  "aggregations": {}}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/opportunities/search' \

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

	  const response = await highLevel.opportunities.searchOpportunity({

	    'q': 'john@deo.com',

	    'location_id': 'i2SpAtBVHSVea1sL6oah',

	    'pipeline_id': 'bCkKGpDsyPP4peuKowkG',

	    'pipeline_stage_id': '7915dedc-8f18-44d5-8bc3-77c04e994a10',

	    'contact_id': 'WFwVrSSjZ2CNHbZThQX2',

	    'assigned_to': '082goXVW3lIExEQPOnd3',

	    'campaignId': 'Y2I9XM7aO1hncuSOlc9L',

	    'id': '123akv4LFn6C9frZoy3e',

	    'order': 'added_asc',

	    'endDate': 'mm-dd-yyyy',

	    'startAfter': '1628008053263',

	    'startAfterId': 'UIaE1WjAwWKdlyD7osQI',

	    'date': 'mm-dd-yyyy',

	    'country': 'US',

	    'getTasks': false,

	    'getNotes': false,

	    'getCalendarEvents': false

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

	  url: 'https://services.leadconnectorhq.com/opportunities/search',

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

	  'path': '/opportunities/search',

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

	  'url': 'https://services.leadconnectorhq.com/opportunities/search',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/opportunities/search')

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

	conn.request("GET", "/opportunities/search", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/opportunities/search"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/opportunities/search',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/opportunities/search', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/opportunities/search');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/opportunities/search');

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

	  .url("https://services.leadconnectorhq.com/opportunities/search")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/opportunities/search")

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

	

	  url := "https://services.leadconnectorhq.com/opportunities/search"

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

	

	url = URI("https://services.leadconnectorhq.com/opportunities/search")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/opportunities/search' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

