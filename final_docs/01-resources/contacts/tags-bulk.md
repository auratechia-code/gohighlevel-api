# Contacts: Tags & Bulk Actions

Manage tags and execute bulk operations across one or more contacts.

## 1. Tag Management

### Add Tags
Add one or more tags to a contact record.

- **Endpoint:** `POST /contacts/{contactId}/tags`

> [!TIP]
> **Official Docs:** [Add Tags](https://marketplace.gohighlevel.com/docs/ghl/contacts/add-tags)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/tags \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/tags',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/tags"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/tags",
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
- **Scopes:** `contacts.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tags` | Array | Yes | Array of strings representing tags. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/seD4PfOuKoVMLkEZqohJ/tags \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "tags": ["Customer", "VIP"]
}'
```

---

### Remove Tags
Remove specified tags from a contact.

- **Endpoint:** `DELETE /contacts/{contactId}/tags`


#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/tags \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/tags',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/tags"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/tags",
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
- **Scopes:** `contacts.write`

---

## 2. Bulk Operations

### Bulk Action Execute
Add/Remove tags, Add to workflow, or delete multiple contacts at once.

- **Endpoint:** `POST /contacts/bulk`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/bulk \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/bulk',
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

url = "https://services.leadconnectorhq.com/contacts/bulk"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/bulk",
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
- **Scopes:** `contacts.write`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ids` | Array | Yes | Array of Contact IDs for the operation. |
| `type` | String | Yes | Type of operation: `ADD_TAG`, `REMOVE_TAG`, `ADD_TO_WORKFLOW`, `REMOVE_FROM_WORKFLOW`, `DELETE`. |
| `data` | Object | No | Data required for the specified type (e.g., `tags` or `workflowId`). |

### Example Request (Bulk Tagging)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/bulk \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "ids": ["seD...J", "ve9...T"],
  "type": "ADD_TAG",
  "data": {
    "tags": ["Bulk Updated"]
  }
}'
```

---

## 3. Business Management
Associate or dissociate contacts from a sub-account business.

- **Endpoint:** `POST /contacts/business/`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/business/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/business/',
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

url = "https://services.leadconnectorhq.com/contacts/business/"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/business/",
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
- **Scopes:** `contacts.write`

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing list of IDs or invalid operation type. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | One or more Contact IDs not found. |
| 422 | `unprocessable_entity` | Operation failed for some records. |
