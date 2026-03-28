---
title: "Create Blog Post"
source: "https://marketplace.gohighlevel.com/docs/ghl/blogs/create-blog-post"
generated_at: "2026-03-28T17:50:27.396287"
tags: ["api", "endpoint", "POST"]
---

# Create Blog Post

The "Create Blog Post" API allows you create blog post for any given blog site. Please use blogs/post.write

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### NODEJS
```javascript
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### PYTHON
```python
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### PHP
```php
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### JAVA
```java
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### GO
```go
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### RUBY
```ruby
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

#### POWERSHELL
```powershell
{  "data": {    "categories": [      "659ecabc4a37969a2b7cc370",      "6683abde331c041f32c07aee"    ],    "tags": [      "Apple",      "Banana"    ],    "archived": false,    "_id": "66c381b38be80858b9af62b6",    "title": "Banana is good source of energy",    "description": "Description",    "imageUrl": "https://storage.googleapis.com/ghl-test/fACm0Ojm5oC70G3DcFmE/media/66b5aa3b1745b2713a8d033f.jpeg",    "status": "PUBLISHED",    "imageAltText": "alt",    "urlSlug": "banana-good-energy",    "canonicalLink": "https://blog.chatgpts.agency/post/test-8384",    "author": "659ec9634a3796e4e47cc360",    "publishedAt": "2024-08-19T17:14:57.000Z",    "updatedAt": "2024-08-19T17:32:36.182Z"  }}
```

