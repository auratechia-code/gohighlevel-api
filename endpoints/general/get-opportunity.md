---
title: "Get Opportunity"
source: "https://marketplace.gohighlevel.com/docs/ghl/opportunities/get-opportunity"
generated_at: "2026-03-28T17:50:27.620940"
tags: ["api", "endpoint", "GET"]
---

# Get Opportunity

Get Opportunity

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### NODEJS
```javascript
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### PYTHON
```python
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### PHP
```php
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### JAVA
```java
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### GO
```go
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### RUBY
```ruby
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

#### POWERSHELL
```powershell
{  "opportunity": {    "id": "yWQobCRIhRguQtD2llvk",    "name": "testing",    "monetaryValue": 500,    "pipelineId": "VDm7RPYC2GLUvdpKmBfC",    "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",    "assignedTo": "zT46WSCPbudrq4zhWMk6",    "status": "open",    "source": "",    "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",    "lastStageChangeAt": "2021-08-03T04:55:17.355Z",    "lastActionDate": "2021-08-03T04:55:17.355Z",    "indexVersion": 1,    "createdAt": "2021-08-03T04:55:17.355Z",    "updatedAt": "2021-08-03T04:55:17.355Z",    "contactId": "zT46WSCPbudrq4zhWMk6",    "locationId": "zT46WSCPbudrq4zhW",    "contact": {      "id": "byMEV0NQinDhq8ZfiOi2",      "name": "John Deo",      "companyName": "Tesla Inc",      "email": "john@deo.com",      "phone": "+1202-555-0107",      "tags": [        "string"      ]    },    "notes": [      [        null      ]    ],    "tasks": [      [        null      ]    ],    "calendarEvents": [      [        null      ]    ],    "lostReasonId": "zT46WSCPbudrq4zhWMk6",    "customFields": [      {        "id": "MgobCB14YMVKuE4Ka8p1",        "fieldValue": "string"      }    ],    "followers": [      [        null      ]    ]  }}
```

