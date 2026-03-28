---
title: "Get available shipping rates"
source: "https://marketplace.gohighlevel.com/docs/ghl/store/get-available-shipping-zones"
generated_at: "2026-03-28T17:50:27.744731"
tags: ["api", "endpoint", "POST"]
---

# Get available shipping rates

This return available shipping rates for country based on order amount

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### NODEJS
```javascript
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### PYTHON
```python
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### PHP
```php
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### JAVA
```java
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### GO
```go
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### RUBY
```ruby
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

#### POWERSHELL
```powershell
{  "status": true,  "message": "Successfully created",  "data": [    {      "name": "North zone",      "description": "Ships next day",      "currency": "USD",      "amount": 99.99,      "isCarrierRate": true,      "shippingCarrierId": "655b33a82209e60b6adb87a5",      "percentageOfRateFee": 10.99,      "shippingCarrierServices": [        {          "name": "Priority Mail Express International",          "value": "PriorityMailExpressInternational"        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingZoneId": "655b33a82209e60b6adb87a5"    }  ]}
```

