---
title: "Create a new category queue"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/create-queue"
generated_at: "2026-03-28T17:50:27.704604"
tags: ["api", "endpoint", "POST"]
---

# Create a new category queue

Creates a queue in draft status for a category. Published posts are auto-added. Use update endpoint to activate.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### PHP
```php
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### JAVA
```java
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### GO
```go
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queue created successfully",    "queue": {      "_id": "686ebf10c78c233e45c28d66",      "locationId": "Qp26qppJgfrTZis7jsBy",      "categoryId": "683702938b19583ce320e5eb",      "timeSlots": [        {          "_id": "686ebf10c78c23d665c28d67",          "dayOfWeek": 0,          "time": "00:00"        }      ],      "enableFuturePosts": true,      "prioritizeNewContent": true,      "status": "draft",      "startDate": "2025-07-09T19:12:16.363Z",      "skipDateTime": [],      "totalPosts": 0,      "lastScheduledTime": null,      "createdBy": "uefV3MmLHs2sjJr2KfmL",      "createdAt": "2025-07-09T19:12:16.366Z",      "updatedAt": "2025-07-09T19:12:16.366Z"    }  },  "traceId": "string"}
```

