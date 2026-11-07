---
url: 'https://docs.workato.com/en/connectors/concur/triggers/new-updated-invoice.md'
description: >-
  The New/updated invoice trigger activates when an invoice is created or
  updated in SAP Concur.
---

# SAP Concur - New/updated invoice trigger

The **New/updated invoice** trigger activates when an invoice is created or updated in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Specify when the recipe should start picking up invoices. When you start the recipe for the first time, it picks up invoices created or updated after the specified date and time. Leave this field empty to get invoices from one hour ago. You can't change this value after running or testing the recipe. |
| Trigger poll interval | Select how frequently to check for new events. |

## Output

| Output field | Description |
| --- | --- |
| Payment request ID | The unique identifier for the payment request. |
| Payment request URI | The URI referencing the payment request. |
| Approval status code | The invoice's approval status code. |
| Payment status code | The code reflecting the invoice payment status. |
| Vendor code | The unique identifier for the vendor. |
| Vendor name | The name of the vendor. |
| Invoice number | The invoice's reference number. |
| Purchase order number | The purchase order number associated with the invoice. |
| Create date | The date when the invoice was created. |
| Paid date | The date when journal entries were integrated with the financial system. |
| User defined date | The invoice date assigned by the user. |
| Last modified date | The most recent modification timestamp. |
| Extracted date | The date the invoice was extracted. |
| Total | The invoice's total amount. |
| Currency code | The three-letter ISO 4217 currency code for the invoice currency. |
| Owner login ID | The login identifier of the invoice owner. |
| Owner name | The name of the invoice owner. |
| Is deleted | Indicates whether the invoice has been deleted. Deleted invoices are retained for history. |
| Payment method | The payment method type classification. |
| ID | The unique resource identifier. |
| URI | The URI to the resource. |

---
