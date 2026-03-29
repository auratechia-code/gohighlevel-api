# Invoices: Management

Standardized documentation for full Invoice lifecycle management.

## 1. Core Operations

### Create Invoice
Generate a new invoice for a specific contact.

- **Endpoint:** `POST /invoices/`

> [!TIP]
> **Official Docs:** [Create Invoice](https://marketplace.gohighlevel.com/docs/ghl/invoices/create-invoice)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/',
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

url = "https://services.leadconnectorhq.com/invoices/"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/",
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
| `contactDetails` | Object | Yes | `id`, `email`, `name`. |
| `invoiceItems` | Array | Yes | List of products/services being billed. |
| `dueDate` | String | Yes | ISO date string (`YYYY-MM-DD`). |
| `currency` | String | Yes | ISO currency code (e.g., `USD`). |

---

### List Invoices
Retrieve a paginated list of invoices for a location.

- **Endpoint:** `GET /invoices/`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/invoices/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/invoices/',
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

url = "https://services.leadconnectorhq.com/invoices/"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/",
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

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `altId` | String | Yes | Location ID. |
| `altType` | String | Yes | Must be `location`. |
| `status` | String | No | Filter by `draft`, `sent`, `paid`, `void`, etc. |

---

### Get Invoice by ID
Fetch precise details of a specific invoice.

- **Endpoint:** `GET /invoices/{invoiceId}`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/invoices/{invoiceId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/invoices/{invoiceId}',
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

url = "https://services.leadconnectorhq.com/invoices/{invoiceId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/{invoiceId}",
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

## 2. Sending & Actions

### Send Invoice
Deliver the invoice to the customer via email.

- **Endpoint:** `POST /invoices/{invoiceId}/send`

> [!TIP]
> **Official Docs:** [Send Invoice](https://marketplace.gohighlevel.com/docs/ghl/invoices/send-invoice)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/{invoiceId}/send \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/{invoiceId}/send',
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

url = "https://services.leadconnectorhq.com/invoices/{invoiceId}/send"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/{invoiceId}/send",
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

### Void Invoice
Cancel an existing invoice.

- **Endpoint:** `POST /invoices/{invoiceId}/void`

> [!TIP]
> **Official Docs:** [Void Invoice](https://marketplace.gohighlevel.com/docs/ghl/invoices/void-invoice)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/{invoiceId}/void \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/{invoiceId}/void',
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

url = "https://services.leadconnectorhq.com/invoices/{invoiceId}/void"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/{invoiceId}/void",
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

## Example Request (Create)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "altId": "ve9EPM428h8vShlRW1KT",
  "altType": "location",
  "name": "Consulting Services",
  "contactDetails": {
    "id": "c6tZZU0rJBf30ZXx9Gli",
    "name": "John Doe",
    "email": "john@example.com"
  },
  "invoiceItems": [
    {
      "name": "Audit Service",
      "qty": 1,
      "amount": 500,
      "currency": "USD"
    }
  ],
  "dueDate": "2024-12-31"
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required fields or invalid currency. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Invoice or Contact ID not found. |
| 422 | `unprocessable_entity` | Cannot send invoice in current status. |
