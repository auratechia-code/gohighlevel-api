# Update Service

**Method:** `PUT` | **URL:** `https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId`

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
| `serviceId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "service": {
    "id": "65e5f6dfacf123513228d384",
    "locationId": "0007BWpSzSwfiuSl0tR2",
    "name": "Hair Styling",
    "description": "Full hair styling session",
    "slug": "hair-styling",
    "eventColor": "#66C61C",
    "coverImage": "https://example.com/cover.jpg",
    "serviceCategoryId": "65e5f6dfacf123513228d381",
    "payment": {
      "amount": 50,
      "deposit": 20,
      "depositType": "amount"
    },
    "serviceDuration": 60,
    "serviceDurationUnit": "mins",
    "preBuffer": 10,
    "preBufferUnit": "mins",
    "postBuffer": 15,
    "postBufferUnit": "mins",
    "isPrivate": false,
    "formId": "65e5f6dfacf123513228d390",
    "variations": [
      {
        "id": "65e5f6dfacf123513228d384",
        "name": "Standard Haircut",
        "serviceDuration": 30,
        "serviceDurationUnit": "mins",
        "payment": {
          "amount": 50,
          "deposit": 20,
          "depositType": "amount"
        },
        "preBuffer": 10,
        "preBufferUnit": "mins",
        "postBuffer": 15,
        "postBufferUnit": "mins"
      }
    ],
    "staff": [
      {
        "id": "65e5f6dfacf123513228d384"
      }
    ]
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling",    "description": "Full hair styling session",    "slug": "hair-styling",    "eventColor": "#66C61C",    "coverImage": "https://example.com/cover.jpg",    "serviceCategoryId": "65e5f6dfacf123513228d381",    "payment": {      "amount": 50,      "deposit": 20,      "depositType": "amount"    },    "serviceDuration": 60,    "serviceDurationUnit": "mins",    "preBuffer": 10,    "preBufferUnit": "mins",    "postBuffer": 15,    "postBufferUnit": "mins",    "isPrivate": false,    "formId": "65e5f6dfacf123513228d390",    "variations": [      {        "id": "65e5f6dfacf123513228d384",        "name": "Standard Haircut",        "serviceDuration": 30,        "serviceDurationUnit": "mins",        "payment": {          "amount": 50,          "deposit": 20,          "depositType": "amount"        },        "preBuffer": 10,        "preBufferUnit": "mins",        "postBuffer": 15,        "postBufferUnit": "mins"      }    ],    "staff": [      {        "id": "65e5f6dfacf123513228d384"      }    ]  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "service": {    "id": "65e5f6dfacf123513228d384",    "locationId": "0007BWpSzSwfiuSl0tR2",    "name": "Hair Styling",    "description": "Full hair styling session",    "slug": "hair-styling",    "eventColor": "#66C61C",    "coverImage": "https://example.com/cover.jpg",    "serviceCategoryId": "65e5f6dfacf123513228d381",    "payment": {      "amount": 50,      "deposit": 20,      "depositType": "amount"    },    "serviceDuration": 60,    "serviceDurationUnit": "mins",    "preBuffer": 10,    "preBufferUnit": "mins",    "postBuffer": 15,    "postBufferUnit": "mins",    "isPrivate": false,    "formId": "65e5f6dfacf123513228d390",    "variations": [      {        "id": "65e5f6dfacf123513228d384",        "name": "Standard Haircut",        "serviceDuration": 30,        "serviceDurationUnit": "mins",        "payment": {          "amount": 50,          "deposit": 20,          "depositType": "amount"        },        "preBuffer": 10,        "preBufferUnit": "mins",        "postBuffer": 15,        "postBufferUnit": "mins"      }    ],    "staff": [      {        "id": "65e5f6dfacf123513228d384"      }    ]  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PUT 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	  const response = await highLevel.calendars.updateServiceCatalog({

	    'serviceId': '65e5f6dfacf123513228d384'

	  },

	  {

	    'name': 'Hair Styling',

	    'description': 'Full hair styling session',

	    'slug': 'hair-styling',

	    'eventColor': '#66C61C',

	    'coverImage': 'https://example.com/cover.jpg',

	    'serviceCategoryId': '65e5f6dfacf123513228d381',

	    'payment': {

	      'amount': 50,

	      'deposit': 20,

	      'depositType': 'amount'

	    },

	    'serviceDuration': 60,

	    'serviceDurationUnit': 'mins',

	    'preBuffer': 10,

	    'preBufferUnit': 'mins',

	    'postBuffer': 15,

	    'postBufferUnit': 'mins',

	    'isPrivate': false,

	    'formId': '65e5f6dfacf123513228d390',

	    'staff': [

	      {

	        'id': '65e5f6dfacf123513228d384'

	      }

	    ],

	    'variations': [

	      {

	        'serviceDuration': 30,

	        'serviceDurationUnit': 'mins',

	        'preBuffer': 10,

	        'preBufferUnit': 'mins',

	        'postBuffer': 15,

	        'postBufferUnit': 'mins',

	        'payment': {

	          'amount': 50,

	          'deposit': 20,

	          'depositType': 'amount'

	        },

	        'id': '65e5f6dfacf123513228d385',

	        'name': 'Standard Haircut'

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

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

	    }

	  ]

	});

	

	let config = {

	  method: 'put',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId',

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

	  'path': '/calendars/services/catalog/:serviceId',

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

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	  'url': 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "name": "Hair Styling",

	    "description": "Full hair styling session",

	    "slug": "hair-styling",

	    "eventColor": "#66C61C",

	    "coverImage": "https://example.com/cover.jpg",

	    "serviceCategoryId": "65e5f6dfacf123513228d381",

	    "payment": {

	      "amount": 50,

	      "deposit": 20,

	      "depositType": "amount"

	    },

	    "serviceDuration": 60,

	    "serviceDurationUnit": "mins",

	    "preBuffer": 10,

	    "preBufferUnit": "mins",

	    "postBuffer": 15,

	    "postBufferUnit": "mins",

	    "isPrivate": false,

	    "formId": "65e5f6dfacf123513228d390",

	    "staff": [

	      {

	        "id": "65e5f6dfacf123513228d384"

	      }

	    ],

	    "variations": [

	      {

	        "serviceDuration": 30,

	        "serviceDurationUnit": "mins",

	        "preBuffer": 10,

	        "preBufferUnit": "mins",

	        "postBuffer": 15,

	        "postBufferUnit": "mins",

	        "payment": {

	          "amount": 50,

	          "deposit": 20,

	          "depositType": "amount"

	        },

	        "id": "65e5f6dfacf123513228d385",

	        "name": "Standard Haircut"

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

	var req = unirest('PUT', 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "name": "Hair Styling",

	    "description": "Full hair styling session",

	    "slug": "hair-styling",

	    "eventColor": "#66C61C",

	    "coverImage": "https://example.com/cover.jpg",

	    "serviceCategoryId": "65e5f6dfacf123513228d381",

	    "payment": {

	      "amount": 50,

	      "deposit": 20,

	      "depositType": "amount"

	    },

	    "serviceDuration": 60,

	    "serviceDurationUnit": "mins",

	    "preBuffer": 10,

	    "preBufferUnit": "mins",

	    "postBuffer": 15,

	    "postBufferUnit": "mins",

	    "isPrivate": false,

	    "formId": "65e5f6dfacf123513228d390",

	    "staff": [

	      {

	        "id": "65e5f6dfacf123513228d384"

	      }

	    ],

	    "variations": [

	      {

	        "serviceDuration": 30,

	        "serviceDurationUnit": "mins",

	        "preBuffer": 10,

	        "preBufferUnit": "mins",

	        "postBuffer": 15,

	        "postBufferUnit": "mins",

	        "payment": {

	          "amount": 50,

	          "deposit": 20,

	          "depositType": "amount"

	        },

	        "id": "65e5f6dfacf123513228d385",

	        "name": "Standard Haircut"

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

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": False,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

	    }

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PUT", "/calendars/services/catalog/:serviceId", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId"

	

	payload = json.dumps({

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": False,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PUT',

	  CURLOPT_POSTFIELDS =>'{

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

	    }

	  ]

	}';

	$request = new Request('PUT', 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId');

	$request->setMethod(HTTP_Request2::METHOD_PUT);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "name": "Hair Styling",\n  "description": "Full hair styling session",\n  "slug": "hair-styling",\n  "eventColor": "#66C61C",\n  "coverImage": "https://example.com/cover.jpg",\n  "serviceCategoryId": "65e5f6dfacf123513228d381",\n  "payment": {\n    "amount": 50,\n    "deposit": 20,\n    "depositType": "amount"\n  },\n  "serviceDuration": 60,\n  "serviceDurationUnit": "mins",\n  "preBuffer": 10,\n  "preBufferUnit": "mins",\n  "postBuffer": 15,\n  "postBufferUnit": "mins",\n  "isPrivate": false,\n  "formId": "65e5f6dfacf123513228d390",\n  "staff": [\n    {\n      "id": "65e5f6dfacf123513228d384"\n    }\n  ],\n  "variations": [\n    {\n      "serviceDuration": 30,\n      "serviceDurationUnit": "mins",\n      "preBuffer": 10,\n      "preBufferUnit": "mins",\n      "postBuffer": 15,\n      "postBufferUnit": "mins",\n      "payment": {\n        "amount": 50,\n        "deposit": 20,\n        "depositType": "amount"\n      },\n      "id": "65e5f6dfacf123513228d385",\n      "name": "Standard Haircut"\n    }\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId');

	$request->setRequestMethod('PUT');

	$body = new http\Message\Body;

	$body->append('{

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Hair Styling\",\n  \"description\": \"Full hair styling session\",\n  \"slug\": \"hair-styling\",\n  \"eventColor\": \"#66C61C\",\n  \"coverImage\": \"https://example.com/cover.jpg\",\n  \"serviceCategoryId\": \"65e5f6dfacf123513228d381\",\n  \"payment\": {\n    \"amount\": 50,\n    \"deposit\": 20,\n    \"depositType\": \"amount\"\n  },\n  \"serviceDuration\": 60,\n  \"serviceDurationUnit\": \"mins\",\n  \"preBuffer\": 10,\n  \"preBufferUnit\": \"mins\",\n  \"postBuffer\": 15,\n  \"postBufferUnit\": \"mins\",\n  \"isPrivate\": false,\n  \"formId\": \"65e5f6dfacf123513228d390\",\n  \"staff\": [\n    {\n      \"id\": \"65e5f6dfacf123513228d384\"\n    }\n  ],\n  \"variations\": [\n    {\n      \"serviceDuration\": 30,\n      \"serviceDurationUnit\": \"mins\",\n      \"preBuffer\": 10,\n      \"preBufferUnit\": \"mins\",\n      \"postBuffer\": 15,\n      \"postBufferUnit\": \"mins\",\n      \"payment\": {\n        \"amount\": 50,\n        \"deposit\": 20,\n        \"depositType\": \"amount\"\n      },\n      \"id\": \"65e5f6dfacf123513228d385\",\n      \"name\": \"Standard Haircut\"\n    }\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId")

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

	HttpResponse<String> response = Unirest.put("https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"name\": \"Hair Styling\",\n  \"description\": \"Full hair styling session\",\n  \"slug\": \"hair-styling\",\n  \"eventColor\": \"#66C61C\",\n  \"coverImage\": \"https://example.com/cover.jpg\",\n  \"serviceCategoryId\": \"65e5f6dfacf123513228d381\",\n  \"payment\": {\n    \"amount\": 50,\n    \"deposit\": 20,\n    \"depositType\": \"amount\"\n  },\n  \"serviceDuration\": 60,\n  \"serviceDurationUnit\": \"mins\",\n  \"preBuffer\": 10,\n  \"preBufferUnit\": \"mins\",\n  \"postBuffer\": 15,\n  \"postBufferUnit\": \"mins\",\n  \"isPrivate\": false,\n  \"formId\": \"65e5f6dfacf123513228d390\",\n  \"staff\": [\n    {\n      \"id\": \"65e5f6dfacf123513228d384\"\n    }\n  ],\n  \"variations\": [\n    {\n      \"serviceDuration\": 30,\n      \"serviceDurationUnit\": \"mins\",\n      \"preBuffer\": 10,\n      \"preBufferUnit\": \"mins\",\n      \"postBuffer\": 15,\n      \"postBufferUnit\": \"mins\",\n      \"payment\": {\n        \"amount\": 50,\n        \"deposit\": 20,\n        \"depositType\": \"amount\"\n      },\n      \"id\": \"65e5f6dfacf123513228d385\",\n      \"name\": \"Standard Haircut\"\n    }\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId"

	  method := "PUT"

	

	  payload := strings.NewReader(`{

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	

	url = URI("https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Put.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "name": "Hair Styling",

	  "description": "Full hair styling session",

	  "slug": "hair-styling",

	  "eventColor": "\#66C61C",

	  "coverImage": "https://example.com/cover.jpg",

	  "serviceCategoryId": "65e5f6dfacf123513228d381",

	  "payment": {

	    "amount": 50,

	    "deposit": 20,

	    "depositType": "amount"

	  },

	  "serviceDuration": 60,

	  "serviceDurationUnit": "mins",

	  "preBuffer": 10,

	  "preBufferUnit": "mins",

	  "postBuffer": 15,

	  "postBufferUnit": "mins",

	  "isPrivate": false,

	  "formId": "65e5f6dfacf123513228d390",

	  "staff": [

	    {

	      "id": "65e5f6dfacf123513228d384"

	    }

	  ],

	  "variations": [

	    {

	      "serviceDuration": 30,

	      "serviceDurationUnit": "mins",

	      "preBuffer": 10,

	      "preBufferUnit": "mins",

	      "postBuffer": 15,

	      "postBufferUnit": "mins",

	      "payment": {

	        "amount": 50,

	        "deposit": 20,

	        "depositType": "amount"

	      },

	      "id": "65e5f6dfacf123513228d385",

	      "name": "Standard Haircut"

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

	  `"name`": `"Hair Styling`",

	  `"description`": `"Full hair styling session`",

	  `"slug`": `"hair-styling`",

	  `"eventColor`": `"#66C61C`",

	  `"coverImage`": `"https://example.com/cover.jpg`",

	  `"serviceCategoryId`": `"65e5f6dfacf123513228d381`",

	  `"payment`": {

	    `"amount`": 50,

	    `"deposit`": 20,

	    `"depositType`": `"amount`"

	  },

	  `"serviceDuration`": 60,

	  `"serviceDurationUnit`": `"mins`",

	  `"preBuffer`": 10,

	  `"preBufferUnit`": `"mins`",

	  `"postBuffer`": 15,

	  `"postBufferUnit`": `"mins`",

	  `"isPrivate`": false,

	  `"formId`": `"65e5f6dfacf123513228d390`",

	  `"staff`": [

	    {

	      `"id`": `"65e5f6dfacf123513228d384`"

	    }

	  ],

	  `"variations`": [

	    {

	      `"serviceDuration`": 30,

	      `"serviceDurationUnit`": `"mins`",

	      `"preBuffer`": 10,

	      `"preBufferUnit`": `"mins`",

	      `"postBuffer`": 15,

	      `"postBufferUnit`": `"mins`",

	      `"payment`": {

	        `"amount`": 50,

	        `"deposit`": 20,

	        `"depositType`": `"amount`"

	      },

	      `"id`": `"65e5f6dfacf123513228d385`",

	      `"name`": `"Standard Haircut`"

	    }

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/services/catalog/:serviceId' -Method 'PUT' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

