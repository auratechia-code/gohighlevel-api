# Update Opportunity

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/opportunities/:id`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: opportunities.write
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
  "opportunity": {
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
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/opportunities/:id' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

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

	  const response = await highLevel.opportunities.updateOpportunity({

	    'id': 'yWQobCRIhRguQtD2llvk'

	  },

	  {

	    'pipelineId': 'bCkKGpDsyPP4peuKowkG',

	    'name': 'First Opps',

	    'pipelineStageId': '7915dedc-8f18-44d5-8bc3-77c04e994a10',

	    'status': 'open',

	    'monetaryValue': 220,

	    'assignedTo': '082goXVW3lIExEQPOnd3',

	    'customFields': [

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': '9039160788'

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': [

	          'test',

	          'test2'

	        ]

	      },

	      {

	        'id': '6dvNaf7VhkQ9snc5vnjJ',

	        'key': 'my_custom_field',

	        'field_value': {}

	      }

	    ]

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

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/opportunities/:id',

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

	  'path': '/opportunities/:id',

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

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PUT',

	  'url': 'https://services.leadconnectorhq.com/opportunities/:id',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "pipelineId": "bCkKGpDsyPP4peuKowkG",

	    "name": "First Opps",

	    "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	    "status": "open",

	    "monetaryValue": 220,

	    "assignedTo": "082goXVW3lIExEQPOnd3",

	    "customFields": [

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "9039160788"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": [

	          "test",

	          "test2"

	        ]

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": {}

	      }

	    ]

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/opportunities/:id')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "pipelineId": "bCkKGpDsyPP4peuKowkG",

	    "name": "First Opps",

	    "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	    "status": "open",

	    "monetaryValue": 220,

	    "assignedTo": "082goXVW3lIExEQPOnd3",

	    "customFields": [

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": "9039160788"

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": [

	          "test",

	          "test2"

	        ]

	      },

	      {

	        "id": "6dvNaf7VhkQ9snc5vnjJ",

	        "key": "my_custom_field",

	        "field_value": {}

	      }

	    ]

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

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/opportunities/:id", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/opportunities/:id"

	

	payload = json.dumps({

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/opportunities/:id',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

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

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/opportunities/:id', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/opportunities/:id');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "pipelineId": "bCkKGpDsyPP4peuKowkG",\n  "name": "First Opps",\n  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",\n  "status": "open",\n  "monetaryValue": 220,\n  "assignedTo": "082goXVW3lIExEQPOnd3",\n  "customFields": [\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": "9039160788"\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": [\n        "test",\n        "test2"\n      ]\n    },\n    {\n      "id": "6dvNaf7VhkQ9snc5vnjJ",\n      "key": "my_custom_field",\n      "field_value": {}\n    }\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/opportunities/:id');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"pipelineId\": \"bCkKGpDsyPP4peuKowkG\",\n  \"name\": \"First Opps\",\n  \"pipelineStageId\": \"7915dedc-8f18-44d5-8bc3-77c04e994a10\",\n  \"status\": \"open\",\n  \"monetaryValue\": 220,\n  \"assignedTo\": \"082goXVW3lIExEQPOnd3\",\n  \"customFields\": [\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"9039160788\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": [\n        \"test\",\n        \"test2\"\n      ]\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": {}\n    }\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/opportunities/:id")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/opportunities/:id")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"pipelineId\": \"bCkKGpDsyPP4peuKowkG\",\n  \"name\": \"First Opps\",\n  \"pipelineStageId\": \"7915dedc-8f18-44d5-8bc3-77c04e994a10\",\n  \"status\": \"open\",\n  \"monetaryValue\": 220,\n  \"assignedTo\": \"082goXVW3lIExEQPOnd3\",\n  \"customFields\": [\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": \"9039160788\"\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": [\n        \"test\",\n        \"test2\"\n      ]\n    },\n    {\n      \"id\": \"6dvNaf7VhkQ9snc5vnjJ\",\n      \"key\": \"my_custom_field\",\n      \"field_value\": {}\n    }\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/opportunities/:id"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

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

	

	url = URI("https://services.leadconnectorhq.com/opportunities/:id")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "pipelineId": "bCkKGpDsyPP4peuKowkG",

	  "name": "First Opps",

	  "pipelineStageId": "7915dedc-8f18-44d5-8bc3-77c04e994a10",

	  "status": "open",

	  "monetaryValue": 220,

	  "assignedTo": "082goXVW3lIExEQPOnd3",

	  "customFields": [

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": "9039160788"

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": [

	        "test",

	        "test2"

	      ]

	    },

	    {

	      "id": "6dvNaf7VhkQ9snc5vnjJ",

	      "key": "my_custom_field",

	      "field_value": {}

	    }

	  ]

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

	  `"pipelineId`": `"bCkKGpDsyPP4peuKowkG`",

	  `"name`": `"First Opps`",

	  `"pipelineStageId`": `"7915dedc-8f18-44d5-8bc3-77c04e994a10`",

	  `"status`": `"open`",

	  `"monetaryValue`": 220,

	  `"assignedTo`": `"082goXVW3lIExEQPOnd3`",

	  `"customFields`": [

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": `"9039160788`"

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": [

	        `"test`",

	        `"test2`"

	      ]

	    },

	    {

	      `"id`": `"6dvNaf7VhkQ9snc5vnjJ`",

	      `"key`": `"my_custom_field`",

	      `"field_value`": {}

	    }

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/opportunities/:id' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

