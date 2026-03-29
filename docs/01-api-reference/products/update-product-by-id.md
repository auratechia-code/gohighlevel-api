# Update Product by ID

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | PUT |
| **Endpoint URL** | `https://services.leadconnectorhq.com/products/:productId` |
| **Scopes Required** | `products.write` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **productId** | `` | No |  |

### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **name** | `string` | No |  |
| **locationId** | `string` | No |  |
| **description** | `string` | No |  |
| **productType** | `string` | No |  |
| **image** | `string` | No |  |
| **statementDescriptor** | `string` | No |  |
| **availableInStore** | `boolean` | No |  |
| **medias** | `object[]` | Yes | An array of medias for the product. Array [ id string required The unique identifier for the media. Example: fzrgusiuu0m title string The title of the media file. Example: 1dd7dcd0-e71d-4cf7-a06b-6d47723d6a29.png url string required The URL where the media file is stored. Example: https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/sample.png type string required The type of the media file (e.g., image, video will be supporting soon). Possible values: [ image , video ] Example: image isFeatured boolean Indicates whether the media is featured. Example: true priceIds array[] Mongo ObjectIds of the prices for which the media is assigned Example: 6578278e879ad2646715ba9c ] |
| **id** | `string` | No |  |
| **title** | `string` | No |  |
| **url** | `string` | No |  |
| **type** | `string` | No |  |
| **isFeatured** | `boolean` | No |  |
| **priceIds** | `array[]` | No |  |
| **variants** | `object[]` | Yes | An array of variants for the product. Array [ id string required A unique identifier for the variant. Example: 38s63qmxfr4 name string required The name of the variant. Example: Size options object[] required An array of options for the variant. Array [ id string required The unique identifier for the option. Example: h4z7u0im2q8 name string required The name of the option. Example: XL ] ] |
| **id** | `string` | No |  |
| **name** | `string` | No |  |
| **options** | `object[]` | Yes | An array of options for the variant. Array [ id string required The unique identifier for the option. Example: h4z7u0im2q8 name string required The name of the option. Example: XL ] |
| **id** | `string` | No |  |
| **name** | `string` | No |  |
| **collectionIds** | `string[]` | No |  |
| **isTaxesEnabled** | `boolean` | No |  |
| **taxes** | `string[]` | No |  |
| **automaticTaxCategoryId** | `string` | No |  |
| **isLabelEnabled** | `boolean` | No |  |
| **label** | `object` | Yes | Details for Product Label title string required The content for the product label. Example: Featured startDate string Start date in YYYY-MM-DDTHH:mm:ssZ format Example: 2024-06-26T05:43:35.000Z endDate string Start date in YYYY-MM-DDTHH:mm:ssZ format Example: 2024-06-30T05:43:39.000Z |
| **title** | `string` | No |  |
| **startDate** | `string` | No |  |
| **endDate** | `string` | No |  |
| **slug** | `string` | No |  |
| **seo** | `object` | No | SEO data for the product that will be displayed in the preview title string SEO title Example: Best Product - Buy Now description string SEO description Example: This is the best product you can buy online with amazing features and great value |
| **title** | `string` | No |  |
| **description** | `string` | No |  |
| **taxInclusive** | `boolean` | No |  |
| **prices** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "_id": "655b33a82209e60b6adb87a5",
  "description": "This is a really awesome product",
  "variants": [
    {
      "id": "38s63qmxfr4",
      "name": "Size",
      "options": [
        {
          "id": "h4z7u0im2q8",
          "name": "XL"
        }
      ]
    }
  ],
  "locationId": "3SwdhCsvxI8Au3KsPJt6",
  "name": "Awesome Product",
  "productType": "PHYSICAL",
  "availableInStore": true,
  "createdAt": "2023-11-20T10:23:36.515Z",
  "updatedAt": "2024-01-23T09:57:04.846Z",
  "statementDescriptor": "abcde",
  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",
  "collectionIds": [
    "65d71377c326ea78e1c47df5",
    "65d71377c326ea78e1c47d34"
  ],
  "isTaxesEnabled": true,
  "taxes": [
    "654492a4e6bef380114de15a"
  ],
  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",
  "label": {
    "title": "Featured",
    "startDate": "2024-06-26T05:43:35.000Z",
    "endDate": "2024-06-30T05:43:39.000Z"
  },
  "slug": "washing-machine"
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **description** | `str` |  |
| **variants** | `list` |  |
| **locationId** | `str` |  |
| **name** | `str` |  |
| **productType** | `str` |  |
| **availableInStore** | `bool` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |
| **statementDescriptor** | `str` |  |
| **image** | `str` |  |
| **collectionIds** | `list` |  |
| **isTaxesEnabled** | `bool` |  |
| **taxes** | `list` |  |
| **automaticTaxCategoryId** | `str` |  |
| **label** | `dict` |  |
| **slug** | `str` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/products/:productId \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}'
```

### 2. NODE SDK

```javascript
const { HighLevel } = require('@gohighlevel/api-client');

