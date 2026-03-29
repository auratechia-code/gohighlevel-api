# Webhook: WorkflowStatusChanged

**Category:** Workflows

## Trigger Source
This event is triggered when a workflowstatuschanged action occurs in the GHL Location.

## Sample Payload
```json
{
  "type": "WorkflowStatusChanged",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "wf_active_1",
  "workflowId": "wf_456",
  "contactId": "cont_123",
  "status": "active",
  "currentStepId": "step_789",
  "dateAdded": "2024-03-29T13:30:00.000Z"
}
```

## Schema Details
| Field | Type | Description |
|-------|------|-------------|
| `type` | String | Event type constant. |
| `locationId` | String | Sub-account ID. |
| `id` | String | Unique event ID. |
| `workflowId` | String | See sample for context. |
| `contactId` | String | See sample for context. |
| `status` | String | See sample for context. |
| `currentStepId` | String | See sample for context. |
