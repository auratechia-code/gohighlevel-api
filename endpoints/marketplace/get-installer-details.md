---
title: "Get Installer Details"
source: "https://marketplace.gohighlevel.com/docs/ghl/marketplace/get-installer-details"
generated_at: "2026-03-28T17:50:27.598525"
tags: ["api", "endpoint", "GET"]
---

# Get Installer Details

Fetches installer details for the authenticated user. This endpoint returns information about the company, location, user, and installation details associated with the current OAuth token.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### NODEJS
```javascript
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### PYTHON
```python
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### PHP
```php
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### JAVA
```java
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### GO
```go
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### RUBY
```ruby
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

#### POWERSHELL
```powershell
{  "installationDetails": {    "companyId": "company123",    "locationId": "location123",    "companyName": "Example Company",    "relationshipNumber": "0-002-230",    "companyEmail": "contact@example.com",    "companyOwnerFullName": "John Doe",    "userId": "user123",    "isWhitelabelCompany": false,    "companyHighLevelPlan": "agency_monthly_497",    "marketplaceAppPlanId": "plan123",    "whitelabelDetails": {      "domain": "example.com",      "logoUrl": "https://example.com/logo.png"    }  }}
```

