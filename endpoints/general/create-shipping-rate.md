---
title: "Create Shipping Rate"
source: "https://marketplace.gohighlevel.com/docs/ghl/store/create-shipping-rate"
generated_at: "2026-03-28T17:50:27.741132"
tags: ["api", "endpoint", "POST"]
---

# Create Shipping Rate

The "Create Shipping Rate" API allows adding a new shipping rate.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### NODEJS
```javascript
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### PYTHON
```python
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### PHP
```php
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### JAVA
```java
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### GO
```go
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### RUBY
```ruby
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### POWERSHELL
```powershell
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "name": "North zone",    "description": "Ships next day",    "currency": "USD",    "amount": 99.99,    "conditionType": "price",    "minCondition": 99.99,    "maxCondition": 99.99,    "isCarrierRate": true,    "shippingCarrierId": "655b33a82209e60b6adb87a5",    "percentageOfRateFee": 10.99,    "shippingCarrierServices": [      {        "name": "Priority Mail Express International",        "value": "PriorityMailExpressInternational"      }    ],    "_id": "655b33a82209e60b6adb87a5",    "shippingZoneId": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

