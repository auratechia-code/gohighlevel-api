# Create Price for a Product

---

## 1. METADATA

| Property | Value |
| :--- | :--- |
| **HTTP Method** | POST |
| **Endpoint URL** | `https://services.leadconnectorhq.com/products/:productId/price` |
| **Scopes Required** | `products/prices.write` |
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
| **type** | `string` | No |  |
| **currency** | `string` | No |  |
| **amount** | `number` | No |  |
| **recurring** | `object` | Yes | The recurring details of the price (if type is recurring). interval string required The interval at which the recurring event occurs. Possible values: [ day , month , week , year ] Example: day intervalCount number required The number of intervals between each occurrence of the event. Example: 1 |
| **interval** | `string` | No |  |
| **intervalCount** | `number` | No |  |
| **description** | `string` | No |  |
| **membershipOffers** | `object[]` | Yes | An array of membership offers associated with the price. Array [ label string required Membership offer label Example: top_50 value string required Membership offer label Example: 50 _id string required The unique identifier for the membership offer. Example: 655b33aa2209e60b6adb87a7 ] |
| **label** | `string` | No |  |
| **value** | `string` | No |  |
| **_id** | `string` | No |  |
| **trialPeriod** | `number` | No |  |
| **totalCycles** | `number` | No |  |
| **setupFee** | `number` | No |  |
| **variantOptionIds** | `string[]` | No |  |
| **compareAtPrice** | `number` | No |  |
| **locationId** | `string` | No |  |
| **userId** | `string` | No |  |
| **meta** | `object` | Yes | Additional metadata associated with the price. source string required The source of the price. Possible values: [ stripe , woocommerce , shopify ] Example: stripe sourceId string The id of the source of the price from where it is imported Example: 123 stripePriceId string required The Stripe price ID associated with the price. Example: price_123 internalSource string required The internal source of the price. Possible values: [ agency_plan , funnel , membership , communities , gokollab , calendar ] Example: agency_plan |
| **source** | `string` | No |  |
| **sourceId** | `string` | No |  |
| **stripePriceId** | `string` | No |  |
| **internalSource** | `string` | No |  |
| **trackInventory** | `boolean` | No |  |
| **availableQuantity** | `number` | No |  |
| **allowOutOfStockPurchases** | `boolean` | No |  |
| **sku** | `string` | No |  |
| **shippingOptions** | `object` | Yes | Shipping options of the Price weight object Weight options of the product value number required Actual weight of the product Example: 10 unit string required Weight unit of the product Possible values: [ kg , lb , g , oz ] Example: kg dimensions object Dimensions of the product height number required Height of the price Example: 10 width number required Width of the price Example: 10 length number required Length of the price Example: 10 unit string required Unit of the price dimensions Possible values: [ cm , in , m ] Example: cm |
| **weight** | `object` | Yes | Weight options of the product value number required Actual weight of the product Example: 10 unit string required Weight unit of the product Possible values: [ kg , lb , g , oz ] Example: kg |
| **value** | `number` | No |  |
| **unit** | `string` | No |  |
| **dimensions** | `object` | Yes | Dimensions of the product height number required Height of the price Example: 10 width number required Width of the price Example: 10 length number required Length of the price Example: 10 unit string required Unit of the price dimensions Possible values: [ cm , in , m ] Example: cm |
| **height** | `number` | No |  |
| **width** | `number` | No |  |
| **length** | `number` | No |  |
| **unit** | `string` | No |  |
| **isDigitalProduct** | `boolean` | No |  |
| **digitalDelivery** | `string[]` | No |  |

---

## 3. RESPONSE

### Success Schema (200/201 OK)

```json
{
  "_id": "655b33aa2209e60b6adb87a7",
  "membershipOffers": [
    {
      "label": "top_50",
      "value": "50",
      "_id": "655b33aa2209e60b6adb87a7"
    }
  ],
  "variantOptionIds": [
    "h4z7u0im2q8",
    "h3nst2ltsnn"
  ],
  "locationId": "3SwdhCsvxI8Au3KsPJt6",
  "product": "655b33a82209e60b6adb87a5",
  "userId": "6YAtzfzpmHAdj0e8GkKp",
  "name": "Red / S",
  "type": "one_time",
  "currency": "INR",
  "amount": 199999,
  "recurring": {
    "interval": "day",
    "intervalCount": 1
  },
  "createdAt": "2023-11-20T10:23:38.645Z",
  "updatedAt": "2024-01-23T09:57:04.852Z",
  "compareAtPrice": 2000000,
  "trackInventory": null,
  "availableQuantity": 5,
  "allowOutOfStockPurchases": true
}
```

### Response Field Table

