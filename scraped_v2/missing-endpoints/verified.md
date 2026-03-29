# Verified Missing Endpoints (API 2.0)

During the audit, several endpoints were flagged as "Missing" based on the documentation gaps. These have been **VERIFIED** to exist in the actual GoHighLevel API 2.0.

## Resource: Users

### Get User by Location (`GET /users/`)

Verified to exist.

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `locationId` | String | **YES** | The unique ID of the sub-account. |

> [!NOTE]
> This endpoint lists all users associated with the specified location.

---

## Resource: Forms & Surveys

### Get Forms (`GET /forms/`)

Verified to exist.

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `locationId` | String | **YES** | The unique ID of the sub-account. |
| `skip` | Number | No | Pagination skip (default `0`). |
| `limit` | Number | No | Pagination limit (default `10`, max `50`). |
| `type` | String | No | Filter by `form`, `survey`, or `quiz`. |

---

## Resource: Advanced Search (Bulk)

### Search Contacts (Advanced) (`POST /contacts/search-contacts-advanced`)

Verified to exist, but the documentation is currently hosted externally in ClickUp.

- **Status**: Active (Beta/Bulk)
- **External Doc**: [ClickUp Documentation Link](https://doc.clickup.com/8631005/d/h/87cpx-158396/6e629989abe7fad)
- **Use Case**: Preferred over `GET /contacts/` for large-scale filtering and segmentation.

---

> [!TIP]
> Use these verified endpoints in your integrations to avoid reliance on deprecated API v1 versions.
