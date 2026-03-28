---
title: "Create Product"
source: "https://marketplace.gohighlevel.com/docs/ghl/products/create-product"
generated_at: "2026-03-28T17:50:27.659164"
tags: ["api", "endpoint", "POST"]
---

# Create Product

The "Create Product" API allows adding a new product to the system. Use this endpoint to create a product with the specified details. Ensure that the required information is provided in the request payload.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### NODEJS
```javascript
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### PYTHON
```python
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### PHP
```php
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### JAVA
```java
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### GO
```go
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### RUBY
```ruby
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

#### POWERSHELL
```powershell
{  "_id": "655b33a82209e60b6adb87a5",  "description": "This is a really awesome product",  "variants": [    {      "id": "38s63qmxfr4",      "name": "Size",      "options": [        {          "id": "h4z7u0im2q8",          "name": "XL"        }      ]    }  ],  "locationId": "3SwdhCsvxI8Au3KsPJt6",  "name": "Awesome Product",  "productType": "PHYSICAL",  "availableInStore": true,  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "statementDescriptor": "abcde",  "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",  "collectionIds": [    "65d71377c326ea78e1c47df5",    "65d71377c326ea78e1c47d34"  ],  "isTaxesEnabled": true,  "taxes": [    "654492a4e6bef380114de15a"  ],  "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",  "label": {    "title": "Featured",    "startDate": "2024-06-26T05:43:35.000Z",    "endDate": "2024-06-30T05:43:39.000Z"  },  "slug": "washing-machine"}
```

