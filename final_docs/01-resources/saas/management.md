# SaaS Mode: Sub-Account Provisioning

Automate the enabling, disabling, and billing of SaaS mode for Sub-Accounts (Locations).

## 1. SaaS State Management

### Enable SaaS for Sub-Account
Activate recurring SaaS billing and whitelabel logic for a location.

- **Endpoint:** `POST /saas/locations/{locationId}/enable`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/saas/locations/{locationId}/enable \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/saas/locations/{locationId}/enable',
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

url = "https://services.leadconnectorhq.com/saas/locations/{locationId}/enable"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/saas/locations/{locationId}/enable",
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
- **Scopes:** `saas.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `stripePlanId` | String | Yes | Stripe ID of the selected plan. |
| `rebillingConfig`| Object | No | SMS/Email markups. |

---

### Disable SaaS for Sub-Account
Deactivate SaaS features and stop recurring revenue for the location.

- **Endpoint:** `DELETE /saas/locations/{locationId}/disable`


#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/saas/locations/{locationId}/disable \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/saas/locations/{locationId}/disable',
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

url = "https://services.leadconnectorhq.com/saas/locations/{locationId}/disable"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/saas/locations/{locationId}/disable",
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
- **Scopes:** `saas.write`

---

### Bulk Enable SaaS
Enable multiple locations simultaneously.

- **Endpoint:** `POST /saas/bulk/enable`

> [!TIP]
> **Official Docs:** [Bulk Enable SaaS](https://marketplace.gohighlevel.com/docs/ghl/saas/bulk-enable-saas-deprecated)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/saas/bulk/enable \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/saas/bulk/enable',
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

url = "https://services.leadconnectorhq.com/saas/bulk/enable"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/saas/bulk/enable",
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
- **Scopes:** `saas.write`

---

## 2. Wallet & Rebilling

### Update Wallet Balance
Force update or top-up the credits for SMS/Phone/Email for a location.

- **Endpoint:** `POST /saas/locations/{locationId}/wallet`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/saas/locations/{locationId}/wallet \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/saas/locations/{locationId}/wallet',
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

url = "https://services.leadconnectorhq.com/saas/locations/{locationId}/wallet"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/saas/locations/{locationId}/wallet",
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
- **Scopes:** `saas.write`

---

### Get Subscription Details
Fetch Stripe subscription status and next billing date.

- **Endpoint:** `GET /saas/locations/{locationId}/subscription`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/saas/locations/{locationId}/subscription \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/saas/locations/{locationId}/subscription',
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

url = "https://services.leadconnectorhq.com/saas/locations/{locationId}/subscription"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/saas/locations/{locationId}/subscription",
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
- **Scopes:** `saas.readonly`

---

## Example Request (Enable SaaS)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/saas/locations/UAXssdawIWAWD/enable \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "stripePlanId": "price_1PXXXXXXXXXXXXX",
  "rebillingConfig": {
    "smsMarkup": 1.5,
    "emailMarkup": 1.5
  }
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `stripePlanId` or invalid location. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Location or Stripe Plan ID not found. |
| 402 | `payment_required` | Agency has outstanding balance or Stripe disconnected. |
| 403 | `forbidden` | Sub-account is already in SaaS mode. |
| 422 | `unprocessable_entity` | Rebilling config out of allowed range (Max 3x). |
| 429 | `rate_limit` | Too many provisioning attempts. |
