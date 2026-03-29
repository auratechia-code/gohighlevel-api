# Webhook: PaymentSuccess

**Category:** Payments

## Trigger Source
This event is triggered when a paymentsuccess action occurs in the GHL Location.

## Sample Payload
```json
{
  "type": "PaymentSuccess",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "txn_123",
  "transactionId": "txn_123",
  "amount": 9700,
  "currency": "USD",
  "source": "Stripe",
  "dateAdded": "2024-03-29T13:15:00.000Z"
}
```

## Schema Details
| Field | Type | Description |
|-------|------|-------------|
| `type` | String | Event type constant. |
| `locationId` | String | Sub-account ID. |
| `id` | String | Unique event ID. |
| `transactionId` | String | See sample for context. |
| `contactId` | String | See sample for context. |
| `amount` | String | See sample for context. |
| `currency` | String | See sample for context. |
| `source` | String | See sample for context. |
