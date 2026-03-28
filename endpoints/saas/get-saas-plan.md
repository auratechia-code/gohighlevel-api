---
title: "Get SaaS Plan"
source: "https://marketplace.gohighlevel.com/docs/ghl/saas/get-saas-plan-deprecated"
generated_at: "2026-03-28T17:50:27.688772"
tags: ["api", "endpoint", "GET"]
---

# Get SaaS Plan

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### NODEJS
```javascript
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### PYTHON
```python
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### PHP
```php
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### JAVA
```java
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### GO
```go
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### RUBY
```ruby
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

#### POWERSHELL
```powershell
{  "planId": "66c4d36534f21f900dc2a265",  "companyId": "66c4d36534f21f900dc2a265",  "title": "AED 1.5 changed",  "description": "AED 1.5",  "saasProducts": [    "2-way-text-messaging",    "gmb-messaging",    "web-chat"  ],  "addOns": [    "YEXT_V2",    "WHATSAPP_V1",    "WORDPRESS_V1",    "AI_EMPLOYEE",    "Ad_Publishing_Connect_Your_BM"  ],  "planLevel": 0,  "trialPeriod": 16,  "setupFee": 100,  "userLimit": 50,  "contactLimit": 50,  "prices": [    {      "id": "66a9edbfcc6c505a22db7976",      "billingInterval": "month",      "active": true,      "amount": 150,      "currency": "AED",      "symbol": "$"    }  ],  "categoryId": "66911cdc98508ec2731979b9",  "snapshotId": "G8KmpIeLnZc7ZMoJoxDx",  "providerLocationId": "r06mdj4OrrERzYDvsOdh",  "productId": "66a9edbfcc6c5090bedb7974",  "isSaaSV2": true,  "createdAt": "2024-07-31T07:54:41.885Z",  "updatedAt": "2025-04-01T12:27:29.167Z"}
```

