---
title: "Update Redirect By Id"
source: "https://marketplace.gohighlevel.com/docs/ghl/funnels/update-redirect-by-id"
generated_at: "2026-03-28T17:50:27.526628"
tags: ["api", "endpoint", "PATCH"]
---

# Update Redirect By Id

The "Update Redirect By Id" API Allows updating an existing URL redirect in the system. Use this endpoint to modify a URL redirect with the specified ID using details provided in the request payload.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PATCH`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### NODEJS
```javascript
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### PYTHON
```python
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### PHP
```php
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### JAVA
```java
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### GO
```go
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### RUBY
```ruby
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

#### POWERSHELL
```powershell
{  "data": {    "id": "6p2RxpgtMKQwO3E6IUaT",    "locationId": "6p2RxpgtMKQwO3E6IUaT",    "domain": "www.example.com",    "path": "/old-path",    "pathLowercase": "/old-path",    "type": "Permanent",    "target": "https://www.example.com/new-path",    "action": "url"  }}
```

