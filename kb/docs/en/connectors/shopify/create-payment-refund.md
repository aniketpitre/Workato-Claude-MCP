---
url: 'https://docs.workato.com/en/connectors/shopify/create-payment-refund.md'
description: >-
  The Create payment/refund action in the Shopify connector lets you create a
  payment or a refund for an order in your store.
---

# Shopify - Create payment/refund action

This action creates a payment or refund in Shopify.

## Input

| Field | Description |
| --- | --- |
| Order ID | The ID of the order to refund. |
| Transaction | A list of transactions to process as refunds. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique identifier for the refund. |
| Order ID | The unique identifier for the order that the order adjustment is associated with. |
| Amount | The value of the discrepancy between the calculated refund and the actual refund. |
| Kind | The order adjustment type. Valid values: shipping\_refund and refund\_discrepancy. |
| Status | The status of the payment/refund. |
| Gateway | The payment gateway. |
| Message | A message associated with this refund. |
| Test | Whether this is a test refund. |
| Authorization | The type of authorization |
| Currency | The currency for the refund. |
| Location ID | The ID of the location where the items should be restocked. |
| User ID | The unique identifier of the user who performed the refund. |
| Parent ID | The parent transaction ID. |
| Device ID | Information about the device used to create the order. |
| Error code | The error code. |
| Source name | The source of the refund transaction. |
| Created at | The date and time when this refund was created. |
| Receipt | The receipt associated with this refund. |
| Payment details | Information about the payment, including credit card company and credit card number. |

---
