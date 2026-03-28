---
title: "Get all categories with their queue status"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/fetch-available-categories"
generated_at: "2026-03-28T17:50:27.709631"
tags: ["api", "endpoint", "GET"]
---

# Get all categories with their queue status

Returns categories with status: "available" (no queue), "in_queue" (active/paused queue), or "draft" (queue in draft).

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### PHP
```php
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### JAVA
```java
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### GO
```go
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 200,  "results": {    "message": "Available categories fetched successfully",    "categories": [      {        "deleted": false,        "_id": "65cb3d2f68baa617aa0c286e",        "name": "Facebook Reel",        "locationId": "fvg1TXIiVxGcdOaL0riG",        "primaryColor": "#004EEB",        "secondaryColor": "#EFF4FF",        "createdBy": "SQ6d63Va2PUbWEZ9k0TD",        "createdAt": "2024-02-13T09:58:07.129Z",        "updatedAt": "2024-02-13T09:58:07.129Z",        "publishedPostsCount": 80,        "status": "in_queue",        "queueDetails": {          "queueId": "67fc07c6d7657c9aee764762",          "prioritizeNewContent": false,          "enableFuturePosts": true        }      }    ],    "meta": {      "count": "100"    }  },  "traceId": "string"}
```

