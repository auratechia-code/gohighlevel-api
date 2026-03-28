---
title: "Search Agents"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/search-agent"
generated_at: "2026-03-28T17:50:27.480674"
tags: ["api", "endpoint", "GET"]
---

# Search Agents

Searches for AI agents based on various criteria including name, status, and configuration. Supports advanced filtering and full-text search capabilities.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### NODEJS
```javascript
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### PYTHON
```python
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### PHP
```php
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### JAVA
```java
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### GO
```go
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### RUBY
```ruby
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

#### POWERSHELL
```powershell
{  "agents": [    {      "id": "emp_123",      "name": "John Doe",      "businessName": "Tech Corp",      "mode": "auto-pilot",      "channels": [        "SMS",        "LIVE_CHAT"      ],      "waitTime": 30,      "waitTimeUnit": "seconds",      "sleepEnabled": false,      "sleepTime": 2,      "sleepTimeUnit": "hours",      "actions": [        {          "id": "action_123",          "type": "triggerWorkflow"        }      ],      "isPrimary": false,      "autoPilotMaxMessages": 25,      "goal": {        "prompt": "Assist customers",        "type": "custom",        "actionId": null      },      "knowledgeBaseIds": [        "kb_123",        "kb_456"      ],      "createdAt": "2024-01-01T00:00:00Z",      "updatedAt": "2024-01-01T00:00:00Z"    }  ],  "totalCount": 100,  "count": 25}
```

