# Authentication & Authorization

The GoHighLevel API 2.0 uses **OAuth 2.0** for Marketplace Applications and **Private Integration Tokens** for internal sub-account tools.

## Mandatory Header (All Requests)

Every API call **MUST** include the `Version` header specifying the snapshot date.

| Header | Required | Value |
| :--- | :--- | :--- |
| **Version** | ✅ | `2021-07-28` |
| **Authorization** | ✅ | `Bearer {ACCESS_TOKEN}` |

---

## 🔐 OAuth 2.0 (Marketplace Apps)

Useful for distributed applications installed across multiple GoHighLevel sub-accounts.

### 1. Request Authorization
Redirect users to:
`https://marketplace.gohighlevel.com/oauth/chooselocation?response_type=code&client_id={CLIENT_ID}&scope={SCOPES}&redirect_uri={REDIRECT_URI}`

### 2. Exchange Code for Token
Exchange the returned `code` for an `access_token` and `refresh_token`:

```bash
curl -X POST 'https://services.leadconnectorhq.com/oauth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'client_id={CLIENT_ID}' \
  -d 'client_secret={CLIENT_SECRET}' \
  -d 'grant_type=authorization_code' \
  -d 'code={CODE}' \
  -d 'user_type=Location' \
  -d 'redirect_uri={REDIRECT_URI}'
```

### 3. Token Rotation
Access tokens expire every 24 hours. Refresh tokens are valid for 365 days. Always implement an automatic refreshment logic.

---

## 🔑 Private Integration Token

Found in **Sub-account Settings > API Keys**. These tokens are static and tied to a single location.

### Usage
Treat as a Bearer token in the `Authorization` header.

```bash
Authorization: Bearer YOUR_API_KEY
```

---

> [!IMPORTANT]
> OAuth 2.0 is the **recommended** method for all integrations. Private Integration Tokens are deprecated for Multi-tenant apps.
