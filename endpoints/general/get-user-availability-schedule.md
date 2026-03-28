---
title: "Get user availability schedule"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/get-schedule-by-id"
generated_at: "2026-03-28T17:50:27.432974"
tags: ["api", "endpoint", "GET"]
---

# Get user availability schedule

Retrieve a specific schedule by its unique identifier. Returns detailed information including rules, timezone, and associated calendars/users.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### NODEJS
```javascript
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### PYTHON
```python
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### PHP
```php
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### JAVA
```java
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### GO
```go
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### RUBY
```ruby
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

#### POWERSHELL
```powershell
{  "schedule": {    "id": "IkqiJlXJ7o9h61tCHHod",    "name": "Business Hours Schedule",    "locationId": "IkqiJlXJ7o9h61tCHHod",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "timezone": "America/New_York",    "dateAdded": "2023-01-15T10:30:00.000Z",    "dateUpdated": "2023-01-20T14:45:00.000Z",    "userId": "IkqiJlXJ7o9h61tCHHod",    "calendarIds": [      "string"    ],    "deleted": false  }}
```

