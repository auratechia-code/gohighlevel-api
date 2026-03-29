# OAuth 2.0 Scopes Inventory

To access non-public endpoints, your application must request the appropriate scopes during the OAuth authorization flow.

## Global Scopes

| Scope Name | Access Level | Description |
| :--- | :--- | :--- |
| `contacts.readonly` | Read | Read contact details, custom fields, and tags. |
| `contacts.write` | Write | Create/Update contacts and manage tags. |
| `opportunities.readonly` | Read | Fetch opportunity details and status. |
| `opportunities.write` | Write | Create/Update opportunities in pipelines. |
| `calendars.readonly` | Read | View calendar groups and appointments. |
| `calendars.write` | Write | Book, update, or cancel appointments. |
| `locations.readonly` | Read | Fetch sub-account (location) metadata. |
| `locations.write` | Write | Update sub-account settings. |
| `users.readonly` | Read | Fetch user profiles and permissions. |
| `users.write` | Write | Create/Update users in the location. |
| `oauth.readonly` | Read | List installed apps and manage secrets. |

---

## Detailed Resource Scopes

| Resource | Read Scope | Write Scope | Endpoints Covered |
| :--- | :--- | :--- | :--- |
| **Contacts** | `contacts.readonly` | `contacts.write` | `/contacts/`, `/contacts/search` |
| **Calendars** | `calendars.readonly` | `calendars.write` | `/calendars/`, `/calendars/events` |
| **Businesses** | `businesses.readonly` | `businesses.write` | `/businesses/` |
| **Courses** | `courses.readonly` | `courses.write` | `/courses/` |
| **Forms** | `forms.readonly` | `forms.write` | `/forms/` |
| **Invoices** | `invoices.readonly` | `invoices.write` | `/invoices/` |
| **Payments** | `payments.readonly` | `payments.write` | `/payments/` |
| **Workflows** | `workflows.readonly` | `workflows.write` | `/workflows/` |

---

> [!TIP]
> Always request the **minimum** required scopes for your integration (Principle of Least Privilege).
