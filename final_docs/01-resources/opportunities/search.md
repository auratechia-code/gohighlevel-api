# Opportunities: Search & Filters

Advanced search for opportunities across pipelines and stages.

## 1. Search Opportunities (Advanced)
Search opportunities using combinations of filters such as pipeline, stage, status, assigned user, and last activity date.

- **Endpoint:** `POST /opportunities/search`
- **Method:** `POST`
- **Scopes:** `opportunities.readonly`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters (Filters)
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `pipelineId` | String | No | Filter by specific pipeline. |
| `pipelineStageId`| String | No | Filter by specific stage. |
| `status` | String | No | Filter by status (`open`, `won`, `lost`, `abandoned`). |
| `assignedTo` | String | No | Filter by assigned user ID. |
| `contactId` | String | No | Filter by associated contact. |
| `query` | String | No | Search by opportunity name. |
| `limit` | Number | No | Page size (max: 100). |
| `offset` | Number | No | Pagination offset. |

### Example Request
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/opportunities/search \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "zT46WSCPbudrq4zhW",
  "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
  "status": "open",
  "limit": 20
}'
```

### Example Response (200 OK)
```json
{
  "opportunities": [
    {
      "id": "yWQobCRIhRguQtD2llvk",
      "name": "Tesla Expansion",
      "monetaryValue": 500,
      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",
      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",
      "status": "open",
      "contactId": "byMEV0NQinDhq8ZfiOi2",
      "createdAt": "2021-08-03T04:55:17.355Z"
    }
  ],
  "total": 1,
  "aggregations": {}
}
```

---

## 2. Paging & Aggregations
The search endpoint returns metadata about total counts and potential aggregations for reporting purposes.

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `locationId`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | User does not have access to this location. |
| 429 | `rate_limit` | Too many requests. |
