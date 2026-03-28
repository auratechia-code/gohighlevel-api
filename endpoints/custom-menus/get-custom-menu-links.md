---
title: "Get Custom Menu Links"
source: "https://marketplace.gohighlevel.com/docs/ghl/custom-menus/get-custom-menus"
generated_at: "2026-03-28T17:50:27.508453"
tags: ["api", "endpoint", "GET"]
---

# Get Custom Menu Links

Fetches a collection of custom menus based on specified criteria. This endpoint allows clients to retrieve custom menu configurations, which may include menu items, categories, and associated metadata. The response can be tailored using query parameters for filtering, sorting, and pagination.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### NODEJS
```javascript
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### PYTHON
```python
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### PHP
```php
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### JAVA
```java
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### GO
```go
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### RUBY
```ruby
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

#### POWERSHELL
```powershell
{  "customMenus": [    {      "id": "12345",      "icon": {        "name": "yin-yang",        "fontFamily": "fab"      },      "title": "Dashboard",      "url": "/dashboard",      "order": 1,      "showOnCompany": true,      "showOnLocation": true,      "showToAllLocations": true,      "locations": [        "gfWreTIHL8pDbggBb7af",        "67WreTIHL8pDbggBb7ty"      ],      "openMode": "iframe",      "userRole": "all",      "allowCamera": false,      "allowMicrophone": false    }  ],  "totalLinks": 100}
```

