# Invoices: Schedules & Templates

Automate recurring billing and streamline creation using standardized templates.

## 1. Recurring Invoice Schedules

### Create Invoice Schedule
Define a frequency and duration for recurring invoices to a contact.

- **Endpoint:** `POST /invoices/schedules`

> [!TIP]
> **Official Docs:** [Create Invoice Schedule](https://marketplace.gohighlevel.com/docs/ghl/invoices/create-invoice-schedule)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/schedules \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/schedules',
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

url = "https://services.leadconnectorhq.com/invoices/schedules"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/schedules",
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
| `name` | String | Yes | Title of the recurring series. |
| `contactDetails` | Object | Yes | `id`, `name`, `email`. |
| `frequency` | String | Yes | `weekly`, `monthly`, `yearly`. |
| `invoiceItems` | Array | Yes | Recurring items to bill. |

---

### List Schedules
Retrieve a list of all active, paused, or completed schedules for a location.

- **Endpoint:** `GET /invoices/schedules`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/invoices/schedules \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/invoices/schedules',
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

url = "https://services.leadconnectorhq.com/invoices/schedules"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/schedules",
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

### Update Schedule Status
Pause, resume, or cancel a recurring sequence.

- **Endpoint:** `PUT /invoices/schedules/{scheduleId}/status`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/invoices/schedules/{scheduleId}/status \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/invoices/schedules/{scheduleId}/status',
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

url = "https://services.leadconnectorhq.com/invoices/schedules/{scheduleId}/status"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/schedules/{scheduleId}/status",
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
- **Scopes:** `invoices.write`

---

## 2. Invoice Templates

### Create Invoice Template
Save a standardized structure for future invoices.

- **Endpoint:** `POST /invoices/templates`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/templates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/invoices/templates',
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

url = "https://services.leadconnectorhq.com/invoices/templates"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/templates",
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

### List Templates
Retrieve all stored templates for a location.

- **Endpoint:** `GET /invoices/templates`

> [!TIP]
> **Official Docs:** [List Templates](https://marketplace.gohighlevel.com/docs/ghl/proposals/list-documents-contracts-templates)

#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/invoices/templates \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/invoices/templates',
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

url = "https://services.leadconnectorhq.com/invoices/templates"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/invoices/templates",
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

## Example (Monthly Subscription Schedule)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/invoices/schedules \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "altId": "ve9EPM428h8vShlRW1KT",
  "altType": "location",
  "name": "Standard Access Plan",
  "contactDetails": {
    "id": "jvzfKTNdE7OYXXXXXX",
    "name": "Alex Doe",
    "email": "alex@example.com"
  },
  "frequency": "monthly",
  "invoiceItems": [
    {
      "name": "Core Platform Access",
      "qty": 1,
      "amount": 97
    }
  ]
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required frequency or items. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Location or Contact not found. |
| 422 | `unprocessable_entity` | Schedule logic error (e.g., end date before start date). |
