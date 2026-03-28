---
title: "List user availability schedule"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/get-all-schedules"
generated_at: "2026-03-28T17:50:27.426695"
tags: ["api", "endpoint", "GET"]
---

# List user availability schedule

Retrieve user availability schedules based on various filters including location, calendar, and user. Supports pagination.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### NODEJS
```javascript
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### PYTHON
```python
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### PHP
```php
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### JAVA
```java
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### GO
```go
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### RUBY
```ruby
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

#### POWERSHELL
```powershell
{  "schedules": [    {      "id": "IkqiJlXJ7o9h61tCHHod",      "name": "Business Hours Schedule",      "locationId": "IkqiJlXJ7o9h61tCHHod",      "rules": [        {          "type": "wday",          "intervals": [            {              "from": "09:00",              "to": "17:00"            }          ],          "date": "2023-04-15",          "day": "monday"        }      ],      "timezone": "America/New_York",      "dateAdded": "2023-01-15T10:30:00.000Z",      "dateUpdated": "2023-01-20T14:45:00.000Z",      "userId": "IkqiJlXJ7o9h61tCHHod",      "calendarIds": [        "string"      ],      "deleted": false    }  ]}
```

