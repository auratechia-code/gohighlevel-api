---
title: "Tasks & Tags"
resource: "locations"
endpoint: "/locations/tasks-tags"
method: "GET|POST|PUT|DELETE"
version: "2021-07-28"
---

# Tasks & Tags

This documentation covers task and tag management at the location level. Tasks are internal to-do items, and tags are for categorizing contacts and other entities.

## Tags
Tags allow for flexible organization and filtering.

### 1. List Tags
Retrieve all tags defined in a location.

- **Method:** `GET`
- **Path:** `https://services.leadconnectorhq.com/locations/{locationId}/tags`
- **Scopes:** `locations.readonly`

---

### 2. Create Tag
- **Method:** `POST`
- **Path:** `/`
- **Scopes:** `locations.write`
- **Request Body:**
  - `name`: (string) **Required.** Tag label.

---

### 3. Delete Tag
- **Method:** `DELETE`
- **Path:** `/{tagId}`
- **Scopes:** `locations.write`

---

## Tasks
Tasks can be one-off, related to a contact, or recurring for the user.

### 1. Search Tasks
- **Method:** `GET`
- **Path:** `https://services.leadconnectorhq.com/locations/{locationId}/tasks/search`
- **Query Params:** `assignedTo`, `contactId`, `completed`.

---

### 2. Create Recurring Task
Define a task that repeats via rules.

- **Method:** `POST`
- **Path:** `/`
- **Scopes:** `locations.write`
- **Request Body:**
  - `title`: (string) **Required.**
  - `body`: (string)
  - `assignedTo`: (string) User ID.
  - `frequency`: `daily`, `weekly`, `monthly`.

---

## Implementation Example (cURL)

### List All Tags
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/locations/LOC_ID_123/tags' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28'
```

### Create a Single Tag
```bash
curl --request POST \
  --url 'https://services.leadconnectorhq.com/locations/LOC_ID_123/tags/' \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --data '{"name": "VIP Customer"}'
```
