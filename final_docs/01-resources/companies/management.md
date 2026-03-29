# Agency: Company Management

Manage top-level agency details, branding, and billing profile.

## 1. Company Information

### Get Company Profile
Retrieve account-level details for the agency.

- **Endpoint:** `GET /companies/{companyId}`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/companies/{companyId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/companies/{companyId}',
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

url = "https://services.leadconnectorhq.com/companies/{companyId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/companies/{companyId}",
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
- **Scopes:** `companies.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Response Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | String | Unique Agency ID. |
| `name` | String | Agency business name. |
| `email` | String | Primary admin email. |
| `phone` | String | Primary agency contact phone. |
| `branding` | Object | Logotype and Whitelabel domain config. |

---

### Update Company Settings
Modify branding assets or admin contact details.

- **Endpoint:** `PUT /companies/{companyId}`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/companies/{companyId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/companies/{companyId}',
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

url = "https://services.leadconnectorhq.com/companies/{companyId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/companies/{companyId}",
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
- **Scopes:** `companies.write`

---

## Example Request (Fetch Profile)
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/companies/UAXssdawIWAWD \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Company ID not found. |
| 403 | `forbidden` | User lack Agency Admin rights. |
| 429 | `rate_limit` | Too many management requests. |
