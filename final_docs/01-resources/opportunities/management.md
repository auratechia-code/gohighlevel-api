# Opportunity Management

Standardized documentation for Opportunity management. Opportunities represent potential deals tracked through pipelines and stages.

## 1. Create Opportunity
Add a new opportunity to a pipeline.

- **Endpoint:** `POST /opportunities/`
- **Scopes:** `opportunities.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pipelineId` | String | Yes | The ID of the pipeline. |
| `locationId` | String | Yes | The ID of the location. |
| `name` | String | Yes | Name/Title of the opportunity. |
| `pipelineStageId` | String | Yes | The ID of the stage within the pipeline. |
| `status` | String | Yes | Status: `open`, `won`, `lost`, `abandoned`. |
| `contactId` | String | No | ID of the contact associated with this opportunity. |
| `monetaryValue`| Number | No | The deal value. |
| `assignedTo` | String | No | ID of the user assigned to this opportunity. |
| `source` | String | No | Opportunity source. |
| `customFields` | Array | No | Array of objects with `id` and `fieldValue`. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/opportunities/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
  "locationId": "zT46WSCPbudrq4zhW",
  "name": "Tesla Fleet Expansion",
  "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",
  "status": "open",
  "monetaryValue": 5000,
  "contactId": "byMEV0NQinDhq8ZfiOi2"
}'
```

---

## 2. Get Opportunity
Retrieve details for a specific opportunity.

- **Endpoint:** `GET /opportunities/{opportunityId}`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/opportunities/{opportunityId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/opportunities/{opportunityId}',
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

url = "https://services.leadconnectorhq.com/opportunities/{opportunityId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/{opportunityId}",
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
- **Scopes:** `opportunities.readonly`

---

## 3. Update Opportunity
Update an existing opportunity (move stages, change status, etc.).

- **Endpoint:** `PUT /opportunities/{opportunityId}`
- **Scopes:** `opportunities.write`

### Example Request (Move Stage)
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/opportunities/yWQobCRIhRguQtD2llvk \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "pipelineStageId": "new_stage_id_here",
  "status": "won"
}'
```

---

## 4. Upsert Opportunity
Create or update an opportunity based on contact association.

- **Endpoint:** `POST /opportunities/upsert`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/opportunities/upsert \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/opportunities/upsert',
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

url = "https://services.leadconnectorhq.com/opportunities/upsert"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/opportunities/upsert",
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
- **Methodology:** Typically checks for an existing open opportunity for the given `contactId` in the specific `pipelineId`.

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required fields or invalid pipeline/stage IDs. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Opportunity ID, Pipeline ID, or Stage ID does not exist. |
| 422 | `unprocessable_entity` | Validation of status or monetary value failed. |
| 429 | `rate_limit` | Too many requests. |
