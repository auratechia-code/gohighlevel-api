---
title: "CUSTOM_OBJECTS API"
source: "https://marketplace.gohighlevel.com/docs/ghl/objects/custom-objects-api"
generated_at: "2026-03-28T17:50:27.611480"
tags: ["api", "endpoint", "Version: 1.0"]
---

# CUSTOM_OBJECTS API

Custom objects are completely customizable objects that allow you to store and manage information tailored to your unique business needs. With custom objects, you can create custom fields, establish relationships, and integrate them into workflows, providing flexibility beyond standard objects like Contacts, Opportunities or Companies.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `Version: 1.0`  
> **URL:** ``

## Code Examples

#### PYTHON
```python
import requests
url = 'https://marketplace.gohighlevel.com/docs/ghl/objects/custom-objects-api'
response = requests.version: 1.0(url, headers={}, json={})
print(response.json())
```

#### NODEJS
```javascript
const axios = require('axios');
axios.version: 1.0('https://marketplace.gohighlevel.com/docs/ghl/objects/custom-objects-api', {}, {headers: {}}).then(r => console.log(r.data));
```

#### CURL
```curl
curl -X Version: 1.0 'https://marketplace.gohighlevel.com/docs/ghl/objects/custom-objects-api' -H 'Authorization: Bearer <TOKEN>' -d '{}'
```

