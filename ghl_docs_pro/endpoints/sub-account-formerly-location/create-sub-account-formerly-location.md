# Create Sub-Account (Formerly Location)

**Method:** `POST` | **URL:** `https://services.leadconnectorhq.com/locations/`

## 🔐 Requirements
```text
AUTHORIZATION: AUTHORIZATION
name: Authorization
type: http
scopes: locations.write
scheme: bearer
bearerFormat: JWT
in: header
description: Use the Access Token generated with user type as Agency (OR) Private Integration Token of Agency.
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
  "id": "ve9EPM428h8vShlRW1KT",
  "companyId": "UAXssdawIWAWD",
  "name": "Mark Shoes",
  "phone": "+1410039940",
  "email": "john.doe@mail.com",
  "address": "4th fleet street",
  "city": "New York",
  "state": "Illinois",
  "domain": "test.msgsndr.com",
  "country": "US",
  "postalCode": "567654",
  "website": "https://yourwebsite.com",
  "timezone": "US/Central",
  "settings": {
    "allowDuplicateContact": false,
    "allowDuplicateOpportunity": false,
    "allowFacebookNameMerge": false,
    "disableContactTimezone": false
  },
  "social": {
    "facebookUrl": "https://www.facebook.com/",
    "googlePlus": "https://www.googleplus.com/",
    "linkedIn": "https://www.linkedIn.com/",
    "foursquare": "https://www.foursquare.com/",
    "twitter": "https://www.foutwitterrsquare.com/",
    "yelp": "https://www.yelp.com/",
    "instagram": "https://www.instagram.com/",
    "youtube": "https://www.youtube.com/",
    "pinterest": "https://www.pinterest.com/",
    "blogRss": "https://www.blogRss.com/",
    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"
  }
}

```
</details>

<details>
<summary>Response 400</summary>

```json
{  "id": "ve9EPM428h8vShlRW1KT",  "companyId": "UAXssdawIWAWD",  "name": "Mark Shoes",  "phone": "+1410039940",  "email": "john.doe@mail.com",  "address": "4th fleet street",  "city": "New York",  "state": "Illinois",  "domain": "test.msgsndr.com",  "country": "US",  "postalCode": "567654",  "website": "https://yourwebsite.com",  "timezone": "US/Central",  "settings": {    "allowDuplicateContact": false,    "allowDuplicateOpportunity": false,    "allowFacebookNameMerge": false,    "disableContactTimezone": false  },  "social": {    "facebookUrl": "https://www.facebook.com/",    "googlePlus": "https://www.googleplus.com/",    "linkedIn": "https://www.linkedIn.com/",    "foursquare": "https://www.foursquare.com/",    "twitter": "https://www.foutwitterrsquare.com/",    "yelp": "https://www.yelp.com/",    "instagram": "https://www.instagram.com/",    "youtube": "https://www.youtube.com/",    "pinterest": "https://www.pinterest.com/",    "blogRss": "https://www.blogRss.com/",    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"  }}
```
</details>

<details>
<summary>Response 401</summary>

```json
{  "id": "ve9EPM428h8vShlRW1KT",  "companyId": "UAXssdawIWAWD",  "name": "Mark Shoes",  "phone": "+1410039940",  "email": "john.doe@mail.com",  "address": "4th fleet street",  "city": "New York",  "state": "Illinois",  "domain": "test.msgsndr.com",  "country": "US",  "postalCode": "567654",  "website": "https://yourwebsite.com",  "timezone": "US/Central",  "settings": {    "allowDuplicateContact": false,    "allowDuplicateOpportunity": false,    "allowFacebookNameMerge": false,    "disableContactTimezone": false  },  "social": {    "facebookUrl": "https://www.facebook.com/",    "googlePlus": "https://www.googleplus.com/",    "linkedIn": "https://www.linkedIn.com/",    "foursquare": "https://www.foursquare.com/",    "twitter": "https://www.foutwitterrsquare.com/",    "yelp": "https://www.yelp.com/",    "instagram": "https://www.instagram.com/",    "youtube": "https://www.youtube.com/",    "pinterest": "https://www.pinterest.com/",    "blogRss": "https://www.blogRss.com/",    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"  }}
```
</details>

