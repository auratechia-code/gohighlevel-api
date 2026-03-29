# List Call Logs

**Method:** `GET` | **URL:** `https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: voice-ai-dashboard.readonly
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Query Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `locationId` | ❌ | agentId string Agent identifier. When provided, returns logs for this agent only. Example: 507f1f77bcf86cd799439011 |
| `agentId` | ❌ | contactId string Contact IDs (comma-separated) to filter by. Example: contact123,contact456 |
| `contactId` | ❌ | callType string Possible values: [ LIVE , TRIAL ] Call type filter. |
| `callType` | ❌ | startDate number Start date filter (Unix timestamp). Must be less than endDate. Both startDate and endDate must be provided together. Example: 1679308800000 |
| `startDate` | ❌ | endDate number End date filter (Unix timestamp). Must be greater than startDate. Both startDate and endDate must be provided together. Example: 1679395199000 |
| `endDate` | ❌ | actionType string Possible values: [ CALL_TRANSFER , DATA_EXTRACTION , IN_CALL_DATA_EXTRACTION , WORKFLOW_TRIGGER , SMS , APPOINTMENT_BOOKING , CUSTOM_ACTION , KNOWLEDGE_BASE ] Action type filter for call logs (comma-separated ACTION_TYPE values) Example: SMS,CALL_TRANSFER,WORKFLOW_TRIGGER |
| `actionType` | ❌ | sortBy string Possible values: [ duration , createdAt ] Field to sort by. Defaults to newest if omitted. |
| `sortBy` | ❌ | sort string Possible values: [ ascend , descend ] Sort direction. Applies only when sortBy is provided. |
| `sort` | ❌ | page number Page number (1-based). Default value: 1 |
| `page` | ❌ | pageSize number Page size (max 50). Default value: 10 |
| `pageSize` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |
| `headers` | ✅ | HTTP headers to include Array [ key string required HTTP header name Example: id value string required HTTP header value Example: 1234567890 ] |
| `key` | ❌ |  |
| `value` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "total": 150,
  "page": 2,
  "pageSize": 10,
  "callLogs": [
    {
      "id": "507f1f77bcf86cd799439011",
      "contactId": "507f1f77bcf86cd799439012",
      "agentId": "507f1f77bcf86cd799439013",
      "isAgentDeleted": false,
      "fromNumber": "+1234567890",
      "createdAt": "2024-01-15T10:30:00.000Z",
      "duration": 180,
      "trialCall": false,
      "executedCallActions": [
        {
          "actionId": "507f1f77bcf86cd799439015",
          "actionType": "CALL_TRANSFER",
          "actionName": "Transfer to Manager",
          "actionParameters": {
            "transferToType": "number",
            "transferToValue": "+12345678901",
            "triggerMessage": "Let me transfer you to a manager right away",
            "hearWhisperMessage": true
          },
          "executedAt": "2024-01-15T10:32:00.000Z",
          "triggerReceivedAt": "2024-01-15T10:31:45.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439016",
          "actionType": "SMS",
          "actionName": "Send Confirmation SMS",
          "actionParameters": {
            "triggerPrompt": "When caller asks for booking confirmation",
            "triggerMessage": "I'll send you a confirmation text",
            "messageBody": "Your appointment is confirmed for tomorrow at 2 PM"
          },
          "executedAt": "2024-01-15T10:33:30.000Z",
          "triggerReceivedAt": "2024-01-15T10:33:15.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439017",
          "actionType": "DATA_EXTRACTION",
          "actionName": "Extract Phone Number",
          "actionParameters": {
            "contactFieldId": "507f1f77bcf86cd799439018",
            "description": "Customer's phone number",
            "examples": [
              "+1234567890",
              "+9876543210"
            ],
            "overwriteExistingValue": false
          },
          "executedAt": "2024-01-15T10:34:15.000Z",
          "triggerReceivedAt": "2024-01-15T10:34:00.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439019",
          "actionType": "WORKFLOW_TRIGGER",
          "actionName": "Start Follow-up Workflow",
          "actionParameters": {
            "triggerPrompt": "When caller requests a quote",
            "triggerMessage": "Let me start that process for you",
            "workflowId": "507f1f77bcf86cd799439020"
          },
          "executedAt": "2024-01-15T10:35:00.000Z",
          "triggerReceivedAt": "2024-01-15T10:34:45.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439021",
          "actionType": "APPOINTMENT_BOOKING",
          "actionName": "Book Consultation",
          "actionParameters": {
            "calendarId": "507f1f77bcf86cd799439022",
            "daysOfOfferingDates": 3,
            "slotsPerDay": 3,
            "hoursBetweenSlots": 1
          },
          "executedAt": "2024-01-15T10:36:45.000Z",
          "triggerReceivedAt": "2024-01-15T10:36:30.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439023",
          "actionType": "CUSTOM_ACTION",
          "actionName": "Check Order Status",
          "actionParameters": {
            "triggerPrompt": "When caller provides order number",
            "triggerMessage": "Let me check that order status",
            "apiDetails": {
              "url": "https://api.example.com/orders",
              "method": "GET",
              "authenticationRequired": true,
              "authenticationValue": "token123",
              "headers": [
                {
                  "key": "Content-Type",
                  "value": "application/json"
                }
              ],
              "parameters": [
                {
                  "name": "orderId",
                  "description": "Order ID to look up",
                  "type": "string",
                  "example": "ORD-12345"
                }
              ]
            },
            "responsePathsToExtract": [
              "data.orderId",
              "status"
            ]
          },
          "executedAt": "2024-01-15T10:37:20.000Z",
          "triggerReceivedAt": "2024-01-15T10:37:05.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439024",
          "actionType": "IN_CALL_DATA_EXTRACTION",
          "actionName": "Extract Email During Call",
          "actionParameters": {
            "contactFieldId": "507f1f77bcf86cd799439025",
            "description": "Customer's email address",
            "examples": [
              "john@example.com",
              "jane@company.com"
            ],
            "overwriteExistingValue": true
          },
          "executedAt": "2024-01-15T10:31:45.000Z",
          "triggerReceivedAt": "2024-01-15T10:31:30.000Z"
        },
        {
          "actionId": "507f1f77bcf86cd799439026",
          "actionType": "KNOWLEDGE_BASE",
          "actionName": "Query Product Info",
          "actionParameters": {
            "triggerPrompt": "When caller asks about pricing",
            "triggerMessage": "Let me look that up for you",
            "knowledgeBaseId": "507f1f77bcf86cd799439027",
            "parameters": [
              {
                "name": "category",
                "description": "Product category to search",
                "type": "string",
                "example": "pricing"
              }
            ]
          },
          "executedAt": "2024-01-15T10:38:10.000Z",
          "triggerReceivedAt": "2024-01-15T10:37:55.000Z"
        }
      ],
      "summary": "Customer called to inquire about product pricing and was transferred to sales team.",
      "transcript": "bot: Hello, how can I help you today?\nhuman: I would like to know about your pricing...",
      "translation": {
        "translatedTranscript": "Translated version of the call transcript"
      },
      "extractedData": {
        "phoneNumber": "+1234567890",
        "customerName": "John Doe",
        "email": "john.doe@example.com",
        "companyName": "Acme Corp",
        "customField1": "Custom value",
        "customField2": "Another value"
      },
      "messageId": "507f1f77bcf86cd799439014"
    }
  ]
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "total": 150,  "page": 2,  "pageSize": 10,  "callLogs": [    {      "id": "507f1f77bcf86cd799439011",      "contactId": "507f1f77bcf86cd799439012",      "agentId": "507f1f77bcf86cd799439013",      "isAgentDeleted": false,      "fromNumber": "+1234567890",      "createdAt": "2024-01-15T10:30:00.000Z",      "duration": 180,      "trialCall": false,      "executedCallActions": [        {          "actionId": "507f1f77bcf86cd799439015",          "actionType": "CALL_TRANSFER",          "actionName": "Transfer to Manager",          "actionParameters": {            "transferToType": "number",            "transferToValue": "+12345678901",            "triggerMessage": "Let me transfer you to a manager right away",            "hearWhisperMessage": true          },          "executedAt": "2024-01-15T10:32:00.000Z",          "triggerReceivedAt": "2024-01-15T10:31:45.000Z"        },        {          "actionId": "507f1f77bcf86cd799439016",          "actionType": "SMS",          "actionName": "Send Confirmation SMS",          "actionParameters": {            "triggerPrompt": "When caller asks for booking confirmation",            "triggerMessage": "I'll send you a confirmation text",            "messageBody": "Your appointment is confirmed for tomorrow at 2 PM"          },          "executedAt": "2024-01-15T10:33:30.000Z",          "triggerReceivedAt": "2024-01-15T10:33:15.000Z"        },        {          "actionId": "507f1f77bcf86cd799439017",          "actionType": "DATA_EXTRACTION",          "actionName": "Extract Phone Number",          "actionParameters": {            "contactFieldId": "507f1f77bcf86cd799439018",            "description": "Customer's phone number",            "examples": [              "+1234567890",              "+9876543210"            ],            "overwriteExistingValue": false          },          "executedAt": "2024-01-15T10:34:15.000Z",          "triggerReceivedAt": "2024-01-15T10:34:00.000Z"        },        {          "actionId": "507f1f77bcf86cd799439019",          "actionType": "WORKFLOW_TRIGGER",          "actionName": "Start Follow-up Workflow",          "actionParameters": {            "triggerPrompt": "When caller requests a quote",            "triggerMessage": "Let me start that process for you",            "workflowId": "507f1f77bcf86cd799439020"          },          "executedAt": "2024-01-15T10:35:00.000Z",          "triggerReceivedAt": "2024-01-15T10:34:45.000Z"        },        {          "actionId": "507f1f77bcf86cd799439021",          "actionType": "APPOINTMENT_BOOKING",          "actionName": "Book Consultation",          "actionParameters": {            "calendarId": "507f1f77bcf86cd799439022",            "daysOfOfferingDates": 3,            "slotsPerDay": 3,            "hoursBetweenSlots": 1          },          "executedAt": "2024-01-15T10:36:45.000Z",          "triggerReceivedAt": "2024-01-15T10:36:30.000Z"        },        {          "actionId": "507f1f77bcf86cd799439023",          "actionType": "CUSTOM_ACTION",          "actionName": "Check Order Status",          "actionParameters": {            "triggerPrompt": "When caller provides order number",            "triggerMessage": "Let me check that order status",            "apiDetails": {              "url": "https://api.example.com/orders",              "method": "GET",              "authenticationRequired": true,              "authenticationValue": "token123",              "headers": [                {                  "key": "Content-Type",                  "value": "application/json"                }              ],              "parameters": [                {                  "name": "orderId",                  "description": "Order ID to look up",                  "type": "string",                  "example": "ORD-12345"                }              ]            },            "responsePathsToExtract": [              "data.orderId",              "status"            ]          },          "executedAt": "2024-01-15T10:37:20.000Z",          "triggerReceivedAt": "2024-01-15T10:37:05.000Z"        },        {          "actionId": "507f1f77bcf86cd799439024",          "actionType": "IN_CALL_DATA_EXTRACTION",          "actionName": "Extract Email During Call",          "actionParameters": {            "contactFieldId": "507f1f77bcf86cd799439025",            "description": "Customer's email address",            "examples": [              "john@example.com",              "jane@company.com"            ],            "overwriteExistingValue": true          },          "executedAt": "2024-01-15T10:31:45.000Z",          "triggerReceivedAt": "2024-01-15T10:31:30.000Z"        },        {          "actionId": "507f1f77bcf86cd799439026",          "actionType": "KNOWLEDGE_BASE",          "actionName": "Query Product Info",          "actionParameters": {            "triggerPrompt": "When caller asks about pricing",            "triggerMessage": "Let me look that up for you",            "knowledgeBaseId": "507f1f77bcf86cd799439027",            "parameters": [              {                "name": "category",                "description": "Product category to search",                "type": "string",                "example": "pricing"              }            ]          },          "executedAt": "2024-01-15T10:38:10.000Z",          "triggerReceivedAt": "2024-01-15T10:37:55.000Z"        }      ],      "summary": "Customer called to inquire about product pricing and was transferred to sales team.",      "transcript": "bot: Hello, how can I help you today?\nhuman: I would like to know about your pricing...",      "translation": {        "translatedTranscript": "Translated version of the call transcript"      },      "extractedData": {        "phoneNumber": "+1234567890",        "customerName": "John Doe",        "email": "john.doe@example.com",        "companyName": "Acme Corp",        "customField1": "Custom value",        "customField2": "Another value"      },      "messageId": "507f1f77bcf86cd799439014"    }  ]}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "total": 150,  "page": 2,  "pageSize": 10,  "callLogs": [    {      "id": "507f1f77bcf86cd799439011",      "contactId": "507f1f77bcf86cd799439012",      "agentId": "507f1f77bcf86cd799439013",      "isAgentDeleted": false,      "fromNumber": "+1234567890",      "createdAt": "2024-01-15T10:30:00.000Z",      "duration": 180,      "trialCall": false,      "executedCallActions": [        {          "actionId": "507f1f77bcf86cd799439015",          "actionType": "CALL_TRANSFER",          "actionName": "Transfer to Manager",          "actionParameters": {            "transferToType": "number",            "transferToValue": "+12345678901",            "triggerMessage": "Let me transfer you to a manager right away",            "hearWhisperMessage": true          },          "executedAt": "2024-01-15T10:32:00.000Z",          "triggerReceivedAt": "2024-01-15T10:31:45.000Z"        },        {          "actionId": "507f1f77bcf86cd799439016",          "actionType": "SMS",          "actionName": "Send Confirmation SMS",          "actionParameters": {            "triggerPrompt": "When caller asks for booking confirmation",            "triggerMessage": "I'll send you a confirmation text",            "messageBody": "Your appointment is confirmed for tomorrow at 2 PM"          },          "executedAt": "2024-01-15T10:33:30.000Z",          "triggerReceivedAt": "2024-01-15T10:33:15.000Z"        },        {          "actionId": "507f1f77bcf86cd799439017",          "actionType": "DATA_EXTRACTION",          "actionName": "Extract Phone Number",          "actionParameters": {            "contactFieldId": "507f1f77bcf86cd799439018",            "description": "Customer's phone number",            "examples": [              "+1234567890",              "+9876543210"            ],            "overwriteExistingValue": false          },          "executedAt": "2024-01-15T10:34:15.000Z",          "triggerReceivedAt": "2024-01-15T10:34:00.000Z"        },        {          "actionId": "507f1f77bcf86cd799439019",          "actionType": "WORKFLOW_TRIGGER",          "actionName": "Start Follow-up Workflow",          "actionParameters": {            "triggerPrompt": "When caller requests a quote",            "triggerMessage": "Let me start that process for you",            "workflowId": "507f1f77bcf86cd799439020"          },          "executedAt": "2024-01-15T10:35:00.000Z",          "triggerReceivedAt": "2024-01-15T10:34:45.000Z"        },        {          "actionId": "507f1f77bcf86cd799439021",          "actionType": "APPOINTMENT_BOOKING",          "actionName": "Book Consultation",          "actionParameters": {            "calendarId": "507f1f77bcf86cd799439022",            "daysOfOfferingDates": 3,            "slotsPerDay": 3,            "hoursBetweenSlots": 1          },          "executedAt": "2024-01-15T10:36:45.000Z",          "triggerReceivedAt": "2024-01-15T10:36:30.000Z"        },        {          "actionId": "507f1f77bcf86cd799439023",          "actionType": "CUSTOM_ACTION",          "actionName": "Check Order Status",          "actionParameters": {            "triggerPrompt": "When caller provides order number",            "triggerMessage": "Let me check that order status",            "apiDetails": {              "url": "https://api.example.com/orders",              "method": "GET",              "authenticationRequired": true,              "authenticationValue": "token123",              "headers": [                {                  "key": "Content-Type",                  "value": "application/json"                }              ],              "parameters": [                {                  "name": "orderId",                  "description": "Order ID to look up",                  "type": "string",                  "example": "ORD-12345"                }              ]            },            "responsePathsToExtract": [              "data.orderId",              "status"            ]          },          "executedAt": "2024-01-15T10:37:20.000Z",          "triggerReceivedAt": "2024-01-15T10:37:05.000Z"        },        {          "actionId": "507f1f77bcf86cd799439024",          "actionType": "IN_CALL_DATA_EXTRACTION",          "actionName": "Extract Email During Call",          "actionParameters": {            "contactFieldId": "507f1f77bcf86cd799439025",            "description": "Customer's email address",            "examples": [              "john@example.com",              "jane@company.com"            ],            "overwriteExistingValue": true          },          "executedAt": "2024-01-15T10:31:45.000Z",          "triggerReceivedAt": "2024-01-15T10:31:30.000Z"        },        {          "actionId": "507f1f77bcf86cd799439026",          "actionType": "KNOWLEDGE_BASE",          "actionName": "Query Product Info",          "actionParameters": {            "triggerPrompt": "When caller asks about pricing",            "triggerMessage": "Let me look that up for you",            "knowledgeBaseId": "507f1f77bcf86cd799439027",            "parameters": [              {                "name": "category",                "description": "Product category to search",                "type": "string",                "example": "pricing"              }            ]          },          "executedAt": "2024-01-15T10:38:10.000Z",          "triggerReceivedAt": "2024-01-15T10:37:55.000Z"        }      ],      "summary": "Customer called to inquire about product pricing and was transferred to sales team.",      "transcript": "bot: Hello, how can I help you today?\nhuman: I would like to know about your pricing...",      "translation": {        "translatedTranscript": "Translated version of the call transcript"      },      "extractedData": {        "phoneNumber": "+1234567890",        "customerName": "John Doe",        "email": "john.doe@example.com",        "companyName": "Acme Corp",        "customField1": "Custom value",        "customField2": "Another value"      },      "messageId": "507f1f77bcf86cd799439014"    }  ]}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs' \

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

	  const response = await highLevel.voiceAi.getCallLogs({

	    'locationId': 'locationId_value',

	    'agentId': '507f1f77bcf86cd799439011',

	    'contactId': 'contact123,contact456',

	    'startDate': 1679308800000,

	    'endDate': 1679395199000,

	    'actionType': 'SMS,CALL_TRANSFER,WORKFLOW_TRIGGER'

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

	  url: 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs',

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

	  'path': '/voice-ai/dashboard/call-logs',

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

	  'url': 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs',

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

	var req = unirest('GET', 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs')

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

	conn.request("GET", "/voice-ai/dashboard/call-logs", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	

	url = "https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs"

	

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs',

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

	$request = new Request('GET', 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs', $headers);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs');

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

	  .url("https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs")

	  .method("GET", body)

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.get("https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs")

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

	

	  url := "https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs"

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

	

	url = URI("https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs")

	

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

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/voice-ai/dashboard/call-logs' -Method 'GET' -Headers $headers

	$response | ConvertTo-Json

```

