# Rate Limits & Response Headers (V2)

GoHighLevel applies strict rate limits across all integration levels (Marketplace Apps, Sub-account/Private Tokens).

## Standard Limits

| Limit Type | Value | Triggered When |
| :--- | :--- | :--- |
| **Burst Limit** | 100 requests / 10 seconds | Exceeding 10 req/s on average. |
| **Daily Limit** | 200,000 requests / day | Reach total daily quota. |

> [!CAUTION]
> Reaching these limits results in a **429 (Too Many Requests)** response.

---

## Response Headers

You should monitor these headers on every response to intelligently throttle your application.

| Header | Description |
| :--- | :--- |
| `X-RateLimit-Limit-Daily` | Your total daily quota (e.g., `200000`). |
| `X-RateLimit-Daily-Remaining` | Remaining daily quota. |
| `X-RateLimit-Max` | Maximum allowed requests in the current window (e.g., `100`). |
| `X-RateLimit-Remaining` | Remaining requests in the current window. |
| `X-RateLimit-Interval-Milliseconds` | Window duration in ms (typically `10000` for 10s). |

### Example Header
```http
X-RateLimit-Limit-Daily: 200000
X-RateLimit-Daily-Remaining: 199950
X-RateLimit-Max: 100
X-RateLimit-Remaining: 95
X-RateLimit-Interval-Milliseconds: 10000
```

---

## Retrying 429 Errors

If you receive a 429 response, do NOT immediately retry the request.

1. **Wait**: Use the `X-RateLimit-Interval-Milliseconds` as a starting point.
2. **Backoff**: Implement an exponential backoff strategy.
3. **Queue**: For bulk operations (e.g. data sync), queue requests and process them sequentially at a rate below 10 req/s.
