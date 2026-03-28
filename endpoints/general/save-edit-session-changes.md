---
title: "Save edit session changes"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/save-edit-session"
generated_at: "2026-03-28T17:50:27.729592"
tags: ["api", "endpoint", "POST"]
---

# Save edit session changes

Applies all staged changes to the live queue and closes the edit session.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### PHP
```php
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### JAVA
```java
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### GO
```go
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 200,  "results": {    "message": "Edit session saved successfully",    "updatedSlots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "totalPostsChanged": 10  },  "traceId": "string"}
```

