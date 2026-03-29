# Webhook Event: Invoice Paid (`InvoicePaid`)

This event is triggered whenever an invoice is successfully paid by a customer.

## Trigger Details

- **Event Category**: `Invoice`
- **Internal Type**: `InvoicePaid`
- **Source**: GHL HighLevel CRM (In-App)
- **Condition**: Triggers when an invoice status changes to `Paid`.

---

## Example Payload

```json
{
  "type": "InvoicePaid",
  "locationId": "string",
  "invoiceId": "string",
  "invoiceNumber": "INV-12345",
  "currency": "USD",
  "totalAmount": 15000,
  "discountAmount": 0,
  "taxAmount": 375,
  "subTotalAmount": 14625,
  "paidAmount": 15000,
  "dueAmount": 0,
  "status": "Paid",
  "dateIssued": "2024-03-29T10:00:00.000Z",
  "dueDate": "2024-04-05T10:00:00.000Z",
  "paidDate": "2024-03-29T11:30:00.000Z",
  "customerName": "John Doe",
  "customerEmail": "john.doe@example.com",
  "contactDetails": {
    "id": "string",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phoneNo": "+1234567890",
    "address": "123 Main St, New York, NY",
    "website": "https://example.com",
    "logoUrl": "https://example.com/logo.png",
    "customValues": [
      "Value 1",
      "Value 2"
    ]
  },
  "lineItems": [
    {
      "id": "string",
      "name": "Consulting Service",
      "description": "Professional consulting",
      "quantity": 1,
      "amount": 15000,
      "tax": 375,
      "discount": 0
    }
  ]
}
```

---

## Implementation Considerations

- **Multiple Payments**: Some invoices may have partial payments. Ensure you check the `dueAmount` and `status`.
- **Concurrency**: Multiple invoices could be paid simultaneously (e.g., during a bulk transaction).
- **Security**: Always verify the `X-GHL-Signature` before processing.
