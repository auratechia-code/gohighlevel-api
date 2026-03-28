---
title: "Get Service Bookings"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/get-service-bookings"
generated_at: "2026-03-28T17:50:27.434152"
tags: ["api", "endpoint", "GET"]
---

# Get Service Bookings

Retrieve service bookings for a location within a given date range, with an optional service location filter.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### NODEJS
```javascript
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### PYTHON
```python
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### PHP
```php
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### JAVA
```java
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### GO
```go
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### RUBY
```ruby
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

#### POWERSHELL
```powershell
{  "bookings": [    {      "bookingId": "7NkT25Vor1v4aQatFsv2",      "locationId": "0007BWpSzSwfiuSl0tR2",      "serviceLocationId": "65e5f6dfacf123513228d384",      "startTime": "2023-09-25T16:00:00+05:30",      "endTime": "2023-09-25T16:30:00+05:30",      "services": [        {          "id": "68e5f6dfacf123513228d384",          "serviceCategoryId": "3c4d5e6f7890123456789abc",          "serviceStaffId": "7NkT25Vor1v4aQatFsv2",          "serviceStartTime": "2023-09-25T16:00:00+05:30",          "serviceEndTime": "2023-09-25T16:30:00+05:30",          "serviceResources": [            {              "id": "6985f6dfacf123513228d384"            }          ],          "serviceAddOns": [            {              "id": "6985f6dfacf123513228d384",              "quantity": 2            }          ]        }      ],      "timezone": "America/New_York",      "status": "confirmed",      "meetingLocation": "123 Main St, Anytown, USA"    }  ]}
```

