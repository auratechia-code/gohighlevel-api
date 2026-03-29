# Create Custom Field

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/locations/:locationId/customFields`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: locations/customFields.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 201</summary>

```json
{
  "customField": {
    "id": "3sv6UEo51C9Bmpo1cKTq",
    "name": "pincode",
    "fieldKey": "contact.pincode",
    "placeholder": "Pin code",
    "dataType": "TEXT",
    "position": 0,
    "picklistOptions": [
      "first option"
    ],
    "picklistImageOptions": [],
    "isAllowedCustomOption": false,
    "isMultiFileAllowed": true,
    "maxFileLimit": 4,
    "locationId": "3sv6UEo51C9Bmpo1cKTq",
    "model": "opportunity"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "customField": {    "id": "3sv6UEo51C9Bmpo1cKTq",    "name": "pincode",    "fieldKey": "contact.pincode",    "placeholder": "Pin code",    "dataType": "TEXT",    "position": 0,    "picklistOptions": [      "first option"    ],    "picklistImageOptions": [],    "isAllowedCustomOption": false,    "isMultiFileAllowed": true,    "maxFileLimit": 4,    "locationId": "3sv6UEo51C9Bmpo1cKTq",    "model": "opportunity"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "customField": {    "id": "3sv6UEo51C9Bmpo1cKTq",    "name": "pincode",    "fieldKey": "contact.pincode",    "placeholder": "Pin code",    "dataType": "TEXT",    "position": 0,    "picklistOptions": [      "first option"    ],    "picklistImageOptions": [],    "isAllowedCustomOption": false,    "isMultiFileAllowed": true,    "maxFileLimit": 4,    "locationId": "3sv6UEo51C9Bmpo1cKTq",    "model": "opportunity"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "customField": {    "id": "3sv6UEo51C9Bmpo1cKTq",    "name": "pincode",    "fieldKey": "contact.pincode",    "placeholder": "Pin code",    "dataType": "TEXT",    "position": 0,    "picklistOptions": [      "first option"    ],    "picklistImageOptions": [],    "isAllowedCustomOption": false,    "isMultiFileAllowed": true,    "maxFileLimit": 4,    "locationId": "3sv6UEo51C9Bmpo1cKTq",    "model": "opportunity"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/locations/:locationId/customFields' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

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

	  const response = await highLevel.locations.createCustomField({

	    'locationId': 've9EPM428h8vShlRW1KT'

	  },

	  {

	    'name': 'Custom Field',

	    'dataType': 'TEXT',

	    'placeholder': 'Placeholder Text',

	    'acceptedFormat': [

	      '.pdf',

	      '.docx',

	      '.jpeg'

	    ],

	    'isMultipleFile': false,

	    'maxNumberOfFiles': 2,

	    'textBoxListOptions': [

	      {

	        'label': 'First',

	        'prefillValue': ''

	      },

	      {

	        'label': 'First',

	        'prefillValue': ''

	      }

	    ],

	    'position': 0,

	    'model': 'opportunity'

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

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/locations/:locationId/customFields',

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

	  'path': '/locations/:locationId/customFields',

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

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/locations/:locationId/customFields',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "name": "Custom Field",

	    "dataType": "TEXT",

	    "placeholder": "Placeholder Text",

	    "acceptedFormat": [

	      ".pdf",

	      ".docx",

	      ".jpeg"

	    ],

	    "isMultipleFile": false,

	    "maxNumberOfFiles": 2,

	    "textBoxListOptions": [

	      {

	        "label": "First",

	        "prefillValue": ""

	      },

	      {

	        "label": "First",

	        "prefillValue": ""

	      }

	    ],

	    "position": 0,

	    "model": "opportunity"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/locations/:locationId/customFields')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "name": "Custom Field",

	    "dataType": "TEXT",

	    "placeholder": "Placeholder Text",

	    "acceptedFormat": [

	      ".pdf",

	      ".docx",

	      ".jpeg"

	    ],

	    "isMultipleFile": false,

	    "maxNumberOfFiles": 2,

	    "textBoxListOptions": [

	      {

	        "label": "First",

	        "prefillValue": ""

	      },

	      {

	        "label": "First",

	        "prefillValue": ""

	      }

	    ],

	    "position": 0,

	    "model": "opportunity"

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

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": False,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/locations/:locationId/customFields", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/locations/:locationId/customFields"

	

	payload = json.dumps({

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": False,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/locations/:locationId/customFields',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

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

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/locations/:locationId/customFields', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/locations/:locationId/customFields');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "name": "Custom Field",\n  "dataType": "TEXT",\n  "placeholder": "Placeholder Text",\n  "acceptedFormat": [\n    ".pdf",\n    ".docx",\n    ".jpeg"\n  ],\n  "isMultipleFile": false,\n  "maxNumberOfFiles": 2,\n  "textBoxListOptions": [\n    {\n      "label": "First",\n      "prefillValue": ""\n    },\n    {\n      "label": "First",\n      "prefillValue": ""\n    }\n  ],\n  "position": 0,\n  "model": "opportunity"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/locations/:locationId/customFields');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Custom Field\",\n  \"dataType\": \"TEXT\",\n  \"placeholder\": \"Placeholder Text\",\n  \"acceptedFormat\": [\n    \".pdf\",\n    \".docx\",\n    \".jpeg\"\n  ],\n  \"isMultipleFile\": false,\n  \"maxNumberOfFiles\": 2,\n  \"textBoxListOptions\": [\n    {\n      \"label\": \"First\",\n      \"prefillValue\": \"\"\n    },\n    {\n      \"label\": \"First\",\n      \"prefillValue\": \"\"\n    }\n  ],\n  \"position\": 0,\n  \"model\": \"opportunity\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/locations/:locationId/customFields")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/locations/:locationId/customFields")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"name\": \"Custom Field\",\n  \"dataType\": \"TEXT\",\n  \"placeholder\": \"Placeholder Text\",\n  \"acceptedFormat\": [\n    \".pdf\",\n    \".docx\",\n    \".jpeg\"\n  ],\n  \"isMultipleFile\": false,\n  \"maxNumberOfFiles\": 2,\n  \"textBoxListOptions\": [\n    {\n      \"label\": \"First\",\n      \"prefillValue\": \"\"\n    },\n    {\n      \"label\": \"First\",\n      \"prefillValue\": \"\"\n    }\n  ],\n  \"position\": 0,\n  \"model\": \"opportunity\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/locations/:locationId/customFields"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

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

	

	url = URI("https://services.leadconnectorhq.com/locations/:locationId/customFields")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "name": "Custom Field",

	  "dataType": "TEXT",

	  "placeholder": "Placeholder Text",

	  "acceptedFormat": [

	    ".pdf",

	    ".docx",

	    ".jpeg"

	  ],

	  "isMultipleFile": false,

	  "maxNumberOfFiles": 2,

	  "textBoxListOptions": [

	    {

	      "label": "First",

	      "prefillValue": ""

	    },

	    {

	      "label": "First",

	      "prefillValue": ""

	    }

	  ],

	  "position": 0,

	  "model": "opportunity"

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

	  `"name`": `"Custom Field`",

	  `"dataType`": `"TEXT`",

	  `"placeholder`": `"Placeholder Text`",

	  `"acceptedFormat`": [

	    `".pdf`",

	    `".docx`",

	    `".jpeg`"

	  ],

	  `"isMultipleFile`": false,

	  `"maxNumberOfFiles`": 2,

	  `"textBoxListOptions`": [

	    {

	      `"label`": `"First`",

	      `"prefillValue`": `"`"

	    },

	    {

	      `"label`": `"First`",

	      `"prefillValue`": `"`"

	    }

	  ],

	  `"position`": 0,

	  `"model`": `"opportunity`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/locations/:locationId/customFields' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

