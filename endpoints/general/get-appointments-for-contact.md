---
title: "Get Appointments for Contact"
source: "https://marketplace.gohighlevel.com/docs/ghl/contacts/get-appointments-for-contact"
generated_at: "2026-03-28T17:50:27.460148"
tags: ["api", "endpoint", "GET"]
---

# Get Appointments for Contact

Get Appointments for Contact

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### NODEJS
```javascript
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### PYTHON
```python
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### PHP
```php
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### JAVA
```java
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### GO
```go
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### RUBY
```ruby
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

#### POWERSHELL
```powershell
{  "events": [    {      "id": "YS3jaqqeehkR2Is80miy",      "calendarId": "YlWd2wuCAZQzh2cH1fVZ",      "status": "booked",      "title": "Test",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "notes": "test",      "startTime": "2021-07-16 11:00:00",      "endTime": "2021-07-16 11:30:00",      "address": "Address",      "locationId": "YlWd2wuCAZQzh2cH1fVZ",      "contactId": "YlWd2wuCAZQzh2cH1fVZ",      "groupId": "YlWd2wuCAZQzh2cH1fVZ",      "appointmentStatus": "booked",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ],      "dateAdded": "2021-07-16 11:00:00",      "dateUpdated": "2021-07-16 11:30:00",      "assignedResources": [        "YlWd2wuCAZQzh2cH1fVZ",        "YlWd2wuCAZQzh2cH1fVZ"      ]    }  ]}
```

