---
title: "List Coupons"
resource: "payments"
endpoint: "/payments/coupons"
method: "GET"
version: "2021-07-28"
---

# List Coupons

The "List Coupons" API allows you to retrieve a list of all coupons available in your location. These coupons correspond to promotional offers and special discounts that can be applied to products and checkout forms.

## Endpoint Information

- **Method:** `GET`
- **Path:** `https://services.leadconnectorhq.com/payments/coupons`
- **Required Scopes:** `payments/coupons.readonly` (Verify based on pattern)
- **Mandatory Header:** `Version: 2021-07-28`

## Request Parameters

### Query Parameters
| Name | Type | Description |
|------|------|-------------|
| `locationId` | `string` | **Required.** The ID of the location to fetch coupons for. |
| `limit` | `integer` | Optional. Number of results per page. Default: 10. |
| `offset` | `integer` | Optional. Number of results to skip. |

## Response Schema (200 OK)

```json
{
  "data": [
    {
      "_id": "67f6c132d9485f9dacd5f123",
      "usageCount": 12,
      "limitPerCustomer": 5,
      "altId": "79t07PzK8Tvf73d12312",
      "altType": "location",
      "name": "NEWT6",
      "code": "NEWT6",
      "discountType": "percentage",
      "discountValue": 25,
      "status": "scheduled",
      "startDate": "2025-04-30T18:30:00.000Z",
      "endDate": "2025-05-30T18:30:00.000Z",
      "applyToFuturePayments": true,
      "applyToFuturePaymentsConfig": {
        "type": "fixed",
        "duration": 3,
        "durationType": "months"
      },
      "productIds": [
        "6241712be68f7a98102ba272"
      ],
      "priceIds": [
        "6241712be68f7a98102ba272"
      ],
      "variantIds": [
        "6241712be68f7a98102ba272"
      ],
      "userId": "q0m15dTLGeiGOXG123123",
      "createdAt": "2025-04-09T18:49:22.026Z",
      "updatedAt": "2025-04-09T18:49:22.026Z"
    }
  ],
  "totalCount": 20,
  "traceId": "c667b18d-8f5e-44cf-a914"
}
```

## Error Catalog

| Status | Message | Description |
|--------|---------|-------------|
| 401 | `Unauthorized` | Invalid or missing access token. |
| 404 | `Not Found` | Location not found. |
| 422 | `Unprocessable Entity` | Validation error (e.g., missing `locationId`). |

## Implementation Examples

### cURL
```bash
curl --request GET \
  --url 'https://services.leadconnectorhq.com/payments/coupons?locationId={LOCATION_ID}' \
  --header 'Authorization: Bearer {YOUR_ACCESS_TOKEN}' \
  --header 'Version: 2021-07-28' \
  --header 'Accept: application/json'
```

### SDK (Node.js)
```javascript
const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://services.leadconnectorhq.com/payments/coupons',
  params: { locationId: 'YOUR_LOCATION_ID' },
  headers: {
    Authorization: 'Bearer YOUR_ACCESS_TOKEN',
    Version: '2021-07-28',
    Accept: 'application/json'
  }
};

axios.request(options).then(function (response) {
  console.log(response.data);
}).catch(function (error) {
  console.error(error);
});
```

> [!NOTE]
> Coupons can be restricted to specific products or price points using the `productIds` and `priceIds` arrays.
