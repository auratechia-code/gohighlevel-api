---
title: "List Inventory"
source: "https://marketplace.gohighlevel.com/docs/ghl/products/get-list-inventory"
generated_at: "2026-03-28T17:50:27.662563"
tags: ["api", "endpoint", "GET"]
---

# List Inventory

The "List Inventory API allows the user to retrieve a paginated list of inventory items. Use this endpoint to fetch details for multiple items in the inventory based on the provided query parameters.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### NODEJS
```javascript
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### PYTHON
```python
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### PHP
```php
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### JAVA
```java
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### GO
```go
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### RUBY
```ruby
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

#### POWERSHELL
```powershell
{  "inventory": [    {      "_id": "6241712be68f7a98102ba272",      "name": "Medium T-shirt",      "availableQuantity": 50,      "sku": "TSHIRT-MED-001",      "allowOutOfStockPurchases": false,      "product": "6241712be68f7a98102ba270",      "updatedAt": "2023-12-12T09:27:42.355Z",      "image": "https://example.com/images/product.jpg",      "productName": "T-shirt"    }  ],  "total": {    "total": 100  }}
```

