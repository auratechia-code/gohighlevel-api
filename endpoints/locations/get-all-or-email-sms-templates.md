---
title: "GET all or email/sms templates"
source: "https://marketplace.gohighlevel.com/docs/ghl/locations/get-all-or-email-sms-templates"
generated_at: "2026-03-28T17:49:52.491348"
tags: ["api", "endpoint", "GET"]
---

# GET all or email/sms templates

GET all or email/sms templates

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### NODEJS
```javascript
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### PYTHON
```python
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### PHP
```php
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### JAVA
```java
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### GO
```go
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### RUBY
```ruby
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

#### POWERSHELL
```powershell
{  "templates": [    {      "id": "2yMwhgTNO19bpintqrap",      "name": "sms template",      "type": "sms",      "template": {        "body": "sms body",        "attachments": []      },      "dateAdded": "2022-01-27T12:31:19.679Z",      "locationId": "ve9EPM428h8vShlRW1KT",      "urlAttachments": []    },    {      "id": "2yMwhgTNO19bpintqrap",      "name": "email template",      "type": "email",      "dateAdded": "2022-01-27T12:31:19.679Z",      "template": {        "subject": "subject text",        "attachments": [],        "html": "<html><head><style>body{font-family: sans-serif;}</style></head><body>testing</body></html>"      },      "locationId": "ve9EPM428h8vShlRW1KT"    }  ],  "totalCount": 100}
```

