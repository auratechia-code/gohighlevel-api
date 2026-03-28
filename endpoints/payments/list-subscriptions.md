---
title: "List Subscriptions"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/list-subscriptions"
generated_at: "2026-03-28T17:50:27.642762"
tags: ["api", "endpoint", "GET"]
---

# List Subscriptions

The "List Subscriptions" API allows to retrieve a paginated list of subscriptions. Customize your results by filtering subscriptions based on name, alt type, subscription status, payment mode, date range, type of source, contact, subscription id, entity id, contact or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve subscription information.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### NODEJS
```javascript
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### PYTHON
```python
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### PHP
```php
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### JAVA
```java
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### GO
```go
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### RUBY
```ruby
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### POWERSHELL
```powershell
{  "data": [    {      "_id": "64bf78af39118e4011926cba",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "status": "active",      "liveMode": "false",      "entityType": "order",      "entityId": "62f4db0f3059ecee61379012",      "entitySourceType": "funnel",      "entitySourceName": "Attribution Funnel",      "entitySourceId": "bevrkPbLaDNXFaqfLKMm",      "entitySourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"sxC4lNhFIavEnLZh5KhC\", pageUrl:  \"/v2/preview/sxC4lNhFIavEnLZh5KhC\", stepId: \"7d303d1f-cb85-403d-b548-bf01de5c7bb0\" }",      "subscriptionId": "I-0UE609H8E43P",      "subscriptionSnapshot": "{ status: \"ACTIVE\", status_update_time: \"2022-08-16T11:06:53Z\", id: \"I-0UE609H8E43P\", plan_id: \"P-82K11750F0313430KMLRGE6Y\", start_time: \"2022-08-16T11:05:31Z\", quantity: 1 }",      "paymentProviderType": "stripe",      "paymentProviderConnectedAccount": "ATn0CqrzrWS5ak185Bsb1xCpyzBDOZ8WdRxyFotppLYePTDhiuQ49H5QXO_L-4HKk1GBn7f9_QhbNK2s",      "ipAddress": "103.100.16.82",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2023-11-20T10:23:36.515Z",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

