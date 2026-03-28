---
title: "Get the generation details"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversation-ai/get-generation-details"
generated_at: "2026-03-28T17:50:27.479552"
tags: ["api", "endpoint", "GET"]
---

# Get the generation details

Retrieves detailed information about AI responses including the System Prompt, Conversation history, Knowledge base, website, FAQ chunks, and Rich Text chunks.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### NODEJS
```javascript
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### PYTHON
```python
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### PHP
```php
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### JAVA
```java
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### GO
```go
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### RUBY
```ruby
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

#### POWERSHELL
```powershell
{  "prompt": "Personality:\nFriendly and professional,\n\nIntent:\nAssist customers with inquiries\n\nAdditional Information:\nHandle basic support queries",  "intent": "Assist customers with product inquiries and support",  "responseMessage": "Hello! I understand you're interested in our products. How can I assist you today?",  "faqs": [    {      "id": "chunk_123",      "content": "Our return policy allows returns within 30 days of purchase.",      "title": "Return Policy FAQ"    }  ],  "website": [    {      "id": "chunk_456",      "content": "We offer free shipping on orders over $50.",      "url": "https://example.com/shipping"    }  ],  "agentId": "emp_123",  "input": "What is your return policy?",  "actionLogs": [    {      "contactUpdateAction": [        {          "fieldId": "field_123",          "value": "John Doe"        }      ]    }  ],  "history": [    {      "role": "user",      "content": "Hi, I have a question about returns"    },    {      "role": "assistant",      "content": "I'll be happy to help you with information about our return policy."    }  ],  "mode": "auto-pilot"}
```

