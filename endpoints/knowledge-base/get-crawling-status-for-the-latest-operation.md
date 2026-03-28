---
title: "Get crawling status for the latest operation"
source: "https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/get-crawling-status-for-latest-operation"
generated_at: "2026-03-28T17:50:27.560598"
tags: ["api", "endpoint", "GET"]
---

# Get crawling status for the latest operation

Get crawling status for the latest operation

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### NODEJS
```javascript
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### PYTHON
```python
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### PHP
```php
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### JAVA
```java
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### GO
```go
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### RUBY
```ruby
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

#### POWERSHELL
```powershell
{  "success": true,  "data": {    "aggregate": [      {        "_id": "Failed",        "records": [          {            "url": "https://developer.mozilla.org/en-US/blog/rss.xml",            "id": "688e41118a188704914d13c0",            "title": "JavaScript Temporal is coming | MDN Blog",            "error": {              "stack": "HttpException: Failed to fetch HTML content\n    at getHtml (/app/dist/apps/conversations-ai/crm-conversations-ai-discover-worker.js:2531:15)",              "response": "Failed to fetch HTML content",              "status": 500,              "options": null,              "message": "Failed to fetch HTML content",              "name": "HttpException"            }          }        ]      }    ],    "operationDetails": {      "discoveredUrlsCount": 66,      "trainedUrlsCount": 0,      "_id": "688e410c8a18870ecf4d13bb",      "locationId": "nnAzVJqSv6PJ1p6zrhvC",      "status": "Pending",      "url": "https://developer.mozilla.org/en-US/blog/",      "mode": "Path",      "knowledgeBaseId": "CCNPhKqSCkTOG8O7dtbq",      "createdAt": "2025-08-02T16:47:08.182Z",      "updatedAt": "2025-08-02T16:48:43.635Z",      "__v": 0,      "robotsFileData": "User-agent: *\nSitemap: https://developer.mozilla.org/sitemap.xml\nDisallow: /api/"    }  }}
```

