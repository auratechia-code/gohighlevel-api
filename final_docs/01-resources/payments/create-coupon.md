---
title: "Create Coupon"
resource: "payments"
endpoint: "/payments/coupons"
method: "POST"
version: "2021-07-28"
---

# Create Coupon

The "Create Coupon" API allows you to create a new promotional coupon with customizable parameters such as discount amount, validity period, usage limits, and applicable products.

## Endpoint Information

- **Method:** `POST`
- **Path:** `https://services.leadconnectorhq.com/payments/coupons`
- **Required Scopes:** `payments/coupons.write`
- **Mandatory Header:** `Version: 2021-07-28`

## Request Body

| Name | Type | Description |
|------|------|-------------|
| `locationId` | `string` | **Required.** The ID of the location to create the coupon in. |
| `name` | `string` | **Required.** Internal name for the coupon. |
| `code` | `string` | **Required.** The actual coupon code (e.g., "SAVE25"). |
| `discountType` | `string` | **Required.** Type of discount: `percentage` or `fixed`. |
| `discountValue` | `number` | **Required.** The value of the discount (e.g., 25 for 25%). |
| `startDate` | `string` | Optional. ISO 8601 date string for when the coupon starts. |
| `endDate` | `string` | Optional. ISO 8601 date string for when the coupon expires. |
| `limitPerCustomer` | `integer` | Optional. Maximum times a single customer can use this coupon. |
| `usageCount` | `integer` | Optional. Total maximum uses allowed for this coupon. |
| `applyToFuturePayments` | `boolean` | Optional. Whether to apply to recurring payments. |
| `productIds` | `array` | Optional. List of product IDs these coupons apply to. |

## Response Schema (201 Created)

```json
{
  "_id": "67f6c132d9485f9dacd5f123",
  "usageCount": 0,
  "limitPerCustomer": 5,
  "altId": "{LOCATION_ID}",
  "altType": "location",
  "name": "NEWT6",
  "code": "NEWT6",
  "discountType": "percentage",
  "discountValue": 25,
  "status": "scheduled",
  "startDate": "2025-04-30T18:30:00.000Z",
  "endDate": "2025-05-30T18:30:00.000Z",
  "applyToFuturePayments": true,
  "userId": "q0m15dTLGeiGOXG123123",
  "createdAt": "2025-04-09T18:49:22.026Z",
  "updatedAt": "2025-04-09T18:49:22.026Z",
  "traceId": "c667b18d-8f5e-44cf-a914"
}
```

## Error Catalog

| Status | Message | Description |
|--------|---------|-------------|
| 400 | `Bad Request` | Missing required fields or invalid data. |
| 401 | `Unauthorized` | Invalid or missing access token. |
| 403 | `Forbidden` | Insufficient permissions for this scope. |
| 422 | `Unprocessable Entity` | A coupon with this code already exists. |

## Implementation Examples

### cURL
```bash
curl --request POST \
  --url 'https://services.leadconnectorhq.com/payments/coupons' \
  --header 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
  --header 'Version: 2021-07-28' \
  --header 'Content-Type: application/json' \
  --data '{
    "locationId": "YOUR_LOCATION_ID",
    "name": "Summer Sale",
    "code": "SUMMER25",
    "discountType": "percentage",
    "discountValue": 25
  }'
```

### SDK (Node.js)
```javascript
const axios = require('axios');

const options = {
  method: 'POST',
  url: 'https://services.leadconnectorhq.com/payments/coupons',
  headers: {
    Authorization: 'Bearer YOUR_ACCESS_TOKEN',
    Version: '2021-07-28',
    'Content-Type': 'application/json'
  },
  data: {
    locationId: 'YOUR_LOCATION_ID',
    name: 'Summer Sale',
    code: 'SUMMER25',
    discountType: 'percentage',
    discountValue: 25
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```
