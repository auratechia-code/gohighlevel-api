---
title: "Update Shipping Rate"
source: "https://marketplace.gohighlevel.com/docs/ghl/store/update-shipping-rate"
generated_at: "2026-03-28T17:50:27.752369"
tags: ["api", "endpoint", "PUT"]
---

# Update Shipping Rate

The "update Shipping Rate" API allows update a shipping rate to the system.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
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

