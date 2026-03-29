# Webhook Event: App Install (`AppInstall`)

This event is triggered whenever your Marketplace Application is installed in a Location.

## Trigger Details

- **Event Category**: `Marketplace`
- **Internal Type**: `AppInstall`
- **Condition**: Triggers when a sub-account/agency completes the OAuth flow and installs your app.

---

## Example Payload

```json
{
  "type": "AppInstall",
  "locationId": "string",
  "appId": "string",
  "installId": "string",
  "userId": "string",
  "installedAt": "2024-03-29T11:00:00.000Z",
  "planId": "string",
  "trialEndsAt": null,
  "status": "Active"
}
```

---

# Webhook Event: App Uninstall (`AppUninstall`)

This event is triggered whenever your Marketplace Application is uninstalled from a Location.

## Trigger Details

- **Event Category**: `Marketplace`
- **Internal Type**: `AppUninstall`
- **Condition**: Triggers when a user removes your app from their installed integrations.

---

## Example Payload

```json
{
  "type": "AppUninstall",
  "locationId": "string",
  "appId": "string",
  "uninstalledAt": "2024-03-29T12:00:00.000Z",
  "uninstalledBy": "string"
}
```

---

> [!CAUTION]
> Always verify the `X-GHL-Signature` before processing these events.
