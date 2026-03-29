# Calendars: Appointments & Scheduling

Manage individual bookings, appointment statuses, and recurring events.

## 1. Appointment Operations

### Create Appointment
Book a new slot on a specific calendar for a contact.

- **Endpoint:** `POST /calendars/events/appointments`

> [!TIP]
> **Official Docs:** [Create Appointment](https://marketplace.gohighlevel.com/docs/ghl/calendars/create-appointment)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/calendars/events/appointments \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/calendars/events/appointments',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/calendars/events/appointments"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("POST", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/events/appointments",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Method:** `POST`
- **Scopes:** `calendars.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `calendarId` | String | Yes | Target calendar ID. |
| `locationId` | String | Yes | ID of the location. |
| `contactId` | String | Yes | ID of the contact booking. |
| `startTime` | String | Yes | ISO date string. |
| `endTime` | String | Yes | ISO date string. |
| `title` | String | No | Event title. |
| `appointmentStatus` | String | No | `confirmed`, `unconfirmed`, `cancelled`. |
| `assignedUserId` | String | No | ID of the user hosting the meeting. |

---

### List Appointments
Fetch all booked events within a timeframe.

- **Endpoint:** `GET /calendars/events/appointments`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/calendars/events/appointments \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/calendars/events/appointments',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/calendars/events/appointments"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/events/appointments",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Method:** `GET`
- **Scopes:** `calendars.readonly`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `calendarId` | String | Yes | Filter by calendar. |
| `startTime` | Number | Yes | Unix timestamp (ms) start. |
| `endTime` | Number | Yes | Unix timestamp (ms) end. |

---

### Update Appointment
Modify time, status, or assigned user for an existing booking.

- **Endpoint:** `PUT /calendars/events/appointments/{appointmentId}`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/calendars/events/appointments/{appointmentId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/calendars/events/appointments/{appointmentId}',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/calendars/events/appointments/{appointmentId}"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("PUT", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/events/appointments/{appointmentId}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Scopes:** `calendars.write`

---

## 2. Blocked Slots

### Create Block Event
Manually block off time segments on a calendar (to prevent bookings).

- **Endpoint:** `POST /calendars/events/block-slots`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/calendars/events/block-slots \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/calendars/events/block-slots',
  headers: {
    'Authorization': 'Bearer <TOKEN>',
    'Version': '2021-07-28'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

```python
import requests

url = "https://services.leadconnectorhq.com/calendars/events/block-slots"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("POST", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/events/block-slots",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <TOKEN>",
    "Version: 2021-07-28"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```
- **Scopes:** `calendars.write`

---

## Example Request (Book Appointment)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/calendars/events/appointments \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "calendarId": "CVokAlI8fgw4WYWoCtQz",
  "locationId": "C2QujeCh8ZnC7al2InWR",
  "contactId": "0007BWpSzSwfiuSl0tR2",
  "startTime": "2024-12-01T10:00:00Z",
  "endTime": "2024-12-01T11:00:00Z",
  "title": "Strategy Session"
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Overlapping booking or missing IDs. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Calendar or Contact ID not found. |
| 409 | `conflict` | The selected slot is already taken. |
| 422 | `unprocessable_entity` | Invalid ISO date format. |
