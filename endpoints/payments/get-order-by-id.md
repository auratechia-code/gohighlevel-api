---
title: "Get Order by ID"
source: "https://marketplace.gohighlevel.com/docs/ghl/payments/get-order-by-id"
generated_at: "2026-03-28T17:50:27.637991"
tags: ["api", "endpoint", "GET"]
---

# Get Order by ID

The "Get Order by ID" API allows to retrieve information for a specific order using its unique identifier. Use this endpoint to fetch details for a single order based on the provided order ID.

## Endpoint Information

> [!IMPORTANT]
> **Method:** `GET`  
> **URL:** ``

## Code Examples

#### CURL
```curl
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### NODEJS
```javascript
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### PYTHON
```python
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### PHP
```php
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### JAVA
```java
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### GO
```go
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### RUBY
```ruby
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

#### POWERSHELL
```powershell
{  "_id": "653f5e0cde5a1314e62a837c",  "altId": "3SwdhCu3svxI8AKsPJt6",  "altType": "location",  "contactId": "XPLSw2SVagl12LMDeTmQ",  "currency": "USD",  "amount": "100",  "status": "completed",  "liveMode": "false",  "createdAt": "2023-11-20T10:23:36.515Z",  "updatedAt": "2024-01-23T09:57:04.846Z",  "fulfillmentStatus": "unfulfilled",  "contactSnapshot": "{ last_name: \"Mcclain\", type: \"lead\", first_name_lower_case: \"rogan\", email: \"anish+11@gohighlevel.com\", last_name_lower_case: \"mcclain\", location_id: \"o6241QsiRwUIJHyjuhos\", company_name: \"Jordan and Cox Trading\"}",  "amountSummary": "{ subtotal: 100, discount: 5 }",  "source": "{ type: \"invoice\", id: \"61dd48ff65b013bc39bb09c6\" }",  "items": "{ _id: 61dd33e88058b9f967ca79dc, authorizeAmount: 0, locationId: \"SBAWb4yu7A4LSc0skQ6g\", name: \"Sample Product\": price: {}, product: { name: \"Testing product\", productType: \"SERVICE\" }}",  "coupon": "{ code: \"FEST10\", _id: \"63455e48901b43d4ef364a20\" }",  "trackingId": "63319ef9-de0a-4c84-aebd-3585fb4a0cdf",  "fingerprint": "5d51db5a-42b0-4b04-ba88-2c046c982a3a",  "meta": "{ couponSessionExpired: true }",  "markAsTest": "false",  "traceId": "d3b16a92-a8ed-4e6b-8467-844750f78ed5",  "automaticTaxesCalculated": true,  "taxCalculationProvider": "taxjar",  "createdBy": "user123"}
```

