# Opportunities: Pipelines & Config

Manage pipeline configurations, retrieve available stages, and handle lost reasons.

## 1. List Pipelines
Fetch all pipelines and stages available in a specific location. Use this to find the `pipelineId` and `pipelineStageId` needed for opportunity creation/updates.

- **Endpoint:** `GET /opportunities/pipelines`
- **Method:** `GET`
- **Scopes:** `opportunities.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | The ID of the location. |

### Example Response (200 OK)
```json
{
  "pipelines": [
    {
      "id": "VDm7RPYC2GLUvdpKmBfC",
      "name": "General Sales",
      "index": 1,
      "stages": [
        {
          "id": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",
          "name": "Lead In",
          "index": 1
        },
        {
          "id": "stage_2_id",
          "name": "Follow-up",
          "index": 2
        }
      ]
    }
  ]
}
```

---

## 2. Lost Reasons

### List Lost Reasons
Fetch standard reasons for losing an opportunity.

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

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `locationId`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | User does not have access to this location. |
| 404 | `not_found` | Location ID not found. |
