# Appointment Body Parameters (V2)

Documentation for creating and updating appointments in GoHighLevel calendars.

## Create Appointment (`POST /calendars/events/appointments/`)

The following fields are supported in the request body.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `title` | String | **YES** | Title for the appointment. |
| `calendarId` | String | **YES** | The unique ID of the calendar. |
| `contactId` | String | **YES** | The unique ID of the contact. |
| `startTime` | String | **YES** | ISO 8601 formatted start date/time. |
| `endTime` | String | No | ISO 8601 formatted end date/time. |
| `locationId` | String | No | The unique ID of the location. |
| `appointmentStatus` | String | No | Initial status: `confirmed`, `unconfirmed`. |
| `assignedUserId` | String | No | The unique ID of the assigned user. |
| `meetingLocationType` | String | No | Type of meeting location (e.g., `Custom`). |
| `description` | String | No | Appointment description. |
| `address` | String | No | Specific address. |
| `ignoreDateRange` | Boolean | No | Bypass calendar date range restricts. |
| `toNotify` | Boolean | No | Send confirmation notifications. |
| `ignoreFreeSlotValidation`| Boolean | No | Skip free slot checking. |
| `rrule` | String | No | Recurring rule string. |

---

## Update Appointment (`PUT /calendars/events/appointments/:eventId/`)

The update operation uses the **same schema** as the Create operation, with the following rules:

1. **All fields are optional**.
2. To only update the status, you can use specialized update endpoints or update the `appointmentStatus` field here.

---

> [!CAUTION]
> If `endTime` is not provided, the API will use the default duration configured in the `calendarId`.
