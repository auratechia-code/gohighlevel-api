---
title: "Create Coupon"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/create-coupon"
generated_at: "2026-03-28T17:50:27.630400"
tags: ["api", "endpoint", "POST"]
---

# Create Coupon

The "Create Coupon" API allows you to create a new promotional coupon with customizable parameters such as discount amount, validity period, usage limits, and applicable products. Use this endpoint to set up promotional offers and special discounts for your customers.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### NODEJS
```javascript
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### PYTHON
```python
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### PHP
```php
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### JAVA
```java
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### GO
```go
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### RUBY
```ruby
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

#### POWERSHELL
```powershell
{  "_id": "67f6c132d9485f9dacd5f123",  "usageCount": 12,  "limitPerCustomer": 5,  "altId": "79t07PzK8Tvf73d12312",  "altType": "location",  "name": "NEWT6",  "code": "NEWT6",  "discountType": "percentage",  "discountValue": 25,  "status": "scheduled",  "startDate": "2025-04-30T18:30:00.000Z",  "endDate": "2025-05-30T18:30:00.000Z",  "applyToFuturePayments": true,  "applyToFuturePaymentsConfig": {    "type": "fixed",    "duration": 3,    "durationType": "months"  },  "userId": "q0m15dTLGeiGOXG123123",  "createdAt": "2025-04-09T18:49:22.026Z",  "updatedAt": "2025-04-09T18:49:22.026Z",  "traceId": "c667b18d-8f5e-44cf-a914"}
```

