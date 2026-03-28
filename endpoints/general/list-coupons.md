---
title: "List Coupons"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/list-coupons"
generated_at: "2026-03-28T17:50:27.639497"
tags: ["api", "endpoint", "GET"]
---

# List Coupons

The "List Coupons" API allows you to retrieve a list of all coupons available in your location. Use this endpoint to view all promotional offers and special discounts for your customers.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### NODEJS
```javascript
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### PYTHON
```python
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### PHP
```php
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### JAVA
```java
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### GO
```go
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### RUBY
```ruby
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### POWERSHELL
```powershell
{  "data": [    {      "_id": "67f6c132d9485f9dacd5f123",      "usageCount": 12,      "limitPerCustomer": 5,      "altId": "79t07PzK8Tvf73d12312",      "altType": "location",      "name": "NEWT6",      "code": "NEWT6",      "discountType": "percentage",      "discountValue": 25,      "status": "scheduled",      "startDate": "2025-04-30T18:30:00.000Z",      "endDate": "2025-05-30T18:30:00.000Z",      "applyToFuturePayments": true,      "applyToFuturePaymentsConfig": {        "type": "fixed",        "duration": 3,        "durationType": "months"      },      "productIds": [        "6241712be68f7a98102ba272"      ],      "priceIds": [        "6241712be68f7a98102ba272"      ],      "variantIds": [        "6241712be68f7a98102ba272"      ],      "userId": "q0m15dTLGeiGOXG123123",      "createdAt": "2025-04-09T18:49:22.026Z",      "updatedAt": "2025-04-09T18:49:22.026Z"    }  ],  "totalCount": 20,  "traceId": "c667b18d-8f5e-44cf-a914"}
```

