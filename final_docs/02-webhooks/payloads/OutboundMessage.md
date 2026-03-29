# Webhook: OutboundMessage

**Category:** Messages

## Trigger Source
This event is triggered when a outboundmessage action occurs in the GHL Location.

## Sample Payload
```json
{
  "type": "OutboundMessage",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "msg_789",
  "messageId": "msg_789",
  "contactId": "cont_123",
  "body": "Hi John, we've updated your ticket.",
  "direction": "outbound",
  "sourceType": "EMAIL",
  "status": "sent",
  "dateAdded": "2024-03-29T12:45:00.000Z"
}
```

## Schema Details
| Field | Type | Description |
|-------|------|-------------|
| `type` | String | Event type constant. |
| `locationId` | String | Sub-account ID. |
| `id` | String | Unique event ID. |
| `messageId` | String | See sample for context. |
| `contactId` | String | See sample for context. |
| `body` | String | See sample for context. |
| `direction` | String | See sample for context. |
| `sourceType` | String | See sample for context. |
| `status` | String | See sample for context. |
