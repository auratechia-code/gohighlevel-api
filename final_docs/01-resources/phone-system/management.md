# Phone System: Number Management

Search, purchase, and configure telephony numbers and tracking pools.

## 1. Number Procurement

### List Available Numbers
Search for new phone numbers by area code or text pattern.

- **Endpoint:** `GET /phone-system/numbers/available`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/phone-system/numbers/available \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/phone-system/numbers/available',
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

url = "https://services.leadconnectorhq.com/phone-system/numbers/available"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/phone-system/numbers/available",
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
- **Scopes:** `phone.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `country` | String | Yes | ISO country code (e.g., `US`). |
| `areaCode` | String | No | 3-digit area code. |
| `pattern` | String | No | Specific digits to search for. |

---

### Purchase Phone Number
Secure a specific number and add it to the location's inventory.

- **Endpoint:** `POST /phone-system/numbers/purchase`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/phone-system/numbers/purchase \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/phone-system/numbers/purchase',
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

url = "https://services.leadconnectorhq.com/phone-system/numbers/purchase"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/phone-system/numbers/purchase",
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
- **Scopes:** `phone.write`

---

## 2. Active Inventory

### List Active Numbers
Retrieve all numbers currently owned by the sub-account.

- **Endpoint:** `GET /phone-system/numbers/active`

> [!TIP]
> **Official Docs:** [List Active Numbers](https://marketplace.gohighlevel.com/docs/ghl/phone-system/active-numbers)

#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/phone-system/numbers/active \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/phone-system/numbers/active',
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

url = "https://services.leadconnectorhq.com/phone-system/numbers/active"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/phone-system/numbers/active",
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
- **Scopes:** `phone.readonly`

---

### Number Pools
Manage groups of tracking numbers for attributed calls.

- **Endpoint:** `GET /phone-system/number-pools`

> [!TIP]
> **Official Docs:** [Number Pools](https://marketplace.gohighlevel.com/docs/ghl/phone-system/number-pools)

#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/phone-system/number-pools \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/phone-system/number-pools',
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

url = "https://services.leadconnectorhq.com/phone-system/number-pools"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/phone-system/number-pools",
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
- **Scopes:** `phone.readonly`

---

## Example Request (Available Search)
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/phone-system/numbers/available?locationId=ve9EPM428h8vShlRW1KT&country=US&areaCode=410' \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `country` or `areaCode`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | User lacks telephony permissions. |
| 404 | `not_found` | No numbers matching the criteria found. |
| 422 | `provider_error` | Twilio/Provider rejected the purchase. |
| 429 | `rate_limit` | Purchasing frequency exceeded. |
| 402 | `payment_required` | Insufficient wallet balance to purchase. |
