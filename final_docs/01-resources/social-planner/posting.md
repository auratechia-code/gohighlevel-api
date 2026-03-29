# Social Planner: Posting & Scheduling

Create, scheduling, and track organic posts across all attached networks.

## 1. Post Creation

### Create Post
Draft and schedule a message for one or more social platforms.

- **Endpoint:** `POST /social-planner/posts`

> [!TIP]
> **Official Docs:** [Create Post](https://marketplace.gohighlevel.com/docs/ghl/social-planner/create-post)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/social-planner/posts \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/social-planner/posts',
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

url = "https://services.leadconnectorhq.com/social-planner/posts"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/posts",
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
- **Scopes:** `socialplanner.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `accountIds` | Array | Yes | List of attached account IDs. |
| `summary` | String | Yes | Body content of the post. |
| `media` | Array | No | Hosted URLs for images/videos. |
| `scheduledDate`| String | No | ISO format. If missing, post is sent immediately. |

---

### List Scheduled Posts
Retrieve future or historical posts for the location.

- **Endpoint:** `GET /social-planner/posts`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/social-planner/posts \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/social-planner/posts',
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

url = "https://services.leadconnectorhq.com/social-planner/posts"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/posts",
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

## 2. Interaction

### Update Scheduled Post
Modify content or time before it is published.

- **Endpoint:** `PUT /social-planner/posts/{postId}`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/social-planner/posts/{postId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/social-planner/posts/{postId}',
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

url = "https://services.leadconnectorhq.com/social-planner/posts/{postId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/posts/{postId}",
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
- **Scopes:** `socialplanner.write`

---

### Delete Post
Abort a scheduled post or delete record of a published post.

- **Endpoint:** `DELETE /social-planner/posts/{postId}`

> [!TIP]
> **Official Docs:** [Delete Post](https://marketplace.gohighlevel.com/docs/ghl/social-planner/delete-post)

#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/social-planner/posts/{postId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/social-planner/posts/{postId}',
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

url = "https://services.leadconnectorhq.com/social-planner/posts/{postId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/social-planner/posts/{postId}",
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

## Example Request (Schedule FB Post)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/social-planner/posts \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "UAXssdawIWAWD",
  "accountIds": ["fb_page_id_123"],
  "summary": "Join our end of summer sale! Discounts up to 50%. #SummerSale #Marketing",
  "scheduledDate": "2024-09-01T10:00:00Z"
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `summary` or account IDs. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `publishing_locked` | Post is currently being published and cannot be modified. |
| 422 | `media_error` | Unsupported media format or file too large. |
| 429 | `api_limit` | Social network rejection due to flooding. |
