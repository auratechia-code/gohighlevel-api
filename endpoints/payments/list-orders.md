---
title: "List Orders"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/list-orders"
generated_at: "2026-03-28T17:50:27.641659"
tags: ["api", "endpoint", "GET"]
---

# List Orders

The "List Orders" API allows to retrieve a paginated list of orders. Customize your results by filtering orders based on name, alt type, order status, payment mode, date range, type of source, contact, funnel products or paginate through the list using the provided query parameters. This endpoint provides a straightforward way to explore and retrieve order information.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### NODEJS
```javascript
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### PYTHON
```python
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### PHP
```php
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### JAVA
```java
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### GO
```go
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### RUBY
```ruby
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

#### POWERSHELL
```powershell
{  "data": [    {      "_id": "653f5e0cde5a1314e62a837c",      "altId": "3SwdhCu3svxI8AKsPJt6",      "altType": "location",      "contactId": "XPLSw2SVagl12LMDeTmQ",      "contactName": "James Bond",      "contactEmail": "james.bond@gohighlevel.com",      "currency": "USD",      "amount": "100",      "subtotal": "100",      "discount": "10",      "status": "completed",      "liveMode": "false",      "totalProducts": "5",      "sourceType": "funnel",      "sourceName": "onestep",      "sourceId": "kDj7BHej9Zyyq3QakJmz",      "sourceMeta": "{ domain: \"app.gohighlevel.com\", pageId:  \"rBVhyYhMsbxbO8ZqOcei\", pageUrl:  \"/v2/preview/rBVhyYhMsbxbO8ZqOcei\", stepId:   \"5a772f62-3fbc-418b-af1b-be8929dd64c2\"}",      "couponCode": "100PER",      "createdAt": "2023-11-20T10:23:36.515Z",      "updatedAt": "2024-01-23T09:57:04.846Z",      "sourceSubType": "one_step_order_form",      "fulfillmentStatus": "unfulfilled",      "onetimeProducts": "1",      "recurringProducts": "1",      "createdBy": "user123"    }  ],  "totalCount": 0}
```

