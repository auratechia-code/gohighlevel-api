# GoHighLevel API 2.0 Technical Library (Verified)

This directory contains high-fidelity, audited, and verified documentation for the GoHighLevel API 2.0. This library replaces the unreliable legacy documentation found in `ghl_docs_pro/`.

## 📂 Directory Structure

### 🔐 [OAuth & Security](./oauth/)
- [**OAuth Scopes Mapping**](./oauth/scopes.md): Complete mapping of 50+ scopes to their endpoints and access levels (Sub-account vs Agency).

### 🪝 [Webhooks](./webhooks/)
- [**Security & Signatures**](./webhooks/security.md): Ed25519 signature verification and the official public key.
- [**Retry Policy**](./webhooks/retries.md): Detailed 429 error retry logic.
- [**Events Inventory**](./webhooks/events_inventory.md): Full list of 63 available webhook events.
- [**Event Payloads**](./webhooks/events/): Detailed schemas for high-priority events:
  - [Invoices (Paid)](./webhooks/events/invoice-paid.md)
  - [Opportunities (Create/Update)](./webhooks/events/opportunities.md)
  - [Appointments (Create)](./webhooks/events/appointments.md)
  - [App Lifecycle (Install/Uninstall)](./webhooks/events/app-lifecycle.md)

### ⚠️ [Errors & Rate Limits](./errors/)
- [**Standard Schemas**](./errors/base_schemas.md): JSON structures for 400, 401, and the "Array Message" 422 error.
- [**Rate Limits**](./errors/rate_limits.md): Burst (100/10s) and Daily (200k) limits with header details.

### 📦 [Body Parameters](./body-params/)
- [**Contacts**](./body-params/contacts.md): Create and Update field mappings.
- [**Opportunities**](./body-params/opportunities.md): Pipeline and status management fields.
- [**Appointments**](./body-params/appointments.md): Calendar booking parameters.

### ✅ [Verified Missing Endpoints](./missing-endpoints/)
- [**Verified Endpoints List**](./missing-endpoints/verified.md): Confirmation of `Users`, `Forms`, and `Search` availability in API 2.0.

---

## 🛠️ Integration Checklist

1. [ ] Use **Header**: `Version: 2021-07-28` on all calls.
2. [ ] Validate **Webhook Signatures** using the Ed25519 public key.
3. [ ] Handle **422 Errors** by parsing the `message` field as an array.
4. [ ] Monitor **Rate Limit Headers** to prevent 429 blocks.
5. [ ] Refer to the **Scopes Table** before requesting user authorization.

---

> [!IMPORTANT]
> This documentation is the "Source of Truth" for AI Agents and CRM Integrations.
