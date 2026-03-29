# Evento: `InvoicePaid`

**Categoría:** Invoices
**Trigger:** Se dispara cuando un comprobante (invoice) es marcado como pagado exitosamente. No incluye pagos parciales.
**Criticidad para agentes IA:** ALTA (Acción de fulfillment inmediata)

## Payload Completo
```json
{
  "type": "InvoicePaid",
  "locationId": "string — ID de la ubicación",
  "id": "string — ID único del evento (idempotencia)",
  "invoiceId": "string — ID del comprobante",
  "contactId": "string — ID del contacto relacionado",
  "amountPaid": "number — Monto real recibido",
  "currency": "string — Código de moneda (USD, EUR, etc.)",
  "status": "string — 'Paid'",
  "paidAt": "ISOString — Fecha y hora del pago"
}
```

## Campos Clave
| Campo | Tipo | Descripción | Usar para |
|-------|------|-------------|-----------|
| `invoiceId` | string | ID de la factura. | Conciliación contable. |
| `amountPaid` | number | Monto pagado. | Verificación de pago total. |
| `paidAt` | string | Timestamp del pago. | Registro histórico. |

## Handler Recomendado (Node.js)
```typescript
case 'InvoicePaid': {
  const { id, amountPaid, invoiceId, locationId } = event;
  // logic: Mark order as complete
  // logic: Trigger fulfillment workflow
  break;
}
```

## Notas de Implementación
> Este evento solo se dispara tras la confirmación exitosa del procesador de pagos (Stripe, etc.) o tras el registro manual del pago total en el dashboard.
