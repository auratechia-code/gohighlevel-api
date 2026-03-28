---
title: "List Shipping Zones"
source: "https://marketplace.gohighlevel.com/docs/ghl/store/list-shipping-zones"
generated_at: "2026-03-28T17:50:27.747792"
tags: ["api", "endpoint", "GET"]
---

# List Shipping Zones

The "List Shipping Zone" API allows to retrieve a list of shipping zone.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### NODEJS
```javascript
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### PYTHON
```python
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### PHP
```php
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### JAVA
```java
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### GO
```go
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### RUBY
```ruby
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

#### POWERSHELL
```powershell
{  "total": 20,  "data": [    {      "altId": "6578278e879ad2646715ba9c",      "altType": "location",      "name": "North zone",      "countries": [        {          "code": "US",          "states": [            {              "code": "VA"            }          ]        }      ],      "_id": "655b33a82209e60b6adb87a5",      "shippingRates": [        {          "altId": "6578278e879ad2646715ba9c",          "altType": "location",          "name": "North zone",          "description": "Ships next day",          "currency": "USD",          "amount": 99.99,          "conditionType": "price",          "minCondition": 99.99,          "maxCondition": 99.99,          "isCarrierRate": true,          "shippingCarrierId": "655b33a82209e60b6adb87a5",          "percentageOfRateFee": 10.99,          "shippingCarrierServices": [            {              "name": "Priority Mail Express International",              "value": "PriorityMailExpressInternational"            }          ],          "_id": "655b33a82209e60b6adb87a5",          "shippingZoneId": "655b33a82209e60b6adb87a5",          "createdAt": "2023-12-12T09:27:42.355Z",          "updatedAt": "2023-12-12T09:27:42.355Z"        }      ],      "createdAt": "2023-12-12T09:27:42.355Z",      "updatedAt": "2023-12-12T09:27:42.355Z"    }  ]}
```

