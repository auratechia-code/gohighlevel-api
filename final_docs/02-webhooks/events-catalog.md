# Webhook Events Catalog

GoHighLevel API 2.0 supports **63 different webhook events** across various CRM resources.

| Event Type | Category | Trigger | Payload Verified |
| :--- | :--- | :--- | :---: |
| `ContactCreated` | Contact | New contact added. | ✅ |
| `ContactUpdated` | Contact | Contact modified. | ⚠️ |
| `ContactDndUpdated`| Contact | DND settings changed. | ⚠️ |
| `OpportunityCreated`| Opportunity | New opportunity added.| ✅ |
| `OpportunityStatusChanged` | Opportunity | Status (Won/Lost) changed. | ✅ |
| `AppointmentCreated`| Calendar | New booking confirmed. | ✅ |
| `InboundMessage` | Message | Incoming Email/SMS/FB. | ⚠️ |
| `OutboundMessage` | Message | Outgoing message sent. | ⚠️ |
| `InvoicePaid` | Invoice | Invoice fully paid. | ✅ |
| `AppInstall` | App | App installed in Location. | ✅ |
| `AppUninstall` | App | App removed. | ✅ |

*(... and 50+ other events listed in the technical inventory ...)*

## Categorized Triggers

### 📢 Contact Events
- `ContactCreated`, `ContactUpdated`, `ContactDelete`, `ContactTagAdded`, `ContactTagRemoved`, `ContactNotesChanged`.

### 💰 Opportunity Events
- `OpportunityCreated`, `OpportunityStatusChanged`, `OpportunityStageChanged`, `OpportunityAssigned`.

### 📅 Calendar Events
- `AppointmentCreated`, `AppointmentStatusChanged`, `AppointmentNotesChanged`.

### 📧 Message Events
- `InboundMessage`, `OutboundMessage`, `CallStatusChanged`.

### 🧾 Invoice & Payments
- `InvoiceSent`, `InvoicePaid`, `PaymentSuccess`, `PaymentFailed`.

---

> [!NOTE]
> For individual event payload details, see the [Payloads Directory](./payloads/).
