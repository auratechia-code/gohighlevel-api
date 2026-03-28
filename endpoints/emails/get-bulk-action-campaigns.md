---
title: "Get Bulk Action Campaigns"
source: "https://marketplace.gohighlevel.com/docs/ghl/emails/fetch-bulk-action-campaigns"
generated_at: "2026-03-28T17:50:27.512918"
tags: ["api", "endpoint", "GET"]
---

# Get Bulk Action Campaigns

Get list of bulk action campaigns for a location

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### NODEJS
```javascript
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### PYTHON
```python
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### PHP
```php
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### JAVA
```java
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### GO
```go
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### RUBY
```ruby
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

#### POWERSHELL
```powershell
{  "campaigns": [    {      "id": "OI72xYec4Mho6VBykTvj",      "name": "Test Mail",      "status": "complete",      "scheduleType": "NOW",      "createdBy": "John Doe",      "deleted": false,      "createdAt": "2025-07-24T11:55:43.598Z",      "updatedAt": "2026-02-09T04:49:12.322Z",      "completedAt": "2025-07-24T11:55:48.000Z",      "emailMetadata": {        "subject": "Welcome to our platform",        "from": "John Doe <john@example.com>",        "name": "John Doe",        "templateId": "6790aeb53c8d1288f555f92b"      }    }  ],  "total": 25}
```

