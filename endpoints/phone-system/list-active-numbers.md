---
title: "List active numbers"
source: "https://marketplace.gohighlevel.com/docs/ghl/phone-system/active-numbers"
generated_at: "2026-03-28T17:50:27.647098"
tags: ["api", "endpoint", "GET"]
---

# List active numbers

Retrieve a paginated list of active phone numbers for a specific location. Supports filtering, pagination, and optional exclusion of number pool assignments.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### NODEJS
```javascript
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### PYTHON
```python
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### PHP
```php
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### JAVA
```java
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### GO
```go
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### RUBY
```ruby
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

#### POWERSHELL
```powershell
{  "numbers": [    {      "phoneNumber": "+14155552671",      "friendlyName": "Sales Line 1",      "sid": "PN1234567890abcdef1234567890abcde",      "countryCode": "US",      "capabilities": {        "voice": true,        "sms": true,        "mms": true,        "fax": false      },      "type": "local",      "isDefaultNumber": false,      "linkedUser": "user_123456789",      "linkedRingAllUsers": [        "user_123",        "user_456"      ],      "inboundCallService": {        "type": "voice_ai",        "value": "68e381b296a83800a27cd1"      },      "forwardingNumber": "+14155552672",      "isGroupConversationEnabled": true,      "addressSid": "AD1234567890abcdef1234567890abcde",      "bundleSid": "BU1234567890abcdef1234567890abcde",      "dateAdded": "2023-01-15T10:30:00Z",      "dateUpdated": "2023-02-20T14:45:00Z",      "origin": "twilio"    }  ],  "isUnderGhl": true,  "pageSize": 100,  "page": 0,  "accountStatus": "active"}
```

