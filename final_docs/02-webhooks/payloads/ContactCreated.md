# Webhook: ContactCreated

**Category:** Contacts

## Trigger Source
This event is triggered when a contactcreated action occurs in the GHL Location.

## Sample Payload
```json
{
  "type": "ContactCreated",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "cont_123",
  "contactId": "cont_123",
  "email": "john.doe@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "dateAdded": "2024-03-29T12:00:00.000Z"
}
```

## Schema Details
| Field | Type | Description |
|-------|------|-------------|
| `type` | String | Event type constant. |
| `locationId` | String | Sub-account ID. |
| `id` | String | Unique event ID. |
| `contactId` | String | See sample for context. |
| `email` | String | See sample for context. |
| `phone` | String | See sample for context. |
| `firstName` | String | See sample for context. |
| `lastName` | String | See sample for context. |
