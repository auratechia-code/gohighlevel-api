---
title: "Fetch slot information for queue items"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-slots"
generated_at: "2026-03-28T17:50:27.712677"
tags: ["api", "endpoint", "POST"]
---

# Fetch slot information for queue items

Returns paginated slot information (scheduledDateTime, isSkipped) for queue items. Pass sessionId to get slots for draft items, or omit for live items. Call this after mutations to refresh slot data.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### PHP
```php
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### JAVA
```java
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### GO
```go
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 200,  "results": {    "message": "Slots fetched successfully",    "slots": [      {        "itemId": "60af88475f1b2c001f5d5f4b",        "scheduledDateTime": "2023-10-15T10:00:00.000Z",        "isSkipped": false      }    ],    "total": 100,    "skip": 0,    "limit": 20,    "timezone": "America/New_York"  },  "traceId": "string"}
```

