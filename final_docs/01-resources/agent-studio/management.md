# Agent Studio: AI Orchestration

Programmatically execute and manage AI agents and their metadata.

## 1. Agent Operations

### Execute Agent
Trigger an AI agent's logic for a specific session or task.

- **Endpoint:** `POST /agent-studio/{agentId}/execute`

> [!TIP]
> **Official Docs:** [Execute Agent](https://marketplace.gohighlevel.com/docs/ghl/agent-studio/execute-agent)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/agent-studio/{agentId}/execute \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/agent-studio/{agentId}/execute',
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

url = "https://services.leadconnectorhq.com/agent-studio/{agentId}/execute"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/agent-studio/{agentId}/execute",
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
- **Scopes:** `agent-studio.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `locationId` | String | Yes | ID of the location. |
| `input` | String | Yes | Plain text or JSON encoded input for the agent. |
| `sessionId` | String | No | Existing session context. |

---

### Update Agent Metadata
Modify descriptive properties or configurations of an AI agent.

- **Endpoint:** `PUT /agent-studio/{agentId}/metadata`


#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/agent-studio/{agentId}/metadata \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/agent-studio/{agentId}/metadata',
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

url = "https://services.leadconnectorhq.com/agent-studio/{agentId}/metadata"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/agent-studio/{agentId}/metadata",
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
- **Method:** `PUT`
- **Scopes:** `agent-studio.write`

---

## 2. Deployment & Staging

### Promote to Production
Move an agent from draft/staging into the active production environment.

- **Endpoint:** `POST /agent-studio/{agentId}/promote`

> [!TIP]
> **Official Docs:** [Promote to Production](https://marketplace.gohighlevel.com/docs/ghl/agent-studio/promote-and-publish)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/agent-studio/{agentId}/promote \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/agent-studio/{agentId}/promote',
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

url = "https://services.leadconnectorhq.com/agent-studio/{agentId}/promote"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/agent-studio/{agentId}/promote",
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
- **Scopes:** `agent-studio.write`

---

## Example Request (Execute Agent)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/agent-studio/bot-123-abc/execute \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "locationId": "ve9EPM428h8vShlRW1KT",
  "input": "Summarize the last 5 contact interactions.",
  "sessionId": "sess_9988776655"
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Malformed input or missing `locationId`. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 404 | `not_found` | Agent ID or Session not found. |
| 422 | `unprocessable_entity` | Agent logic error during execution. |
| 429 | `quota_exceeded` | AI Model token limits reached. |
