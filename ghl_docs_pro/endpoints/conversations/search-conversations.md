# Search Conversations

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/conversations/search`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: conversations.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ | contactId string Contact Id Example: 9VEmS0si86GW6gXWU89b |
| `contactId` | ❌ | assignedTo string User IDs that conversations are assigned to. Multiple IDs can be provided as comma-separated values. Use "unassigned" to fetch conversations not assigned to any user. Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik |
| `assignedTo` | ❌ | followers string User IDs of followers to filter conversations by. Multiple IDs can be provided as comma-separated values. Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik |
| `followers` | ❌ | mentions string User Id of the mention. Multiple values are comma separated. Example: ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik |
| `mentions` | ❌ | query string Search paramater as a string Example: Search string |
| `query` | ❌ | sort string Possible values: [ asc , desc ] Sort paramater - asc or desc Example: asc |
| `sort` | ❌ | startAfterDate any Search to begin after the specified date - should contain the sort value of the last document Example: 1600854 |
| `startAfterDate` | ❌ | id string Id of the conversation Example: ABCHkzuJQ8ZMd4Te84GK |
| `id` | ❌ | limit number Limit of conversations - Default is 20 Example: 20 |
| `limit` | ❌ | lastMessageType string Possible values: [ TYPE_CALL , TYPE_SMS , TYPE_EMAIL , TYPE_SMS_REVIEW_REQUEST , TYPE_WEBCHAT , TYPE_SMS_NO_SHOW_REQUEST , TYPE_CAMPAIGN_SMS , TYPE_CAMPAIGN_CALL , TYPE_CAMPAIGN_EMAIL , TYPE_CAMPAIGN_VOICEMAIL , TYPE_FACEBOOK , TYPE_CAMPAIGN_FACEBOOK , TYPE_CAMPAIGN_MANUAL_CALL , TYPE_CAMPAIGN_MANUAL_SMS , TYPE_GMB , TYPE_CAMPAIGN_GMB , TYPE_REVIEW , TYPE_INSTAGRAM , TYPE_WHATSAPP , TYPE_CUSTOM_SMS , TYPE_CUSTOM_EMAIL , TYPE_CUSTOM_PROVIDER_SMS , TYPE_CUSTOM_PROVIDER_EMAIL , TYPE_IVR_CALL , TYPE_ACTIVITY_CONTACT , TYPE_ACTIVITY_INVOICE , TYPE_ACTIVITY_PAYMENT , TYPE_ACTIVITY_OPPORTUNITY , TYPE_LIVE_CHAT , TYPE_LIVE_CHAT_INFO_MESSAGE , TYPE_ACTIVITY_APPOINTMENT , TYPE_FACEBOOK_COMMENT , TYPE_INSTAGRAM_COMMENT , TYPE_CUSTOM_CALL , TYPE_INTERNAL_COMMENT , TYPE_ACTIVITY_EMPLOYEE_ACTION_LOG ] Type of the last message in the conversation as a string Example: TYPE_SMS |
| `lastMessageType` | ❌ | lastMessageAction string Possible values: [ automated , manual ] Action of the last outbound message in the conversation as string. Example: manual |
| `lastMessageAction` | ❌ | lastMessageDirection string Possible values: [ inbound , outbound ] Direction of the last message in the conversation as string. Example: inbound |
| `lastMessageDirection` | ❌ | status string Possible values: [ all , read , unread , starred , recents ] The status of the conversation to be filtered - all, read, unread, starred Example: all |
| `status` | ❌ | sortBy string Possible values: [ last_manual_message_date , last_message_date , score_profile ] The sorting of the conversation to be filtered as - manual messages or all messages Example: last_message_date |
| `sortBy` | ❌ | sortScoreProfile string Id of score profile on which sortBy.ScoreProfile should sort on Example: ABCHkzuJQ8ZMd4Te84GK |
| `sortScoreProfile` | ❌ | scoreProfile string Id of score profile on which conversations should get filtered out, works with scoreProfileMin & scoreProfileMax Example: ABCHkzuJQ8ZMd4Te84GK |
| `scoreProfile` | ❌ | scoreProfileMin number Minimum value for score Example: ABCHkzuJQ8ZMd4Te84GK |
| `scoreProfileMin` | ❌ | scoreProfileMax number Maximum value for score Example: ABCHkzuJQ8ZMd4Te84GK |
| `scoreProfileMax` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "conversations": [
    {
      "id": "ABCHkzuJQ8ZMd4Te84GK",
      "contactId": "ABCHkzuJQ8ZMd4Te84GK",
      "locationId": "ABCHkzuJQ8ZMd4Te84GK",
      "lastMessageBody": "This is a sample message body",
      "lastMessageType": "TYPE_SMS",
      "type": "TYPE_PHONE",
      "unreadCount": 1,
      "fullName": "John Doe",
      "contactName": "John Doe Company",
      "email": "johndoe@mailingdomain.com",
      "phone": "+15550001234"
    }
  ],
  "total": 100
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "conversations": [    {      "id": "ABCHkzuJQ8ZMd4Te84GK",      "contactId": "ABCHkzuJQ8ZMd4Te84GK",      "locationId": "ABCHkzuJQ8ZMd4Te84GK",      "lastMessageBody": "This is a sample message body",      "lastMessageType": "TYPE_SMS",      "type": "TYPE_PHONE",      "unreadCount": 1,      "fullName": "John Doe",      "contactName": "John Doe Company",      "email": "johndoe@mailingdomain.com",      "phone": "+15550001234"    }  ],  "total": 100}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "conversations": [    {      "id": "ABCHkzuJQ8ZMd4Te84GK",      "contactId": "ABCHkzuJQ8ZMd4Te84GK",      "locationId": "ABCHkzuJQ8ZMd4Te84GK",      "lastMessageBody": "This is a sample message body",      "lastMessageType": "TYPE_SMS",      "type": "TYPE_PHONE",      "unreadCount": 1,      "fullName": "John Doe",      "contactName": "John Doe Company",      "email": "johndoe@mailingdomain.com",      "phone": "+15550001234"    }  ],  "total": 100}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/conversations/search' \

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

	  const response = await highLevel.conversations.searchConversation({

	    'locationId': 'ABCHkzuJQ8ZMd4Te84GK',

	    'contactId': '9VEmS0si86GW6gXWU89b',

	    'assignedTo': 'ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik',

	    'followers': 'ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik',

	    'mentions': 'ABCHkzuJQ8ZMd4Te84GK,fGiae4CHkzoskh8thsik',

	    'query': 'Search string',

	    'sort': 'asc',

	    'startAfterDate': 1600854,

	    'id': 'ABCHkzuJQ8ZMd4Te84GK',

	    'limit': 20,

	    'lastMessageType': 'TYPE_SMS',

	    'lastMessageAction': 'manual',

	    'lastMessageDirection': 'inbound',

	    'status': 'all',

	    'sortBy': 'last_message_date',

	    'sortScoreProfile': 'ABCHkzuJQ8ZMd4Te84GK',

	    'scoreProfile': 'ABCHkzuJQ8ZMd4Te84GK',

	    'scoreProfileMin': 'ABCHkzuJQ8ZMd4Te84GK',

	    'scoreProfileMax': 'ABCHkzuJQ8ZMd4Te84GK'

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

	  url: 'https://services.leadconnectorhq.com/conversations/search',

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

	  'path': '/conversations/search',

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

	  'url': 'https://services.leadconnectorhq.com/conversations/search',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/conversations/search')

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

	conn.request("GET", "/conversations/search", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/conversations/search"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/conversations/search',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/conversations/search', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/conversations/search');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/conversations/search');

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

	  .url("https://services.leadconnectorhq.com/conversations/search")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/conversations/search")

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

	

	  url := "https://services.leadconnectorhq.com/conversations/search"

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

	

	url = URI("https://services.leadconnectorhq.com/conversations/search")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversations/search' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

