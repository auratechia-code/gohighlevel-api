---
title: "Agent AI Bot & Indicators"
resource: "conversations"
endpoint: "/conversations/agent-ai"
method: "POST"
version: "2021-07-28"
---

# Agent AI Bot & Indicators

This resource focuses on advanced interaction features for Live Chat and AI bot behaviors.

## Mandatory Header
- **Version:** `2021-07-28`

## Endpoints

### 1. Bot Typing Indicator
Triggers a "typing..." indicator in the target Live Chat window to simulate human or bot activity.

- **Method:** `POST`
- **Path:** `https://services.leadconnectorhq.com/conversations/agentai-indicator/`
- **Scopes:** `conversations.write`
- **Request Body:**
  - `conversationId`: (string) **Required.**
  - `locationId`: (string) **Required.**
  - `active`: (boolean) `true` to show, `false` to hide.

---

### 2. Add Inbound Message (Mock/Proxy)
Inject a message into a conversation as if it came from the contact (useful for migration or custom chat providers).

- **Method:** `POST`
- **Path:** `https://services.leadconnectorhq.com/conversations/inbound-message/`
- **Request Body:**
  - `type`: `LiveChat`, `SMS`, `WhatsApp`, etc.
  - `contactId`: (string) **Required.**
  - `locationId`: (string) **Required.**
  - `message`: (string) **Required.**

---

## Implementation Example (cURL)

### Toggle Typing Indicator
```bash
curl --request POST \
  --url 'https://services.leadconnectorhq.com/conversations/agentai-indicator/' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --data '{
    "conversationId": "CONV_ID_123",
    "locationId": "LOC_ID_123",
    "active": true
  }'
```
