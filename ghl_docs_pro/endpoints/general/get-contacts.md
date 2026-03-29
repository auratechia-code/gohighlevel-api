# Get Contacts

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/contacts/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ | startAfterId string Start After Id Example: UIaE1WjAwWKdlyD7osQI |
| `startAfterId` | ❌ | startAfter number Start Afte Example: 1603870249758 |
| `startAfter` | ❌ | query string Contact Query Example: John |
| `query` | ❌ | limit number Limit Per Page records count. will allow maximum up to 100 and default will be 20 Default value: 20 Example: 20 |
| `limit` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "contacts": [
    {
      "id": "ocQHyuzHvysMo5N5VsXc",
      "locationId": "C2QujeCh8ZnC7al2InWR",
      "email": "JohnDeo@gmail.com",
      "timezone": "Asia/Calcutta",
      "country": "DE",
      "source": "xyz form",
      "dateAdded": "2020-10-29T09:31:30.255Z",
      "customFields": [
        {
          "id": "MgobCB14YMVKuE4Ka8p1",
          "value": "name"
        }
      ],
      "tags": [
        "nisi sint commodo amet",
        "consequat"
      ],
      "businessId": "641c094001436dbc2081e642",
      "attributions": [
        {
          "url": "Trigger Link",
          "campaign": "string",
          "utmSource": "string",
          "utmMedium": "string",
          "utmContent": "string",
          "referrer": "https: //www.google.com",
          "campaignId": "string",
          "fbclid": "string",
          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",
          "msclikid": "string",
          "dclid": "string",
          "fbc": "string",
          "fbp": "fb. 1.1674748390986.1171287961",
          "fbEventId": "Mozilla/5.0",
          "userAgent": "Mozilla/5.0",
          "ip": "58.111.106.198",
          "medium": "survey",
          "mediumId": "FglfHAn30PRwsZVyQlKp"
        }
      ],
      "followers": "641c094001436dbc2081e642"
    }
  ],
  "count": 10
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/contacts/' \

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

	  const response = await highLevel.contacts.getContacts({

	    'locationId': 've9EPM428h8vShlRW1KT',

	    'startAfterId': 'UIaE1WjAwWKdlyD7osQI',

	    'startAfter': 1603870249758,

	    'query': 'John',

	    'limit': 20

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

	  url: 'https://services.leadconnectorhq.com/contacts/',

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

	  'path': '/contacts/',

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

	  'url': 'https://services.leadconnectorhq.com/contacts/',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/contacts/')

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

	conn.request("GET", "/contacts/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/contacts/"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/contacts/',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/contacts/', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/contacts/');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/contacts/');

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

	  .url("https://services.leadconnectorhq.com/contacts/")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/contacts/")

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

	

	  url := "https://services.leadconnectorhq.com/contacts/"

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

	

	url = URI("https://services.leadconnectorhq.com/contacts/")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

