---
title: "Get Blocked Slots"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/get-blocked-slots"
generated_at: "2026-03-28T17:50:27.428502"
tags: ["api", "endpoint", "GET"]
---

# Get Blocked Slots

Get Blocked Slots

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### NODEJS
```javascript
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### PYTHON
```python
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### PHP
```php
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### JAVA
```java
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### GO
```go
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### RUBY
```ruby
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

#### POWERSHELL
```powershell
{  "events": [    {      "id": "string",      "address": "https://meet.google.com/yqp-gogr-wve",      "title": "Appointment with GHL Dev team",      "calendarId": "BqTwX8QFwXzpegMve9EQ",      "locationId": "0007BWpSzSwfiuSl0tR2",      "contactId": "9NkT25Vor1v4aQatFsv2",      "groupId": "9NkT25Vor1v4aQatFsv2",      "appointmentStatus": "confirmed",      "assignedUserId": "YlWd2wuCAZQzh2cH1fVZ",      "users": [        "YlWd2wuCAZQzh2cH1fVZ",        "9NkT25Vor1v4aQatFsv2"      ],      "notes": "Some dummy note",      "description": "Some dummy description",      "isRecurring": "true",      "rrule": "string",      "deleted": false,      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:00:00+05:30",      "dateAdded": "2023-09-25T16:00:00+05:30",      "dateUpdated": "2023-09-25T16:00:00+05:30",      "assignedResources": [        "string"      ],      "createdBy": {        "userId": "string",        "source": "string"      },      "masterEventId": "ocWd2wuBGAQzh2cH1fSZ"    }  ]}
```

