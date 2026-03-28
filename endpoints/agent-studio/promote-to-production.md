---
title: "Promote to Production"
source: "https://marketplace.gohighlevel.com/docs/ghl/agent-studio/promote-and-publish"
generated_at: "2026-03-28T17:50:27.384914"
tags: ["api", "endpoint", "POST"]
---

# Promote to Production

Promotes a draft version to production.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### NODEJS
```javascript
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### PYTHON
```python
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### PHP
```php
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### JAVA
```java
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### GO
```go
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### RUBY
```ruby
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

#### POWERSHELL
```powershell
{  "success": true,  "message": "Draft published to production successfully. New draft version created for future edits.",  "data": {    "productionVersion": {      "versionId": "v1a2b3c4d5e6f7g8h9i0",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v2",      "state": "prod",      "isPublished": true,      "version": 2,      "publishedAt": "2024-02-27T12:00:00.000Z",      "publishedBy": "usr_abc123def456",      "publishedByName": "John Doe",      "publishedByEmail": "john.doe@example.com"    },    "newDraftVersion": {      "versionId": "v2b3c4d5e6f7g8h9i0j1",      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "versionName": "Customer Support Agent v3",      "state": "draft",      "isPublished": false,      "version": 3,      "createdAt": "2024-02-27T12:00:00.000Z"    }  }}
```