| Name | Type | Description |
| :--- | :--- | :--- |
| **_id** | `str` |  |
| **membershipOffers** | `list` |  |
| **variantOptionIds** | `list` |  |
| **locationId** | `str` |  |
| **product** | `str` |  |
| **userId** | `str` |  |
| **name** | `str` |  |
| **type** | `str` |  |
| **currency** | `str` |  |
| **amount** | `int` |  |
| **recurring** | `dict` |  |
| **createdAt** | `str` |  |
| **updatedAt** | `str` |  |
| **compareAtPrice** | `int` |  |
| **trackInventory** | `NoneType` |  |
| **availableQuantity** | `int` |  |
| **allowOutOfStockPurchases** | `bool` |  |

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
  --url https://services.leadconnectorhq.com/products/:productId/price \
  --header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --data '{
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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
    const response = await ghl.api.request('POST', 'https://services.leadconnectorhq.com/products/:productId/price', {
      headers: { 'Version': '2021-07-28' },
      body: {
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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
  url: 'https://services.leadconnectorhq.com/products/:productId/price',
  headers: { 
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>', 
    'Version': '2021-07-28', 
    'Content-Type': 'application/json', 
    'Accept': 'application/json'
  },
  data : {
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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
  'path': '/products/:productId/price',
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
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
}));
req.end();
```

### 5. REQUEST NODE

```javascript
const request = require('request');

const options = {
  'method': 'POST',
  'url': 'https://services.leadconnectorhq.com/products/:productId/price',
  'headers': {
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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

unirest('POST', 'https://services.leadconnectorhq.com/products/:productId/price')
  .headers({
    'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
    'Version': '2021-07-28',
    'Content-Type': 'application/json'
  })
  .send(JSON.stringify({
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
}))
  .end(res => console.log(res.raw_body));
```

### 7. PYTHON

```python
import requests
import json

url = "https://services.leadconnectorhq.com/products/:productId/price"
headers = {
  'Authorization': 'Bearer <YOUR_ACCESS_TOKEN>',
  'Version': '2021-07-28',
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=json.dumps({
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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
$response = $client->request('POST', 'https://services.leadconnectorhq.com/products/:productId/price', [
  'headers' => $headers,
  'body' => '{
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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
    .uri(URI.create("https://services.leadconnectorhq.com/products/:productId/price"))
    .header("Authorization", "Bearer <YOUR_ACCESS_TOKEN>")
    .header("Version", "2021-07-28")
    .header("Content-Type", "application/json")
    .method("POST", HttpRequest.BodyPublishers.ofString("{
  \"name\": \"string\",
  \"type\": \"string\",
  \"currency\": \"string\",
  \"amount\": 123,
  \"recurring\": \"string\",
  \"interval\": \"string\",
  \"intervalCount\": 123,
  \"description\": \"string\",
  \"membershipOffers\": \"string\",
  \"label\": \"string\",
  \"value\": 123,
  \"_id\": \"string\",
  \"trialPeriod\": 123,
  \"totalCycles\": 123,
  \"setupFee\": 123,
  \"variantOptionIds\": \"string\",
  \"compareAtPrice\": 123,
  \"locationId\": \"string\",
  \"userId\": \"string\",
  \"meta\": \"string\",
  \"source\": \"string\",
  \"sourceId\": \"string\",
  \"stripePriceId\": \"string\",
  \"internalSource\": \"string\",
  \"trackInventory\": true,
  \"availableQuantity\": 123,
  \"allowOutOfStockPurchases\": true,
  \"sku\": \"string\",
  \"shippingOptions\": \"string\",
  \"weight\": \"string\",
  \"unit\": \"string\",
  \"dimensions\": \"string\",
  \"height\": 123,
  \"width\": 123,
  \"length\": 123,
  \"isDigitalProduct\": true,
  \"digitalDelivery\": \"string\"
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
  url := "https://services.leadconnectorhq.com/products/:productId/price"
  payload := strings.NewReader(`{
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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

url = URI("https://services.leadconnectorhq.com/products/:productId/price")
http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true
request = Net::HTTP::Post.new(url)
request["Authorization"] = "Bearer <YOUR_ACCESS_TOKEN>"
request["Version"] = "2021-07-28"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "string",
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
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
  "type": "string",
  "currency": "string",
  "amount": 123,
  "recurring": "string",
  "interval": "string",
  "intervalCount": 123,
  "description": "string",
  "membershipOffers": "string",
  "label": "string",
  "value": 123,
  "_id": "string",
  "trialPeriod": 123,
  "totalCycles": 123,
  "setupFee": 123,
  "variantOptionIds": "string",
  "compareAtPrice": 123,
  "locationId": "string",
  "userId": "string",
  "meta": "string",
  "source": "string",
  "sourceId": "string",
  "stripePriceId": "string",
  "internalSource": "string",
  "trackInventory": true,
  "availableQuantity": 123,
  "allowOutOfStockPurchases": true,
  "sku": "string",
  "shippingOptions": "string",
  "weight": "string",
  "unit": "string",
  "dimensions": "string",
  "height": 123,
  "width": 123,
  "length": 123,
  "isDigitalProduct": true,
  "digitalDelivery": "string"
}'

$response = Invoke-RestMethod 'https://services.leadconnectorhq.com/products/:productId/price' -Method 'POST' -Headers $headers -Body $body
$response | ConvertTo-Json
```

---

## 5. NOTES

- Ensure the `Version: 2021-07-28` header is included.
