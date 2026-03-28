---
title: "Get notification"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/find-event-notification"
generated_at: "2026-03-28T17:50:27.426145"
tags: ["api", "endpoint", "GET"]
---

# Get notification

Find Event notification by notificationId

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### NODEJS
```javascript
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### PYTHON
```python
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### PHP
```php
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### JAVA
```java
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### GO
```go
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### RUBY
```ruby
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

#### POWERSHELL
```powershell
{  "_id": "string",  "receiverType": "contact",  "additionalEmailIds": [    "example1@email.com",    "example2@email.com"  ],  "additionalPhoneNumbers": [    "+919876744444",    "+919876744445"  ],  "channel": "email",  "notificationType": "confirmation",  "isActive": true,  "additionalWhatsappNumbers": [    "+919876744444",    "+919876744445"  ],  "templateId": "0as9d8as0d",  "body": "This is a test notification",  "subject": "Test Notification",  "afterTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "beforeTime": [    {      "timeOffset": 1,      "unit": "hours"    }  ],  "selectedUsers": [    "user1",    "user2"  ],  "deleted": false}
```

