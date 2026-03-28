---
title: "List Products"
source: "https://marketplace.gohighlevel.com/docs/ghl/products/list-invoices"
generated_at: "2026-03-28T17:50:27.669305"
tags: ["api", "endpoint", "GET"]
---

# List Products

The "List Products" API allows to retrieve a paginated list of products. Customize your results by filtering products based on name or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve product information.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### NODEJS
```javascript
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### PYTHON
```python
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### PHP
```php
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### JAVA
```java
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### GO
```go
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### RUBY
```ruby
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

#### POWERSHELL
```powershell
{  "products": [    {      "_id": "655b33a82209e60b6adb87a5",      "description": "This is a really awesome product",      "variants": [        {          "id": "38s63qmxfr4",          "name": "Size",          "options": [            {              "id": "h4z7u0im2q8",              "name": "XL"            }          ]        }      ],      "locationId": "3SwdhCsvxI8Au3KsPJt6",      "name": "Awesome Product",      "productType": "PHYSICAL",      "availableInStore": true,      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "statementDescriptor": "abcde",      "image": "https://storage.googleapis.com/ghl-test/3SwdhCsvxI8Au3KsPJt6/media/65af8d5df88bdb4b1022ee90.png",      "collectionIds": [        "65d71377c326ea78e1c47df5",        "65d71377c326ea78e1c47d34"      ],      "isTaxesEnabled": true,      "taxes": [        "654492a4e6bef380114de15a"      ],      "automaticTaxCategoryId": "65d71377c326ea78e1c47df5",      "label": {        "title": "Featured",        "startDate": "2024-06-26T05:43:35.000Z",        "endDate": "2024-06-30T05:43:39.000Z"      },      "slug": "washing-machine"    }  ],  "total": [    {      "total": 20    }  ]}
```

