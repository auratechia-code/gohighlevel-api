# OAuth 2.0 Scopes (API 2.0)

This document provides a complete mapping of OAuth scopes required for various operations in the GoHighLevel API 2.0.

## Scope Contexts

- **Sub-Account**: Scopes used for operations within a specific location.
- **Agency (Company)**: Scopes used for agency-wide operations, managing multiple locations, or company-level resources.
- **Sub-Account, Agency**: Scopes that work in both contexts depending on the token type.

---

## Complete Scopes Mapping

| Scope | API Resource / Endpoints | Webhook Events | Access Type |
| :--- | :--- | :--- | :--- |
| `businesses.readonly` | `GET /businesses` | | Sub-Account |
| `businesses.write` | `POST /businesses`, `PUT`, `DELETE` | | Sub-Account |
| `calendars.readonly` | `GET /calendars/`, `GET /calendars/:calendarId/free-slots` | | Sub-Account |
| `calendars.write` | `POST /calendars/`, `PUT`, `DELETE` | | Sub-Account |
| `calendars/groups.readonly` | `GET /calendars/groups` | | Sub-Account |
| `calendars/groups.write` | `POST /calendars/groups`, `PUT`, `DELETE`, `status` | | Sub-Account |
| `calendars/resources.readonly` | `GET /calendars/resources/:resourceType` | | Sub-Account |
| `calendars/events.readonly` | `GET /calendars/events`, `GET /calendars/blocked-slots` | | Sub-Account |
| `calendars/events.write` | `POST /calendars/events/appointments`, `DELETE` | | Sub-Account |
| `campaigns.readonly` | `GET /campaigns/` | `CampaignStatusUpdate` | Sub-Account |
| `contacts.readonly` | `GET /contacts/:contactId`, `GET /contacts/`, `tasks`, `notes`, `appointments` | `ContactCreate`, `ContactDelete`, `ContactDndUpdate`, `ContactTagUpdate`, `NoteCreate`, `TaskCreate` | Sub-Account |
| `contacts.write` | `POST /contacts/`, `PUT`, `DELETE`, `tasks`, `tags`, `notes`, `campaigns`, `workflow` | | Sub-Account |
| `conversations.readonly` | `GET /conversations/:conversationsId`, `search` | `ConversationUnreadWebhook` | Sub-Account |
| `conversations.write` | `POST /conversations/`, `PUT`, `DELETE` | | Sub-Account |
| `conversations/message.readonly` | `GET conversations/messages/:messageId`, `transcription` | `InboundMessage`, `OutboundMessage` | Sub-Account |
| `conversations/message.write` | `POST /conversations/messages`, `upload`, `status`, `schedule` | `ConversationProviderOutboundMessage` | Sub-Account |
| `forms.readonly` | `GET /forms/`, `GET /forms/submissions` | | Sub-Account |
| `forms.write` | `POST /forms/upload-custom-files` | | Sub-Account |
| `invoices.readonly` | `GET /invoices/`, `GET /invoices/:invoiceId` | | Sub-Account |
| `invoices.write` | `POST /invoices`, `send`, `void`, `record-payment`, `text2pay` | | Sub-Account |
| `invoices/schedule.write` | `POST /invoices/schedule`, `auto-payment`, `cancel` | | Sub-Account |
| `invoices/template.write` | `POST /invoices/template/`, `PUT`, `DELETE` | | Sub-Account |
| `invoices/estimate.write` | `POST /invoices/estimate`, `send`, `invoice` | | Sub-Account |
| `locations.readonly` | `GET /locations/:locationId`, `search`, `timeZones` | `LocationCreate`, `LocationUpdate` | Sub-Account, Agency |
| `locations.write` | `POST /locations/`, `PUT`, `DELETE` | | Agency |
| `locations/customValues.readonly` | `GET /locations/:locationId/customValues` | | Sub-Account |
| `locations/customValues.write` | `POST`, `PUT`, `DELETE` | | Sub-Account |
| `locations/customFields.readonly` | `GET /locations/:locationId/customFields` | | Sub-Account |
| `locations/customFields.write` | `POST`, `PUT`, `DELETE` | | Sub-Account |
| `locations/tags.write` | `POST`, `PUT`, `DELETE` | | Sub-Account |
| `medias.write` | `POST /medias/upload-file`, `DELETE` | | Sub-Account |
| `opportunities.readonly` | `GET /opportunities/search`, `pipelines` | `OpportunityCreate`, `OpportunityDelete`, `OpportunityStageUpdate`, `OpportunityStatusUpdate` | Sub-Account |
| `opportunities.write` | `POST /opportunities`, `PUT`, `DELETE`, `status` | | Sub-Account |
| `payments/orders.readonly` | `GET /payments/orders/` | | Sub-Account |
| `payments/transactions.readonly` | `GET /payments/transactions/` | | Sub-Account |
| `payments/subscriptions.readonly` | `GET /payments/subscriptions/` | | Sub-Account |
| `products.readonly` | `GET /products/`, `reviews`, `stats` | | Sub-Account |
| `products.write` | `POST /products/`, `PUT`, `DELETE`, `bulk-update` | | Sub-Account |
| `oauth.readonly` | `GET /oauth/installedLocations` | | Agency |
| `oauth.write` | `POST /oauth/locationToken`, `DELETE installations` | | Sub-Account, Agency |
| `saas/location.write` | `PUT /update-saas-subscription`, `POST /enable-saas` | | Sub-Account, Agency |
| `snapshots.readonly` | `GET /snapshots`, `snapshot-status` | | Agency |
| `users.readonly` | `GET /users/`, `GET /users/:userId` | | Sub-Account, Agency |
| `users.write` | `POST /users/`, `PUT`, `DELETE` | | Sub-Account, Agency |
| `workflows.readonly` | `GET /workflows/` | | Sub-Account |
| `companies.readonly` | `GET /companies/:companyId` | | Agency |
| `associations.readonly` | `GET /associations/`, `key`, `objectKey` | `AssociationCreate`, `AssociationUpdate`, `AssociationDelete` | Sub-Account |
| `voice-ai-dashboard.readonly` | `GET /voice-ai/dashboard/call-logs` | `VoiceAiCallEnd` | Sub-Account |
| `voice-ai-agents.write` | `POST /voice-ai/agents`, `PATCH`, `DELETE` | | Sub-Account |

---

> [!TIP]
> Always request the minimum number of scopes required for your application to improve security and user trust.
