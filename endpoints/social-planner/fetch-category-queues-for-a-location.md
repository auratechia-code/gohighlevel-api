---
title: "Fetch category queues for a location"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-queues"
generated_at: "2026-03-28T17:50:27.712190"
tags: ["api", "endpoint", "POST"]
---

# Fetch category queues for a location

Retrieves a paginated list of all category queues for a given location, excluding any that have been marked as deleted.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### PHP
```php
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### JAVA
```java
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### GO
```go
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 201,  "results": {    "message": "Queues fetched successfully",    "queues": [      {        "_id": "60af88475f1b2c001f5d5f4b",        "locationId": "location-123",        "categoryId": "60af88475f1b2c001f5d5f4b",        "timeSlots": [          {            "dayOfWeek": 0,            "time": "09:00"          }        ],        "enableFuturePosts": false,        "prioritizeNewContent": false,        "currentOrder": 1000,        "status": "active",        "startDate": "2023-01-01T12:00:00Z",        "skipDateTime": [          "2023-01-02T12:00:00Z"        ],        "currentPostId": "60af88475f1b2c001f5d5f4b",        "totalPosts": 10,        "lastScheduledTime": "2023-01-01T12:00:00Z",        "createdBy": "user-123",        "createdAt": "2023-01-01T00:00:00Z",        "updatedAt": "2023-01-01T00:00:00Z",        "category": {          "_id": "6756f381be2553245b08d30c",          "name": "Category Name",          "primaryColor": "#FFFFFF",          "secondaryColor": "#000000",          "deleted": false,          "locationId": "fvg1TXIiVxGcdOaL0riG",          "createdBy": "SQ6d63Va2PUbWEZ9k0TD",          "createdAt": "2024-12-09T13:41:21.385Z",          "updatedAt": "2024-12-09T13:41:21.385Z"        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

