---
title: "Attach facebook pages"
source: "https://marketplace.gohighlevel.com/docs/ghl/social-planner/attach-facebook-page-group"
generated_at: "2026-03-28T17:50:27.696870"
tags: ["api", "endpoint", "POST"]
---

# Attach facebook pages

Attach facebook pages

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### NODEJS
```javascript
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### PYTHON
```python
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### PHP
```php
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### JAVA
```java
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### GO
```go
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### RUBY
```ruby
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

#### POWERSHELL
```powershell
{  "success": true,  "statusCode": 201,  "message": "Added Facebook Account",  "results": {    "_id": "65f2d989a4f2f1e5322c3856",    "oAuthId": "u37swmmLbA02zgqKPpxITe2",    "oldId": "u37swmmLbA02zgqKPpxITe2",    "locationId": "u37swmmLbA02zgqKPpxITe2",    "originId": "u37swmmLbA02zgqKPpxITe2",    "platform": "facebook",    "type": "page",    "name": "Account Name",    "avatar": "u37swmmLbA02zgqKPpxITe2",    "meta": {      "pageId": "u37swmmLbA02zgqKPpxITe2",      "page": {        "id": "u37swmmLbA02zgqKPpxITe2",        "name": "Account Name",        "avatar": "u37swmmLbA02zgqKPpxITe2"      },      "storeCode": "122",      "isVerified": "true",      "verified": true,      "protected": true,      "locationId": "u37swmmLbA02zgqKPpxITe2",      "accountId": "u37swmmLbA02zgqKPpxITe2",      "openId": "u37swmmLbA02zgqKPpxITe2",      "urn": "u37swmmLbA02zgqKPpxITe2",      "username": "testUser",      "storefrontAddress": {        "regionCode": "30021",        "languageCode": "E001",        "postalCode": "1221",        "administrativeArea": "Down Town",        "locality": "Louis Street",        "addressLines": [          "207",          "county"        ]      }    },    "active": true,    "deleted": true,    "createdAt": "2024-03-14T11:03:37.015Z",    "updatedAt": "2024-03-14T11:03:37.015Z"  }}
```

