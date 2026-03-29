# Locations: Custom Fields & Values

Define and manage custom metadata globally for a location (Sub-Account).

## 1. Custom Fields

### Create Custom Field
Add a new field definition available for Contacts, Opportunities, etc.

- **Endpoint:** `POST /locations/{locationId}/custom-fields`

> [!TIP]
> **Official Docs:** [Create Custom Field](https://marketplace.gohighlevel.com/docs/ghl/locations/create-custom-field)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/locations/{locationId}/custom-fields \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/locations/{locationId}/custom-fields',
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

url = "https://services.leadconnectorhq.com/locations/{locationId}/custom-fields"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/locations/{locationId}/custom-fields",
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
- **Scopes:** `locations.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | String | Yes | Label for the field (e.g., "Car Make"). |
| `dataType` | String | Yes | `TEXT`, `NUMBER`, `DATE`, `SINGLE_SELECT`, `MULTI_SELECT`, `CHECKBOX`. |
| `placeholder`| String | No | Input hint. |
| `options` | Array | No | List of values for select/checkbox types. |

---

### List Custom Fields
Retrieve all field definitions for the location.

- **Endpoint:** `GET /locations/{locationId}/custom-fields`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/locations/{locationId}/custom-fields \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/locations/{locationId}/custom-fields',
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

url = "https://services.leadconnectorhq.com/locations/{locationId}/custom-fields"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/locations/{locationId}/custom-fields",
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
- **Scopes:** `locations.readonly`

---

## 2. Custom Values (Global Snippets)

### Create Custom Value
Define a global variable (e.g., `{{custom_values.brand_color}}`).

- **Endpoint:** `POST /locations/{locationId}/custom-values`

> [!TIP]
> **Official Docs:** [Create Custom Value](https://marketplace.gohighlevel.com/docs/ghl/locations/create-custom-value)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/locations/{locationId}/custom-values \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/locations/{locationId}/custom-values',
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

url = "https://services.leadconnectorhq.com/locations/{locationId}/custom-values"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/locations/{locationId}/custom-values",
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
- **Scopes:** `locations.write`

### List Custom Values
Retrieve all location-wide dynamic variables.

- **Endpoint:** `GET /locations/{locationId}/custom-values`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/locations/{locationId}/custom-values \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/locations/{locationId}/custom-values',
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

url = "https://services.leadconnectorhq.com/locations/{locationId}/custom-values"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/locations/{locationId}/custom-values",
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
- **Scopes:** `locations.readonly`

---

## Example Request (Create Field)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/locations/ve9EPM428h8vShlRW1KT/custom-fields \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "name": "Vehicle Type",
  "dataType": "SINGLE_SELECT",
  "options": [
    { "label": "Sedan", "value": "sedan" },
    { "label": "SUV", "value": "suv" }
  ]
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `name` or invalid `dataType`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Location ID not found. |
| 409 | `conflict` | Field name or Custom Value key already exists. |
| 422 | `unprocessable_entity` | Options array missing for `SINGLE_SELECT`. |
