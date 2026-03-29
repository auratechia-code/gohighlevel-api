# User Management

Standardized documentation for User management endpoints. Users are individual accounts within the platform (Agency or Sub-account level).

## 1. Create User
Create a new user with specific permissions and roles.

- **Endpoint:** `POST /users/`
- **Scopes:** `users.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `firstName` | String | Yes | User's first name. |
| `lastName` | String | Yes | User's last name. |
| `email` | String | Yes | User's email (used as login). |
| `password` | String | Yes | User's password. |
| `role` | String | Yes | User role (e.g., "admin", "user"). |
| `locationIds`| Array | No | List of Location IDs the user has access to. |
| `permissions`| Object | No | Key-value mapping of specific functionality toggles (see example). |
| `type` | String | No | Account type (`agency`, `account`). |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/users/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "firstName": "John",
  "lastName": "Deo",
  "email": "john@deo.com",
  "password": "secure_password_here",
  "role": "admin",
  "type": "account",
  "locationIds": ["ve9EPM428h8vShlRW1KT"],
  "permissions": {
    "contactsEnabled": true,
    "conversationsEnabled": true,
    "opportunitiesEnabled": true
  }
}'
```

---

## 2. Get User
Retrieve details for a specific user.

- **Endpoint:** `GET /users/{userId}`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/users/{userId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/users/{userId}',
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

url = "https://services.leadconnectorhq.com/users/{userId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/users/{userId}",
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
- **Scopes:** `users.readonly`

---

## 3. Update User
Modify user details, permissions, or access roles.

- **Endpoint:** `PUT /users/{userId}`
- **Scopes:** `users.write`

---

## 4. Delete User
Permanently remove a user record.

- **Endpoint:** `DELETE /users/{userId}`
- **Scopes:** `users.write`

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required fields or invalid role. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | User ID does not exist. |
| 422 | `unprocessable_entity` | Email already in use or permission mismatch. |
