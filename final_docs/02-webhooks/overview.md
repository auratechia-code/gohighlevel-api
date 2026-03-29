# Webhooks Overview

GoHighLevel provides a robust webhook system to notify your application of events in real-time.

## Security & Validation

All webhooks from GHL API 2.0 are signed using **Ed25519 (EdDSA)**. You **MUST** verify the signature to ensure the request originated from GoHighLevel.

### Public Key
```text
MCowBQYDK2VwAyEAi2HR1srL4o18O8BRa7gVJY7G7bupbN3H9AwJrHCDiOg=
```

### Verification Logic
1. Retrieve the signature from the `X-GHL-Signature` header.
2. Verify it against the raw request body using the Ed25519 algorithm and the public key above.
3. If verification fails, discard the request.

---

## Retry Policy

GHL implements a specific retry policy for webhooks based on the HTTP response from your server.

| Status Code | Action |
| :--- | :--- |
| **2xx** | Success. No further action. |
| **429** | **Retry**. Up to 6 attempts over ~70 minutes. |
| **Other (4xx/5xx)** | **No Retry**. The event is dropped. |

---

## Setup & Registration

1. **Marketplace App**: Configure your webhook URL in the App Developer Portal.
2. **Global Webhooks**: Use the `POST /webhooks/` API (if available) to register endpoints programmatically.
3. **Workflows**: Add a "Webhook" action inside a GHL Workflow.
