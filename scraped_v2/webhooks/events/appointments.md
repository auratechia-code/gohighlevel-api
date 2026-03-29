# Webhook Event: Appointment Created (`AppointmentCreate`)

Triggered whenever a new appointment is booked in a calendar.

## Trigger Details

- **Event Category**: `Calendar`
- **Internal Type**: `AppointmentCreate`
- **Condition**: New appointment record created.

---

## Example Payload

```json
{
  "type": "AppointmentCreate",
  "locationId": "ve9EPM428h8vShlRW1KT",
  "appointment": {
    "id": "apt_123",
    "address": "123 Main St",
    "title": "Strategy Session",
    "calendarId": "cal_456",
    "contactId": "cnt_789",
    "startTime": "2024-04-01T10:00:00.000Z",
    "endTime": "2024-04-01T11:00:00.000Z",
    "status": "confirmed"
  }
}
```

---

> [!CAUTION]
> Always verify the `X-GHL-Signature` before processing.
