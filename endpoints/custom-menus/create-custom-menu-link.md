---
title: "Create Custom Menu Link"
source: "https://marketplace.gohighlevel.com/docs/ghl/custom-menus/create-custom-menu"
generated_at: "2026-03-28T17:50:27.507003"
tags: ["api", "endpoint", "POST"]
---

# Create Custom Menu Link

Creates a new custom menu for a company. Requires authentication and proper permissions. For Icon Usage Details please refer tohttps://doc.clickup.com/8631005/d/h/87cpx-243696/d60fa70db6b92b2

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### NODEJS
```javascript
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### PYTHON
```python
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### PHP
```php
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### JAVA
```java
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### GO
```go
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### RUBY
```ruby
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

#### POWERSHELL
```powershell
{  "customMenu": {    "id": "12345",    "icon": {      "name": "yin-yang",      "fontFamily": "fab"    },    "title": "Dashboard",    "url": "/dashboard",    "order": 1,    "showOnCompany": true,    "showOnLocation": true,    "showToAllLocations": true,    "locations": [      "gfWreTIHL8pDbggBb7af",      "67WreTIHL8pDbggBb7ty"    ],    "openMode": "iframe",    "userRole": "all",    "allowCamera": false,    "allowMicrophone": false  }}
```

