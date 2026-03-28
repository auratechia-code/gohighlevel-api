---
title: "Update Action"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/update-action"
generated_at: "2026-03-28T17:50:27.481372"
tags: ["api", "endpoint", "PUT"]
---

# Update Action

Updates an existing action's configuration. This includes modifying the action name, description, trigger conditions, and behavior settings.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
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

