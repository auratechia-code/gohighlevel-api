---
title: "Create White-label Integration Provider"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/create-integration-provider"
generated_at: "2026-03-28T17:50:27.632283"
tags: ["api", "endpoint", "POST"]
---

# Create White-label Integration Provider

The "Create White-label Integration Provider" API allows adding a new payment provider integration to the system which is built on top of Authorize.net or NMI. Use this endpoint to create a integration provider with the specified details. Ensure that the required information is provided in the request payload. This endpoint can be only invoked using marketplace-app token

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### NODEJS
```javascript
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### PYTHON
```python
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### PHP
```php
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### JAVA
```java
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### GO
```go
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### RUBY
```ruby
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

#### POWERSHELL
```powershell
{  "_id": "65cb47dda50f4f13ced4b870",  "altId": "Z4Bxl8J4SaPEPLq9IQ8g",  "altType": "location",  "title": "Example",  "route": "epd",  "provider": "nmi",  "description": "Lorem",  "imageUrl": "https://example.com/assets/pmd/img/payments/nmi-logo.webp",  "createdAt": "2024-02-13T10:43:41.026Z",  "updatedAt": "2024-02-13T10:43:41.026Z"}
```

