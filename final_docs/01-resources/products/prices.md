# Products: Prices

Define pricing strategies, billing cycles, and currency for items in the catalog.

## 1. Price Configuration

### Create Price for Product
Attach a new pricing tier to an existing product.

- **Endpoint:** `POST /products/{productId}/prices`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/products/{productId}/prices \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/products/{productId}/prices',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/products/{productId}/prices"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("POST", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/products/{productId}/prices",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Method:** `POST`
- **Scopes:** `products.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | String | Yes | Public name for the price (e.g., "Monthly Plan"). |
| `type` | String | Yes | `one_time`, `recurring`. |
| `currency` | String | Yes | ISO currency code (e.g., `USD`, `EUR`). |
| `amount` | Number | Yes | Price amount in smallest currency unit (e.g., `1000` = $10.00). |
| `recurring`| Object | No | `{ "interval": "month", "intervalCount": 1 }`. Required if type is `recurring`. |
| `compareAtPrice`| Number | No | Pre-discount price for display. |

---

### List Prices for Product
Retrieve all available pricing tiers for a specific item.

- **Endpoint:** `GET /products/{productId}/prices`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/products/{productId}/prices \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/products/{productId}/prices',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/products/{productId}/prices"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/products/{productId}/prices",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Scopes:** `products.readonly`

---

### Update Price
Modify name or status of a price block. Note: Some financial fields (like amount) may be immutable after the first transaction.

- **Endpoint:** `PUT /products/{productId}/prices/{priceId}`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/products/{productId}/prices/{priceId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/products/{productId}/prices/{priceId}',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/products/{productId}/prices/{priceId}"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("PUT", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/products/{productId}/prices/{priceId}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Scopes:** `products.write`

---

## Example Request (Recurring Price)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/products/655b33a82209e60b6adb87a5/prices \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "name": "Standard Monthly",
  "type": "recurring",
  "currency": "USD",
  "amount": 4900,
  "recurring": {
    "interval": "month",
    "intervalCount": 1
  }
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `amount` or `currency`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Product ID not found. |
| 403 | `forbidden` | Pricing locked due to active subscriptions. |
| 422 | `unprocessable_entity` | `recurring` object missing for recurring type. |
