# Bulk Edit Products and Prices

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/products/bulk-update/edit` |
| **Scopes Required** | `N/A` |
| **Authentication** | OAuth Access Token / Private Integration Token |
| **Token Type** | Sub-Account Token |

---

## 2. REQUEST

### Header Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **Version** | `` | No |  |

### Path Parameters

N/A
### Query Parameters

N/A
### Body Parameters

| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **altId** | `string` | No |  |
| **altType** | `string` | No |  |
| **products** | `object[]` | Yes | Array of products to update. Note: The total count includes all prices within each product. Array [ _id string required Product ID Example: 64a1b2c3d4e5f67890123456 name string Product name Example: Premium Product description string Product description Example: A high-quality premium product with excellent features and durability image string Product image Example: https://example.com/product-image.jpg availableInStore boolean Product availability in store Example: true prices object[] Array of price variants for the product Array [ _id string required Price ID Example: 64a1b2c3d4e5f67890123456 name string Price name Example: Standard Plan amount number Price amount Example: 99.99 currency string Price currency Example: USD compareAtPrice number Compare at price Example: 129.99 availableQuantity number Available quantity Example: 100 trackInventory boolean Track inventory Example: true allowOutOfStockPurchases boolean Allow out of stock purchases Example: false sku string SKU Example: SKU-001 trialPeriod number Trial period in days Example: 7 totalCycles number Total billing cycles Example: 12 setupFee number Setup fee Example: 25 shippingOptions object Shipping options weight object Weight options of the product value number required Actual weight of the product Example: 10 unit string required Weight unit of the product Possible values: [ kg , lb , g , oz ] Example: kg dimensions object Dimensions of the product height number required Height of the price Example: 10 width number required Width of the price Example: 10 length number required Length of the price Example: 10 unit string required Unit of the price dimensions Possible values: [ cm , in , m ] Example: cm recurring object Recurring details interval string required The interval at which the recurring event occurs. Possible values: [ day , month , week , year ] Example: day intervalCount number required The number of intervals between each occurrence of the event. Example: 1 ] collectionIds string[] Collection IDs Example: ["64a1b2c3d4e5f67890123458","64a1b2c3d4e5f67890123459"] isLabelEnabled boolean Enable product label Example: true isTaxesEnabled boolean Enable taxes Example: true seo object SEO metadata for the product title string SEO title Example: Best Product - Buy Now description string SEO description Example: This is the best product you can buy online with amazing features and great value slug string Product URL slug Example: premium-product automaticTaxCategoryId string Automatic tax category ID Example: 64a1b2c3d4e5f67890123460 taxInclusive boolean Tax inclusive pricing Example: false taxes object[] Product taxes medias object[] Product media label object Product label ] |
| **_id** | `string` | No |  |
| **name** | `string` | No |  |
| **description** | `string` | No |  |
| **image** | `string` | No |  |
| **availableInStore** | `boolean` | No |  |
| **prices** | `object[]` | Yes | Array of price variants for the product Array [ _id string required Price ID Example: 64a1b2c3d4e5f67890123456 name string Price name Example: Standard Plan amount number Price amount Example: 99.99 currency string Price currency Example: USD compareAtPrice number Compare at price Example: 129.99 availableQuantity number Available quantity Example: 100 trackInventory boolean Track inventory Example: true allowOutOfStockPurchases boolean Allow out of stock purchases Example: false sku string SKU Example: SKU-001 trialPeriod number Trial period in days Example: 7 totalCycles number Total billing cycles Example: 12 setupFee number Setup fee Example: 25 shippingOptions object Shipping options weight object Weight options of the product value number required Actual weight of the product Example: 10 unit string required Weight unit of the product Possible values: [ kg , lb , g , oz ] Example: kg dimensions object Dimensions of the product height number required Height of the price Example: 10 width number required Width of the price Example: 10 length number required Length of the price Example: 10 unit string required Unit of the price dimensions Possible values: [ cm , in , m ] Example: cm recurring object Recurring details interval string required The interval at which the recurring event occurs. Possible values: [ day , month , week , year ] Example: day intervalCount number required The number of intervals between each occurrence of the event. Example: 1 ] |
| **_id** | `string` | No |  |
| **name** | `string` | No |  |
| **amount** | `number` | No |  |
| **currency** | `string` | No |  |
| **compareAtPrice** | `number` | No |  |
| **availableQuantity** | `number` | No |  |
| **trackInventory** | `boolean` | No |  |
| **allowOutOfStockPurchases** | `boolean` | No |  |
| **sku** | `string` | No |  |
| **trialPeriod** | `number` | No |  |
| **totalCycles** | `number` | No |  |
| **setupFee** | `number` | No |  |
| **shippingOptions** | `object` | Yes | Shipping options weight object Weight options of the product value number required Actual weight of the product Example: 10 unit string required Weight unit of the product Possible values: [ kg , lb , g , oz ] Example: kg dimensions object Dimensions of the product height number required Height of the price Example: 10 width number required Width of the price Example: 10 length number required Length of the price Example: 10 unit string required Unit of the price dimensions Possible values: [ cm , in , m ] Example: cm |
| **weight** | `object` | Yes | Weight options of the product value number required Actual weight of the product Example: 10 unit string required Weight unit of the product Possible values: [ kg , lb , g , oz ] Example: kg |
| **value** | `number` | No |  |
| **unit** | `string` | No |  |
| **dimensions** | `object` | Yes | Dimensions of the product height number required Height of the price Example: 10 width number required Width of the price Example: 10 length number required Length of the price Example: 10 unit string required Unit of the price dimensions Possible values: [ cm , in , m ] Example: cm |
| **height** | `number` | No |  |
| **width** | `number` | No |  |
| **length** | `number` | No |  |
| **unit** | `string` | No |  |
| **recurring** | `object` | Yes | Recurring details interval string required The interval at which the recurring event occurs. Possible values: [ day , month , week , year ] Example: day intervalCount number required The number of intervals between each occurrence of the event. Example: 1 |
| **interval** | `string` | No |  |
| **intervalCount** | `number` | No |  |
| **collectionIds** | `string[]` | No |  |
| **isLabelEnabled** | `boolean` | No |  |
| **isTaxesEnabled** | `boolean` | No |  |
| **seo** | `object` | No | SEO metadata for the product title string SEO title Example: Best Product - Buy Now description string SEO description Example: This is the best product you can buy online with amazing features and great value |
| **title** | `string` | No |  |
| **description** | `string` | No |  |
| **slug** | `string` | No |  |
| **automaticTaxCategoryId** | `string` | No |  |
| **taxInclusive** | `boolean` | No |  |
| **taxes** | `object[]` | No |  |
| **medias** | `object[]` | No |  |
| **label** | `object` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "message": "Products updated successfully",
  "status": true,
  "updatedCount": 5
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **message** | `str` |  |
| **status** | `bool` |  |
| **updatedCount** | `int` |  |

### Error Codes

| Status Code | Description |
| :--- | :--- |
| **400 Bad Request** | Invalid input parameters. |
| **401 Unauthorized** | Invalid Token. |

---

## 4. CODE EXAMPLES

### 1. CURL

```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/products/bulk-update/edit \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/products/bulk-update/edit', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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
  method: 'post',
  url: 'https://services.leadconnectorhq.com/products/bulk-update/edit',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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
  'method': 'POST',
  'hostname': 'services.leadconnectorhq.com',
  'path': '/products/bulk-update/edit',
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
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/products/bulk-update/edit',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/products/bulk-update/edit')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/products/bulk-update/edit"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/products/bulk-update/edit', [
  'headers' => $headers,
  'body' => '{
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/products/bulk-update/edit"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"altId\": \"string\",
  \"altType\": \"string\",
  \"products\": \"string\",
  \"_id\": \"string\",
  \"name\": \"string\",
  \"description\": \"string\",
  \"image\": \"string\",
  \"availableInStore\": true,
  \"prices\": \"string\",
  \"amount\": 123,
  \"currency\": \"string\",
  \"compareAtPrice\": 123,
  \"availableQuantity\": 123,
  \"trackInventory\": true,
  \"allowOutOfStockPurchases\": true,
  \"sku\": \"string\",
  \"trialPeriod\": 123,
  \"totalCycles\": 123,
  \"setupFee\": 123,
  \"shippingOptions\": \"string\",
  \"weight\": \"string\",
  \"value\": 123,
  \"unit\": \"string\",
  \"dimensions\": \"string\",
  \"height\": 123,
  \"width\": 123,
  \"length\": 123,
  \"recurring\": \"string\",
  \"interval\": \"string\",
  \"intervalCount\": 123,
  \"collectionIds\": \"string\",
  \"isLabelEnabled\": true,
  \"isTaxesEnabled\": true,
  \"seo\": \"string\",
  \"title\": \"string\",
  \"slug\": \"string\",
  \"automaticTaxCategoryId\": \"string\",
  \"taxInclusive\": true,
  \"taxes\": \"string\",
  \"medias\": \"string\",
  \"label\": \"string\"
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
  url := "https://services.leadconnectorhq.com/products/bulk-update/edit"
  payload := strings.NewReader(`{
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
}`)
  req, _ := http.NewRequest("POST", url, payload)
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

url = URI("https://services.leadconnectorhq.com/products/bulk-update/edit")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
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
  "altId": "string",
  "altType": "string",
  "products": "string",
  "_id": "string",
  "name": "string",
  "description": "string",
  "image": "string",
  "availableInStore": true,
  "prices": "string",
  "amount": 123,
  "currency": "string",
  "compareAtPrice": 123,
  "availableQuantity": 123,
  "trackInventory": true,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "shippingOptions": "string",
  "weight": "string",
  "value": 123,
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "collectionIds": "string",
  "isLabelEnabled": true,
  "isTaxesEnabled": true,
  "seo": "string",
  "title": "string",
  "slug": "string",
  "automaticTaxCategoryId": "string",
  "taxInclusive": true,
  "taxes": "string",
  "medias": "string",
  "label": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/bulk-update/edit' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
