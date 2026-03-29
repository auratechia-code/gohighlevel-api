# Payments: Integrations & Providers

Standardized documentation for Payment configuration, integrations, and coupon management.

## 1. Integrations & Providers

### List Provider Configurations
Retrieve existing payment integrations (e.g., Stripe, PayPal, Authorize.net) for a location.

- **Endpoint:** `GET /payments/integrations/provider-config`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/payments/integrations/provider-config \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/payments/integrations/provider-config',
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

url = "https://services.leadconnectorhq.com/payments/integrations/provider-config"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/payments/integrations/provider-config",
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
- **Method:** `GET`
- **Scopes:** `payments.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |

---

### Disconnect Provider
Disconnect a payment provider integration.

- **Endpoint:** `DELETE /payments/integrations/provider-config`


#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/payments/integrations/provider-config \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/payments/integrations/provider-config',
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

url = "https://services.leadconnectorhq.com/payments/integrations/provider-config"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("DELETE", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/payments/integrations/provider-config",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "DELETE",
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
- **Method:** `DELETE`
- **Scopes:** `payments.write`

---

## 2. Coupon Management

### Create Coupon
Define a discount coupon for use in checkouts or invoices.

- **Endpoint:** `POST /payments/coupons`

> [!TIP]
> **Official Docs:** [Create Coupon](https://marketplace.gohighlevel.com/docs/ghl/payments/create-coupon)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/payments/coupons \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/payments/coupons',
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

url = "https://services.leadconnectorhq.com/payments/coupons"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/payments/coupons",
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
- **Scopes:** `payments.write`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `name` | String | Yes | Descriptive name of the coupon. |
| `couponCode` | String | Yes | The code customers enter (e.g., "SAVE50"). |
| `type` | String | Yes | `percentage` or `fixed_amount`. |
| `value` | Number | Yes | Discount amount or percentage. |
| `startDate` | String | No | ISO date string. |
| `endDate` | String | No | ISO date string. |
| `maxRedemptions`| Number | No | Total usage limit. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/payments/coupons \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "Spring Sale 2024",
  "couponCode": "SPRING50",
  "type": "percentage",
  "value": 50,
  "maxRedemptions": 100
}'
```

---

## List Coupons
Retrieve all active and expired coupons for a location.

- **Endpoint:** `GET /payments/coupons`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/payments/coupons \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/payments/coupons',
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

url = "https://services.leadconnectorhq.com/payments/coupons"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/payments/coupons",
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
- **Scopes:** `payments.readonly`

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required coupon fields. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | Permission denied to manage payments. |
| 422 | `unprocessable_entity` | Coupon code already exists. |
