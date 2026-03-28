---
title: "Update Custom Menu Link"
source: "https://marketplace.gohighlevel.com/docs/ghl/custom-menus/update-custom-menu"
generated_at: "2026-03-28T17:50:27.510030"
tags: ["api", "endpoint", "PUT"]
---

# Update Custom Menu Link

Updates an existing custom menu for a given company. Requires authentication and proper permissions.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### NODEJS
```javascript
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### PYTHON
```python
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### PHP
```php
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### JAVA
```java
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### GO
```go
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### RUBY
```ruby
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### POWERSHELL
```powershell
{  "success": true,  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

