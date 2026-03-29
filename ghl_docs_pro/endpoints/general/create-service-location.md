# Create Service Location

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/calendars/services/locations`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
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
  "id": "65e5f6dfacf123513228d384",
  "locationId": "0007BWpSzSwfiuSl0tR2",
  "name": "Downtown Wellness Center",
  "slug": "downtown-wellness-center",
  "isActive": true,
  "isPrivate": false,
  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",
  "locationType": "offline",
  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",
  "phone": "+1-415-555-0198"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "id": "65e5f6dfacf123513228d384",  "locationId": "0007BWpSzSwfiuSl0tR2",  "name": "Downtown Wellness Center",  "slug": "downtown-wellness-center",  "isActive": true,  "isPrivate": false,  "coverImage": "https://storage.example.com/locations/downtown-wellness-center/cover.jpg",  "locationType": "offline",  "address": "456 Market Street, Suite 200, San Francisco, CA 94105",  "phone": "+1-415-555-0198"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/calendars/services/locations' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

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

	  const response = await highLevel.calendars.createServiceLocation({

	    'locationId': '0007BWpSzSwfiuSl0tR2',

	    'name': 'Midtown Therapy Studio',

	    'slug': 'midtown-therapy-studio',

	    'phone': '+1-212-555-0174',

	    'address': '789 5th Avenue, Floor 3, New York, NY 10022 / Home Service',

	    'coverImage': 'https://storage.example.com/locations/midtown-therapy-studio/cover.jpg',

	    'locationType': 'offline'

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

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/calendars/services/locations',

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

	  'path': '/calendars/services/locations',

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

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/calendars/services/locations',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "0007BWpSzSwfiuSl0tR2",

	    "name": "Midtown Therapy Studio",

	    "slug": "midtown-therapy-studio",

	    "phone": "+1-212-555-0174",

	    "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	    "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	    "locationType": "offline"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/calendars/services/locations')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "0007BWpSzSwfiuSl0tR2",

	    "name": "Midtown Therapy Studio",

	    "slug": "midtown-therapy-studio",

	    "phone": "+1-212-555-0174",

	    "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	    "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	    "locationType": "offline"

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

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/calendars/services/locations", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/calendars/services/locations"

	

	payload = json.dumps({

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/calendars/services/locations',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

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

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/calendars/services/locations', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/calendars/services/locations');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "0007BWpSzSwfiuSl0tR2",\n  "name": "Midtown Therapy Studio",\n  "slug": "midtown-therapy-studio",\n  "phone": "+1-212-555-0174",\n  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",\n  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",\n  "locationType": "offline"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/calendars/services/locations');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"0007BWpSzSwfiuSl0tR2\",\n  \"name\": \"Midtown Therapy Studio\",\n  \"slug\": \"midtown-therapy-studio\",\n  \"phone\": \"+1-212-555-0174\",\n  \"address\": \"789 5th Avenue, Floor 3, New York, NY 10022 / Home Service\",\n  \"coverImage\": \"https://storage.example.com/locations/midtown-therapy-studio/cover.jpg\",\n  \"locationType\": \"offline\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/calendars/services/locations")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/calendars/services/locations")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"0007BWpSzSwfiuSl0tR2\",\n  \"name\": \"Midtown Therapy Studio\",\n  \"slug\": \"midtown-therapy-studio\",\n  \"phone\": \"+1-212-555-0174\",\n  \"address\": \"789 5th Avenue, Floor 3, New York, NY 10022 / Home Service\",\n  \"coverImage\": \"https://storage.example.com/locations/midtown-therapy-studio/cover.jpg\",\n  \"locationType\": \"offline\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/calendars/services/locations"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

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

	

	url = URI("https://services.leadconnectorhq.com/calendars/services/locations")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "0007BWpSzSwfiuSl0tR2",

	  "name": "Midtown Therapy Studio",

	  "slug": "midtown-therapy-studio",

	  "phone": "+1-212-555-0174",

	  "address": "789 5th Avenue, Floor 3, New York, NY 10022 / Home Service",

	  "coverImage": "https://storage.example.com/locations/midtown-therapy-studio/cover.jpg",

	  "locationType": "offline"

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

	  `"locationId`": `"0007BWpSzSwfiuSl0tR2`",

	  `"name`": `"Midtown Therapy Studio`",

	  `"slug`": `"midtown-therapy-studio`",

	  `"phone`": `"+1-212-555-0174`",

	  `"address`": `"789 5th Avenue, Floor 3, New York, NY 10022 / Home Service`",

	  `"coverImage`": `"https://storage.example.com/locations/midtown-therapy-studio/cover.jpg`",

	  `"locationType`": `"offline`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/services/locations' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

