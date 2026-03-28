---
title: "Get event calendar availability schedule"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/get-calendar-schedule"
generated_at: "2026-03-28T17:50:27.430943"
tags: ["api", "endpoint", "GET"]
---

# Get event calendar availability schedule

Retrieve the availability schedule for a specific event calendar. Returns the schedule associated with the calendar ID provided in the path.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### NODEJS
```javascript
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### PYTHON
```python
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### PHP
```php
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### JAVA
```java
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### GO
```go
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### RUBY
```ruby
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

#### POWERSHELL
```powershell
{  "schedule": {    "timezone": "America/New_York",    "rules": [      {        "type": "wday",        "intervals": [          {            "from": "09:00",            "to": "17:00"          }        ],        "date": "2023-04-15",        "day": "monday"      }    ],    "calendarId": "WvVX9LpvlBO6K506xLbp",    "dateAdded": "string",    "dateUpdated": "string"  }}
```

