---
title: "Delete File or Folder"
source: "https://marketplace.gohighlevel.com/docs/ghl/medias/delete-media-content"
generated_at: "2026-03-28T17:50:27.605079"
tags: ["api", "endpoint", "DELETE"]
---

# Delete File or Folder

Deletes specific file or folder from the media storage

## Endpoint Information

> [!IMPORTANT]
> **Method:** `DELETE`  
> **URL:** ``

## Code Examples

#### CURL
```curl
	curl -L -X DELETE 'https://services.leadconnectorhq.com/medias/:id' \

	-H 'Authorization: Bearer <TOKEN>'

```

#### NODEJS
```javascript
	const { HighLevel } = require('@gohighlevel/api-client');

	

	const highLevel = new HighLevel({

	  clientId: 'your_client_id_here',

	  clientSecret: 'your_client_secret_here',

	});

	

	try {

	  const response = await highLevel.medias.deleteMediaContent({

	    'id': 'id_value',

	    'altType': 'location',

	    'altId': 'altId_value'

	  });

	  console.log(response);

	} catch (error) {

	  console.error('Error:', error);

	}

```

#### PYTHON
```python
	import http.client

	

	conn = http.client.HTTPSConnection("services.leadconnectorhq.com")

	payload = ''

	headers = {

	  'Authorization': 'Bearer <TOKEN>'

	}

	conn.request("DELETE", "/medias/:id", payload, headers)

	res = conn.getresponse()

	data = res.read()

	print(data.decode("utf-8"))

```

#### PHP
```php
	<?php

	

	$curl = curl_init();

	

	curl_setopt_array($curl, array(

	  CURLOPT_URL => 'https://services.leadconnectorhq.com/medias/:id',

	  CURLOPT_RETURNTRANSFER => true,

	  CURLOPT_ENCODING => '',

	  CURLOPT_MAXREDIRS => 10,

	  CURLOPT_TIMEOUT => 0,

	  CURLOPT_FOLLOWLOCATION => true,

	  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

	  CURLOPT_CUSTOMREQUEST => 'DELETE',

	  CURLOPT_HTTPHEADER => array(

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

	MediaType mediaType = MediaType.parse("text/plain");

	RequestBody body = RequestBody.create(mediaType, "");

	Request request = new Request.Builder()

	  .url("https://services.leadconnectorhq.com/medias/:id")

	  .method("DELETE", body)

	  .addHeader("Authorization", "Bearer <TOKEN>")

	  .build();

	Response response = client.newCall(request).execute();

```

#### GO
```go
	package main

	

	import (

	  "fmt"

	  "net/http"

	  "io"

	)

	

	func main() {

	

	  url := "https://services.leadconnectorhq.com/medias/:id"

	  method := "DELETE"

	

	  client := &http.Client {

	  }

	  req, err := http.NewRequest(method, url, nil)

	

	  if err != nil {

	    fmt.Println(err)

	    return

	  }

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

	require "net/http"

	

	url = URI("https://services.leadconnectorhq.com/medias/:id")

	

	https = Net::HTTP.new(url.host, url.port)

	https.use_ssl = true

	

	request = Net::HTTP::Delete.new(url)

	request["Authorization"] = "Bearer <TOKEN>"

	

	response = https.request(request)

	puts response.read_body

```

#### POWERSHELL
```powershell
	$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"

	$headers.Add("Authorization", "Bearer <TOKEN>")

	

	$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/medias/:id' -Method 'DELETE' -Headers $headers

	$response | ConvertTo-Json

```

