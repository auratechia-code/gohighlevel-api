# Contact Body Parameters (V2)

Highly accurate body parameter mapping for Contact operations.

## Create Contact (`POST /contacts/`)

The following fields are supported in the request body.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `locationId` | String | **YES** | The unique ID of the sub-account. |
| `firstName` | String | No | First name of the contact. |
| `lastName` | String | No | Last name of the contact. |
| `email` | String | No | Primary email address. Must be unique within the location if deduplication is enabled. |
| `phone` | String | No | Primary phone number (E.164 format recommended). |
| `address1` | String | No | Street address. |
| `city` | String | No | City. |
| `state` | String | No | State or Province. |
| `postalCode` | String | No | Zip or Postal code. |
| `country` | String | No | Country. |
| `website` | String | No | Website URL. |
| `timezone` | String | No | Timezone (e.g., `America/New_York`). |
| `dnd` | Boolean | No | Set global DND status. |
| `dndSettings` | Object | No | Granular DND settings for Mail, SMS, etc. |
| `tags` | Array | No | Array of tag strings. |
| `customFields` | Array | No | Array of objects: `{ "id": "fieldId", "value": "value" }`. |
| `source` | String | No | Original source of the contact. |
| `companyName` | String | No | Associated company name. |
| `assignedTo` | String | No | User ID to whom the contact is assigned. |

---

## Update Contact (`PUT /contacts/:contactId`)

The update operation uses the **same schema** as the Create operation, with the following rules:

1. **`locationId` is NOT required**: The contact is already scoped to a location via its ID.
2. **All fields are Nullable/Optional**: Only provide the fields you wish to update.
3. **Tags**: Sending the `tags` array will typically **append** or **overwrite** depending on the specific integration settings. It is safer to use the granular `/tags` endpoints for precise management.

---

> [!IMPORTANT]
> Always include the `Version: 2021-07-28` header when making these requests.
