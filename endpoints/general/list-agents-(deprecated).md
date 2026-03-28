---
title: "List Agents (Deprecated)"
source: "https://marketplace.gohighlevel.com/docs/ghl/agent-studio/get-agents-deprecated"
generated_at: "2026-03-28T17:50:27.384396"
tags: ["api", "endpoint", "GET"]
---

# List Agents (Deprecated)

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### NODEJS
```javascript
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### PYTHON
```python
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### PHP
```php
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### JAVA
```java
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### GO
```go
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### RUBY
```ruby
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

#### POWERSHELL
```powershell
{  "success": true,  "message": "Agents retrieved successfully",  "agents": [    {      "agentId": "p1q2r3s4t5u6v7w8x9y0z1a2",      "name": "Marketing Assistant",      "description": "AI agent specialized in marketing strategy and content creation",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-15T10:30:00.000Z",      "updatedAt": "2024-02-20T14:45:00.000Z"    },    {      "agentId": "b3c4d5e6f7g8h9i0j1k2l3m4",      "name": "Customer Support Bot",      "description": "AI agent for handling customer inquiries and support tickets",      "locationId": "C2QujeCh8ZnC7al2InWR",      "status": "active",      "createdAt": "2024-01-10T09:15:00.000Z",      "updatedAt": "2024-02-18T16:20:00.000Z"    }  ],  "pagination": {    "total": 25,    "limit": 20,    "offset": 0,    "hasMore": true  }}
```

