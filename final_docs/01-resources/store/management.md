# Store: Settings & Shipping

Configure eCommerce components, shipping rules, and carriers for the online store.

## 1. Store Global Settings

### Get/Update Settings
Manage shop identity, currency, and checkout behavior.

- **Endpoint:** `GET /store/settings`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/store/settings \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/store/settings',
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

url = "https://services.leadconnectorhq.com/store/settings"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/store/settings",
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
- **Method:** `GET` / `POST`
- **Scopes:** `objects.readonly` / `objects.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Configuration Properties
| Property | Type | Description |
|-----------|------|-------------|
| `name` | String | Public store name. |
| `currency` | String | ISO currency code. |
| `taxEnabled` | Boolean | Automatic tax calculation logic. |
| `shipping` | Object | Default shipping origins. |

---

## 2. Logistics (Shipping)

### Create Shipping Zone
Define geographical areas for specific delivery rates (e.g., "North America").

- **Endpoint:** `POST /store/shipping/zones`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/store/shipping/zones \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/store/shipping/zones',
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

url = "https://services.leadconnectorhq.com/store/shipping/zones"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/store/shipping/zones",
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
- **Scopes:** `objects.write`

---

### List Shipping Carriers
Retrieve integrated shipping providers (UPS, FedEx, USPS).

- **Endpoint:** `GET /store/shipping/carriers`

> [!TIP]
> **Official Docs:** [List Shipping Carriers](https://marketplace.gohighlevel.com/docs/ghl/store/list-shipping-carriers)

#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/store/shipping/carriers \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/store/shipping/carriers',
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

url = "https://services.leadconnectorhq.com/store/shipping/carriers"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/store/shipping/carriers",
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
- **Scopes:** `objects.readonly`

---

### Create Shipping Rate
Define the cost for shipping within a specific zone (e.g. "Flat Rate $10").

- **Endpoint:** `POST /store/shipping/rates`

> [!TIP]
> **Official Docs:** [Create Shipping Rate](https://marketplace.gohighlevel.com/docs/ghl/store/create-shipping-rate)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/store/shipping/rates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/store/shipping/rates',
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

url = "https://services.leadconnectorhq.com/store/shipping/rates"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/store/shipping/rates",
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
- **Scopes:** `objects.write`

---

## Example Request (Fetch Settings)
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/store/settings?locationId=ve9EPM428h8vShlRW1KT \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `locationId` or invalid rate data. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Store not initialized for this location. |
| 403 | `forbidden` | Insufficient thread access permissions. |
| 422 | `provider_error` | Shipping carrier rejection. |
