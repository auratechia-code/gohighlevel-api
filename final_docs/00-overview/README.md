# GoHighLevel API 2.0: Master Knowledge Base

Welcome to the standardized technical library for GoHighLevel API 2.0. This documentation is optimized for both human developers and AI Agents.

---

## 🚀 00. Overview & Core Concepts
- [**Authentication**](./authentication.md): OAuth 2.0, Scopes, and Private Integration Tokens.
- [**Rate Limits**](./rate-limits.md): 10/10s burst, 200k/day limits, and backoff strategies.
- [**Error Catalog**](./error-catalog.md): Handling 422 arrays and standard JSON errors.
- [**Scopes Table**](./scopes.md): Mapping 50+ scopes to endpoint permissions.

---

## 📦 01. Resources (CRUD & Logic)
| Resource | Description | Endpoints |
| :--- | :--- | :--- |
| **Contacts** | Contact records, custom fields, notes, and tasks. | [View Docs](../01-resources/contacts/management.md) |
| **Conversations** | Multi-channel messaging, attachments, and status. | [View Docs](../01-resources/conversations/management.md) |
| **Opportunities** | Pipelines, stages, and deal management. | [View Docs](../01-resources/opportunities/management.md) |
| **Locations** | Sub-account lifecycle and custom identifiers. | [View Docs](../01-resources/locations/management.md) |
| **Calendars** | Booking, appointments, and availability. | [View Docs](../01-resources/calendars/management.md) |
| **Products** | Inventory, pricing, and collections. | [View Docs](../01-resources/products/management.md) |
| **Funnels** | Landing pages and URL redirects. | [View Docs](../01-resources/funnels/management.md) |
| **Social Planner** | Post scheduling and account attachment. | [View Docs](../01-resources/social-planner/posting.md) |
| **SaaS** | Agency-level provisioning and rebilling. | [View Docs](../01-resources/saas/management.md) |
| **Users** | Personnel management and permissions. | [View Docs](../01-resources/users/management.md) |
| **Voice AI** | Agent actions and call analysis. | [View Docs](../01-resources/voice-ai/management.md) |

---

## 🪝 02. Webhooks (Real-time Events)
- [**Events Catalog**](../02-webhooks/events-catalog.md): List of 63 supported events.
- [**Security & Verification**](../02-webhooks/overview.md): Ed25519 signature validation.
- [**Event Payloads**](../02-webhooks/payloads/): Trigger-specific JSON schemas.

---

## 🛠️ Implementation Specs (API 2.0)
- **Base URL**: `https://services.leadconnectorhq.com`
- **Mandatory Header**: `Version: 2021-07-28`
- **Auth Format**: `Authorization: Bearer <ACCESS_TOKEN>`

---

> [!IMPORTANT]
> This library was programmatically hydrated with official documentation URLs and multi-language code snippets (cURL, Node.js, Python, PHP) on 2026-03-29.
