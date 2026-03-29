# Search Object Records

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/objects/:schemaKey/records/search`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: objects/record.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `schemaKey` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "records": [
    {
      "id": "661c06b4ffde146bdb469442",
      "owner": [
        "sx6wyHhbFdRXh302Lunr"
      ],
      "followers": [
        "sx6wyHhbFdRXh302Lunr",
        "v5cEPM428h8vShlRW1KT"
      ],
      "properties": {
        "customer_number": 1424,
        "ticket_name": "Customer not able login",
        "phone_number": "+917000000000",
        "money": {
          "currency": "default",
          "value": 100
        },
        "type_of_ticket": "doubt",
        "section_of_app": [
          "contacts",
          "smartlist"
        ],
        "recieved_on": "2024-07-11",
        "my_files": [
          {
            "url": "---url_of_file---"
          }
        ],
        "my_textbox_list.option_a": "Value 1",
        "my_textbox_list.option_b": "Value 2"
      },
      "createdAt": "2024-07-29T15:51:28.071Z",
      "updatedAt": "2024-07-29T15:51:28.071Z",
      "locationId": "ve9EPM428h8vShlRW1KT",
      "objectId": "6d6f6e676f5f6576656e7473",
      "objectKey": "custom_objects.pet",
      "createdBy": {
        "channel": "WEB_USER",
        "createdAt": "2025-01-02T09:35:39.032Z",
        "source": "PUBLIC_API",
        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"
      },
      "lastUpdatedBy": {
        "channel": "WEB_USER",
        "createdAt": "2025-01-02T09:35:39.032Z",
        "source": "PUBLIC_API",
        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"
      },
      "searchAfter": [
        1738683828372,
        "67a235b49b289431bcf657f8"
      ]
    }
  ],
  "total": 20
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "records": [    {      "id": "661c06b4ffde146bdb469442",      "owner": [        "sx6wyHhbFdRXh302Lunr"      ],      "followers": [        "sx6wyHhbFdRXh302Lunr",        "v5cEPM428h8vShlRW1KT"      ],      "properties": {        "customer_number": 1424,        "ticket_name": "Customer not able login",        "phone_number": "+917000000000",        "money": {          "currency": "default",          "value": 100        },        "type_of_ticket": "doubt",        "section_of_app": [          "contacts",          "smartlist"        ],        "recieved_on": "2024-07-11",        "my_files": [          {            "url": "---url_of_file---"          }        ],        "my_textbox_list.option_a": "Value 1",        "my_textbox_list.option_b": "Value 2"      },      "createdAt": "2024-07-29T15:51:28.071Z",      "updatedAt": "2024-07-29T15:51:28.071Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "objectId": "6d6f6e676f5f6576656e7473",      "objectKey": "custom_objects.pet",      "createdBy": {        "channel": "WEB_USER",        "createdAt": "2025-01-02T09:35:39.032Z",        "source": "PUBLIC_API",        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"      },      "lastUpdatedBy": {        "channel": "WEB_USER",        "createdAt": "2025-01-02T09:35:39.032Z",        "source": "PUBLIC_API",        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"      },      "searchAfter": [        1738683828372,        "67a235b49b289431bcf657f8"      ]    }  ],  "total": 20}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "records": [    {      "id": "661c06b4ffde146bdb469442",      "owner": [        "sx6wyHhbFdRXh302Lunr"      ],      "followers": [        "sx6wyHhbFdRXh302Lunr",        "v5cEPM428h8vShlRW1KT"      ],      "properties": {        "customer_number": 1424,        "ticket_name": "Customer not able login",        "phone_number": "+917000000000",        "money": {          "currency": "default",          "value": 100        },        "type_of_ticket": "doubt",        "section_of_app": [          "contacts",          "smartlist"        ],        "recieved_on": "2024-07-11",        "my_files": [          {            "url": "---url_of_file---"          }        ],        "my_textbox_list.option_a": "Value 1",        "my_textbox_list.option_b": "Value 2"      },      "createdAt": "2024-07-29T15:51:28.071Z",      "updatedAt": "2024-07-29T15:51:28.071Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "objectId": "6d6f6e676f5f6576656e7473",      "objectKey": "custom_objects.pet",      "createdBy": {        "channel": "WEB_USER",        "createdAt": "2025-01-02T09:35:39.032Z",        "source": "PUBLIC_API",        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"      },      "lastUpdatedBy": {        "channel": "WEB_USER",        "createdAt": "2025-01-02T09:35:39.032Z",        "source": "PUBLIC_API",        "sourceId": "26653146-ec82-435d-8a99-84ecdb7fde13"      },      "searchAfter": [        1738683828372,        "67a235b49b289431bcf657f8"      ]    }  ],  "total": 20}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

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

	  const response = await highLevel.objects.searchObjectRecords({

	    'schemaKey': '632c34b4c9b7da3358ac9891'

	  },

	  {

	    'locationId': 've9EPM428h8vShlRW1KT',

	    'page': 1,

	    'pageLimit': 10,

	    'query': 'Buddy',

	    'searchAfter': [

	      'sx6wyHhbFdRXh302Lunr',

	      'sx6wyHhbFdRXh302Lunr'

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

	  ]

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search',

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

	  'path': '/objects/:schemaKey/records/search',

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

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

	  ]

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "ve9EPM428h8vShlRW1KT",

	    "page": 1,

	    "pageLimit": 10,

	    "query": "Buddy",

	    "searchAfter": [

	      "sx6wyHhbFdRXh302Lunr",

	      "sx6wyHhbFdRXh302Lunr"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "ve9EPM428h8vShlRW1KT",

	    "page": 1,

	    "pageLimit": 10,

	    "query": "Buddy",

	    "searchAfter": [

	      "sx6wyHhbFdRXh302Lunr",

	      "sx6wyHhbFdRXh302Lunr"

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/objects/:schemaKey/records/search", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/objects/:schemaKey/records/search"

	

	payload = json.dumps({

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

	  ]

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

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

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

	  ]

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/objects/:schemaKey/records/search');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "ve9EPM428h8vShlRW1KT",\n  "page": 1,\n  "pageLimit": 10,\n  "query": "Buddy",\n  "searchAfter": [\n    "sx6wyHhbFdRXh302Lunr",\n    "sx6wyHhbFdRXh302Lunr"\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/objects/:schemaKey/records/search');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"ve9EPM428h8vShlRW1KT\",\n  \"page\": 1,\n  \"pageLimit\": 10,\n  \"query\": \"Buddy\",\n  \"searchAfter\": [\n    \"sx6wyHhbFdRXh302Lunr\",\n    \"sx6wyHhbFdRXh302Lunr\"\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/objects/:schemaKey/records/search")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/objects/:schemaKey/records/search")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"ve9EPM428h8vShlRW1KT\",\n  \"page\": 1,\n  \"pageLimit\": 10,\n  \"query\": \"Buddy\",\n  \"searchAfter\": [\n    \"sx6wyHhbFdRXh302Lunr\",\n    \"sx6wyHhbFdRXh302Lunr\"\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/objects/:schemaKey/records/search"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

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

	

	url = URI("https://services.leadconnectorhq.com/objects/:schemaKey/records/search")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "ve9EPM428h8vShlRW1KT",

	  "page": 1,

	  "pageLimit": 10,

	  "query": "Buddy",

	  "searchAfter": [

	    "sx6wyHhbFdRXh302Lunr",

	    "sx6wyHhbFdRXh302Lunr"

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

	  `"locationId`": `"ve9EPM428h8vShlRW1KT`",

	  `"page`": 1,

	  `"pageLimit`": 10,

	  `"query`": `"Buddy`",

	  `"searchAfter`": [

	    `"sx6wyHhbFdRXh302Lunr`",

	    `"sx6wyHhbFdRXh302Lunr`"

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/objects/:schemaKey/records/search' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

