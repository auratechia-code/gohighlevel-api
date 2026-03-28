---
title: "Update Agent"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/update-agent"
generated_at: "2026-03-28T17:50:27.481924"
tags: ["api", "endpoint", "PUT"]
---

# Update Agent

Updates an existing AI agent's configuration. All fields in the agent configuration can be updated including name, status, actions, and behavior settings.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### NODEJS
```javascript
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### PYTHON
```python
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### PHP
```php
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### JAVA
```java
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### GO
```go
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### RUBY
```ruby
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

#### POWERSHELL
```powershell
{  "id": "emp_123",  "name": "John Doe",  "businessName": "Tech Corp",  "mode": "auto-pilot",  "channels": [    "SMS",    "Live_Chat"  ],  "waitTime": 30,  "waitTimeUnit": "seconds",  "sleepEnabled": false,  "sleepTime": 2,  "sleepTimeUnit": "hours",  "actions": [    {      "id": "actionId123",      "type": "triggerWorkflow"    }  ],  "isPrimary": false,  "autoPilotMaxMessages": 25,  "goal": "Assist customers with inquiries",  "personality": "Friendly and helpful",  "instructions": "Provide excellent customer service",  "knowledgeBaseIds": [    "kb_123",    "kb_456"  ]}
```

