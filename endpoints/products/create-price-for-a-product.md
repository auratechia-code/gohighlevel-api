---
title: "Create Price for a Product"
source: "https://marketplace.gohighlevel.com/docs/ghl/products/create-price-for-product"
generated_at: "2026-03-28T17:50:27.658623"
tags: ["api", "endpoint", "POST"]
---

# Create Price for a Product

The "Create Price for a Product" API allows adding a new price associated with a specific product to the system. Use this endpoint to create a price with the specified details for a particular product. Ensure that the required information is provided in the request payload.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### NODEJS
```javascript
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### PYTHON
```python
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### PHP
```php
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### JAVA
```java
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### GO
```go
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### RUBY
```ruby
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

#### POWERSHELL
```powershell
{  "_id": "655b33aa2209e60b6adb87a7",  "membershipOffers": [    {      "label": "top_50",      "value": "50",      "_id": "655b33aa2209e60b6adb87a7"    }  ],  "variantOptionIds": [    "h4z7u0im2q8",    "h3nst2ltsnn"  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "product": "655b33a82209e60b6adb87a5",  "userId": "6YAtzfzpmHAdj0e8GkKp",  "name": "Red / S",  "type": "one_time",  "currency": "INR",  "amount": 199999,  "recurring": {    "interval": "day",    "intervalCount": 1  },  "createdAt": "2023-11-20T10:23:38.645Z",  "updatedAt": "2024-01-23T09:57:04.852Z",  "compareAtPrice": 2000000,  "trackInventory": null,  "availableQuantity": 5,  "allowOutOfStockPurchases": true}
```

