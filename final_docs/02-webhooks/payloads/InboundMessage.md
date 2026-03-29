# Webhook: InboundMessage

**Category:** Messages

## Trigger Source
This event is triggered when a inboundmessage action occurs in the GHL Location.

## Sample Payload
```json
{
  "type": "InboundMessage",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "msg_456",
  "messageId": "msg_456",
  "contactId": "cont_123",
  "body": "Hello, I need help with my booking.",
  "direction": "inbound",
  "sourceType": "SMS",
  "dateAdded": "2024-03-29T12:30:00.000Z"
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
