---
title: "Create new provider config"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/create-config"
generated_at: "2026-03-28T17:50:27.629639"
tags: ["api", "endpoint", "POST"]
---

# Create new provider config

API to create a new payment config for given location

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### NODEJS
```javascript
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### PYTHON
```python
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### PHP
```php
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### JAVA
```java
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### GO
```go
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### RUBY
```ruby
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

#### POWERSHELL
```powershell
{  "name": "Company Paypal Integration",  "description": "This payment gateway supports payments in India via UPI, Net banking, cards and wallets.",  "paymentsUrl": "https://testpayment.paypal.com",  "queryUrl": "https://testsubscription.paypal.com",  "imageUrl": "https://testsubscription.paypal.com",  "_id": "662a44ad19a2a44d3cd9d749",  "locationId": "Lk3nlfk4lxlelVEwcW",  "marketplaceAppId": "65f0b217a05c774da7f1efa5",  "paymentProvider": "{ live: { liveMode: true }, test: { liveMode: false, apiKey: \"y5ZQxryRFXZHvUJZdLXXXXXX\", publishableKey: \"rzp_test_zPRoVMLOa0A9wo\" }}",  "deleted": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "traceId": "302d2cf4-1ba0-4bf5-bc3b-f8fa76fda58a"}
```

