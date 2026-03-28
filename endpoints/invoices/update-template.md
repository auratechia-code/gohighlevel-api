---
title: "Update template"
source: "https://marketplace.gohighlevel.com/docs/ghl/invoices/update-invoice-template"
generated_at: "2026-03-28T17:50:27.554329"
tags: ["api", "endpoint", "PUT"]
---

# Update template

API to update an template by template id

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### NODEJS
```javascript
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### PYTHON
```python
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### PHP
```php
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### JAVA
```java
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### GO
```go
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### RUBY
```ruby
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

#### POWERSHELL
```powershell
{  "_id": "6578278e879ad2646715ba9c",  "altId": "6578278e879ad2646715ba9c",  "altType": "location",  "name": "New Template",  "businessDetails": {    "name": "Alex",    "address": {      "addressLine1": "9931 Beechwood",      "city": "St. Houston",      "state": "TX",      "countryCode": "USA",      "postalCode": "559-6993"    },    "phoneNo": "+1-214-559-6993",    "website": "www.example.com"  },  "currency": "USD",  "discount": {    "type": "percentage",    "value": 0  },  "items": [    {      "taxes": [],      "_id": "c6tZZU0rJBf30ZXx9Gli",      "productId": "c6tZZU0rJBf30ZXx9Gli",      "priceId": "c6tZZU0rJBf30ZXx9Gli",      "currency": "USD",      "name": "Macbook Pro",      "qty": 1,      "amount": 999    }  ],  "invoiceNumberPrefix": "INV-",  "total": 999,  "createdAt": "2023-12-12T09:27:42.355Z",  "updatedAt": "2023-12-12T09:27:42.355Z"}
```

