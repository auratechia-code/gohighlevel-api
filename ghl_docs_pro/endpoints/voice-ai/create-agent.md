# Create Agent

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/voice-ai/agents`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: voice-ai-agents.write
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
  "id": "507f1f77bcf86cd799439011",
  "locationId": "LOC123456789ABCDEF",
  "agentName": "Customer Support Agent",
  "businessName": "Acme Corporation",
  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",
  "agentPrompt": "You are a helpful customer service representative.",
  "voiceId": "507f1f77bcf86cd799439011",
  "language": "en-US",
  "patienceLevel": "medium",
  "maxCallDuration": 600,
  "sendUserIdleReminders": true,
  "reminderAfterIdleTimeSeconds": 5,
  "inboundNumber": "+1234567890",
  "numberPoolId": "pool_507f1f77bcf86cd799439011",
  "callEndWorkflowIds": [],
  "sendPostCallNotificationTo": {
    "admins": true,
    "allUsers": false,
    "contactAssignedUser": false,
    "specificUsers": [],
    "customEmails": []
  },
  "agentWorkingHours": [],
  "timezone": "America/New_York",
  "isAgentAsBackupDisabled": false,
  "translation": {
    "enabled": false,
    "language": "es"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/voice-ai/agents' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

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

	  const response = await highLevel.voiceAi.createAgent({

	    'locationId': 'LOC123456789ABCDEF',

	    'agentName': 'Customer Support Agent',

	    'businessName': 'Acme Corporation',

	    'welcomeMessage': 'Hello! Thank you for calling Acme Corporation. How can I assist you today?',

	    'agentPrompt': 'You are a helpful customer service representative. Always be polite and professional.',

	    'voiceId': '507f1f77bcf86cd799439011',

	    'language': 'en-US',

	    'patienceLevel': 'low',

	    'maxCallDuration': 600,

	    'sendUserIdleReminders': true,

	    'reminderAfterIdleTimeSeconds': 5,

	    'inboundNumber': '+1234567890',

	    'numberPoolId': 'pool_507f1f77bcf86cd799439011',

	    'callEndWorkflowIds': [

	      'wf_507f1f77bcf86cd799439011',

	      'wf_507f1f77bcf86cd799439012'

	    ],

	    'sendPostCallNotificationTo': {

	      'admins': true,

	      'allUsers': false,

	      'contactAssignedUser': false,

	      'specificUsers': [

	        'user_507f1f77bcf86cd799439011'

	      ],

	      'customEmails': [

	        'manager@company.com'

	      ]

	    },

	    'agentWorkingHours': [

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

	    'timezone': 'America/New_York',

	    'isAgentAsBackupDisabled': false,

	    'translation': {

	      'enabled': false,

	      'language': 'es'

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

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

	  }

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/voice-ai/agents',

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

	  'path': '/voice-ai/agents',

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

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

	  }

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/voice-ai/agents',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "locationId": "LOC123456789ABCDEF",

	    "agentName": "Customer Support Agent",

	    "businessName": "Acme Corporation",

	    "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	    "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	    "voiceId": "507f1f77bcf86cd799439011",

	    "language": "en-US",

	    "patienceLevel": "low",

	    "maxCallDuration": 600,

	    "sendUserIdleReminders": true,

	    "reminderAfterIdleTimeSeconds": 5,

	    "inboundNumber": "+1234567890",

	    "numberPoolId": "pool_507f1f77bcf86cd799439011",

	    "callEndWorkflowIds": [

	      "wf_507f1f77bcf86cd799439011",

	      "wf_507f1f77bcf86cd799439012"

	    ],

	    "sendPostCallNotificationTo": {

	      "admins": true,

	      "allUsers": false,

	      "contactAssignedUser": false,

	      "specificUsers": [

	        "user_507f1f77bcf86cd799439011"

	      ],

	      "customEmails": [

	        "manager@company.com"

	      ]

	    },

	    "agentWorkingHours": [

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

	    "timezone": "America/New_York",

	    "isAgentAsBackupDisabled": false,

	    "translation": {

	      "enabled": false,

	      "language": "es"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/voice-ai/agents')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "locationId": "LOC123456789ABCDEF",

	    "agentName": "Customer Support Agent",

	    "businessName": "Acme Corporation",

	    "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	    "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	    "voiceId": "507f1f77bcf86cd799439011",

	    "language": "en-US",

	    "patienceLevel": "low",

	    "maxCallDuration": 600,

	    "sendUserIdleReminders": true,

	    "reminderAfterIdleTimeSeconds": 5,

	    "inboundNumber": "+1234567890",

	    "numberPoolId": "pool_507f1f77bcf86cd799439011",

	    "callEndWorkflowIds": [

	      "wf_507f1f77bcf86cd799439011",

	      "wf_507f1f77bcf86cd799439012"

	    ],

	    "sendPostCallNotificationTo": {

	      "admins": true,

	      "allUsers": false,

	      "contactAssignedUser": false,

	      "specificUsers": [

	        "user_507f1f77bcf86cd799439011"

	      ],

	      "customEmails": [

	        "manager@company.com"

	      ]

	    },

	    "agentWorkingHours": [

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

	    "timezone": "America/New_York",

	    "isAgentAsBackupDisabled": false,

	    "translation": {

	      "enabled": false,

	      "language": "es"

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

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": True,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": True,

	    "allUsers": False,

	    "contactAssignedUser": False,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": False,

	  "translation": {

	    "enabled": False,

	    "language": "es"

	  }

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/voice-ai/agents", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/voice-ai/agents"

	

	payload = json.dumps({

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": True,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": True,

	    "allUsers": False,

	    "contactAssignedUser": False,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": False,

	  "translation": {

	    "enabled": False,

	    "language": "es"

	  }

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/voice-ai/agents',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

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

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

	  }

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/voice-ai/agents', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/voice-ai/agents');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "locationId": "LOC123456789ABCDEF",\n  "agentName": "Customer Support Agent",\n  "businessName": "Acme Corporation",\n  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",\n  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",\n  "voiceId": "507f1f77bcf86cd799439011",\n  "language": "en-US",\n  "patienceLevel": "low",\n  "maxCallDuration": 600,\n  "sendUserIdleReminders": true,\n  "reminderAfterIdleTimeSeconds": 5,\n  "inboundNumber": "+1234567890",\n  "numberPoolId": "pool_507f1f77bcf86cd799439011",\n  "callEndWorkflowIds": [\n    "wf_507f1f77bcf86cd799439011",\n    "wf_507f1f77bcf86cd799439012"\n  ],\n  "sendPostCallNotificationTo": {\n    "admins": true,\n    "allUsers": false,\n    "contactAssignedUser": false,\n    "specificUsers": [\n      "user_507f1f77bcf86cd799439011"\n    ],\n    "customEmails": [\n      "manager@company.com"\n    ]\n  },\n  "agentWorkingHours": [\n    {\n      "dayOfTheWeek": 1,\n      "intervals": [\n        {\n          "startHour": 9,\n          "startMinute": 0,\n          "endHour": 17,\n          "endMinute": 30\n        }\n      ]\n    }\n  ],\n  "timezone": "America/New_York",\n  "isAgentAsBackupDisabled": false,\n  "translation": {\n    "enabled": false,\n    "language": "es"\n  }\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/voice-ai/agents');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"locationId\": \"LOC123456789ABCDEF\",\n  \"agentName\": \"Customer Support Agent\",\n  \"businessName\": \"Acme Corporation\",\n  \"welcomeMessage\": \"Hello! Thank you for calling Acme Corporation. How can I assist you today?\",\n  \"agentPrompt\": \"You are a helpful customer service representative. Always be polite and professional.\",\n  \"voiceId\": \"507f1f77bcf86cd799439011\",\n  \"language\": \"en-US\",\n  \"patienceLevel\": \"low\",\n  \"maxCallDuration\": 600,\n  \"sendUserIdleReminders\": true,\n  \"reminderAfterIdleTimeSeconds\": 5,\n  \"inboundNumber\": \"+1234567890\",\n  \"numberPoolId\": \"pool_507f1f77bcf86cd799439011\",\n  \"callEndWorkflowIds\": [\n    \"wf_507f1f77bcf86cd799439011\",\n    \"wf_507f1f77bcf86cd799439012\"\n  ],\n  \"sendPostCallNotificationTo\": {\n    \"admins\": true,\n    \"allUsers\": false,\n    \"contactAssignedUser\": false,\n    \"specificUsers\": [\n      \"user_507f1f77bcf86cd799439011\"\n    ],\n    \"customEmails\": [\n      \"manager@company.com\"\n    ]\n  },\n  \"agentWorkingHours\": [\n    {\n      \"dayOfTheWeek\": 1,\n      \"intervals\": [\n        {\n          \"startHour\": 9,\n          \"startMinute\": 0,\n          \"endHour\": 17,\n          \"endMinute\": 30\n        }\n      ]\n    }\n  ],\n  \"timezone\": \"America/New_York\",\n  \"isAgentAsBackupDisabled\": false,\n  \"translation\": {\n    \"enabled\": false,\n    \"language\": \"es\"\n  }\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/voice-ai/agents")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/voice-ai/agents")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"locationId\": \"LOC123456789ABCDEF\",\n  \"agentName\": \"Customer Support Agent\",\n  \"businessName\": \"Acme Corporation\",\n  \"welcomeMessage\": \"Hello! Thank you for calling Acme Corporation. How can I assist you today?\",\n  \"agentPrompt\": \"You are a helpful customer service representative. Always be polite and professional.\",\n  \"voiceId\": \"507f1f77bcf86cd799439011\",\n  \"language\": \"en-US\",\n  \"patienceLevel\": \"low\",\n  \"maxCallDuration\": 600,\n  \"sendUserIdleReminders\": true,\n  \"reminderAfterIdleTimeSeconds\": 5,\n  \"inboundNumber\": \"+1234567890\",\n  \"numberPoolId\": \"pool_507f1f77bcf86cd799439011\",\n  \"callEndWorkflowIds\": [\n    \"wf_507f1f77bcf86cd799439011\",\n    \"wf_507f1f77bcf86cd799439012\"\n  ],\n  \"sendPostCallNotificationTo\": {\n    \"admins\": true,\n    \"allUsers\": false,\n    \"contactAssignedUser\": false,\n    \"specificUsers\": [\n      \"user_507f1f77bcf86cd799439011\"\n    ],\n    \"customEmails\": [\n      \"manager@company.com\"\n    ]\n  },\n  \"agentWorkingHours\": [\n    {\n      \"dayOfTheWeek\": 1,\n      \"intervals\": [\n        {\n          \"startHour\": 9,\n          \"startMinute\": 0,\n          \"endHour\": 17,\n          \"endMinute\": 30\n        }\n      ]\n    }\n  ],\n  \"timezone\": \"America/New_York\",\n  \"isAgentAsBackupDisabled\": false,\n  \"translation\": {\n    \"enabled\": false,\n    \"language\": \"es\"\n  }\n}")

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

	

	  url := "https://services.leadconnectorhq.com/voice-ai/agents"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

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

	

	url = URI("https://services.leadconnectorhq.com/voice-ai/agents")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "locationId": "LOC123456789ABCDEF",

	  "agentName": "Customer Support Agent",

	  "businessName": "Acme Corporation",

	  "welcomeMessage": "Hello\! Thank you for calling Acme Corporation. How can I assist you today?",

	  "agentPrompt": "You are a helpful customer service representative. Always be polite and professional.",

	  "voiceId": "507f1f77bcf86cd799439011",

	  "language": "en-US",

	  "patienceLevel": "low",

	  "maxCallDuration": 600,

	  "sendUserIdleReminders": true,

	  "reminderAfterIdleTimeSeconds": 5,

	  "inboundNumber": "+1234567890",

	  "numberPoolId": "pool_507f1f77bcf86cd799439011",

	  "callEndWorkflowIds": [

	    "wf_507f1f77bcf86cd799439011",

	    "wf_507f1f77bcf86cd799439012"

	  ],

	  "sendPostCallNotificationTo": {

	    "admins": true,

	    "allUsers": false,

	    "contactAssignedUser": false,

	    "specificUsers": [

	      "user_507f1f77bcf86cd799439011"

	    ],

	    "customEmails": [

	      "manager@company.com"

	    ]

	  },

	  "agentWorkingHours": [

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

	  "timezone": "America/New_York",

	  "isAgentAsBackupDisabled": false,

	  "translation": {

	    "enabled": false,

	    "language": "es"

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

	  `"locationId`": `"LOC123456789ABCDEF`",

	  `"agentName`": `"Customer Support Agent`",

	  `"businessName`": `"Acme Corporation`",

	  `"welcomeMessage`": `"Hello! Thank you for calling Acme Corporation. How can I assist you today?`",

	  `"agentPrompt`": `"You are a helpful customer service representative. Always be polite and professional.`",

	  `"voiceId`": `"507f1f77bcf86cd799439011`",

	  `"language`": `"en-US`",

	  `"patienceLevel`": `"low`",

	  `"maxCallDuration`": 600,

	  `"sendUserIdleReminders`": true,

	  `"reminderAfterIdleTimeSeconds`": 5,

	  `"inboundNumber`": `"+1234567890`",

	  `"numberPoolId`": `"pool_507f1f77bcf86cd799439011`",

	  `"callEndWorkflowIds`": [

	    `"wf_507f1f77bcf86cd799439011`",

	    `"wf_507f1f77bcf86cd799439012`"

	  ],

	  `"sendPostCallNotificationTo`": {

	    `"admins`": true,

	    `"allUsers`": false,

	    `"contactAssignedUser`": false,

	    `"specificUsers`": [

	      `"user_507f1f77bcf86cd799439011`"

	    ],

	    `"customEmails`": [

	      `"manager@company.com`"

	    ]

	  },

	  `"agentWorkingHours`": [

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

	  `"timezone`": `"America/New_York`",

	  `"isAgentAsBackupDisabled`": false,

	  `"translation`": {

	    `"enabled`": false,

	    `"language`": `"es`"

	  }

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/voice-ai/agents' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

