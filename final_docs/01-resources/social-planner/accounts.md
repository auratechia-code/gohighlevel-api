# Social Planner: Account Attachment

Connect social media profiles to a location for automated organic posting.

## 1. OAuth Integration

### Start OAuth Flow
Initiate the connection process for specific social networks.

- **Available Networks:** Facebook, Instagram, LinkedIn, TikTok, X (Twitter), Google Business Profile.
- **Method:** `GET`
- **Scopes:** `socialplanner.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

---

### Attach Account Profile
Once OAuth is complete, select the specific page or profile to monitor.

- **Endpoint:** `POST /social-planner/accounts/attach`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/social-planner/accounts/attach \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/social-planner/accounts/attach',
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

url = "https://services.leadconnectorhq.com/social-planner/accounts/attach"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/accounts/attach",
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

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `platform` | String | Yes | `facebook`, `instagram`, `linkedin`, `tiktok`, `twitter`, `google`. |
| `platformId` | String | Yes | Internal ID from the social network. |
| `token` | String| Yes | Platform access token. |

---

## 2. Inventory

### Get Connected Accounts
Retrieve a list of all active social connections for the location.

- **Endpoint:** `GET /social-planner/accounts/`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/social-planner/accounts/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/social-planner/accounts/',
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

url = "https://services.leadconnectorhq.com/social-planner/accounts/"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/accounts/",
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
- **Scopes:** `socialplanner.readonly`

---

### Delete Connection
Remove a social profile from the planner.

- **Endpoint:** `DELETE /social-planner/accounts/{accountId}`


#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/social-planner/accounts/{accountId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/social-planner/accounts/{accountId}',
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

url = "https://services.leadconnectorhq.com/social-planner/accounts/{accountId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/accounts/{accountId}",
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
- **Scopes:** `socialplanner.write`

---

## Example Request (List Accounts)
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/social-planner/accounts/?locationId=UAXssdawIWAWD \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | Account already attached to another location. |
| 422 | `invalid_token` | Platform token has expired or was revoked. |
| 429 | `api_limit` | Social platform rate limit reached. |
