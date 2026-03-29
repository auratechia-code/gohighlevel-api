# API Error Catalog

GoHighLevel returns JSON-formatted error objects for all non-2xx status codes.

| Status | Error | Typical Cause | Recommended Action |
| :--- | :--- | :--- | :--- |
| **400** | `BAD_REQUEST` | Missing required parameters or malformed body. | Check request path and body types. |
| **401** | `UNAUTHORIZED` | Invalid or expired Access Token. | Refresh token via OAuth flow. |
| **404** | `NOT_FOUND` | Resource (ID) does not exist or URL is incorrect. | Verify resource ID in path. |
| **422** | `UNPROCESSABLE` | Data failed business logic or validation (e.g., duplicate email). | Check `message` array for details. |
| **429** | `RATE_LIMIT` | Quota exceeded. | Inspect headers and back off. |
| **500** | `SERVER_ERROR` | Internal platform issue. | Wait and retry later. |

---

## ⚠️ Special Case: 422 Unprocessable Entity

For 422 errors, the `message` field is **ALWAYS an Array of strings**, not a single string.

### Example Response
```json
{
  "statusCode": 422,
  "message": [
    "Unprocessable Entity: Email already exists",
    "Unprocessable Entity: Invalid Location ID"
  ],
  "error": "Unprocessable Entity"
}
```

### Recommendation (Node.js)
Always parse the message correctly to prevent crashes:
```typescript
if (error.statusCode === 422) {
  const details = Array.isArray(error.message) ? error.message.join(', ') : error.message;
  console.log(`Validation Failed: ${details}`);
}
```

---

## Standard Error Schema (Other Codes)

For 400, 401, 404, etc., the schema is as follows:

```json
{
  "statusCode": 401,
  "message": "Invalid token: access token is invalid",
  "error": "Unauthorized"
}
```
