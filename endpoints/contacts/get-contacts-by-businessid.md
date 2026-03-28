---
title: "Get Contacts By BusinessId"
source: "https://marketplace.gohighlevel.com/docs/ghl/contacts/get-contacts-by-business-id"
generated_at: "2026-03-28T17:50:27.461310"
tags: ["api", "endpoint", "GET"]
---

# Get Contacts By BusinessId

Get Contacts By BusinessId

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### NODEJS
```javascript
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### PYTHON
```python
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### PHP
```php
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### JAVA
```java
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### GO
```go
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### RUBY
```ruby
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

#### POWERSHELL
```powershell
{  "contacts": [    {      "id": "ocQHyuzHvysMo5N5VsXc",      "locationId": "C2QujeCh8ZnC7al2InWR",      "email": "JohnDeo@gmail.com",      "timezone": "Asia/Calcutta",      "country": "DE",      "source": "xyz form",      "dateAdded": "2020-10-29T09:31:30.255Z",      "customFields": [        {          "id": "MgobCB14YMVKuE4Ka8p1",          "value": "name"        }      ],      "tags": [        "nisi sint commodo amet",        "consequat"      ],      "businessId": "641c094001436dbc2081e642",      "attributions": [        {          "url": "Trigger Link",          "campaign": "string",          "utmSource": "string",          "utmMedium": "string",          "utmContent": "string",          "referrer": "https: //www.google.com",          "campaignId": "string",          "fbclid": "string",          "gclid": "CjOKCQjwnNyUBhCZARISAI9AYIFtNnIcWcYGIOQINz_ZoFI5SSLRRugSoPZoiEu27IZBY£1-MAIWmEaAo2VEALW_WCB",          "msclikid": "string",          "dclid": "string",          "fbc": "string",          "fbp": "fb. 1.1674748390986.1171287961",          "fbEventId": "Mozilla/5.0",          "userAgent": "Mozilla/5.0",          "ip": "58.111.106.198",          "medium": "survey",          "mediumId": "FglfHAn30PRwsZVyQlKp"        }      ],      "followers": "641c094001436dbc2081e642"    }  ],  "count": 10}
```