## 💻 Code Examples

### CURL
#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/locations/' \

	-H 'Content-Type: application/json' \

	-H 'Accept: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	--data-raw '{

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

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

	  const response = await highLevel.locations.createLocation({

	    'name': 'Mark Shoes',

	    'phone': '+1410039940',

	    'companyId': 'UAXssdawIWAWD',

	    'address': '4th fleet street',

	    'city': 'New York',

	    'state': 'Illinois',

	    'country': 'US',

	    'postalCode': '567654',

	    'website': 'https://yourwebsite.com',

	    'timezone': 'US/Central',

	    'prospectInfo': {

	      'firstName': 'John',

	      'lastName': 'Doe',

	      'email': 'john.doe@mail.com'

	    },

	    'settings': {

	      'allowDuplicateContact': false,

	      'allowDuplicateOpportunity': false,

	      'allowFacebookNameMerge': false,

	      'disableContactTimezone': false

	    },

	    'social': {

	      'facebookUrl': 'https://www.facebook.com/',

	      'googlePlus': 'https://www.googleplus.com/',

	      'linkedIn': 'https://www.linkedIn.com/',

	      'foursquare': 'https://www.foursquare.com/',

	      'twitter': 'https://www.foutwitterrsquare.com/',

	      'yelp': 'https://www.yelp.com/',

	      'instagram': 'https://www.instagram.com/',

	      'youtube': 'https://www.youtube.com/',

	      'pinterest': 'https://www.pinterest.com/',

	      'blogRss': 'https://www.blogRss.com/',

	      'googlePlacesId': 'ChIJJGPdVbQTrjsRGUkefteUeFk'

	    },

	    'mailgun': {

	      'apiKey': 'key-XXXXXXXXXXX',

	      'domain': 'replies.yourdomain.com'

	    },

	    'snapshotId': 'XXXXXXXXXXX'

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

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

	});

	

	let config = {

	  method: 'post',

	  maxBodyLength: Infinity,

	  url: 'https://services.leadconnectorhq.com/locations/',

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

	  'path': '/locations/',

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

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

	});

	

	req.write(postData);

	

	req.end();

