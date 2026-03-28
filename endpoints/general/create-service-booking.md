---
title: "Create Service Booking"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/create-service-booking"
generated_at: "2026-03-28T17:50:27.416857"
tags: ["api", "endpoint", "POST"]
---

# Create Service Booking

Create a new service booking

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### NODEJS
```javascript
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### PYTHON
```python
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### PHP
```php
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### JAVA
```java
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### GO
```go
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### RUBY
```ruby
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

#### POWERSHELL
```powershell
{  "bookingId": "7NkT25Vor1v4aQatFsv2",  "locationId": "0007BWpSzSwfiuSl0tR2",  "serviceLocationId": "65e5f6dfacf123513228d384",  "startTime": "2023-09-25T16:00:00+05:30",  "endTime": "2023-09-25T16:30:00+05:30",  "services": [    {      "id": "68e5f6dfacf123513228d384",      "serviceCategoryId": "3c4d5e6f7890123456789abc",      "serviceStaffId": "7NkT25Vor1v4aQatFsv2",      "serviceStartTime": "2023-09-25T16:00:00+05:30",      "serviceEndTime": "2023-09-25T16:30:00+05:30",      "serviceResources": [        {          "id": "6985f6dfacf123513228d384"        }      ],      "serviceAddOns": [        {          "id": "6985f6dfacf123513228d384",          "quantity": 2        }      ]    }  ],  "timezone": "America/New_York",  "status": "confirmed",  "meetingLocation": "123 Main St, Anytown, USA",  "messages": [    "Meeting location is not supported for the selected service location and has been ignored."  ]}
```

