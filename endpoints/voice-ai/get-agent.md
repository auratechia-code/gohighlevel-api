---
title: "Get Agent"
source: "https://marketplace.gohighlevel.com/docs/ghl/voice-ai/get-agent"
generated_at: "2026-03-28T17:50:27.766908"
tags: ["api", "endpoint", "GET"]
---

# Get Agent

Retrieve detailed configuration and settings for a specific voice AI agent

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### NODEJS
```javascript
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### PYTHON
```python
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### PHP
```php
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### JAVA
```java
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### GO
```go
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### RUBY
```ruby
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

#### POWERSHELL
```powershell
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  },  "actions": [    {      "_id": "507f1f77bcf86cd799439011",      "actionType": "CALL_TRANSFER",      "name": "Transfer to Manager",      "actionParameters": {        "triggerPrompt": "When caller asks for manager",        "triggerMessage": "Let me transfer you",        "transferToType": "number",        "transferToValue": "+1234567890"      }    }  ]}
```

