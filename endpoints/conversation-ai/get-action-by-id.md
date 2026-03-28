---
title: "Get Action by ID"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/get-action-by-id"
generated_at: "2026-03-28T17:50:27.478231"
tags: ["api", "endpoint", "GET"]
---

# Get Action by ID

Retrieves detailed information about a specific action using its unique identifier. Returns the action configuration, associated agents, and performance metrics.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### NODEJS
```javascript
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### PYTHON
```python
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### PHP
```php
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### JAVA
```java
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### GO
```go
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### RUBY
```ruby
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

#### POWERSHELL
```powershell
{  "data": {    "id": "actionId123",    "name": "Trigger Workflow",    "type": "triggerWorkflow",    "agentId": "agentId123",    "details": {      "workflowIds": [        "workflow123",        "workflow456"      ],      "triggerCondition": "When user requests appointment",      "triggerMessage": "Workflow triggered successfully"    }  },  "success": true}
```

