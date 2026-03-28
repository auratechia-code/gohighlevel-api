---
title: "Custom Fields V2"
source: "https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2"
generated_at: "2026-03-28T17:50:27.500602"
tags: ["api", "endpoint", ""]
---

# Custom Fields V2

Custom fields are data points that allow you to capture and store specific information tailored to your business requirements. You can create fields across field types like text, numeric, selection options and special fields like date/time or signature

## Endpoint Information

> [!IMPORTANT]
> **Method:** ``  
> **URL:** ``

## Code Examples

#### PYTHON
```python
import requests
url = 'https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2'
response = requests.get(url, headers={}, json={})
print(response.json())
```

#### NODEJS
```javascript
const axios = require('axios');
axios.get('https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2', {}, {headers: {}}).then(r => console.log(r.data));
```

#### CURL
```curl
curl -X GET 'https://marketplace.gohighlevel.com/docs/ghl/custom-fields/custom-fields-v-2' -H 'Authorization: Bearer <TOKEN>' -d '{}'
```

