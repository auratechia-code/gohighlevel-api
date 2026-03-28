---
title: "Get rebilling config for an app subscription and usage plans"
source: "https://marketplace.gohighlevel.com/docs/ghl/marketplace/get-rebilling-config-for-app"
generated_at: "2026-03-28T17:50:27.599062"
tags: ["api", "endpoint", "GET"]
---

# Get rebilling config for an app subscription and usage plans

Get rebilling config for an app subscription and usage plans for the authenticated sub-account. This endpoint returns the subscription and usage plans for an app.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### NODEJS
```javascript
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### PYTHON
```python
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### PHP
```php
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### JAVA
```java
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### GO
```go
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### RUBY
```ruby
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

#### POWERSHELL
```powershell
{  "plans": {    "subscription": [      {        "resellingAmount": 0,        "baseAmount": 999,        "planId": "5ae000000000000000000000",        "features": [          "feature1",          "feature2"        ],        "paymentType": "month",        "name": "Monthly Plan - 999",        "paymentTime": "month"      }    ],    "usage": [      {        "productType": "workflow_action",        "productName": "Send Group iMessage",        "usageUnit": "action / message",        "meterId": "680b97022b4a34420f5f9b93",        "meterName": "Send Group iMessage",        "fixedPricePerUnit": 0.01001,        "priceType": "fixed",        "minPricePerUnit": "0.01001",        "maxPricePerUnit": "0.01001",        "executionLimitPerCycle": 1000      }    ]  }}
```

