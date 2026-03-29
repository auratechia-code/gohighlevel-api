# Get Calendar Events

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/calendars/events`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: calendars/events.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ✅ | userId string User Id - Owner of an appointment. Either of userId, groupId or calendarId is required Example: CVokAlI8fgw4WYWoCtQz |
| `userId` | ✅ | calendarId string Either of calendarId, userId or groupId is required Example: BqTwX8QFwXzpegMve9EQ |
| `calendarId` | ✅ | groupId string Either of groupId, calendarId or userId is required Example: ocQHyuzHvysMo5N5VsXc |
| `groupId` | ✅ | startTime string required Start Time (in millis) Example: 1680373800000 |
| `startTime` | ✅ | endTime string required End Time (in millis) Example: 1680978599999 |
| `endTime` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "events": [
    {
      "id": "string",
      "address": "https://meet.google.com/yqp-gogr-wve",
      "title": "Appointment with GHL Dev team",
      "calendarId": "BqTwX8QFwXzpegMve9EQ",
      "locationId": "0007BWpSzSwfiuSl0tR2",
      "contactId": "9NkT25Vor1v4aQatFsv2",
      "groupId": "9NkT25Vor1v4aQatFsv2",
      "appointmentStatus": "confirmed",
      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",
      "users": [
        "YlWd2wuCAZQzh2cH1fVZ",
        "9NkT25Vor1v4aQatFsv2"
      ],
      "notes": "Some dummy note",
      "description": "Some dummy description",
      "isRecurring": "true",
      "rrule": "string",
      "deleted": false,
      "startTime": "2023-09-25T16:00:00+05:30",
      "endTime": "2023-09-25T16:00:00+05:30",
      "dateAdded": "2023-09-25T16:00:00+05:30",
      "dateUpdated": "2023-09-25T16:00:00+05:30",
      "assignedResources": [
        "string"
      ],
      "createdBy": {
        "userId": "string",
        "source": "string"
      },
      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"
    }
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/calendars/events' \

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

	  const response = await highLevel.calendars.getCalendarEvents({

	    'locationId': '0007BWpSzSwfiuSl0tR2',

	    'userId': 'CVokAlI8fgw4WYWoCtQz',

	    'calendarId': 'BqTwX8QFwXzpegMve9EQ',

	    'groupId': 'ocQHyuzHvysMo5N5VsXc',

	    'startTime': '1680373800000',

	    'endTime': '1680978599999'

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

	  url: 'https://services.leadconnectorhq.com/calendars/events',

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

	  'path': '/calendars/events',

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

	  'url': 'https://services.leadconnectorhq.com/calendars/events',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/calendars/events')

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

	conn.request("GET", "/calendars/events", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/calendars/events"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/calendars/events',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/calendars/events', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/calendars/events');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/calendars/events');

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

	  .url("https://services.leadconnectorhq.com/calendars/events")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/calendars/events")

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

	

	  url := "https://services.leadconnectorhq.com/calendars/events"

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

	

	url = URI("https://services.leadconnectorhq.com/calendars/events")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/calendars/events' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

