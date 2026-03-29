# Contacts: Campaigns & Workflows

Manage contact enrollment in active automation campaigns and workflows.

## 1. Automation Enrollment

### Add Contact to Campaign
Trigger a legacy automation campaign for a contact.

- **Endpoint:** `POST /contacts/{contactId}/campaigns`

> [!TIP]
> **Official Docs:** [Add Contact to Campaign](https://marketplace.gohighlevel.com/docs/ghl/contacts/add-contact-to-campaign)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/campaigns \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/campaigns',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/campaigns"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/campaigns",
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
| `campaignId`| String | Yes | ID of the campaign to start. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/seD4PfOuKoVMLkEZqohJ/campaigns \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "campaignId": "y0BeYjuRIlDwsDcOHOJo"
}'
```

---

### Add Contact to Workflow
Trigger a modern automation workflow for a contact.

- **Endpoint:** `POST /contacts/{contactId}/workflows`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/workflows \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/workflows',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/workflows"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/workflows",
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
| `workflowId`| String | Yes | ID of the workflow to start. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/seD4PfOuKoVMLkEZqohJ/workflows \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "workflowId": "ve9EPM428h8vShlRW1KT"
}'
```

---

## 2. Removal Actions

### Remove Contact from Workflow
Remove a contact from a specific active workflow.

- **Endpoint:** `DELETE /contacts/{contactId}/workflows/{workflowId}`


#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/workflows/{workflowId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/workflows/{workflowId}',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/workflows/{workflowId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/workflows/{workflowId}",
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

### Remove Contact from All Campaigns
Hard-stop all active campaigns for a contact.

- **Endpoint:** `DELETE /contacts/{contactId}/campaigns/all`


#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/contacts/{contactId}/campaigns/all \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}/campaigns/all',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}/campaigns/all"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}/campaigns/all",
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

## 3. Workflow Memberships
Checking what workflows a contact is currently part of.

- **Endpoint:** `GET /contacts/{contactId}/workflow-memberships`
- **Method:** `GET`
- **Scopes:** `contacts.readonly`

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing ID or unauthorized trigger. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Contact ID or Workflow ID does not exist. |
| 422 | `unprocessable_entity` | Workflow enrollment failed. |
