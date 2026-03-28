---
title: "Custom Fields V2 API"
source: "https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2-api"
generated_at: "2026-03-28T17:50:27.501830"
tags: ["api", "endpoint", "Version: 1.0"]
---

# Custom Fields V2 API

Custom fields are data points that allow you to capture and store specific information tailored to your business requirements. You can create fields across field types like text, numeric, selection options and special fields like date/time or signature

## Endpoint Information

> [!IMPORTANT]
> **Method:** `Version: 1.0`  
> **URL:** ``

## Code Examples

#### PYTHON
```python
import requests
url = 'https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2-api'
response = requests.version: 1.0(url, headers={}, json={})
print(response.json())
```

#### NODEJS
```javascript
const axios = require('axios');
axios.version: 1.0('https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2-api', {}, {headers: {}}).then(r => console.log(r.data));
```

#### CURL
```curl
curl -X Version: 1.0 'https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2-api' -H 'Authorization: Bearer <TOKEN>' -d '{}'
```

