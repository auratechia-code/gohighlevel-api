---
title: "Get Blog posts by Blog ID"
source: "https://marketplace.gohighlevel.com/docs/ghl/blogs/get-blog-post"
generated_at: "2026-03-28T17:50:27.397968"
tags: ["api", "endpoint", "GET"]
---

# Get Blog posts by Blog ID

The "Get Blog posts by Blog ID" API allows you get blog posts for any given blog site using blog ID.Please use blogs/posts.readonly

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### NODEJS
```javascript
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### PYTHON
```python
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### PHP
```php
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### JAVA
```java
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### GO
```go
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### RUBY
```ruby
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

#### POWERSHELL
```powershell
{  "blogs": [    {      "categories": [        "659ecabc4a37969a2b7cc370",        "6683abde331c041f32c07aee"      ],      "tags": [        "Apple",        "Banana"      ],      "archived": false,      "_id": "66c381b38be80858b9af62b6",      "title": "Banana is good source of energy",      "description": "Description",      "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",      "status": "PUBLISHED",      "imageAltText": "alt",      "urlSlug": "banana-good-energy",      "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",      "author": "659ec9634a3796e4e47cc360",      "publishedAt": "2024-08-19T17:14:57.000Z",      "updatedAt": "2024-08-19T17:32:36.182Z"    }  ]}
```

