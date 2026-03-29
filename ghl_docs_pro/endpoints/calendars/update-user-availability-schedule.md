# Update user availability schedule

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/calendars/schedules/:id`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: calendars.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `id` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "schedule": {
    "id": "IkqiJlXJ7o9h61tCHHod",
    "name": "Business Hours Schedule",
    "locationId": "IkqiJlXJ7o9h61tCHHod",
    "rules": [
      {
        "type": "wday",
        "intervals": [
          {
            "from": "09:00",
            "to": "17:00"
          }
        ],
        "date": "2023-04-15",
        "day": "monday"
      }
    ],
    "timezone": "America/New_York",
    "dateAdded": "2023-01-15T10:30:00.000Z",
    "dateUpdated": "2023-01-20T14:45:00.000Z",
    "userId": "IkqiJlXJ7o9h61tCHHod",
    "calendarIds": [
      "string"
    ],
    "deleted": false
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```
</details>

<details>
<summary>Response 404</summary>

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/schedules/:id' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

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

	  const response = await highLevel.calendars.updateSchedule({

	    'id': 'sch123def456ghi789'

	  },

	  {

	    'name': 'Updated Business Hours',

	    'rules': [

	      {

	        'type': 'wday',

	        'day': 'monday',

	        'intervals': [

	          {

	            'from': '08:00',

	            'to': '18:00'

	          }

	        ]

	      }

	    ],

	    'timezone': 'America/Los_Angeles'

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

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/calendars/schedules/:id',

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

	  'path': '/calendars/schedules/:id',

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

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/calendars/schedules/:id',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "name": "Updated Business Hours",

	    "rules": [

	      {

	        "type": "wday",

	        "day": "monday",

	        "intervals": [

	          {

	            "from": "08:00",

	            "to": "18:00"

	          }

	        ]

	      }

	    ],

	    "timezone": "America/Los_Angeles"

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/calendars/schedules/:id')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "name": "Updated Business Hours",

	    "rules": [

	      {

	        "type": "wday",

	        "day": "monday",

	        "intervals": [

	          {

	            "from": "08:00",

	            "to": "18:00"

	          }

	        ]

	      }

	    ],

	    "timezone": "America/Los_Angeles"

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

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/calendars/schedules/:id", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/calendars/schedules/:id"

	

	payload = json.dumps({

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/calendars/schedules/:id',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

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

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/calendars/schedules/:id', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/calendars/schedules/:id');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "name": "Updated Business Hours",\n  "rules": [\n    {\n      "type": "wday",\n      "day": "monday",\n      "intervals": [\n        {\n          "from": "08:00",\n          "to": "18:00"\n        }\n      ]\n    }\n  ],\n  "timezone": "America/Los_Angeles"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/calendars/schedules/:id');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Updated Business Hours\",\n  \"rules\": [\n    {\n      \"type\": \"wday\",\n      \"day\": \"monday\",\n      \"intervals\": [\n        {\n          \"from\": \"08:00\",\n          \"to\": \"18:00\"\n        }\n      ]\n    }\n  ],\n  \"timezone\": \"America/Los_Angeles\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/calendars/schedules/:id")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/calendars/schedules/:id")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"name\": \"Updated Business Hours\",\n  \"rules\": [\n    {\n      \"type\": \"wday\",\n      \"day\": \"monday\",\n      \"intervals\": [\n        {\n          \"from\": \"08:00\",\n          \"to\": \"18:00\"\n        }\n      ]\n    }\n  ],\n  \"timezone\": \"America/Los_Angeles\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/calendars/schedules/:id"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

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

	

	url = URI("https://services.leadconnectorhq.com/calendars/schedules/:id")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "name": "Updated Business Hours",

	  "rules": [

	    {

	      "type": "wday",

	      "day": "monday",

	      "intervals": [

	        {

	          "from": "08:00",

	          "to": "18:00"

	        }

	      ]

	    }

	  ],

	  "timezone": "America/Los_Angeles"

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

	  `"name`": `"Updated Business Hours`",

	  `"rules`": [

	    {

	      `"type`": `"wday`",

	      `"day`": `"monday`",

	      `"intervals`": [

	        {

	          `"from`": `"08:00`",

	          `"to`": `"18:00`"

	        }

	      ]

	    }

	  ],

	  `"timezone`": `"America/Los_Angeles`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/schedules/:id' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

