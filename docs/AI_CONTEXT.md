# AI Context: GoHighLevel (GHL) API 2.0

This document provides high-fidelity context for LLMs (Claude, GPT, Gemini, etc.) to ensure accurate code generation and technical support for the GHL API.

## 🌟 Technical Source of Truth
The primary source of truth for all endpoint schemas, parameters, and examples is the `docs/01-api-reference/` directory. 
**DO NOT alucinate endpoints.** If an endpoint is not in this directory, it is likely deprecated or internal.

## 🛠️ Mandatory Request Headers
Every request to the GHL API must include:
- `Authorization: Bearer {{ACCESS_TOKEN}}`
- `Version: 2021-07-28` (Crucial: Using any other version may result in 404 or outdated schemas).
- `Content-Type: application/json`

## 🔗 Base URLs
- **Production**: `https://services.leadconnectorhq.com`
- **Deprecated (V1)**: `https://api.gohighlevel.com` (Do not use).

## 🔑 Authentication & Tokens
- **Location Token (Sub-Account)**: Used for resource-level operations (contacts, calendars, etc.). Scopes are typically `contacts.readonly`, `calendars.write`, etc.
- **Agency Token**: Used for account management and high-level configuration.
- Use the appropriate scope for the operation as defined in the `METADATA` section of each endpoint doc.

## ⚠️ Error Handling & Troubleshooting
| Code | Meaning | Common Cause |
| :--- | :--- | :--- |
| **401** | Unauthorized | Expired token or incorrect Bearer format. |
| **403** | Forbidden | Missing required scope in the token. |
| **404** | Not Found | Incorrect `Version` header or invalid resource ID. |
| **422** | Unprocessable Entity | Validation error (check request body schema). |
| **429** | Too Many Requests | Rate limit exceeded. |

## 📉 Rate Limits & Pagination
- **Rate Limits**: Respect the 429 status code and implement exponential backoff.
- **Pagination**: Most GET collections use `limit` and `offset` (or `skip`). The response includes a `meta` object with `total`, `nextPage`, etc.

## 🚫 Critical Restrictions
- **Do not use `internal/`**: This folder contains raw data and tools, not stable documentation.
- **Do not invent fields**: Only use fields documented in the response schemas.
- **V1 vs V2**: This library exclusively covers API 2.0. Do not assume compatibility with legacy "GHL V1" implementations.
