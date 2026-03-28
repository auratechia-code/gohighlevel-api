---
title: "Update queue settings or status"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/update-queue"
generated_at: "2026-03-28T17:50:27.737646"
tags: ["api", "endpoint", "PUT"]
---

# Update queue settings or status

Updates queue status (active/paused/deleted), time slots, or skip dates.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### PHP
```php
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### JAVA
```java
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### GO
```go
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 200,  "results": {    "message": "Queue paused successfully.",    "queue": {      "_id": "60af88475f1b2c001f5d5f4b",      "locationId": "location-123",      "categoryId": "60af88475f1b2c001f5d5f4b",      "timeSlots": [        {          "dayOfWeek": 0,          "time": "09:00"        }      ],      "enableFuturePosts": false,      "prioritizeNewContent": false,      "currentOrder": 1000,      "status": "active",      "startDate": "2023-01-01T12:00:00Z",      "skipDateTime": [        "2023-01-02T12:00:00Z"      ],      "currentPostId": "60af88475f1b2c001f5d5f4b",      "totalPosts": 10,      "lastScheduledTime": "2023-01-01T12:00:00Z",      "createdBy": "user-123",      "createdAt": "2023-01-01T00:00:00Z",      "updatedAt": "2023-01-01T00:00:00Z"    }  },  "traceId": "string"}
```

