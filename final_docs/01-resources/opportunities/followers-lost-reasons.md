# Opportunities: Followers & Status

Manage opportunity status, lost reasons, and follower associations.

## 1. Status Management

### Update Opportunity Status
Specifically update an opportunity's status to `won`, `lost`, `abandoned`, or `open`.

- **Endpoint:** `PATCH /opportunities/{opportunityId}/status`

> [!TIP]
> **Official Docs:** [Update Opportunity Status](https://marketplace.gohighlevel.com/docs/ghl/opportunities/update-opportunity-status)

#### Example Requests
```bash
curl --request PATCH \
  --url https://services.leadconnectorhq.com/opportunities/{opportunityId}/status \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PATCH',
  url: 'https://services.leadconnectorhq.com/opportunities/{opportunityId}/status',
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

url = "https://services.leadconnectorhq.com/opportunities/{opportunityId}/status"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("PATCH", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/{opportunityId}/status",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "PATCH",
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
- **Method:** `PATCH`
- **Scopes:** `opportunities.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | String | Yes | New status: `open`, `won`, `lost`, `abandoned`. |
| `lostReasonId` | String | No | Recommended when status is `lost`. |

---

## 2. Follower Management

### List Followers
Retrieve users who are tracking this opportunity.

- **Endpoint:** `GET /opportunities/{opportunityId}/followers`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers',
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

url = "https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers",
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
- **Scopes:** `opportunities.readonly`

### Add Followers
Assign users as followers to an opportunity.

- **Endpoint:** `POST /opportunities/{opportunityId}/followers`

> [!TIP]
> **Official Docs:** [Add Followers](https://marketplace.gohighlevel.com/docs/ghl/opportunities/add-followers-opportunity)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers',
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

url = "https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers",
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
- **Scopes:** `opportunities.write`

### Remove Followers
Remove specific users from following an opportunity.

- **Endpoint:** `DELETE /opportunities/{opportunityId}/followers`

> [!TIP]
> **Official Docs:** [Remove Followers](https://marketplace.gohighlevel.com/docs/ghl/opportunities/remove-followers-opportunity)

#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers',
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

url = "https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/{opportunityId}/followers",
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
- **Method:** `DELETE`
- **Scopes:** `opportunities.write`

---

## 3. Lost Reasons Configuration

### Get Lost Reasons
List valid reasons for losing a deal in a location.

- **Endpoint:** `GET /opportunities/lost-reason`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/opportunities/lost-reason \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/opportunities/lost-reason',
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

url = "https://services.leadconnectorhq.com/opportunities/lost-reason"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/lost-reason",
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
- **Scopes:** `opportunities.readonly`

### Example Response
```json
{
  "lostReasons": [
    {
      "id": "lost_reason_id",
      "name": "Price too high",
      "locationId": "zT46WSCPbudrq4zhW"
    }
  ]
}
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Status provided is not in the valid enum list. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Opportunity or reason not found. |
| 403 | `forbidden` | Permission denied to update status. |
