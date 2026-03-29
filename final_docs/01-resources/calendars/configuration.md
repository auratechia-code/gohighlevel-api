---
title: "Calendar Groups & Configuration"
resource: "calendars"
endpoint: "/calendars/groups"
method: "GET|POST|PUT|DELETE"
version: "2021-07-28"
---

# Calendar Groups & Configuration

This sub-resource manages calendar organization (groups), staff availability, and location-based resources (rooms/equipment).

## Calendar Groups
Groups allow multiple calendars to be organized into categories, often used for different types of services or teams.

### 1. List Calendar Groups
- **Method:** `GET`
- **Path:** `https://services.leadconnectorhq.com/calendars/groups`
- **Query Params:** `locationId` (string) **Required.**

### 2. Create Calendar Group
- **Method:** `POST`
- **Path:** `https://services.leadconnectorhq.com/calendars/groups/`
- **Scopes:** `calendars.write`
- **Request Body:**
  - `name`: (string) **Required.**
  - `locationId`: (string) **Required.**
  - `slug`: (string) **Required.** Unique URL identifier.
  - `isActive`: (boolean) Default: `true`.

---

## Staff Availability
Define specific schedules for team members to govern when they can be booked within Round Robin or Collective calendars.

### 1. List User Availability Schedules
- **Method:** `GET`
- **Path:** `https://services.leadconnectorhq.com/calendars/user-availability`
- **Query Params:** `userId` (string) **Required.**

### 2. Create User Availability (POST)
Define the days/times a specific user is available for booking.

- **Endpoint:** `POST /calendars/user-availability/`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/calendars/user-availability/ \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/calendars/user-availability/',
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

url = "https://services.leadconnectorhq.com/calendars/user-availability/"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/user-availability/",
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
- **Request Body:**
  - `userId`: (string) **Required.**
  - `locationId`: (string) **Required.**
  - `schedule`: (array) Day-by-day availability (e.g., `mon`, `tue`).

---

## Equipment & Rooms (Resources)
Manage physical entities that are required for specific booking types.

- **Endpoint:** `GET /calendars/resources/`
- **Sub-Endpoints:** `POST`, `PUT`, `DELETE`
- **Resource Types:** `equipment`, `room`.

**Example Resource Object:**
```json
{
  "id": "res_123",
  "name": "Meeting Room A",
  "type": "room",
  "locationId": "loc_123",
  "capacity": 10
}
```

---

## Implementation Example (cURL)

### List Groups
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/calendars/groups?locationId=YOUR_LOCATION_ID' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28'
```

### Validate Group Slug
Before creating a group, you must ensure the URL slug is unique.
```bash
curl --request POST \
  --url 'https://services.leadconnectorhq.com/calendars/groups/validate-slug' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28' \
  --data '{"slug": "demo-group", "locationId": "loc_123"}'
```
