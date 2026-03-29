# Webhook Events: Opportunities

Documentation for events related to Opportunity management.

## Opportunity Created (`OpportunityCreate`)

Triggered whenever a new opportunity is added to a pipeline.

### Trigger Details
- **Type**: `OpportunityCreate`
- **Condition**: New record added to `POST /opportunities/`.

### Example Payload
```json
{
  "type": "OpportunityCreate",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "opp_123",
  "contactId": "mTkSCb1UBjb5tk4OvB69",
  "monetaryValue": 150,
  "name": "New Deal",
  "pipelineId": "pip_456",
  "pipelineStageId": "stage_789",
  "source": "Google Ads",
  "status": "open",
  "dateAdded": "2024-03-29T12:00:00.000Z"
}
```

---

## Opportunity Status Changed (`OpportunityStatusUpdate`)

Triggered whenever an opportunity status is updated (e.g., to `Won` or `Lost`).

### Trigger Details
- **Type**: `OpportunityStatusUpdate`
- **Condition**: Status field modified.

### Example Payload
```json
{
  "type": "OpportunityStatusUpdate",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "id": "opp_123",
  "assignedTo": "user_789",
  "contactId": "mTkSCb1UBjb5tk4OvB69",
  "monetaryValue": 250,
  "name": "Updated Deal",
  "pipelineId": "pip_456",
  "pipelineStageId": "stage_789",
  "source": "Referral",
  "status": "won",
  "dateAdded": "2024-03-29T12:00:00.000Z"
}
```