const ghl = new HighLevel({
  clientId: 'YOUR_CLIENT_ID',
  clientSecret: 'YOUR_CLIENT_SECRET'
});

async function executeRequest() {
  try {
    const response = await ghl.api.request('PUT', 'https://services.leadconnectorhq.com/products/:productId', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}
    });
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

### 3. AXIOS

```javascript
const axios = require('axios');

const config = {
  method: 'put',
  url: 'https://services.leadconnectorhq.com/products/:productId',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}
};

axios(config)
.then(response => console.log(JSON.stringify(response.data)))
.catch(error => console.log(error));
```

### 4. NATIVE NODE

```javascript
const https = require('follow-redirects').https;

const options = {
  'method': 'PUT',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/products/:productId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
};

const req = https.request(options, (res) => {
  let chunks = [];
  res.on("data", (chunk) => chunks.push(chunk));
  res.on("end", () => console.log(Buffer.concat(chunks).toString()));
});

req.write(JSON.stringify({
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'PUT',
  'url': 'https://services.leadconnectorhq.com/products/:productId',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
})
};

request(options, (error, response) => {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

### 6. UNIREST NODE

```javascript
const unirest = require('unirest');

unirest('PUT', 'https://services.leadconnectorhq.com/products/:productId')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/products/:productId"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("PUT", url, headers=headers, data=json.dumps({
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}))
print(response.text)
```

### 8. PHP

```php
<?php
use GuzzleHttp\Client;
$client = new Client();
$headers = [
  'Authorization' => 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version' => '2021-07-28',
  'Content-Type' => 'application/json'
];
$response = $client->request('PUT', 'https://services.leadconnectorhq.com/products/:productId', [
  'headers' => $headers,
  'body' => '{
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}'
]);
echo $response->getBody();
```

### 9. JAVA

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://services.leadconnectorhq.com/products/:productId"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("PUT", HttpRequest.BodyPublishers.ofString("{
  \"name\": \"string\",
  \"locationId\": \"string\",
  \"description\": \"string\",
  \"productType\": \"string\",
  \"image\": \"string\",
  \"statementDescriptor\": \"string\",
  \"availableInStore\": true,
  \"medias\": \"string\",
  \"id\": \"string\",
  \"title\": \"string\",
  \"url\": \"string\",
  \"type\": \"string\",
  \"isFeatured\": true,
  \"priceIds\": \"string\",
  \"variants\": \"string\",
  \"options\": \"string\",
  \"collectionIds\": \"string\",
  \"isTaxesEnabled\": true,
  \"taxes\": \"string\",
  \"automaticTaxCategoryId\": \"string\",
  \"isLabelEnabled\": true,
  \"label\": \"string\",
  \"startDate\": \"string\",
  \"endDate\": \"string\",
  \"slug\": \"string\",
  \"seo\": \"string\",
  \"taxInclusive\": true,
  \"prices\": \"string\"
}"))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

### 10. GO

```go
package main
import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)
func main() {
  url := "https://services.leadconnectorhq.com/products/:productId"
  payload := strings.NewReader(`{
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}`)
  req, _ := http.NewRequest("PUT", url, payload)
  req.Header.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
  req.Header.Add("Version", "2021-07-28")
  req.Header.Add("Content-Type", "application/json")
  res, _ := http.DefaultClient.Do(req)
  defer res.Body.Close()
  body, _ := ioutil.ReadAll(res.Body)
  fmt.Println(string(body))
}
```

### 11. RUBY

```ruby
require 'net/http'
require 'uri'
require 'json'

url = URI("https://services.leadconnectorhq.com/products/:productId")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Put.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
})
response = http.request(request)
puts response.read_body
```

### 12. POWERSHELL

```powershell
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$headers.Add("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
$headers.Add("Version", "2021-07-28")
$headers.Add("Content-Type", "application/json")

$body = '{
  "name": "string",
  "locationId": "string",
  "description": "string",
  "productType": "string",
  "image": "string",
  "statementDescriptor": "string",
  "availableInStore": true,
  "medias": "string",
  "id": "string",
  "title": "string",
  "url": "string",
  "type": "string",
  "isFeatured": true,
  "priceIds": "string",
  "variants": "string",
  "options": "string",
  "collectionIds": "string",
  "isTaxesEnabled": true,
  "taxes": "string",
  "automaticTaxCategoryId": "string",
  "isLabelEnabled": true,
  "label": "string",
  "startDate": "string",
  "endDate": "string",
  "slug": "string",
  "seo": "string",
  "taxInclusive": true,
  "prices": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/:productId' -Method 'PUT' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
