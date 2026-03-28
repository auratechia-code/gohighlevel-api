---
title: "Get message by message id"
source: "https://marketplace.gohighlevel.com/docs/ghl/conversations/get-message"
generated_at: "2026-03-28T17:50:27.491525"
tags: ["api", "endpoint", "GET"]
---

# Get message by message id

Get message by message id.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### NODEJS
```javascript
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### PYTHON
```python
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### PHP
```php
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### JAVA
```java
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### GO
```go
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### RUBY
```ruby
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

#### POWERSHELL
```powershell
{  "id": "ve9EPM428h8vShlRW1KT",  "altId": "msg_123456789",  "type": 1,  "messageType": "SMS",  "locationId": "ve9EPM428h8vShlRW1KT",  "contactId": "ve9EPM428h8vShlRW1KT",  "conversationId": "ve9EPM428h8vShlRW1KT",  "dateAdded": "2024-03-27T18:13:49.000Z",  "body": "Hi there",  "direction": "inbound",  "status": "connected",  "contentType": "text/plain",  "attachments": [    "string"  ],  "meta": {    "callDuration": 120,    "callStatus": "completed",    "email": {      "email": {        "messageIds": [          "ve9EPM428kjkvShlRW1KT",          "ve9EPs1028kjkvShlRW1KT"        ]      }    },    "ig": {      "ig": {        "page_id": "1234567890",        "page_name": "Instagram Page"      }    },    "fb": {      "fb": {        "page_id": "1234567890",        "page_name": "Facebook Page"      }    }  },  "source": "workflow",  "userId": "ve9EPM428kjkvShlRW1KT",  "conversationProviderId": "ve9EPM428kjkvShlRW1KT",  "chatWidgetId": "67b0cc8cf14b19d85ace7s35",  "from": "+14155551234",  "to": "+14155555678",  "error": "string"}
```

