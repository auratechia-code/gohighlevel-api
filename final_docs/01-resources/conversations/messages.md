---
title: "Messaging & Communication"
resource: "conversations"
endpoint: "/conversations/messages"
method: "GET|POST|PUT"
version: "2021-07-28"
---

# Messaging & Communication

This resource focuses on the actual transmission of data (messages). Supporting SMS, Email, WhatsApp, Facebook, Instagram DM, and Live Chat.

## Mandatory Header
- **Version:** `2021-07-28`

## Endpoints

### 1. Send Outbound Message
Initiate a new message to a contact via a specific channel.

- **Method:** `POST`
- **Path:** `/`
- **Scopes:** `conversations.write`
- **Request Body (Standard):**
  - `type`: (string) **Required.** `SMS`, `Email`, `WhatsApp`, `FB`, `IG`, `LiveChat`.
  - `contactId`: (string) **Required.** (Use if no `conversationId`)
  - `locationId`: (string) **Required.**
  - `message`: (string) **Required.** The text body.
  - `subject`: (string) Required for Email.
  - `attachments`: (array) Optional URLs for media files.

---

### 2. Fetch Message History
Retrieve all messages within a specific conversation.

- **Method:** `GET`
- **Path:** `/{conversationId}/messages`
- **Scopes:** `conversations.readonly`
- **Pagination:** `limit` (max 50), `offset`.

**Response (200 OK):**
```json
{
  "messages": [
    {
      "id": "msg_123",
      "body": "Hi there!",
      "direction": "outbound",
      "status": "delivered",
      "dateAdded": "2023-10-31T10:00:00Z"
    }
  ]
}
```

---

### 3. Update Message Status
Used to mark messages as delivered or read manually if not handled via Webhooks.

- **Method:** `PUT`
- **Path:** `/{messageId}/status`
- **Request Body:**
  - `status`: `delivered`, `read`, `failed`.

---

### 4. Upload & Add Attachments
- **Method:** `POST`
- **Path:** `/upload-attachments`
- **Content-Type:** `multipart/form-data`

---

## Implementation Example (cURL)

### Send SMS
```bash
curl --request POST \
  --url 'https://services.leadconnectorhq.com/conversations/messages/' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --data '{
    "type": "SMS",
    "contactId": "CONTACT_ID_123",
    "locationId": "LOCATION_ID_123",
    "message": "Hello from GHL API!"
  }'
```

### Fetch History
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/conversations/conv_123/messages' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28'
```
