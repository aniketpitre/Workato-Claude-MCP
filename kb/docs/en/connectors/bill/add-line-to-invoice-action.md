---
url: 'https://docs.workato.com/en/connectors/bill/add-line-to-invoice-action.md'
description: >-
  The Add line to invoice action in the BILL connector adds a line item,
  including item, quantity, and price, to an existing invoice in BILL.
---

# BILL - Add line to invoice action

The **Add line to invoice** action adds a line item to an existing invoice in BILL.

## Input

| Field | Description |
| --- | --- |
| Invoice ID | Provide the internal ID of the invoice to update. |
| Item ID | Provide the internal ID of the item associated with the invoice. |
| Description | Enter a description for the invoice. |
| Quantity | Enter the quantity of items sold or the number of hours spent providing the service. |
| Price | Enter the price per item or hour. |
| Taxable | Specify whether the line item is taxable or not. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the modified invoice. |
| Is active | The status of the invoice. |
| Customer ID | The ID of the customer account associated with the invoice. |
| Customer | An object that contains information about the customer account associated with the invoice, such as its `ID`, `Name`, `Account type`, and `Parent customer ID`. |
| Job ID | The ID of the job associated with the invoice. |
| Invoice number | The user-generated number assigned to the invoice. |
| Invoice date | The invoice creation date. |
| Due date | The invoice due date. |
| Created time | The date and time when the invoice was created. |
| Updated time | The date and time when the invoice was last updated. |
| Amount | The total cost of all items in the invoice. |
| Amount due | The outstanding balance owed by the customer. |
| Payment status | The payment status of the invoice. |
| Description | Provides a description of the invoice. |
| PO number | The purchase order number associated with the invoice. |
| Is to be printed | Indicates whether bill.com prints and mails the invoice to the customer. |
| Is to be emailed | Indicates whether bill.com emails the invoice to the customer. |
| Item sales tax | The ID of the sales tax applied to all taxable items in the invoice. |
| Sales tax percentage | The sales tax percentage applied to all taxable items in the invoice. |
| Sales tax total | The total amount of sales tax applied to the invoice. |
| Department ID | The ID of the department associated with the invoice. |
| Pay to bank account ID | The ID of the bank account receiving the invoice payment. |
| Pay to chart of account ID | The ID of the chart of accounts receiving the invoice payment. |
| Invoice line items | A datatree that contains information about invoice line items, such as their `ID`, `Invoice ID`, `Item ID`, and `Description`. |

---
