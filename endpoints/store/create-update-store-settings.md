---
title: "Create/Update Store Settings"
source: "https://marketplace.gohighlevel.com/docs/ghl/store/create-store-setting"
generated_at: "2026-03-28T17:49:52.652754"
tags: ["api", "endpoint", "POST"]
---

# Create/Update Store Settings

Create or update store settings by altId and altType.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### NODEJS
```javascript
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### PYTHON
```python
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### PHP
```php
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### JAVA
```java
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### GO
```go
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### RUBY
```ruby
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

#### POWERSHELL
```powershell
{  "status": true,  "message": "Successfully created",  "data": {    "altId": "6578278e879ad2646715ba9c",    "altType": "location",    "shippingOrigin": {      "name": "ABC Store",      "country": "US",      "state": "VA",      "city": "Tokyo",      "street1": "Street 1",      "street2": "Street 2",      "zip": "674561",      "phone": "+1-214-559-6993",      "email": "john@deo.com"    },    "storeOrderNotification": {      "enabled": true,      "subject": "Your order is placed !",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "storeOrderFulfillmentNotification": {      "enabled": true,      "subject": "Order fulfilled",      "emailTemplateId": "6788d542f0462ffd6bc29bb9",      "defaultEmailTemplateId": "6788d542f0462ffd6bc29bb9"    },    "_id": "655b33a82209e60b6adb87a5",    "createdAt": "2023-12-12T09:27:42.355Z",    "updatedAt": "2023-12-12T09:27:42.355Z"  }}
```

