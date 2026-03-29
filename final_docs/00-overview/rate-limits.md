# Rate Limits & Throttling

GoHighLevel applies strict rate limits to ensure platform stability. All integrations (Marketplace Apps and Private Tokens) are subject to these quotas.

## Quotas

| Limit Type | Value | Reset Window |
| :--- | :--- | :--- |
| **Burst Limit** | 100 requests | 10 seconds |
| **Daily Limit** | 200,000 requests | 24 hours |

> [!CAUTION]
> Exceeding these limits will result in an HTTP **429 (Too Many Requests)** error.

---

## Response Headers

Monitor these headers to implement intelligent client-side throttling:

| Header | Description |
| :--- | :--- |
| `X-RateLimit-Limit-Daily` | Your total daily quota (e.g., `200000`). |
| `X-RateLimit-Daily-Remaining` | Remaining daily quota. |
| `X-RateLimit-Max` | Maximum allowed requests in the current window (e.g., `100`). |
| `X-RateLimit-Remaining` | Remaining requests in the current window. |
| `X-RateLimit-Interval-Milliseconds` | Window duration in ms (typically `10000`). |

---

## Backoff Strategy

When a 429 error is encountered, follow this strategy:

1. **Inspect `Retry-After`**: If present, wait for the specified number of seconds.
2. **Exponential Backoff**: If not present, wait $2^n$ seconds (where $n$ is the number of retries).
3. **Queueing**: For bulk operations, queue requests and process them at a steady rate of < 10 requests per second.
