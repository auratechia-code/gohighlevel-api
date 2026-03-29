# Voice-AI: Agent Management

Configure and deploy AI voice agents for automated telephony and IVR handling.

## 1. Agent Lifecycle

### Create Agent
Define a new Voice AI persona for the location.

- **Endpoint:** `POST /voice-ai/agents`

> [!TIP]
> **Official Docs:** [Create Agent](https://marketplace.gohighlevel.com/docs/ghl/voice-ai/create-agent)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/voice-ai/agents \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/voice-ai/agents',
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

url = "https://services.leadconnectorhq.com/voice-ai/agents"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/voice-ai/agents",
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
- **Scopes:** `voiceai.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `name` | String | Yes | Agent name (internal). |
| `voice` | String | Yes | ID of the selected voice (e.g. `ElevenLabs-ID`). |
| `prompt` | String | Yes | Scripting and behavior guidelines. |
| `language` | String | No | Language code (default: `en-US`). |

---

### List Agents
Fetch all configured agents for the sub-account.

- **Endpoint:** `GET /voice-ai/agents`


#### Example Requests
```bash
curl --request GET \
  --url https://services.leadconnectorhq.com/voice-ai/agents \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/voice-ai/agents',
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

url = "https://services.leadconnectorhq.com/voice-ai/agents"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/voice-ai/agents",
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
- **Scopes:** `voiceai.readonly`

---

### Delete Agent
Remove an agent profile from the system.

- **Endpoint:** `DELETE /voice-ai/agents/{agentId}`

> [!TIP]
> **Official Docs:** [Delete Agent](https://marketplace.gohighlevel.com/docs/ghl/voice-ai/delete-agent)

#### Example Requests
```bash
curl --request DELETE \
  --url https://services.leadconnectorhq.com/voice-ai/agents/{agentId} \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'DELETE',
  url: 'https://services.leadconnectorhq.com/voice-ai/agents/{agentId}',
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

url = "https://services.leadconnectorhq.com/voice-ai/agents/{agentId}"

headers = {
    "Authorization": "Bearer <TOKEN>",
    "Version": "2021-07-28"
}

response = requests.request("DELETE", url, headers=headers)

print(response.text)
```

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://services.leadconnectorhq.com/voice-ai/agents/{agentId}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "DELETE",
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
- **Scopes:** `voiceai.write`

---

## 2. Agent Actions

### Create Agent Action
Attach tools (e.g., Transfer to Human, Book Appointment) to an agent.

- **Endpoint:** `POST /voice-ai/agents/{agentId}/actions`

> [!TIP]
> **Official Docs:** [Create Agent Action](https://marketplace.gohighlevel.com/docs/ghl/voice-ai/create-action)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/voice-ai/agents/{agentId}/actions \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/voice-ai/agents/{agentId}/actions',
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

url = "https://services.leadconnectorhq.com/voice-ai/agents/{agentId}/actions"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/voice-ai/agents/{agentId}/actions",
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
- **Scopes:** `voiceai.write`

---

## Example Request (Create Agent)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/voice-ai/agents \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "name": "Receptionist AI",
  "voice": "alloy",
  "prompt": "You are a helpful office receptionist for Acme Marketing. You answer incoming calls and book appointments."
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing `voice` or `prompt`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Agent ID not found. |
| 422 | `provider_error` | External voice synthesis provider unavailable. |
| 403 | `forbidden` | Insufficient thread access permissions. |
| 429 | `rate_limit` | Agent modification frequency exceeded. |
