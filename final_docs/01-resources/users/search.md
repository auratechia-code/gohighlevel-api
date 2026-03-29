# Users: Search & Filtering

Retrieve lists of users based on location or account-level attributes.

## 1. Search Users
Fetch a list of users, potentially filtered by location or name.

- **Endpoint:** `GET /users/`
- **Method:** `GET`
- **Scopes:** `users.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location to list users from. |
| `limit` | Number | No | Page size (max: 100). |
| `offset` | Number | No | Pagination offset. |

### Example Request
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/users/?locationId=ve9EPM428h8vShlRW1KT' \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

---

## 2. Get User by Email
Find a user by their registered email address.

- **Endpoint:** `GET /users/search`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/users/search \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/users/search',
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

url = "https://services.leadconnectorhq.com/users/search"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/users/search",
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
- **Scopes:** `users.readonly`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `email` | String | Yes | Email address to search for. |

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `locationId` or `email`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | User does not have access to this location. |
| 404 | `not_found` | User not found for given email. |
