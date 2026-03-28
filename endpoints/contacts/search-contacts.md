---
title: "Search Contacts"
source: "https://marketplace.gohighlevel.com/docs/ghl/contacts/search-contacts-advanced"
generated_at: "2026-03-28T17:50:27.468803"
tags: ["api", "endpoint", "POST"]
---

# Search Contacts

Search contacts based on combinations of advanced filters. Documentation Link -https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
	curl -L 'https://services.leadconnectorhq.com/contacts/search' \

	-H 'Content-Type: application/json' \

	-H 'Authorization: Bearer <TOKEN>' \

	-d '{}'

```

#### NODEJS
```javascript
	const { HighLevel } = require('@gohighlevel/api-client');

	

	const highLevel = new HighLevel({

	  clientId: 'your_client_id_here',

	  clientSecret: 'your_client_secret_here',

	});

	

	try {

	  const response = await highLevel.contacts.searchContactsAdvanced();

	  console.log(response);

	} catch (error) {

	  console.error('Error:', error);

	}

```

#### PYTHON
```python
	import http.client

	import json

	

	conn = http.client.HTTPSConnection("services.leadconnectorhq.com")

	payload = json.dumps({})

	headers = {

	  'Content-Type': 'application/json',

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("POST", "/contacts/search", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### PHP
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/contacts/search',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'POST',

	  CURLOPT_POSTFIELDS =>'{}',

	  CURLOPT_HTTPHEADER => array(

	    'Content-Type: application/json',

	    'Authorization: Bearer <TOKEN>'

	  ),

	));

	

	$response = curl_exec($curl);

	

	curl_close($curl);

	echo $response;

```

#### JAVA
```java
	OkHttpClient client = new OkHttpClient().newBuilder()

	  .build();

	MediaType mediaType = MediaType.parse("application/json");

	RequestBody body = RequestBody.create(mediaType, "{}");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/contacts/search")

	  .method("POST", body)

	  .addHeader("Content-Type", "application/json")

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### GO
```go
	package main

	

	import (

	  "fmt"

	  "strings"

	  "net/http"

	  "io"

	)

	

	func main() {

	

	  url := "https://services.leadconnectorhq.com/contacts/search"

	  method := "POST"

	

	  payload := strings.NewReader(`{}`)

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, payload)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

	  req.Header.Add("Content-Type", "application/json")

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

#### RUBY
```ruby
	require "uri"

	require "json"

	require "net/http"

	

	url = URI("https://services.leadconnectorhq.com/contacts/search")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Post.new(url)

	request["Content-Type"] = "application/json"

	request["Authorization"] = "Bearer <TOKEN>"

	request.body = JSON.dump({})

	

	response = https.request(request)

	puts response.read_body

```

#### POWERSHELL
```powershell
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"

	$headers.Add("Content-Type", "application/json")

	$headers.Add("Authorization", "Bearer <TOKEN>")

	

	$body = @"

	{}

	"@

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/contacts/search' -Method 'POST' -Headers $headers -Body $body

	$response | ConvertTo-Json

```

