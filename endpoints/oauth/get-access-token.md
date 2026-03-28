---
title: "Get Access Token"
source: "https://marketplace.gohighlevel.com/docs/ghl/oauth/get-access-token"
generated_at: "2026-03-28T17:50:27.608863"
tags: ["api", "endpoint", "POST"]
---

# Get Access Token

Use Access Tokens to access GoHighLevel resources on behalf of an authenticated location/company.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `POST`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### NODEJS
```javascript
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### PYTHON
```python
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### PHP
```php
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### JAVA
```java
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### GO
```go
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### RUBY
```ruby
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

#### POWERSHELL
```powershell
{  "access_token": "ab12dc0ae1234a7898f9ff06d4f69gh",  "token_type": "Bearer",  "expires_in": 86399,  "refresh_token": "xy34dc0ae1234a4858f9ff06d4f66ba",  "scope": "conversations/message.readonly conversations/message.write",  "userType": "Location",  "locationId": "l1C08ntBrFjLS0elLIYU",  "companyId": "l1C08ntBrFjLS0elLIYU",  "approvedLocations": [    "l1C08ntBrFjLS0elLIYU"  ],  "userId": "l1C08ntBrFjLS0elLIYU",  "planId": "l1C08ntBrFjLS0elLIYU",  "isBulkInstallation": "Bearer",  "installToFutureLocations": true,  "approveAllLocations": true}
```

