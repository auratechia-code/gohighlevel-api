---
title: "Get all FAQs by knowledge base with pagination support"
source: "https://marketplace.gohighlevel.com/docs/ghl/knowledge-base/list"
generated_at: "2026-03-28T17:50:27.562924"
tags: ["api", "endpoint", "GET"]
---

# Get all FAQs by knowledge base with pagination support

Retrieves FAQs for a knowledge base. Supports pagination using limit and lastFaqId parameters.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### NODEJS
```javascript
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### PYTHON
```python
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### PHP
```php
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### JAVA
```java
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### GO
```go
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### RUBY
```ruby
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

#### POWERSHELL
```powershell
{  "count": 150,  "faqs": [    {      "id": "3rzeElC1FOVY91veVBkp",      "question": "What is 1+2?",      "questionLowerCase": "what is 1+2?",      "answer": "3",      "knowledgeBaseId": "I1rITlYLJofFosIqC4Np",      "locationId": "qIyivCmsuEOSnyoFYEej",      "trainedUrlId": "688e6b6d8a1887e6d94d1475",      "deleted": false,      "createdAt": "2025-08-02T19:47:57.243Z",      "updatedAt": "2025-08-02T19:47:57.243Z"    }  ],  "lastFaqId": "3rzeElC1FOVY91veVBkp",  "hasMore": true}
```

