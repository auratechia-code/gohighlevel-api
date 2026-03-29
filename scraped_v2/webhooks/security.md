# Webhook Security & Verification (API 2.0)

GoHighLevel API 2.0 uses a signature-based verification system to ensure that webhook requests are authentic and have not been tampered with.

## Signature Headers

| Header | Description | Algorithm |
| :--- | :--- | :--- |
| `X-GHL-Signature` | **Primary Signature** for API 2.0. | Ed25519 (EdDSA) |
| `X-WH-Signature` | **Legacy Signature**. Deprecated on 1 July 2026. | RSA-SHA256 |

> [!IMPORTANT]
> It is highly recommended to use the `X-GHL-Signature` (Ed25519) for all new integrations.

## EdDSA Verification (X-GHL-Signature)

Verification is done using the provided Public Key and the raw request body.

### Public Key
**`MCowBQYDK2VwAyEAi2HR1srL4o18O8BRa7gVJY7G7bupbN3H9AwJrHCDiOg=`**

### How to Verify
1. **Get Raw Request Body**: Ensure you capture the exact JSON payload from the request as a string/byte array.
2. **Decode Signature**: The `X-GHL-Signature` header is a Base64 encoded string.
3. **Verify**: Use an Ed25519 verification library with the Public Key to check if the payload matches the signature.

---

## Retries and Reliability

GHL implement a selective retry policy to ensure data delivery without overloading your server.

### Retry Trigger
Webhooks are retried **ONLY** for:
- **HTTP 429 (Too Many Requests)**

> [!CAUTION]
> Webhooks are **NOT** retried for HTTP 400, 401, 404, or any 5xx errors. Ensure your endpoint responds with 200/201/204 fast and handles internal logic asynchronously.

### Retry Policy
- **Limit**: Up to 6 attempts.
- **Interval**: 10 minutes + jitter (randomized offset).
- **Total Duration**: Approximately 1 hour and 10 minutes.

### Rate Limits
GHL can send thousands of webhooks concurrently. Ensure your endpoint has:
- Adequate concurrency capacity.
- Asynchronous processing logic.
- Proper error handling (return 200 even if internal processing fails, then log the error).
