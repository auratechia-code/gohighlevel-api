# Send a new message

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/conversations/messages`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: conversations/message.write
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
<summary>Response 200</summary>

```json
{
  "conversationId": "ABC12h2F6uBrIkfXYazb",
  "emailMessageId": "rnGyqh2F6uBrIkfhFo9A",
  "messageId": "t22c6DQcTDf3MjRhwf77",
  "messageIds": [
    "string"
  ],
  "msg": "Message queued successfully."
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "conversationId": "ABC12h2F6uBrIkfXYazb",  "emailMessageId": "rnGyqh2F6uBrIkfhFo9A",  "messageId": "t22c6DQcTDf3MjRhwf77",  "messageIds": [    "string"  ],  "msg": "Message queued successfully."}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "conversationId": "ABC12h2F6uBrIkfXYazb",  "emailMessageId": "rnGyqh2F6uBrIkfhFo9A",  "messageId": "t22c6DQcTDf3MjRhwf77",  "messageIds": [    "string"  ],  "msg": "Message queued successfully."}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/conversations/messages' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

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

	  const response = await highLevel.conversations.sendANewMessage({

	    'type': 'Email',

	    'contactId': 'abc123def456',

	    'appointmentId': 'appt123',

	    'attachments': [

	      'https://storage.com/file1.pdf',

	      'https://storage.com/file2.jpg'

	    ],

	    'emailFrom': 'sender@company.com',

	    'emailCc': [

	      'cc1@company.com',

	      'cc2@company.com'

	    ],

	    'emailBcc': [

	      'bcc1@company.com',

	      'bcc2@company.com'

	    ],

	    'html': '<p>Hello World</p>',

	    'message': 'Hello, how can I help you today?',

	    'subject': 'Important Update',

	    'replyMessageId': 'msg123',

	    'templateId': 'template123',

	    'threadId': 'thread123',

	    'scheduledTimestamp': 1669287863,

	    'conversationProviderId': 'provider123',

	    'emailTo': 'recipient@company.com',

	    'emailReplyMode': 'reply_all',

	    'fromNumber': '+1499499299',

	    'toNumber': '+1439499299',

	    'status': 'delivered',

	    'mentions': [

	      'userId123',

	      'userId456'

	    ],

	    'userId': 'user123'

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

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/conversations/messages',

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

	  'path': '/conversations/messages',

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

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/conversations/messages',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "type": "Email",

	    "contactId": "abc123def456",

	    "appointmentId": "appt123",

	    "attachments": [

	      "https://storage.com/file1.pdf",

	      "https://storage.com/file2.jpg"

	    ],

	    "emailFrom": "sender@company.com",

	    "emailCc": [

	      "cc1@company.com",

	      "cc2@company.com"

	    ],

	    "emailBcc": [

	      "bcc1@company.com",

	      "bcc2@company.com"

	    ],

	    "html": "<p>Hello World</p>",

	    "message": "Hello, how can I help you today?",

	    "subject": "Important Update",

	    "replyMessageId": "msg123",

	    "templateId": "template123",

	    "threadId": "thread123",

	    "scheduledTimestamp": 1669287863,

	    "conversationProviderId": "provider123",

	    "emailTo": "recipient@company.com",

	    "emailReplyMode": "reply_all",

	    "fromNumber": "+1499499299",

	    "toNumber": "+1439499299",

	    "status": "delivered",

	    "mentions": [

	      "userId123",

	      "userId456"

	    ],

	    "userId": "user123"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/conversations/messages')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "type": "Email",

	    "contactId": "abc123def456",

	    "appointmentId": "appt123",

	    "attachments": [

	      "https://storage.com/file1.pdf",

	      "https://storage.com/file2.jpg"

	    ],

	    "emailFrom": "sender@company.com",

	    "emailCc": [

	      "cc1@company.com",

	      "cc2@company.com"

	    ],

	    "emailBcc": [

	      "bcc1@company.com",

	      "bcc2@company.com"

	    ],

	    "html": "<p>Hello World</p>",

	    "message": "Hello, how can I help you today?",

	    "subject": "Important Update",

	    "replyMessageId": "msg123",

	    "templateId": "template123",

	    "threadId": "thread123",

	    "scheduledTimestamp": 1669287863,

	    "conversationProviderId": "provider123",

	    "emailTo": "recipient@company.com",

	    "emailReplyMode": "reply_all",

	    "fromNumber": "+1499499299",

	    "toNumber": "+1439499299",

	    "status": "delivered",

	    "mentions": [

	      "userId123",

	      "userId456"

	    ],

	    "userId": "user123"

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

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/conversations/messages", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/conversations/messages"

	

	payload = json.dumps({

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/conversations/messages',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

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

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/conversations/messages', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/conversations/messages');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "type": "Email",\n  "contactId": "abc123def456",\n  "appointmentId": "appt123",\n  "attachments": [\n    "https://storage.com/file1.pdf",\n    "https://storage.com/file2.jpg"\n  ],\n  "emailFrom": "sender@company.com",\n  "emailCc": [\n    "cc1@company.com",\n    "cc2@company.com"\n  ],\n  "emailBcc": [\n    "bcc1@company.com",\n    "bcc2@company.com"\n  ],\n  "html": "<p>Hello World</p>",\n  "message": "Hello, how can I help you today?",\n  "subject": "Important Update",\n  "replyMessageId": "msg123",\n  "templateId": "template123",\n  "threadId": "thread123",\n  "scheduledTimestamp": 1669287863,\n  "conversationProviderId": "provider123",\n  "emailTo": "recipient@company.com",\n  "emailReplyMode": "reply_all",\n  "fromNumber": "+1499499299",\n  "toNumber": "+1439499299",\n  "status": "delivered",\n  "mentions": [\n    "userId123",\n    "userId456"\n  ],\n  "userId": "user123"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/conversations/messages');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"type\": \"Email\",\n  \"contactId\": \"abc123def456\",\n  \"appointmentId\": \"appt123\",\n  \"attachments\": [\n    \"https://storage.com/file1.pdf\",\n    \"https://storage.com/file2.jpg\"\n  ],\n  \"emailFrom\": \"sender@company.com\",\n  \"emailCc\": [\n    \"cc1@company.com\",\n    \"cc2@company.com\"\n  ],\n  \"emailBcc\": [\n    \"bcc1@company.com\",\n    \"bcc2@company.com\"\n  ],\n  \"html\": \"<p>Hello World</p>\",\n  \"message\": \"Hello, how can I help you today?\",\n  \"subject\": \"Important Update\",\n  \"replyMessageId\": \"msg123\",\n  \"templateId\": \"template123\",\n  \"threadId\": \"thread123\",\n  \"scheduledTimestamp\": 1669287863,\n  \"conversationProviderId\": \"provider123\",\n  \"emailTo\": \"recipient@company.com\",\n  \"emailReplyMode\": \"reply_all\",\n  \"fromNumber\": \"+1499499299\",\n  \"toNumber\": \"+1439499299\",\n  \"status\": \"delivered\",\n  \"mentions\": [\n    \"userId123\",\n    \"userId456\"\n  ],\n  \"userId\": \"user123\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/conversations/messages")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/conversations/messages")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"type\": \"Email\",\n  \"contactId\": \"abc123def456\",\n  \"appointmentId\": \"appt123\",\n  \"attachments\": [\n    \"https://storage.com/file1.pdf\",\n    \"https://storage.com/file2.jpg\"\n  ],\n  \"emailFrom\": \"sender@company.com\",\n  \"emailCc\": [\n    \"cc1@company.com\",\n    \"cc2@company.com\"\n  ],\n  \"emailBcc\": [\n    \"bcc1@company.com\",\n    \"bcc2@company.com\"\n  ],\n  \"html\": \"<p>Hello World</p>\",\n  \"message\": \"Hello, how can I help you today?\",\n  \"subject\": \"Important Update\",\n  \"replyMessageId\": \"msg123\",\n  \"templateId\": \"template123\",\n  \"threadId\": \"thread123\",\n  \"scheduledTimestamp\": 1669287863,\n  \"conversationProviderId\": \"provider123\",\n  \"emailTo\": \"recipient@company.com\",\n  \"emailReplyMode\": \"reply_all\",\n  \"fromNumber\": \"+1499499299\",\n  \"toNumber\": \"+1439499299\",\n  \"status\": \"delivered\",\n  \"mentions\": [\n    \"userId123\",\n    \"userId456\"\n  ],\n  \"userId\": \"user123\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/conversations/messages"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

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

	

	url = URI("https://services.leadconnectorhq.com/conversations/messages")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "type": "Email",

	  "contactId": "abc123def456",

	  "appointmentId": "appt123",

	  "attachments": [

	    "https://storage.com/file1.pdf",

	    "https://storage.com/file2.jpg"

	  ],

	  "emailFrom": "sender@company.com",

	  "emailCc": [

	    "cc1@company.com",

	    "cc2@company.com"

	  ],

	  "emailBcc": [

	    "bcc1@company.com",

	    "bcc2@company.com"

	  ],

	  "html": "<p>Hello World</p>",

	  "message": "Hello, how can I help you today?",

	  "subject": "Important Update",

	  "replyMessageId": "msg123",

	  "templateId": "template123",

	  "threadId": "thread123",

	  "scheduledTimestamp": 1669287863,

	  "conversationProviderId": "provider123",

	  "emailTo": "recipient@company.com",

	  "emailReplyMode": "reply_all",

	  "fromNumber": "+1499499299",

	  "toNumber": "+1439499299",

	  "status": "delivered",

	  "mentions": [

	    "userId123",

	    "userId456"

	  ],

	  "userId": "user123"

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

	  `"type`": `"Email`",

	  `"contactId`": `"abc123def456`",

	  `"appointmentId`": `"appt123`",

	  `"attachments`": [

	    `"https://storage.com/file1.pdf`",

	    `"https://storage.com/file2.jpg`"

	  ],

	  `"emailFrom`": `"sender@company.com`",

	  `"emailCc`": [

	    `"cc1@company.com`",

	    `"cc2@company.com`"

	  ],

	  `"emailBcc`": [

	    `"bcc1@company.com`",

	    `"bcc2@company.com`"

	  ],

	  `"html`": `"<p>Hello World</p>`",

	  `"message`": `"Hello, how can I help you today?`",

	  `"subject`": `"Important Update`",

	  `"replyMessageId`": `"msg123`",

	  `"templateId`": `"template123`",

	  `"threadId`": `"thread123`",

	  `"scheduledTimestamp`": 1669287863,

	  `"conversationProviderId`": `"provider123`",

	  `"emailTo`": `"recipient@company.com`",

	  `"emailReplyMode`": `"reply_all`",

	  `"fromNumber`": `"+1499499299`",

	  `"toNumber`": `"+1439499299`",

	  `"status`": `"delivered`",

	  `"mentions`": [

	    `"userId123`",

	    `"userId456`"

	  ],

	  `"userId`": `"user123`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversations/messages' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

