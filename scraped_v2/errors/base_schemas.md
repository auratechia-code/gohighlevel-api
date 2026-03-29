# API Error Schemas (V2)

GoHighLevel API 2.0 returns standardized JSON objects for error responses. 

> [!WARNING]
> The `message` field format varies depending on the status code (as seen in official documentation for `POST /contacts/`).

## Common Error Codes

### 400 Bad Request
Triggered when the request is malformed or missing required parameters.
```json
{
  "statusCode": 400,
  "message": "Bad Request"
}
```

### 401 Unauthorized
Triggered when the `Authorization` header is missing, invalid, or expired.
```json
{
  "statusCode": 401,
  "message": "Invalid token: access token is invalid",
  "error": "Unauthorized"
}
```

### 422 Unprocessable Entity
Triggered by validation errors (e.g., invalid email format, missing required body fields).
```json
{
  "statusCode": 422,
  "message": [
    "Unprocessable Entity"
  ],
  "error": "Unprocessable Entity"
}
```
> [!NOTE]
> For 422 errors, the `message` field is typically an **array of strings**, listing the specific validation failures.

---

## Error Handling Best Practices

1. **Check the `statusCode`**: Always use the HTTP status code as the first point of truth.
2. **Handle `message` Dynamically**: Since it can be a string or an array, your error parser should handle both types to avoid runtime crashes.
3. **Log the `error` Field**: Use the `error` field (if present) for high-level classification.
