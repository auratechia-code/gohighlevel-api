---
title: "Update Contacts Tags"
source: "https://marketplace.gohighlevel.com/docs/ghl/contacts/create-association"
generated_at: "2026-03-28T17:50:27.453974"
tags: ["api", "endpoint", "POST"]
---

# Update Contacts Tags

Allows you to update tags to multiple contacts at once, you can add or remove tags from the contacts

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### NODEJS
```javascript
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### PYTHON
```python
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### PHP
```php
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### JAVA
```java
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### GO
```go
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### RUBY
```ruby
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

#### POWERSHELL
```powershell
{  "succeded": true,  "errorCount": 0,  "responses": [    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "Tags updated",      "type": "success",      "oldTags": [        "tag-1",        "tag-2"      ],      "tagsAdded": [],      "tagsRemoved": []    },    {      "contactId": "abcdef",      "message": "contact id is not a valid firebase id",      "type": "error"    },    {      "contactId": "qFSqySFkVvNzOSqgGqFi",      "message": "contact is deleted",      "type": "error"    },    {      "contactId": "3ualbhnV7j3n3a9r2moD",      "message": "contact does not belong to location",      "type": "error"    }  ]}
```

