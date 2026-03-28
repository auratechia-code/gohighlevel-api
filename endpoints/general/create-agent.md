---
title: "Create Agent"
source: "https://marketplace.gohighlevel.com/docs/ghl/voice-ai/create-agent"
generated_at: "2026-03-28T17:50:27.764386"
tags: ["api", "endpoint", "POST"]
---

# Create Agent

Create a new voice AI agent configuration and settings

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### NODEJS
```javascript
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### PYTHON
```python
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### PHP
```php
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### JAVA
```java
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### GO
```go
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### RUBY
```ruby
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

#### POWERSHELL
```powershell
{  "id": "507f1f77bcf86cd799439011",  "locationId": "LOC123456789ABCDEF",  "agentName": "Customer Support Agent",  "businessName": "Acme Corporation",  "welcomeMessage": "Hello! Thank you for calling. How can I assist you today?",  "agentPrompt": "You are a helpful customer service representative.",  "voiceId": "507f1f77bcf86cd799439011",  "language": "en-US",  "patienceLevel": "medium",  "maxCallDuration": 600,  "sendUserIdleReminders": true,  "reminderAfterIdleTimeSeconds": 5,  "inboundNumber": "+1234567890",  "numberPoolId": "pool_507f1f77bcf86cd799439011",  "callEndWorkflowIds": [],  "sendPostCallNotificationTo": {    "admins": true,    "allUsers": false,    "contactAssignedUser": false,    "specificUsers": [],    "customEmails": []  },  "agentWorkingHours": [],  "timezone": "America/New_York",  "isAgentAsBackupDisabled": false,  "translation": {    "enabled": false,    "language": "es"  }}
```

