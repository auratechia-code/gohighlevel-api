# Contacts: Tasks & Notes

Manage tasks and notes associated with specific contact records. These are essential for tracking interaction history and internal responsibilities.

## 1. Notes Management

### Create Note
Create an internal note for a contact.

- **Endpoint:** `POST /contacts/{contactId}/notes`

> [!TIP]
> **Official Docs:** [Create Note](https://marketplace.gohighlevel.com/docs/ghl/contacts/create-note)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/notes \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/notes',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/notes"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/notes",
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
| `body` | String | Yes | Content of the note. |
| `userId` | String | No | The ID of the user who created the note. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/seD4PfOuKoVMLkEZqohJ/notes \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "body": "Follow-up required after the next webinar.",
  "userId": "y0BeYjuRIlDwsDcOHOJo"
}'
```

---

## List Notes
Retrieve all notes associated with a contact.

- **Endpoint:** `GET /contacts/{contactId}/notes`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/notes \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/notes',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/notes"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/notes",
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
- **Scopes:** `contacts.readonly`

---

## 2. Tasks Management

### Create Task
Assign an internal task related to a contact.

- **Endpoint:** `POST /contacts/{contactId}/tasks`

> [!TIP]
> **Official Docs:** [Create Task](https://marketplace.gohighlevel.com/docs/ghl/contacts/create-task)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/tasks \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/tasks',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/tasks"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/tasks",
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
| `title` | String | Yes | Short title for the task. |
| `description`| String | No | Detailed task description. |
| `dueDate` | String | No | ISO 8601 date string (YYYY-MM-DDTHH:mm:ss.sssZ). |
| `assignedTo` | String | No | ID of the user assigned to this task. |
| `completed` | Boolean | No | Task status (default: false). |

---

## List Tasks
Retrieve all tasks associated with a contact.

- **Endpoint:** `GET /contacts/{contactId}/tasks`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/tasks \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/tasks',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/tasks"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/tasks",
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
- **Scopes:** `contacts.readonly`

---

## Update Task
Modify a task's title, description, or status (completed/incomplete).

- **Endpoint:** `PUT /contacts/{contactId}/tasks/{taskId}`
- **Method:** `PUT`
- **Scopes:** `contacts.write`

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing body or title. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Contact ID or Task ID does not exist. |
| 422 | `unprocessable_entity` | Validation of dates failed. |
