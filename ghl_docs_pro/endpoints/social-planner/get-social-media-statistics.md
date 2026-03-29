# Get Social Media Statistics

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/social-media-posting/statistics`

## 🔐 Requirements
```text
N/A
```

## 📥 Parameters
### Query Parameters
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
  "results": {
    "dayRange": [
      "Mon",
      "Tue",
      "Wed",
      "Thu",
      "Fri",
      "Sat",
      "Sun"
    ],
    "totals": {
      "posts": 0,
      "likes": 0,
      "followers": 0,
      "impressions": 0,
      "comments": 0
    },
    "postPerformance": {
      "posts": {
        "google": [
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ]
      },
      "impressions": [
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "likes": [
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "comments": [
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    },
    "breakdowns": {
      "posts": {
        "total": 0,
        "totalChange": 0,
        "platforms": {
          "google": {
            "value": 0,
            "change": 0
          }
        }
      },
      "impressions": {
        "total": 0,
        "totalChange": 0,
        "platforms": {
          "google": {
            "value": 0,
            "change": 0
          }
        }
      },
      "reach": {
        "total": 0,
        "totalChange": 0,
        "platforms": {
          "google": {
            "value": 0,
            "change": 0
          }
        }
      },
      "engagement": {
        "google": {
          "likes": 0,
          "comments": 0,
          "shares": 0,
          "change": 0
        }
      }
    },
    "platformTotals": {
      "impressions": {
        "google": {
          "total": 0,
          "series": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        }
      },
      "followers": {
        "google": {
          "total": 0,
          "series": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        }
      },
      "likes": {
        "google": {
          "total": 0,
          "series": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        }
      }
    },
    "demographics": {
      "gender": {
        "totals": {
          "male": {
            "total": 0,
            "percentage": 0
          },
          "female": {
            "total": 0,
            "percentage": 0
          },
          "unknown": {
            "total": 0,
            "percentage": 0
          }
        }
      },
      "age": {
        "totals": {
          "13-17": 0,
          "18-24": 0,
          "25-34": 0,
          "35-44": 0,
          "45-54": 0,
          "55-64": 0,
          "65+": 0
        }
      }
    }
  },
  "message": "Analytics Built Successfully",
  "traceId": "42fc8dd8-d55b-475f-944f-9efb90d77564"
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "results": {    "dayRange": [      "Mon",      "Tue",      "Wed",      "Thu",      "Fri",      "Sat",      "Sun"    ],    "totals": {      "posts": 0,      "likes": 0,      "followers": 0,      "impressions": 0,      "comments": 0    },    "postPerformance": {      "posts": {        "google": [          0,          0,          0,          0,          0,          0,          0        ]      },      "impressions": [        0,        0,        0,        0,        0,        0,        0      ],      "likes": [        0,        0,        0,        0,        0,        0,        0      ],      "comments": [        0,        0,        0,        0,        0,        0,        0      ]    },    "breakdowns": {      "posts": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "impressions": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "reach": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "engagement": {        "google": {          "likes": 0,          "comments": 0,          "shares": 0,          "change": 0        }      }    },    "platformTotals": {      "impressions": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      },      "followers": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      },      "likes": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      }    },    "demographics": {      "gender": {        "totals": {          "male": {            "total": 0,            "percentage": 0          },          "female": {            "total": 0,            "percentage": 0          },          "unknown": {            "total": 0,            "percentage": 0          }        }      },      "age": {        "totals": {          "13-17": 0,          "18-24": 0,          "25-34": 0,          "35-44": 0,          "45-54": 0,          "55-64": 0,          "65+": 0        }      }    }  },  "message": "Analytics Built Successfully",  "traceId": "42fc8dd8-d55b-475f-944f-9efb90d77564"}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "results": {    "dayRange": [      "Mon",      "Tue",      "Wed",      "Thu",      "Fri",      "Sat",      "Sun"    ],    "totals": {      "posts": 0,      "likes": 0,      "followers": 0,      "impressions": 0,      "comments": 0    },    "postPerformance": {      "posts": {        "google": [          0,          0,          0,          0,          0,          0,          0        ]      },      "impressions": [        0,        0,        0,        0,        0,        0,        0      ],      "likes": [        0,        0,        0,        0,        0,        0,        0      ],      "comments": [        0,        0,        0,        0,        0,        0,        0      ]    },    "breakdowns": {      "posts": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "impressions": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "reach": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "engagement": {        "google": {          "likes": 0,          "comments": 0,          "shares": 0,          "change": 0        }      }    },    "platformTotals": {      "impressions": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      },      "followers": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      },      "likes": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      }    },    "demographics": {      "gender": {        "totals": {          "male": {            "total": 0,            "percentage": 0          },          "female": {            "total": 0,            "percentage": 0          },          "unknown": {            "total": 0,            "percentage": 0          }        }      },      "age": {        "totals": {          "13-17": 0,          "18-24": 0,          "25-34": 0,          "35-44": 0,          "45-54": 0,          "55-64": 0,          "65+": 0        }      }    }  },  "message": "Analytics Built Successfully",  "traceId": "42fc8dd8-d55b-475f-944f-9efb90d77564"}
```
</details>

