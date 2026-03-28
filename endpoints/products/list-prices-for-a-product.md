---
title: "List Prices for a Product"
source: "https://marketplace.gohighlevel.com/docs/ghl/products/list-prices-for-product"
generated_at: "2026-03-28T17:50:27.670824"
tags: ["api", "endpoint", "GET"]
---

# List Prices for a Product

The "List Prices for a Product" API allows retrieving a paginated list of prices associated with a specific product. Customize your results by filtering prices or paginate through the list using the provided query parameters.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### NODEJS
```javascript
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### PYTHON
```python
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### PHP
```php
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### JAVA
```java
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### GO
```go
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### RUBY
```ruby
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

#### POWERSHELL
```powershell
{  "prices": [    {      "_id": "655b33aa2209e60b6adb87a7",      "membershipOffers": [        {          "label": "top_50",          "value": "50",          "_id": "655b33aa2209e60b6adb87a7"        }      ],      "variantOptionIds": [        "h4z7u0im2q8",        "h3nst2ltsnn"      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "product": "655b33a82209e60b6adb87a5",      "userId": "6YAtzfzpmHAdj0e8GkKp",      "name": "Red / S",      "type": "one_time",      "currency": "INR",      "amount": 199999,      "recurring": {        "interval": "day",        "intervalCount": 1      },      "createdAt": "2023-11-20T10:23:38.645Z",      "updatedAt": "2024-01-23T09:57:04.852Z",      "compareAtPrice": 2000000,      "trackInventory": null,      "availableQuantity": 5,      "allowOutOfStockPurchases": true    }  ],  "total": 10}
```

