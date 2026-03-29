# Update Recurring Task

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `id` | ✅ | locationId string required Location Id Example: sx6wyHhbFdRXh302Lunr |
| `locationId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "recurringTask": {
    "id": "sx6wyHhbFdRXh302Lunr",
    "title": "Task Name",
    "description": "Task Description",
    "locationId": "sx6wyHhbFdRXh302Lunr",
    "updatedAt": "2021-04-15T10:00:00.000Z",
    "createdAt": "2021-04-15T10:00:00.000Z",
    "rruleOptions": {
      "createTaskIfOverDue": false,
      "interval": 1,
      "intervalType": "hourly",
      "startDate": "2024-10-29T12:34:03.000Z",
      "dueAfterSeconds": 600,
      "count": 550
    },
    "totalOccurrence": 10,
    "deleted": false,
    "assignedTo": "sx6wyHhbFdRXh302Lunr",
    "contactId": "v5cEPM428h8vShlRW1KT"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

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

	  const response = await highLevel.locations.updateRecurringTask({

	    'id': 'sx6wyHhbFdRXh302Lunr',

	    'locationId': 'sx6wyHhbFdRXh302Lunr'

	  },

	  {

	    'title': 'Task Name',

	    'description': 'Task Description',

	    'contactIds': [

	      'sx6wyHhbFdRXh302Lunr'

	    ],

	    'owners': [

	      'sx6wyHhbFdRXh302Lunr'

	    ],

	    'rruleOptions': {

	      'intervalType': 'hourly',

	      'interval': 1,

	      'startDate': '2025-07-23T10:00:00.000Z',

	      'dueAfterSeconds': 600

	    },

	    'ignoreTaskCreation': true

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

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id',

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

	  'path': '/locations/:locationId/recurring-tasks/:id',

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

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "title": "Task Name",

	    "description": "Task Description",

	    "contactIds": [

	      "sx6wyHhbFdRXh302Lunr"

	    ],

	    "owners": [

	      "sx6wyHhbFdRXh302Lunr"

	    ],

	    "rruleOptions": {

	      "intervalType": "hourly",

	      "interval": 1,

	      "startDate": "2025-07-23T10:00:00.000Z",

	      "dueAfterSeconds": 600

	    },

	    "ignoreTaskCreation": true

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "title": "Task Name",

	    "description": "Task Description",

	    "contactIds": [

	      "sx6wyHhbFdRXh302Lunr"

	    ],

	    "owners": [

	      "sx6wyHhbFdRXh302Lunr"

	    ],

	    "rruleOptions": {

	      "intervalType": "hourly",

	      "interval": 1,

	      "startDate": "2025-07-23T10:00:00.000Z",

	      "dueAfterSeconds": 600

	    },

	    "ignoreTaskCreation": true

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

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": True

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/locations/:locationId/recurring-tasks/:id", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id"

	

	payload = json.dumps({

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": True

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

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

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "title": "Task Name",\n  "description": "Task Description",\n  "contactIds": [\n    "sx6wyHhbFdRXh302Lunr"\n  ],\n  "owners": [\n    "sx6wyHhbFdRXh302Lunr"\n  ],\n  "rruleOptions": {\n    "intervalType": "hourly",\n    "interval": 1,\n    "startDate": "2025-07-23T10:00:00.000Z",\n    "dueAfterSeconds": 600\n  },\n  "ignoreTaskCreation": true\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"title\": \"Task Name\",\n  \"description\": \"Task Description\",\n  \"contactIds\": [\n    \"sx6wyHhbFdRXh302Lunr\"\n  ],\n  \"owners\": [\n    \"sx6wyHhbFdRXh302Lunr\"\n  ],\n  \"rruleOptions\": {\n    \"intervalType\": \"hourly\",\n    \"interval\": 1,\n    \"startDate\": \"2025-07-23T10:00:00.000Z\",\n    \"dueAfterSeconds\": 600\n  },\n  \"ignoreTaskCreation\": true\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"title\": \"Task Name\",\n  \"description\": \"Task Description\",\n  \"contactIds\": [\n    \"sx6wyHhbFdRXh302Lunr\"\n  ],\n  \"owners\": [\n    \"sx6wyHhbFdRXh302Lunr\"\n  ],\n  \"rruleOptions\": {\n    \"intervalType\": \"hourly\",\n    \"interval\": 1,\n    \"startDate\": \"2025-07-23T10:00:00.000Z\",\n    \"dueAfterSeconds\": 600\n  },\n  \"ignoreTaskCreation\": true\n}")

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

	

	  url := "https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

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

	

	url = URI("https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "title": "Task Name",

	  "description": "Task Description",

	  "contactIds": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "owners": [

	    "sx6wyHhbFdRXh302Lunr"

	  ],

	  "rruleOptions": {

	    "intervalType": "hourly",

	    "interval": 1,

	    "startDate": "2025-07-23T10:00:00.000Z",

	    "dueAfterSeconds": 600

	  },

	  "ignoreTaskCreation": true

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

	  `"title`": `"Task Name`",

	  `"description`": `"Task Description`",

	  `"contactIds`": [

	    `"sx6wyHhbFdRXh302Lunr`"

	  ],

	  `"owners`": [

	    `"sx6wyHhbFdRXh302Lunr`"

	  ],

	  `"rruleOptions`": {

	    `"intervalType`": `"hourly`",

	    `"interval`": 1,

	    `"startDate`": `"2025-07-23T10:00:00.000Z`",

	    `"dueAfterSeconds`": 600

	  },

	  `"ignoreTaskCreation`": true

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/locations/:locationId/recurring-tasks/:id' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

