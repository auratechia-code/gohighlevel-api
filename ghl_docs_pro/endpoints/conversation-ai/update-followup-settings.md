# Update Followup Settings

**Method:** `PATCH` | **URL:** `https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: conversation-ai.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Sub-Account (OR) Private Integration Token of Sub-Account.
```

## 📥 Parameters
### Path Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `agentId` | ❌ |  |

### Header Parameters
| Name | Required | Description |
| :--- | :--- | :--- |
| `Version` | ❌ |  |

## 📤 Responses
<details>
<summary>Response 200</summary>

```json
{
  "data": {
    "id": "actionId123",
    "name": "Trigger Workflow",
    "type": "triggerWorkflow",
    "agentId": "agentId123",
    "details": {
      "workflowIds": [
        "workflow123",
        "workflow456"
      ],
      "triggerCondition": "When user requests appointment",
      "triggerMessage": "Workflow triggered successfully"
    }
  },
  "success": true
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L -X PATCH 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

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

	  const response = await highLevel.conversationAi.updateFollowupSettings({

	    'agentId': 'agentId_value'

	  },

	  {

	    'actionIds': [

	      'edxcfghbnjkimd'

	    ],

	    'followupSettings': {

	      'dynamicChannelSwitching': true,

	      'followUpHours': true,

	      'workingHours': [

	        {

	          'dayOfTheWeek': 1,

	          'intervals': [

	            {

	              'startHour': 9,

	              'startMinute': 0,

	              'endHour': 17,

	              'endMinute': 30

	            }

	          ]

	        }

	      ],

	      'timezoneToUse': 'contact'

	    }

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

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

	});

	

	let config = {

	  method: 'patch',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings',

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

	  'method': 'PATCH',

	  'hostname': 'services.leadconnectorhq.com',

	  'path': '/conversation-ai/agents/:agentId/followup-settings',

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

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'PATCH',

	  'url': 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "actionIds": [

	      "edxcfghbnjkimd"

	    ],

	    "followupSettings": {

	      "dynamicChannelSwitching": true,

	      "followUpHours": true,

	      "workingHours": [

	        {

	          "dayOfTheWeek": 1,

	          "intervals": [

	            {

	              "startHour": 9,

	              "startMinute": 0,

	              "endHour": 17,

	              "endMinute": 30

	            }

	          ]

	        }

	      ],

	      "timezoneToUse": "contact"

	    }

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

	var req = unirest('PATCH', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "actionIds": [

	      "edxcfghbnjkimd"

	    ],

	    "followupSettings": {

	      "dynamicChannelSwitching": true,

	      "followUpHours": true,

	      "workingHours": [

	        {

	          "dayOfTheWeek": 1,

	          "intervals": [

	            {

	              "startHour": 9,

	              "startMinute": 0,

	              "endHour": 17,

	              "endMinute": 30

	            }

	          ]

	        }

	      ],

	      "timezoneToUse": "contact"

	    }

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

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": True,

	    "followUpHours": True,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("PATCH", "/conversation-ai/agents/:agentId/followup-settings", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings"

	

	payload = json.dumps({

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": True,

	    "followUpHours": True,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	

	response = requests.request("PATCH", url, headers=headers, data=payload)

	

	print(response.text)

```

### PHP
#### CURL
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'PATCH',

	  CURLOPT_POSTFIELDS =>'{

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

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

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

	}';

	$request = new Request('PATCH', 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings');

	$request->setMethod('PATCH');

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "actionIds": [\n    "edxcfghbnjkimd"\n  ],\n  "followupSettings": {\n    "dynamicChannelSwitching": true,\n    "followUpHours": true,\n    "workingHours": [\n      {\n        "dayOfTheWeek": 1,\n        "intervals": [\n          {\n            "startHour": 9,\n            "startMinute": 0,\n            "endHour": 17,\n            "endMinute": 30\n          }\n        ]\n      }\n    ],\n    "timezoneToUse": "contact"\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings');

	$request->setRequestMethod('PATCH');

	$body = new http\Message\Body;

	$body->append('{

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"actionIds\": [\n    \"edxcfghbnjkimd\"\n  ],\n  \"followupSettings\": {\n    \"dynamicChannelSwitching\": true,\n    \"followUpHours\": true,\n    \"workingHours\": [\n      {\n        \"dayOfTheWeek\": 1,\n        \"intervals\": [\n          {\n            \"startHour\": 9,\n            \"startMinute\": 0,\n            \"endHour\": 17,\n            \"endMinute\": 30\n          }\n        ]\n      }\n    ],\n    \"timezoneToUse\": \"contact\"\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings")

	  .method("PATCH", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.patch("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"actionIds\": [\n    \"edxcfghbnjkimd\"\n  ],\n  \"followupSettings\": {\n    \"dynamicChannelSwitching\": true,\n    \"followUpHours\": true,\n    \"workingHours\": [\n      {\n        \"dayOfTheWeek\": 1,\n        \"intervals\": [\n          {\n            \"startHour\": 9,\n            \"startMinute\": 0,\n            \"endHour\": 17,\n            \"endMinute\": 30\n          }\n        ]\n      }\n    ],\n    \"timezoneToUse\": \"contact\"\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings"

	  method := "PATCH"

	

	  payload := strings.NewReader(`{

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

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

	

	url = URI("https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Patch.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "actionIds": [

	    "edxcfghbnjkimd"

	  ],

	  "followupSettings": {

	    "dynamicChannelSwitching": true,

	    "followUpHours": true,

	    "workingHours": [

	      {

	        "dayOfTheWeek": 1,

	        "intervals": [

	          {

	            "startHour": 9,

	            "startMinute": 0,

	            "endHour": 17,

	            "endMinute": 30

	          }

	        ]

	      }

	    ],

	    "timezoneToUse": "contact"

	  }

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

	  `"actionIds`": [

	    `"edxcfghbnjkimd`"

	  ],

	  `"followupSettings`": {

	    `"dynamicChannelSwitching`": true,

	    `"followUpHours`": true,

	    `"workingHours`": [

	      {

	        `"dayOfTheWeek`": 1,

	        `"intervals`": [

	          {

	            `"startHour`": 9,

	            `"startMinute`": 0,

	            `"endHour`": 17,

	            `"endMinute`": 30

	          }

	        ]

	      }

	    ],

	    `"timezoneToUse`": `"contact`"

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/conversation-ai/agents/:agentId/followup-settings' -Method 'PATCH' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

