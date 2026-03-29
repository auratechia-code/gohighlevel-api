# Webhook: CallStatusChanged

**Category:** Messages

## Trigger Source
This event is triggered when a callstatuschanged action occurs in the GHL Location.

## Sample Payload
```json
{
  "type": "CallStatusChanged",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "call_000",
  "callId": "call_000",
  "contactId": "cont_123",
  "callStatus": "answered",
  "direction": "inbound",
  "duration": 120,
  "dateAdded": "2024-03-29T13:00:00.000Z"
}
```

## Schema Details
| Field | Type | Description |
|-------|------|-------------|
| `type` | String | Event type constant. |
| `locationId` | String | Sub-account ID. |
| `id` | String | Unique event ID. |
| `callId` | String | See sample for context. |
| `contactId` | String | See sample for context. |
| `callStatus` | String | See sample for context. |
| `direction` | String | See sample for context. |
| `duration` | String | See sample for context. |
