---
title: "Create Agent Action"
source: "https://marketplace.gohighlevel.com/docs/ghl/voice-ai/create-action"
generated_at: "2026-03-28T17:50:27.763846"
tags: ["api", "endpoint", "POST"]
---

# Create Agent Action

Create a new action for a voice AI agent. Actions define specific behaviors and capabilities for the agent during calls.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### NODEJS
```javascript
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### PYTHON
```python
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### PHP
```php
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### JAVA
```java
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### GO
```go
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### RUBY
```ruby
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

#### POWERSHELL
```powershell
{  "id": "507f1f77bcf86cd799439011",  "actionType": "CALL_TRANSFER",  "name": "Transfer to Manager",  "actionParameters": {    "triggerPrompt": "When the caller asks to speak to a manager",    "transferToType": "number",    "transferToValue": "+12345678901",    "triggerMessage": "Let me transfer you to a manager right away",    "hearWhisperMessage": true  }}
```

