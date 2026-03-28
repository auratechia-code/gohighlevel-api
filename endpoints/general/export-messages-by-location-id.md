---
title: "Export messages by location ID"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversations/export-messages-by-location"
generated_at: "2026-03-28T17:50:27.489647"
tags: ["api", "endpoint", "GET"]
---

# Export messages by location ID

Export messages for a specific location with cursor-based pagination support.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### NODEJS
```javascript
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### PYTHON
```python
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### PHP
```php
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### JAVA
```java
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### GO
```go
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### RUBY
```ruby
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

#### POWERSHELL
```powershell
{  "messages": [    {      "id": "ve9EPM428h8vShlRW1KT",      "altId": "msg_123456789",      "type": 1,      "messageType": "SMS",      "locationId": "ve9EPM428h8vShlRW1KT",      "contactId": "ve9EPM428h8vShlRW1KT",      "conversationId": "ve9EPM428h8vShlRW1KT",      "dateAdded": "2024-03-27T18:13:49.000Z",      "body": "Hi there",      "direction": "inbound",      "status": "connected",      "contentType": "text/plain",      "attachments": [        "string"      ],      "meta": {        "callDuration": 120,        "callStatus": "completed",        "email": {          "email": {            "messageIds": [              "ve9EPM428kjkvShlRW1KT",              "ve9EPs1028kjkvShlRW1KT"            ]          }        },        "ig": {          "ig": {            "page_id": "1234567890",            "page_name": "Instagram Page"          }        },        "fb": {          "fb": {            "page_id": "1234567890",            "page_name": "Facebook Page"          }        }      },      "source": "workflow",      "userId": "ve9EPM428kjkvShlRW1KT",      "conversationProviderId": "ve9EPM428kjkvShlRW1KT",      "chatWidgetId": "67b0cc8cf14b19d85ace7s35",      "from": "+14155551234",      "to": "+14155555678",      "error": "string"    }  ],  "nextCursor": "a748514c-f49e-4fa8-9954-b53afc78d81d",  "total": 1234}
```

