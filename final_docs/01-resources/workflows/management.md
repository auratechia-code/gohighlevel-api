# Workflows: Management

Retrieve and monitor automation workflows.

## 1. Workflow Operations

### List Workflows
Fetch all automation workflows belonging to a location.

- **Endpoint:** `GET /workflows/`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/workflows/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/workflows/',
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

url = "https://services.leadconnectorhq.com/workflows/"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/workflows/",
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
- **Scopes:** `workflows.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |

### Example Response (200 OK)
```json
{
  "workflows": [
    {
      "id": "78559bb3-b920-461e-b010-7b2a2816d2a9",
      "name": "New Lead Nurture",
      "status": "published",
      "version": 2,
      "locationId": "eBG6WapS3v4ZqwA45MTxtYJ",
      "createdAt": "2024-03-29T11:33:49.000Z",
      "updatedAt": "2024-03-29T11:33:49.000Z"
    }
  ]
}
```

---

## 2. Trigger Events
Workflows are typically triggered via:
1. **Internal CRM Actions:** (e.g., Tag Added, Opportunity Stage Changed).
2. **Form Submissions:** (via Form ID).
3. **Webhooks:** (External systems triggering GHL workflows).
4. **API Enrollment:** (See [Contacts: Campaigns & Workflows](../contacts/campaigns-workflows.md)).

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `locationId`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | User does not have workflow permissions. |
| 500 | `internal_error` | System timeout fetching automations. |
