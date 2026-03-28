---
title: "Get Campaigns"
source: "https://marketplace.gohighlevel.com/docs/ghl/emails/fetch-campaigns"
generated_at: "2026-03-28T17:50:27.513828"
tags: ["api", "endpoint", "GET"]
---

# Get Campaigns

Get Campaigns

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### NODEJS
```javascript
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### PYTHON
```python
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### PHP
```php
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### JAVA
```java
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### GO
```go
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### RUBY
```ruby
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

#### POWERSHELL
```powershell
{  "schedules": [    {      "name": "Untitled new campaign",      "repeatAfter": "string",      "id": "string",      "parentId": "string",      "childCount": 0,      "campaignType": "string",      "bulkActionVersion": "string",      "_id": "string",      "status": "string",      "sendDays": [        "string"      ],      "deleted": true,      "migrated": true,      "archived": true,      "hasTracking": true,      "isPlainText": true,      "hasUtmTracking": true,      "enableResendToUnopened": true,      "locationId": "string",      "templateId": "string",      "templateType": "string",      "createdAt": "string",      "updatedAt": "string",      "__v": 0,      "documentId": "string",      "downloadUrl": "string",      "templateDataDownloadUrl": "string",      "child": [        "string"      ]    }  ],  "total": [    "string"  ],  "traceId": "string"}
```

