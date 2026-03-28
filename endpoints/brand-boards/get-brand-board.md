---
title: "Get Brand Board"
source: "https://marketplace.gohighlevel.com/docs/ghl/brand-boards/get-brand-board-by-id"
generated_at: "2026-03-28T17:50:27.401729"
tags: ["api", "endpoint", "GET"]
---

# Get Brand Board

Retrieves a specific Brand Board by its ID

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### NODEJS
```javascript
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### PYTHON
```python
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### PHP
```php
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### JAVA
```java
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### GO
```go
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### RUBY
```ruby
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

#### POWERSHELL
```powershell
{  "_id": "507f1f77bcf86cd799439011",  "locationId": "ve9EPM428h8vShlRW1KT",  "name": "My Brand Board",  "logos": [    {      "id": "logo_abc123",      "url": "https://storage.googleapis.com/bucket/logos/my-logo.png",      "label": "Primary Logo",      "path": "/locations/ve9EPM428h8vShlRW1KT/logos/my-logo.png"    }  ],  "colors": [    {      "id": "color_xyz789",      "hexa": "#FF5733FF",      "rgba": "rgba(255, 87, 51, 1)",      "hex": "#FF5733",      "rgb": "rgb(255, 87, 51)",      "label": "Brand Orange"    }  ],  "fonts": [    {      "id": "font_def456",      "font": "Montserrat",      "fallback": "sans-serif",      "label": "Heading Font"    }  ],  "default": false,  "deleted": false,  "parentId": "507f1f77bcf86cd799439011",  "folderId": "507f1f77bcf86cd799439011",  "originId": "507f1f77bcf86cd799439011",  "meta": {    "updatedBy": "user_abc123",    "lastAction": "UPDATE",    "sourceId": "507f1f77bcf86cd799439011",    "sourceType": "blank"  },  "createdAt": "2024-01-05T12:00:00.000Z",  "updatedAt": "2024-01-05T12:00:00.000Z"}
```

