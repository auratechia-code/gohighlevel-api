---
title: "Update Recurring Task"
source: "https://marketplace.gohighlevel.com/docs/ghl/locations/update-recurring-task"
generated_at: "2026-03-28T17:50:27.592878"
tags: ["api", "endpoint", "PUT"]
---

# Update Recurring Task

Update Recurring Task

## Endpoint Information

> [!IMPORTANT]
> **Method:** `PUT`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### NODEJS
```javascript
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### PYTHON
```python
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### PHP
```php
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### JAVA
```java
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### GO
```go
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### RUBY
```ruby
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

#### POWERSHELL
```powershell
{  "recurringTask": {    "id": "sx6wyHhbFdRXh302Lunr",    "title": "Task Name",    "description": "Task Description",    "locationId": "sx6wyHhbFdRXh302Lunr",    "updatedAt": "2021-04-15T10:00:00.000Z",    "createdAt": "2021-04-15T10:00:00.000Z",    "rruleOptions": {      "createTaskIfOverDue": false,      "interval": 1,      "intervalType": "hourly",      "startDate": "2024-10-29T12:34:03.000Z",      "dueAfterSeconds": 600,      "count": 550    },    "totalOccurrence": 10,    "deleted": false,    "assignedTo": "sx6wyHhbFdRXh302Lunr",    "contactId": "v5cEPM428h8vShlRW1KT"  }}
```

