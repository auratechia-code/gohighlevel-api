---
title: "Attach Action to Agent"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/create-action"
generated_at: "2026-03-28T17:50:27.475730"
tags: ["api", "endpoint", "POST"]
---

# Attach Action to Agent

Creates and attach a new action for an AI agent. Actions define specific tasks or behaviors that the agent can perform, such as booking appointments, sending follow-ups, or collecting information.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
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

