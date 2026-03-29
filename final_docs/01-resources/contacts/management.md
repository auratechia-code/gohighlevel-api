# Contact Management

Standardized documentation for the Contact management endpoints. Contacts are the primary entities in GoHighLevel, representing leads or customers.

## 1. Create Contact
Create a new contact record in a specific location.

- **Endpoint:** `POST /contacts/`
- **Scopes:** `contacts.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | The ID of the location where the contact will be created. |
| `firstName` | String | No | Contact's first name. |
| `lastName` | String | No | Contact's last name. |
| `email` | String | No | Contact's email address. |
| `phone` | String | No | Contact's phone number in E.164 format. |
| `companyName`| String | No | Name of the company. |
| `address1` | String | No | Primary address line. |
| `city` | String | No | City name. |
| `state` | String | No | State or province code. |
| `country` | String | No | Country code (e.g., "US"). |
| `postalCode` | String | No | Postal or zip code. |
| `website` | String | No | Website URL. |
| `timezone` | String | No | Contact's timezone (e.g., "America/New_York"). |
| `source` | String | No | Source of the lead (e.g., "Marketing Site"). |
| `tags` | Array | No | String array of tags to apply. |
| `customFields`| Array | No | Array of objects with `id` and `value`. |
| `dnd` | Boolean | No | Enable/Disable Do Not Disturb. |
| `dndSettings`| Object | No | Granular DND settings for specific channels (Call, Email, SMS, WhatsApp, GMB, FB). |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "phone": "+18832327657",
  "tags": ["Lead", "High Priority"],
  "customFields": [{"id": "MgobCB14YMVKuE4Ka8p1", "value": "Referral"}]
}'
```

---

## 2. Get Contact
Retrieve details for a specific contact.

- **Endpoint:** `GET /contacts/{contactId}`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/contacts/{contactId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}",
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
- **Scopes:** `contacts.readonly`

### Example Response (200 OK)
```json
{
  "contact": {
    "id": "seD4PfOuKoVMLkEZqohJ",
    "locationId": "ve9EPM428h8vShlRW1KT",
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "phone": "+18832327657",
    "type": "customer",
    "dateAdded": "2021-08-31T09:59:41.937Z",
    "customFields": [...]
  }
}
```

---

## 3. Update Contact
Update an existing contact record.

- **Endpoint:** `PUT /contacts/{contactId}`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/contacts/{contactId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/contacts/{contactId}',
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

url = "https://services.leadconnectorhq.com/contacts/{contactId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/{contactId}",
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
- **Scopes:** `contacts.write`

---

## 4. Upsert Contact
Create or update a contact based on lookup keys (Email/Phone).

- **Endpoint:** `POST /contacts/upsert`
- **Methodology:** The Upsert API adheres to the "Allow Duplicate Contact" setting at the Location level. It checks Email/Phone as defined in the sequence.

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/upsert \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com"
}'
```

---

## 5. Search Contacts (Advanced)
Search contacts using complex filter combinations.

- **Endpoint:** `POST /contacts/search`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/contacts/search \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/contacts/search',
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

url = "https://services.leadconnectorhq.com/contacts/search"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/contacts/search",
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
- **Scopes:** `contacts.readonly`

### Advanced Filter Example
Use this to search by specific criteria like `last_activity`, `tag`, or `custom_field`.

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required fields or invalid format. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Contact ID does not exist. |
| 422 | `unprocessable_entity` | Validation failed (e.g., duplicated email if settings prohibit). |