<details>
<summary>Response 422</summary>

```json
{  "results": {    "dayRange": [      "Mon",      "Tue",      "Wed",      "Thu",      "Fri",      "Sat",      "Sun"    ],    "totals": {      "posts": 0,      "likes": 0,      "followers": 0,      "impressions": 0,      "comments": 0    },    "postPerformance": {      "posts": {        "google": [          0,          0,          0,          0,          0,          0,          0        ]      },      "impressions": [        0,        0,        0,        0,        0,        0,        0      ],      "likes": [        0,        0,        0,        0,        0,        0,        0      ],      "comments": [        0,        0,        0,        0,        0,        0,        0      ]    },    "breakdowns": {      "posts": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "impressions": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "reach": {        "total": 0,        "totalChange": 0,        "platforms": {          "google": {            "value": 0,            "change": 0          }        }      },      "engagement": {        "google": {          "likes": 0,          "comments": 0,          "shares": 0,          "change": 0        }      }    },    "platformTotals": {      "impressions": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      },      "followers": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      },      "likes": {        "google": {          "total": 0,          "series": [            0,            0,            0,            0,            0,            0,            0          ]        }      }    },    "demographics": {      "gender": {        "totals": {          "male": {            "total": 0,            "percentage": 0          },          "female": {            "total": 0,            "percentage": 0          },          "unknown": {            "total": 0,            "percentage": 0          }        }      },      "age": {        "totals": {          "13-17": 0,          "18-24": 0,          "25-34": 0,          "35-44": 0,          "45-54": 0,          "55-64": 0,          "65+": 0        }      }    }  },  "message": "Analytics Built Successfully",  "traceId": "42fc8dd8-d55b-475f-944f-9efb90d77564"}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/social-media-posting/statistics' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-d '{

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

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

	  const response = await highLevel.socialPlanner.getStatistics({

	    'locationId': 'w37swmmLbA02zgqKPpxITe2'

	  },

	  {

	    'profileIds': [

	      '67a5a9aa776c837de4aa5b12'

	    ],

	    'platforms': [

	      'facebook',

	      'instagram'

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

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

	  ]

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/social-media-posting/statistics',

	  headers: { 

	    'Content-Type': 'application/json', 

	    'Accept': 'application/json'

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

	  'path': '/social-media-posting/statistics',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

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

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

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

	  'url': 'https://services.leadconnectorhq.com/social-media-posting/statistics',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  },

	  body: JSON.stringify({

	    "profileIds": [

	      "67a5a9aa776c837de4aa5b12"

	    ],

	    "platforms": [

	      "facebook",

	      "instagram"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/social-media-posting/statistics')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json'

	  })

	  .send(JSON.stringify({

	    "profileIds": [

	      "67a5a9aa776c837de4aa5b12"

	    ],

	    "platforms": [

	      "facebook",

	      "instagram"

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

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

	}

	conn.request("POST", "/social-media-posting/statistics", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/social-media-posting/statistics"

	

	payload = json.dumps({

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

	  ]

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json'

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/social-media-posting/statistics',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

	  ]

	}',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/json',

	    'Accept: application/json'

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

	  'Accept' => 'application/json'

	];

	$body = '{

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

	  ]

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/social-media-posting/statistics', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/social-media-posting/statistics');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

	));

	$request->setBody('{\n  "profileIds": [\n    "67a5a9aa776c837de4aa5b12"\n  ],\n  "platforms": [\n    "facebook",\n    "instagram"\n  ]\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/social-media-posting/statistics');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

	  ]

	}');

	$request->setBody($body);

	$request->setOptions(array());

	$request->setHeaders(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json'

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"profileIds\": [\n    \"67a5a9aa776c837de4aa5b12\"\n  ],\n  \"platforms\": [\n    \"facebook\",\n    \"instagram\"\n  ]\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/social-media-posting/statistics")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Accept", "application/json")

	  .build();

	Response response = client.newCall(request).execute();

```

#### UNIREST
```java
	Unirest.setTimeouts(0, 0);

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/social-media-posting/statistics")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .body("{\n  \"profileIds\": [\n    \"67a5a9aa776c837de4aa5b12\"\n  ],\n  \"platforms\": [\n    \"facebook\",\n    \"instagram\"\n  ]\n}")

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

	

	  url := "https://services.leadconnectorhq.com/social-media-posting/statistics"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

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

	

	url = URI("https://services.leadconnectorhq.com/social-media-posting/statistics")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request.body = JSON.dump({

	  "profileIds": [

	    "67a5a9aa776c837de4aa5b12"

	  ],

	  "platforms": [

	    "facebook",

	    "instagram"

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

	

	$body = @"

	{

	  `"profileIds`": [

	    `"67a5a9aa776c837de4aa5b12`"

	  ],

	  `"platforms`": [

	    `"facebook`",

	    `"instagram`"

	  ]

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/social-media-posting/statistics' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

