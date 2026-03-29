# Calendars: Availability & Free Slots

Check real-time availability and manage user/calendar schedules.

## 1. Finding Free Time

### Get Free Slots
Determine available booking times for a specific calendar.

- **Endpoint:** `GET /calendars/free-slots`

> [!TIP]
> **Official Docs:** [Get Free Slots](https://marketplace.gohighlevel.com/docs/ghl/calendars/get-slots)

#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/calendars/free-slots \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/calendars/free-slots',
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

url = "https://services.leadconnectorhq.com/calendars/free-slots"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/free-slots",
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
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Query Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `calendarId` | String | Yes | Target calendar ID. |
| `startDate` | Number | Yes | Start Unix timestamp (ms). |
| `endDate` | Number | Yes | End Unix timestamp (ms). |
| `timezone` | String | No | Timezone for results (e.g., `America/New_York`). |

---

## 2. User & Event Schedules

### List User Availability
Retrieve the working hours and availability settings for a specific user.

- **Endpoint:** `GET /calendars/availability/user/{userId}`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/calendars/availability/user/{userId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/calendars/availability/user/{userId}',
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

url = "https://services.leadconnectorhq.com/calendars/availability/user/{userId}"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/availability/user/{userId}",
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
- **Scopes:** `calendars.readonly`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |

---

### Create User Schedule
Define repeating availability (e.g., Mon-Fri 9 AM - 5 PM) for a user.

- **Endpoint:** `POST /calendars/availability/user`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/calendars/availability/user \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/calendars/availability/user',
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

url = "https://services.leadconnectorhq.com/calendars/availability/user"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/calendars/availability/user",
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

## Example Request (Free Slots Search)
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/calendars/free-slots?calendarId=CVokAlI8fgw4WYWoCtQz&startDate=1733047200000&endDate=1733133600000' \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `startDate` or `endDate`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | User or Calendar ID not found. |
| 422 | `unprocessable_entity` | Invalid timezone string. |
| 429 | `rate_limit` | Too many availability checks. |
