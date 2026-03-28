---
title: "Execute Agent"
source: "https://marketplace.gohighlevel.com/docs/ghl/agent-studio/execute-agent"
generated_at: "2026-03-28T17:50:27.381117"
tags: ["api", "endpoint", "POST"]
---

# Execute Agent

Executes the specified agent and returns a non-streaming JSON response with the complete agent output. The agent must be in active status and belong to the specified location. locationId is required in the request body.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### NODEJS
```javascript
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### PYTHON
```python
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### PHP
```php
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### JAVA
```java
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### GO
```go
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### RUBY
```ruby
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

#### POWERSHELL
```powershell
{  "success": true,  "executionId": "a1b2c3d4e5f6g7h8i9j0k1l2",  "interactionId": "m9n8o7p6q5r4s3t2u1v0w9x8",  "response": "I can help you with various tasks...",  "type": "text",  "nextExpectedInput": "text",  "goalCompletion": false,  "executionStatus": "completed",  "flowSwitch": false,  "attachments": [],  "generativeOutputs": []}
```

