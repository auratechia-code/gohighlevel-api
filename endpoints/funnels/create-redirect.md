---
title: "Create Redirect"
source: "https://marketplace.gohighlevel.com/docs/ghl/funnels/create-redirect"
generated_at: "2026-03-28T17:50:27.521862"
tags: ["api", "endpoint", "POST"]
---

# Create Redirect

The "Create Redirect" API Allows adding a new url redirect to the system. Use this endpoint to create a url redirect with the specified details. Ensure that the required information is provided in the request payload.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
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

