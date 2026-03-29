# Conversations: Messaging

Send and receive communications across various channels (SMS, Email, WhatsApp, Facebook, Instagram, Live Chat).

## 1. Sending Messages

### Send a New Message
Dispatch a message through any available provider for the contact.

- **Endpoint:** `POST /conversations/messages`

> [!TIP]
> **Official Docs:** [Send a New Message](https://marketplace.gohighlevel.com/docs/ghl/conversations/send-a-new-message)

#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/conversations/messages \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/conversations/messages',
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

url = "https://services.leadconnectorhq.com/conversations/messages"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/conversations/messages",
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
- **Scopes:** `conversations.write`
- **Headers:** 
  - `Version: 2021-07-28`
  - `Authorization: Bearer <TOKEN>`

### Body Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | String | Yes | `SMS`, `Email`, `WhatsApp`, `FB`, `IG`, `LiveChat`. |
| `contactId` | String | Yes | ID of the recipient contact. |
| `message` | String | Yes | Text content of the message. |
| `emailFrom` | String | No | Sender email (required if type is `Email`). |
| `subject` | String | No | Email subject line. |
| `attachments`| Array | No | List of hosted file URLs to attach. |

---

### Inbound Message Handling
Process incoming messages from external providers manually (rarely used, mostly handled by Webhooks).

- **Endpoint:** `POST /conversations/messages/inbound`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/conversations/messages/inbound \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/conversations/messages/inbound',
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

url = "https://services.leadconnectorhq.com/conversations/messages/inbound"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/conversations/messages/inbound",
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
- **Scopes:** `conversations.write`

---

## 2. Interaction & Status

### Update Message Status
Mark as read, unread, or update delivery state.

- **Endpoint:** `PUT /conversations/messages/{messageId}/status`

> [!TIP]
> **Official Docs:** [Update Message Status](https://marketplace.gohighlevel.com/docs/ghl/conversations/update-message-status)

#### Example Requests
```bash
curl --request PUT \
  --url https://services.leadconnectorhq.com/conversations/messages/{messageId}/status \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'PUT',
  url: 'https://services.leadconnectorhq.com/conversations/messages/{messageId}/status',
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

url = "https://services.leadconnectorhq.com/conversations/messages/{messageId}/status"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/conversations/messages/{messageId}/status",
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
- **Scopes:** `conversations.write`

### Typing Indicator (Live Chat)
Show or hide the "Agent is typing..." state in the live chat widget.

- **Endpoint:** `POST /conversations/messages/agent-typing`


#### Example Requests
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/conversations/messages/agent-typing \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Version: 2021-07-28'
```

```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/conversations/messages/agent-typing',
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

url = "https://services.leadconnectorhq.com/conversations/messages/agent-typing"

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
  CURLOPT_URL => "https://services.leadconnectorhq.com/conversations/messages/agent-typing",
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
- **Scopes:** `conversations.write`

---

## Example Request (Send SMS)
```bash
curl --request POST \
  --url https://services.leadconnectorhq.com/conversations/messages \
  --header 'Authorization: Bearer <TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'Version: 2021-07-28' \
  --data '{
  "type": "SMS",
  "contactId": "jvzfKTNdE7OYXXXXXX",
  "message": "Hi! This is a test message from our AI assistant."
}'
```

---

## Error Catalog
| HTTP | Code | Message |
|------|------|---------|
| 400 | `invalid_input` | Missing required fields or unsupported channel. |
| 401 | `unauthorized` | Missing or invalid Bearer token. |
| 403 | `forbidden` | Recipient has DND (Do Not Disturb) enabled. |
| 422 | `provider_error` | External provider (Twilio, Mailgun) rejected the message. |
| 429 | `rate_limit` | Sending limit exceeded. |
