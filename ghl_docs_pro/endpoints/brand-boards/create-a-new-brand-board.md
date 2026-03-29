# Create a new brand board

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/brand-boards/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: brand-boards/design-kit.write
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
  "_id": "507f1f77bcf86cd799439011",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "My Brand Board",
  "logos": [
    {
      "id": "logo_abc123",
      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",
      "label": "Primary Logo",
      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"
    }
  ],
  "colors": [
    {
      "id": "color_xyz789",
      "hexa": "#FF5733FF",
      "rgba": "rgba(255, 87, 51, 1)",
      "hex": "#FF5733",
      "rgb": "rgb(255, 87, 51)",
      "label": "Brand Orange"
    }
  ],
  "fonts": [
    {
      "id": "font_def456",
      "font": "Montserrat",
      "fallback": "sans-serif",
      "label": "Heading Font"
    }
  ],
  "default": false,
  "deleted": false,
  "parentId": "507f1f77bcf86cd799439011",
  "folderId": "507f1f77bcf86cd799439011",
  "originId": "507f1f77bcf86cd799439011",
  "meta": {
    "updatedBy": "user_abc123",
    "lastAction": "UPDATE",
    "sourceId": "507f1f77bcf86cd799439011",
    "sourceType": "blank"
  },
  "createdAt": "2024-01-05T12:00:00.000Z",
  "updatedAt": "2024-01-05T12:00:00.000Z"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```
</details>

<details>
<summary>Response 403</summary>

```json
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/brand-boards/' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

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

	  const response = await highLevel.brandBoards.createBrandBoard({

	    'locationId': 've9EPM428h8vShlRW1KT',

	    'name': 'My Brand Board',

	    'logos': [

	      {

	        'id': 'logo_abc123',

	        'url': 'https://storage.googleapis.com/bucket/logos/my-logo.png',

	        'label': 'Primary Logo',

	        'path': '/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png'

	      }

	    ],

	    'colors': [

	      {

	        'id': 'color_xyz789',

	        'hexa': '#FF5733FF',

	        'rgba': 'rgba(255, 87, 51, 1)',

	        'hex': '#FF5733',

	        'rgb': 'rgb(255, 87, 51)',

	        'label': 'Brand Orange'

	      }

	    ],

	    'fonts': [

	      {

	        'id': 'font_def456',

	        'font': 'Montserrat',

	        'fallback': 'sans-serif',

	        'label': 'Heading Font'

	      }

	    ],

	    'default': true,

	    'brandBoardId': '507f1f77bcf86cd799439011',

	    'parentId': '507f1f77bcf86cd799439011',

	    'type': 'blank'

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/brand-boards/',

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

	  'path': '/brand-boards/',

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/brand-boards/',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "ve9EPM428h8vShlRW1KT",

	    "name": "My Brand Board",

	    "logos": [

	      {

	        "id": "logo_abc123",

	        "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	        "label": "Primary Logo",

	        "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	      }

	    ],

	    "colors": [

	      {

	        "id": "color_xyz789",

	        "hexa": "#FF5733FF",

	        "rgba": "rgba(255, 87, 51, 1)",

	        "hex": "#FF5733",

	        "rgb": "rgb(255, 87, 51)",

	        "label": "Brand Orange"

	      }

	    ],

	    "fonts": [

	      {

	        "id": "font_def456",

	        "font": "Montserrat",

	        "fallback": "sans-serif",

	        "label": "Heading Font"

	      }

	    ],

	    "default": true,

	    "brandBoardId": "507f1f77bcf86cd799439011",

	    "parentId": "507f1f77bcf86cd799439011",

	    "type": "blank"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/brand-boards/')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "ve9EPM428h8vShlRW1KT",

	    "name": "My Brand Board",

	    "logos": [

	      {

	        "id": "logo_abc123",

	        "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	        "label": "Primary Logo",

	        "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	      }

	    ],

	    "colors": [

	      {

	        "id": "color_xyz789",

	        "hexa": "#FF5733FF",

	        "rgba": "rgba(255, 87, 51, 1)",

	        "hex": "#FF5733",

	        "rgb": "rgb(255, 87, 51)",

	        "label": "Brand Orange"

	      }

	    ],

	    "fonts": [

	      {

	        "id": "font_def456",

	        "font": "Montserrat",

	        "fallback": "sans-serif",

	        "label": "Heading Font"

	      }

	    ],

	    "default": true,

	    "brandBoardId": "507f1f77bcf86cd799439011",

	    "parentId": "507f1f77bcf86cd799439011",

	    "type": "blank"

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": True,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/brand-boards/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/brand-boards/"

	

	payload = json.dumps({

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": True,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/brand-boards/',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/brand-boards/', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/brand-boards/');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "ve9EPM428h8vShlRW1KT",\n  "name": "My Brand Board",\n  "logos": [\n    {\n      "id": "logo_abc123",\n      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",\n      "label": "Primary Logo",\n      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"\n    }\n  ],\n  "colors": [\n    {\n      "id": "color_xyz789",\n      "hexa": "#FF5733FF",\n      "rgba": "rgba(255, 87, 51, 1)",\n      "hex": "#FF5733",\n      "rgb": "rgb(255, 87, 51)",\n      "label": "Brand Orange"\n    }\n  ],\n  "fonts": [\n    {\n      "id": "font_def456",\n      "font": "Montserrat",\n      "fallback": "sans-serif",\n      "label": "Heading Font"\n    }\n  ],\n  "default": true,\n  "brandBoardId": "507f1f77bcf86cd799439011",\n  "parentId": "507f1f77bcf86cd799439011",\n  "type": "blank"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/brand-boards/');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"ve9EPM428h8vShlRW1KT\",\n  \"name\": \"My Brand Board\",\n  \"logos\": [\n    {\n      \"id\": \"logo_abc123\",\n      \"url\": \"https://storage.googleapis.com/bucket/logos/my-logo.png\",\n      \"label\": \"Primary Logo\",\n      \"path\": \"/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png\"\n    }\n  ],\n  \"colors\": [\n    {\n      \"id\": \"color_xyz789\",\n      \"hexa\": \"#FF5733FF\",\n      \"rgba\": \"rgba(255, 87, 51, 1)\",\n      \"hex\": \"#FF5733\",\n      \"rgb\": \"rgb(255, 87, 51)\",\n      \"label\": \"Brand Orange\"\n    }\n  ],\n  \"fonts\": [\n    {\n      \"id\": \"font_def456\",\n      \"font\": \"Montserrat\",\n      \"fallback\": \"sans-serif\",\n      \"label\": \"Heading Font\"\n    }\n  ],\n  \"default\": true,\n  \"brandBoardId\": \"507f1f77bcf86cd799439011\",\n  \"parentId\": \"507f1f77bcf86cd799439011\",\n  \"type\": \"blank\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/brand-boards/")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/brand-boards/")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"ve9EPM428h8vShlRW1KT\",\n  \"name\": \"My Brand Board\",\n  \"logos\": [\n    {\n      \"id\": \"logo_abc123\",\n      \"url\": \"https://storage.googleapis.com/bucket/logos/my-logo.png\",\n      \"label\": \"Primary Logo\",\n      \"path\": \"/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png\"\n    }\n  ],\n  \"colors\": [\n    {\n      \"id\": \"color_xyz789\",\n      \"hexa\": \"#FF5733FF\",\n      \"rgba\": \"rgba(255, 87, 51, 1)\",\n      \"hex\": \"#FF5733\",\n      \"rgb\": \"rgb(255, 87, 51)\",\n      \"label\": \"Brand Orange\"\n    }\n  ],\n  \"fonts\": [\n    {\n      \"id\": \"font_def456\",\n      \"font\": \"Montserrat\",\n      \"fallback\": \"sans-serif\",\n      \"label\": \"Heading Font\"\n    }\n  ],\n  \"default\": true,\n  \"brandBoardId\": \"507f1f77bcf86cd799439011\",\n  \"parentId\": \"507f1f77bcf86cd799439011\",\n  \"type\": \"blank\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/brand-boards/"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

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

	

	url = URI("https://services.leadconnectorhq.com/brand-boards/")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "name": "My Brand Board",

	  "logos": [

	    {

	      "id": "logo_abc123",

	      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",

	      "label": "Primary Logo",

	      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"

	    }

	  ],

	  "colors": [

	    {

	      "id": "color_xyz789",

	      "hexa": "\#FF5733FF",

	      "rgba": "rgba(255, 87, 51, 1)",

	      "hex": "\#FF5733",

	      "rgb": "rgb(255, 87, 51)",

	      "label": "Brand Orange"

	    }

	  ],

	  "fonts": [

	    {

	      "id": "font_def456",

	      "font": "Montserrat",

	      "fallback": "sans-serif",

	      "label": "Heading Font"

	    }

	  ],

	  "default": true,

	  "brandBoardId": "507f1f77bcf86cd799439011",

	  "parentId": "507f1f77bcf86cd799439011",

	  "type": "blank"

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

	  `"locationId`": `"ve9EPM428h8vShlRW1KT`",

	  `"name`": `"My Brand Board`",

	  `"logos`": [

	    {

	      `"id`": `"logo_abc123`",

	      `"url`": `"https://storage.googleapis.com/bucket/logos/my-logo.png`",

	      `"label`": `"Primary Logo`",

	      `"path`": `"/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png`"

	    }

	  ],

	  `"colors`": [

	    {

	      `"id`": `"color_xyz789`",

	      `"hexa`": `"#FF5733FF`",

	      `"rgba`": `"rgba(255, 87, 51, 1)`",

	      `"hex`": `"#FF5733`",

	      `"rgb`": `"rgb(255, 87, 51)`",

	      `"label`": `"Brand Orange`"

	    }

	  ],

	  `"fonts`": [

	    {

	      `"id`": `"font_def456`",

	      `"font`": `"Montserrat`",

	      `"fallback`": `"sans-serif`",

	      `"label`": `"Heading Font`"

	    }

	  ],

	  `"default`": true,

	  `"brandBoardId`": `"507f1f77bcf86cd799439011`",

	  `"parentId`": `"507f1f77bcf86cd799439011`",

	  `"type`": `"blank`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/brand-boards/' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

