---
title: "Get Services"
source: "https://marketplace.gohighlevel.com/docs/ghl/calendars/get-services-catalog"
generated_at: "2026-03-28T17:50:27.436849"
tags: ["api", "endpoint", "GET"]
---

# Get Services

Get all services in a location.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### NODEJS
```javascript
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### PYTHON
```python
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### PHP
```php
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### JAVA
```java
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### GO
```go
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### RUBY
```ruby
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

#### POWERSHELL
```powershell
{  "services": [    {      "id": "65e5f6dfacf123513228d384",      "locationId": "0007BWpSzSwfiuSl0tR2",      "name": "Hair Styling",      "description": "Full hair styling session",      "slug": "hair-styling",      "eventColor": "#66C61C",      "coverImage": "https://example.com/cover.jpg",      "serviceCategoryId": "65e5f6dfacf123513228d381",      "payment": {        "amount": 50,        "deposit": 20,        "depositType": "amount"      },      "serviceDuration": 60,      "serviceDurationUnit": "mins",      "preBuffer": 10,      "preBufferUnit": "mins",      "postBuffer": 15,      "postBufferUnit": "mins",      "isPrivate": false,      "formId": "65e5f6dfacf123513228d390",      "variations": [        {          "id": "65e5f6dfacf123513228d384",          "name": "Standard Haircut",          "serviceDuration": 30,          "serviceDurationUnit": "mins",          "payment": {            "amount": 50,            "deposit": 20,            "depositType": "amount"          },          "preBuffer": 10,          "preBufferUnit": "mins",          "postBuffer": 15,          "postBufferUnit": "mins"        }      ],      "staff": [        {          "id": "65e5f6dfacf123513228d384"        }      ]    }  ]}
```

