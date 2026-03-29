# Opportunity Body Parameters (V2)

Documentation for creating and updating Opportunities in GoHighLevel.

## Create Opportunity (`POST /opportunities/`)

The following fields are supported in the request body.

| Field | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `pipelineId` | String | **YES** | The unique ID of the pipeline. | `VDm7RPYC2GLUvdpKmBfC` |
| `locationId` | String | **YES** | The unique ID of the location. | `ve9EPM428h8vShlRW1KT` |
| `name` | String | **YES** | Name of the opportunity. | `First Deals` |
| `contactId` | String | **YES** | The unique ID of the contact. | `mTkSCb1UBjb5tk4OvB69` |
| `status` | String | **YES** | Status: `open`, `won`, `lost`, `abandoned`. | `open` |
| `pipelineStageId`| String | No | ID of the pipeline stage. | `7915dedc-8f18...` |
| `monetaryValue` | Number | No | The monetary value of the deal. | `220` |
| `assignedTo` | String | No | The ID of the user assigned to it. | `082goXVW3lIE...` |
| `customFields` | Array | No | Array of objects: `{id: string, key: string, field_value: any}`. | |

---

## Update Opportunity (`PUT /opportunities/:id`)

The update operation uses the **same schema** as the Create operation, with the following rules:

1. **`pipelineId` is NOT required** if updating status/stage in the same pipeline.
2. **`locationId` is NOT required**.
3. **All fields are optional**.
4. To update the status, use `PUT /opportunities/:id/status` for a dedicated endpoint or update the `status` field in the main object.

---

> [!IMPORTANT]
> Always include the `Version: 2021-07-28` header when making these requests.