```

#### REQUEST
```nodejs
	var request = require('request');

	var options = {

	  'method': 'POST',

	  'url': 'https://services.leadconnectorhq.com/locations/',

	  'headers': {

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  },

	  body: JSON.stringify({

	    "name": "Mark Shoes",

	    "phone": "+1410039940",

	    "companyId": "UAXssdawIWAWD",

	    "address": "4th fleet street",

	    "city": "New York",

	    "state": "Illinois",

	    "country": "US",

	    "postalCode": "567654",

	    "website": "https://yourwebsite.com",

	    "timezone": "US/Central",

	    "prospectInfo": {

	      "firstName": "John",

	      "lastName": "Doe",

	      "email": "john.doe@mail.com"

	    },

	    "settings": {

	      "allowDuplicateContact": false,

	      "allowDuplicateOpportunity": false,

	      "allowFacebookNameMerge": false,

	      "disableContactTimezone": false

	    },

	    "social": {

	      "facebookUrl": "https://www.facebook.com/",

	      "googlePlus": "https://www.googleplus.com/",

	      "linkedIn": "https://www.linkedIn.com/",

	      "foursquare": "https://www.foursquare.com/",

	      "twitter": "https://www.foutwitterrsquare.com/",

	      "yelp": "https://www.yelp.com/",

	      "instagram": "https://www.instagram.com/",

	      "youtube": "https://www.youtube.com/",

	      "pinterest": "https://www.pinterest.com/",

	      "blogRss": "https://www.blogRss.com/",

	      "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	    },

	    "mailgun": {

	      "apiKey": "key-XXXXXXXXXXX",

	      "domain": "replies.yourdomain.com"

	    },

	    "snapshotId": "XXXXXXXXXXX"

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

	var req = unirest('POST', 'https://services.leadconnectorhq.com/locations/')

	  .headers({

	    'Content-Type': 'application/json',

	    'Accept': 'application/json',

	    'Authorization': 'Bearer <TOKEN>'

	  })

	  .send(JSON.stringify({

	    "name": "Mark Shoes",

	    "phone": "+1410039940",

	    "companyId": "UAXssdawIWAWD",

	    "address": "4th fleet street",

	    "city": "New York",

	    "state": "Illinois",

	    "country": "US",

	    "postalCode": "567654",

	    "website": "https://yourwebsite.com",

	    "timezone": "US/Central",

	    "prospectInfo": {

	      "firstName": "John",

	      "lastName": "Doe",

	      "email": "john.doe@mail.com"

	    },

	    "settings": {

	      "allowDuplicateContact": false,

	      "allowDuplicateOpportunity": false,

	      "allowFacebookNameMerge": false,

	      "disableContactTimezone": false

	    },

	    "social": {

	      "facebookUrl": "https://www.facebook.com/",

	      "googlePlus": "https://www.googleplus.com/",

	      "linkedIn": "https://www.linkedIn.com/",

	      "foursquare": "https://www.foursquare.com/",

	      "twitter": "https://www.foutwitterrsquare.com/",

	      "yelp": "https://www.yelp.com/",

	      "instagram": "https://www.instagram.com/",

	      "youtube": "https://www.youtube.com/",

	      "pinterest": "https://www.pinterest.com/",

	      "blogRss": "https://www.blogRss.com/",

	      "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	    },

	    "mailgun": {

	      "apiKey": "key-XXXXXXXXXXX",

	      "domain": "replies.yourdomain.com"

	    },

	    "snapshotId": "XXXXXXXXXXX"

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

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": False,

	    "allowDuplicateOpportunity": False,

	    "allowFacebookNameMerge": False,

	    "disableContactTimezone": False

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

	})

	headers = {

	  'Content-Type': 'application/json',

	  'Accept': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/locations/", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### REQUESTS
```python
	import requests

	import json

	

	url = "https://services.leadconnectorhq.com/locations/"

	

	payload = json.dumps({

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": False,

	    "allowDuplicateOpportunity": False,

	    "allowFacebookNameMerge": False,

	    "disableContactTimezone": False

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

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

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/locations/',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

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

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

	}';

	$request = new Request('POST', 'https://services.leadconnectorhq.com/locations/', $headers, $body);

	$res = $client->sendAsync($request)->wait();

	echo $res->getBody();

```

#### HTTP_REQUEST2
```php
	<?php

	require_once 'HTTP/Request2.php';

	$request = new HTTP_Request2();

	$request->setUrl('https://services.leadconnectorhq.com/locations/');

	$request->setMethod(HTTP_Request2::METHOD_POST);

	$request->setConfig(array(

	  'follow_redirects' => TRUE

	));

	$request->setHeader(array(

	  'Content-Type' => 'application/json',

	  'Accept' => 'application/json',

	  'Authorization' => 'Bearer <TOKEN>'

	));

	$request->setBody('{\n  "name": "Mark Shoes",\n  "phone": "+1410039940",\n  "companyId": "UAXssdawIWAWD",\n  "address": "4th fleet street",\n  "city": "New York",\n  "state": "Illinois",\n  "country": "US",\n  "postalCode": "567654",\n  "website": "https://yourwebsite.com",\n  "timezone": "US/Central",\n  "prospectInfo": {\n    "firstName": "John",\n    "lastName": "Doe",\n    "email": "john.doe@mail.com"\n  },\n  "settings": {\n    "allowDuplicateContact": false,\n    "allowDuplicateOpportunity": false,\n    "allowFacebookNameMerge": false,\n    "disableContactTimezone": false\n  },\n  "social": {\n    "facebookUrl": "https://www.facebook.com/",\n    "googlePlus": "https://www.googleplus.com/",\n    "linkedIn": "https://www.linkedIn.com/",\n    "foursquare": "https://www.foursquare.com/",\n    "twitter": "https://www.foutwitterrsquare.com/",\n    "yelp": "https://www.yelp.com/",\n    "instagram": "https://www.instagram.com/",\n    "youtube": "https://www.youtube.com/",\n    "pinterest": "https://www.pinterest.com/",\n    "blogRss": "https://www.blogRss.com/",\n    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"\n  },\n  "mailgun": {\n    "apiKey": "key-XXXXXXXXXXX",\n    "domain": "replies.yourdomain.com"\n  },\n  "snapshotId": "XXXXXXXXXXX"\n}');

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

	$request->setRequestUrl('https://services.leadconnectorhq.com/locations/');

	$request->setRequestMethod('POST');

	$body = new http\Message\Body;

	$body->append('{

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

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

	RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Mark Shoes\",\n  \"phone\": \"+1410039940\",\n  \"companyId\": \"UAXssdawIWAWD\",\n  \"address\": \"4th fleet street\",\n  \"city\": \"New York\",\n  \"state\": \"Illinois\",\n  \"country\": \"US\",\n  \"postalCode\": \"567654\",\n  \"website\": \"https://yourwebsite.com\",\n  \"timezone\": \"US/Central\",\n  \"prospectInfo\": {\n    \"firstName\": \"John\",\n    \"lastName\": \"Doe\",\n    \"email\": \"john.doe@mail.com\"\n  },\n  \"settings\": {\n    \"allowDuplicateContact\": false,\n    \"allowDuplicateOpportunity\": false,\n    \"allowFacebookNameMerge\": false,\n    \"disableContactTimezone\": false\n  },\n  \"social\": {\n    \"facebookUrl\": \"https://www.facebook.com/\",\n    \"googlePlus\": \"https://www.googleplus.com/\",\n    \"linkedIn\": \"https://www.linkedIn.com/\",\n    \"foursquare\": \"https://www.foursquare.com/\",\n    \"twitter\": \"https://www.foutwitterrsquare.com/\",\n    \"yelp\": \"https://www.yelp.com/\",\n    \"instagram\": \"https://www.instagram.com/\",\n    \"youtube\": \"https://www.youtube.com/\",\n    \"pinterest\": \"https://www.pinterest.com/\",\n    \"blogRss\": \"https://www.blogRss.com/\",\n    \"googlePlacesId\": \"ChIJJGPdVbQTrjsRGUkefteUeFk\"\n  },\n  \"mailgun\": {\n    \"apiKey\": \"key-XXXXXXXXXXX\",\n    \"domain\": \"replies.yourdomain.com\"\n  },\n  \"snapshotId\": \"XXXXXXXXXXX\"\n}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/locations/")

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

	HttpResponse<String> response = Unirest.post("https://services.leadconnectorhq.com/locations/")

	  .header("Content-Type", "application/json")

	  .header("Accept", "application/json")

	  .header("Authorization", "Bearer <TOKEN>")

	  .body("{\n  \"name\": \"Mark Shoes\",\n  \"phone\": \"+1410039940\",\n  \"companyId\": \"UAXssdawIWAWD\",\n  \"address\": \"4th fleet street\",\n  \"city\": \"New York\",\n  \"state\": \"Illinois\",\n  \"country\": \"US\",\n  \"postalCode\": \"567654\",\n  \"website\": \"https://yourwebsite.com\",\n  \"timezone\": \"US/Central\",\n  \"prospectInfo\": {\n    \"firstName\": \"John\",\n    \"lastName\": \"Doe\",\n    \"email\": \"john.doe@mail.com\"\n  },\n  \"settings\": {\n    \"allowDuplicateContact\": false,\n    \"allowDuplicateOpportunity\": false,\n    \"allowFacebookNameMerge\": false,\n    \"disableContactTimezone\": false\n  },\n  \"social\": {\n    \"facebookUrl\": \"https://www.facebook.com/\",\n    \"googlePlus\": \"https://www.googleplus.com/\",\n    \"linkedIn\": \"https://www.linkedIn.com/\",\n    \"foursquare\": \"https://www.foursquare.com/\",\n    \"twitter\": \"https://www.foutwitterrsquare.com/\",\n    \"yelp\": \"https://www.yelp.com/\",\n    \"instagram\": \"https://www.instagram.com/\",\n    \"youtube\": \"https://www.youtube.com/\",\n    \"pinterest\": \"https://www.pinterest.com/\",\n    \"blogRss\": \"https://www.blogRss.com/\",\n    \"googlePlacesId\": \"ChIJJGPdVbQTrjsRGUkefteUeFk\"\n  },\n  \"mailgun\": {\n    \"apiKey\": \"key-XXXXXXXXXXX\",\n    \"domain\": \"replies.yourdomain.com\"\n  },\n  \"snapshotId\": \"XXXXXXXXXXX\"\n}")

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

	

	  url := "https://services.leadconnectorhq.com/locations/"

	  method := "POST"

	

	  payload := strings.NewReader(`{

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

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

	

	url = URI("https://services.leadconnectorhq.com/locations/")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Accept"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({

	  "name": "Mark Shoes",

	  "phone": "+1410039940",

	  "companyId": "UAXssdawIWAWD",

	  "address": "4th fleet street",

	  "city": "New York",

	  "state": "Illinois",

	  "country": "US",

	  "postalCode": "567654",

	  "website": "https://yourwebsite.com",

	  "timezone": "US/Central",

	  "prospectInfo": {

	    "firstName": "John",

	    "lastName": "Doe",

	    "email": "john.doe@mail.com"

	  },

	  "settings": {

	    "allowDuplicateContact": false,

	    "allowDuplicateOpportunity": false,

	    "allowFacebookNameMerge": false,

	    "disableContactTimezone": false

	  },

	  "social": {

	    "facebookUrl": "https://www.facebook.com/",

	    "googlePlus": "https://www.googleplus.com/",

	    "linkedIn": "https://www.linkedIn.com/",

	    "foursquare": "https://www.foursquare.com/",

	    "twitter": "https://www.foutwitterrsquare.com/",

	    "yelp": "https://www.yelp.com/",

	    "instagram": "https://www.instagram.com/",

	    "youtube": "https://www.youtube.com/",

	    "pinterest": "https://www.pinterest.com/",

	    "blogRss": "https://www.blogRss.com/",

	    "googlePlacesId": "ChIJJGPdVbQTrjsRGUkefteUeFk"

	  },

	  "mailgun": {

	    "apiKey": "key-XXXXXXXXXXX",

	    "domain": "replies.yourdomain.com"

	  },

	  "snapshotId": "XXXXXXXXXXX"

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

	  `"name`": `"Mark Shoes`",

	  `"phone`": `"+1410039940`",

	  `"companyId`": `"UAXssdawIWAWD`",

	  `"address`": `"4th fleet street`",

	  `"city`": `"New York`",

	  `"state`": `"Illinois`",

	  `"country`": `"US`",

	  `"postalCode`": `"567654`",

	  `"website`": `"https://yourwebsite.com`",

	  `"timezone`": `"US/Central`",

	  `"prospectInfo`": {

	    `"firstName`": `"John`",

	    `"lastName`": `"Doe`",

	    `"email`": `"john.doe@mail.com`"

	  },

	  `"settings`": {

	    `"allowDuplicateContact`": false,

	    `"allowDuplicateOpportunity`": false,

	    `"allowFacebookNameMerge`": false,

	    `"disableContactTimezone`": false

	  },

	  `"social`": {

	    `"facebookUrl`": `"https://www.facebook.com/`",

	    `"googlePlus`": `"https://www.googleplus.com/`",

	    `"linkedIn`": `"https://www.linkedIn.com/`",

	    `"foursquare`": `"https://www.foursquare.com/`",

	    `"twitter`": `"https://www.foutwitterrsquare.com/`",

	    `"yelp`": `"https://www.yelp.com/`",

	    `"instagram`": `"https://www.instagram.com/`",

	    `"youtube`": `"https://www.youtube.com/`",

	    `"pinterest`": `"https://www.pinterest.com/`",

	    `"blogRss`": `"https://www.blogRss.com/`",

	    `"googlePlacesId`": `"ChIJJGPdVbQTrjsRGUkefteUeFk`"

	  },

	  `"mailgun`": {

	    `"apiKey`": `"key-XXXXXXXXXXX`",

	    `"domain`": `"replies.yourdomain.com`"

	  },

	  `"snapshotId`": `"XXXXXXXXXXX`"

	}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/locations/' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

