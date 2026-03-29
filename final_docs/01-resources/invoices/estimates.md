# Invoices: Estimates (Proposals)

Manage business estimates, proposals, and their conversion to invoices.

## 1. Estimate Operations

### Create New Estimate
Prepare a professional estimate for a contact.

- **Endpoint:** `POST /invoices/estimates`

> [!TIP]
> **Official Docs:** [Create New Estimate](https://marketplace.gohighlevel.com/docs/ghl/invoices/create-new-estimate)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/estimates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/estimates',
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

url = "https://services.leadconnectorhq.com/invoices/estimates"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/estimates",
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
- **Scopes:** `invoices.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `altId` | String | Yes | Location ID. |
| `altType` | String | Yes | Must be `location`. |
| `name` | String | Yes | Title of the estimate. |
| `contactDetails` | Object | Yes | `id`, `name`, `email`. |
| `items` | Array | Yes | Line items including `amount`, `qty`, and `type` (`one_time` or `recurring`). |
| `expiryDate` | String | No | ISO date string for estimate expiration. |

---

### List Estimates
Retrieve all estimates for a location.

- **Endpoint:** `GET /invoices/estimates`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/invoices/estimates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/invoices/estimates',
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

url = "https://services.leadconnectorhq.com/invoices/estimates"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/estimates",
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
- **Scopes:** `invoices.readonly`

---

### Send Estimate
Send the estimate to the customer for review and approval.

- **Endpoint:** `POST /invoices/estimates/{estimateId}/send`

> [!TIP]
> **Official Docs:** [Send Estimate](https://marketplace.gohighlevel.com/docs/ghl/invoices/send-estimate)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/send \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/send',
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

url = "https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/send"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/send",
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
- **Scopes:** `invoices.write`

---

### Convert Estimate to Invoice
Transform an approved estimate into a billable invoice.

- **Endpoint:** `POST /invoices/estimates/{estimateId}/convert`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/convert \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/convert',
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

url = "https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/convert"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/estimates/{estimateId}/convert",
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
- **Scopes:** `invoices.write`

---

## 2. Estimate Templates

### List Estimate Templates
Fetch predefined structures for estimates.

- **Endpoint:** `GET /invoices/estimates/templates`

> [!TIP]
> **Official Docs:** [List Estimate Templates](https://marketplace.gohighlevel.com/docs/ghl/invoices/list-estimate-templates)

#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/invoices/estimates/templates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/invoices/estimates/templates',
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

url = "https://services.leadconnectorhq.com/invoices/estimates/templates"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/estimates/templates",
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
- **Scopes:** `invoices.readonly`

---

## Example Request (Create Estimate)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/estimates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "altId": "ve9EPM428h8vShlRW1KT",
  "altType": "location",
  "name": "Software Development Proposal",
  "contactDetails": {
    "id": "jvzfKTNdE7OYXXXXXX",
    "name": "Jane Smith",
    "email": "jane@example.com"
  },
  "items": [
    {
      "name": "Backend Refactor",
      "qty": 1,
      "amount": 2500,
      "type": "one_time"
    }
  ]
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required fields. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Estimate ID not found. |
| 412 | `precondition_failed` | Cannot convert estimate until approved. |
