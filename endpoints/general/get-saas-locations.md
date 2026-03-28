---
title: "Get SaaS Locations"
source: "https://marketplace.gohighlevel.com/docs/ghl/saas/get-saas-locations-deprecated"
generated_at: "2026-03-28T17:50:27.687542"
tags: ["api", "endpoint", "GET"]
---

# Get SaaS Locations

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### NODEJS
```javascript
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### PYTHON
```python
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### PHP
```php
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### JAVA
```java
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### GO
```go
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### RUBY
```ruby
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

#### POWERSHELL
```powershell
{  "locations": [    {      "locationId": "locationId1",      "companyId": "companyId1",      "saasMode": "saasV2",      "subscriptionId": "subscriptionId1",      "customerId": "customerId1",      "name": "John Doe",      "email": "john.doe@example.com",      "providerLocationId": "r06mdj4OrrERzYDvsOdh",      "isSaaSV2": true,      "subscriptionInfo": {        "priceId": "price_1QDPY5FpU9DlKp7RQ8BXfywx",        "saasPlanId": "66c4d36534f21f900dc2a265",        "stripeProductId": "prod_1QDPY5FpU9DlKp7RQ8BXfywx",        "subscriptionStatus": "active"      }    }  ],  "pagination": {    "page": 1,    "limit": 10,    "total": 100,    "totalPages": 10,    "hasNext": true,    "hasPrev": true  }}
```

