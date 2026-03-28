---
title: "Search Opportunities"
source: "https://marketplace.gohighlevel.com/docs/ghl/opportunities/search-opportunities-advanced"
generated_at: "2026-03-28T17:50:27.625424"
tags: ["api", "endpoint", "POST"]
---

# Search Opportunities

Search Opportunities based on combinations of advanced filters. Documentation Link -https://doc.clickup.com/8631005/d/h/87cpx-424216/7bf11bc9b94f80f

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### NODEJS
```javascript
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### PYTHON
```python
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### PHP
```php
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### JAVA
```java
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### GO
```go
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### RUBY
```ruby
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

#### POWERSHELL
```powershell
{  "opportunities": [    {      "id": "yWQobCRIhRguQtD2llvk",      "name": "testing",      "monetaryValue": 500,      "pipelineId": "VDm7RPYC2GLUvdpKmBfC",      "pipelineStageId": "e93ba61a-53b3-45e7-985a-c7732dbcdb69",      "assignedTo": "zT46WSCPbudrq4zhWMk6",      "status": "open",      "source": "",      "lastStatusChangeAt": "2021-08-03T04:55:17.355Z",      "lastStageChangeAt": "2021-08-03T04:55:17.355Z",      "lastActionDate": "2021-08-03T04:55:17.355Z",      "indexVersion": 1,      "createdAt": "2021-08-03T04:55:17.355Z",      "updatedAt": "2021-08-03T04:55:17.355Z",      "contactId": "zT46WSCPbudrq4zhWMk6",      "locationId": "zT46WSCPbudrq4zhW",      "contact": {        "id": "byMEV0NQinDhq8ZfiOi2",        "name": "John Deo",        "companyName": "Tesla Inc",        "email": "john@deo.com",        "phone": "+1202-555-0107",        "tags": [          "string"        ]      },      "notes": [        [          null        ]      ],      "tasks": [        [          null        ]      ],      "calendarEvents": [        [          null        ]      ],      "lostReasonId": "zT46WSCPbudrq4zhWMk6",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "fieldValue": "string"        }      ],      "followers": [        [          null        ]      ]    }  ],  "total": 100,  "aggregations": {}}
```

