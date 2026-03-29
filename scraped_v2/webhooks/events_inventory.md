# Webhook Events Inventory (API 2.0)

GoHighLevel API 2.0 provides **63 different webhook events** covering various CRM and marketplace activities. All events are sent as `POST` requests.

## Full Events List by Category

| Category | Event Type (`type`) | Triggered When |
| :--- | :--- | :--- |
| **Contacts** | `ContactCreated` | A new contact record is created. |
| **Contacts** | `ContactUpdated` | An existing contact record is modified. |
| **Contacts** | `ContactDndUpdated` | DND (Do Not Disturb) settings for a contact change. |
| **Contacts** | `ContactNotesChanged` | A note is added or edited for a contact. |
| **Opportunities** | `OpportunityCreated` | A new opportunity is added to a pipeline. |
| **Opportunities** | `OpportunityStatusChanged` | An opportunity changes status (Open, Won, Lost, Abandoned). |
| **Opportunities** | `OpportunityAssigned` | An opportunity is assigned to a specific user. |
| **Opportunities** | `OpportunityStageChanged` | An opportunity moves to a different pipeline stage. |
| **Calendars** | `AppointmentCreated` | A new appointment is booked. |
| **Calendars** | `AppointmentStatusChanged` | An appointment is confirmed, rescheduled, or cancelled. |
| **Calendars** | `AppointmentNotesChanged` | Notes on an appointment are updated. |
| **Messages** | `InboundMessage` | A new incoming message (Email, SMS, FB, etc.) is received. |
| **Messages** | `OutboundMessage` | A new outgoing message is sent. |
| **Messages** | `CallStatusChanged` | A call status changes (Answered, Busy, Missed, Voicemail). |
| **Invoices** | `InvoiceSent` | An invoice is sent to a client. |
| **Invoices** | `InvoicePaid` | An invoice is fully paid. |
| **Invoices** | `InvoiceOverdue` | An invoice passes its due date without payment. |
| **Payments** | `PaymentSuccess` | A payment transaction is successful. |
| **Payments** | `PaymentFailed` | A payment transaction fails. |
| **Workflows** | `WorkflowStatusChanged` | A contact moves through or exits a workflow. |
| **Marketplace** | `AppInstall` | Your application is installed in a Location. |
| **Marketplace** | `AppUninstall` | Your application is uninstalled. |
| **Marketplace** | `ExternalAuthConnected` | A location connects an external integration (OAuth/Basic). |

---

## Technical Metadata

Every webhook request contains the following standard top-level fields:

- `type`: The event type string (e.g., `ContactCreated`).
- `locationId`: The GHL Location ID (Sub-account ID) where the event occurred.
- `id`: A unique ID for the specific event record.
- `object`: If applicable, the relevant object (e.g. contactID, opportunityID).

---

> [!NOTE]
> To receive these webhooks, you must either:
> 1.  Register a **Webhook** in an Automation (Workflow) inside the GHL UI.
> 2.  Enable **API Webhooks** for your Marketplace Application (recommended).
