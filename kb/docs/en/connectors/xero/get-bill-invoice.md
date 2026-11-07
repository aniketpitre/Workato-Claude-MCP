---
url: 'https://docs.workato.com/en/connectors/xero/get-bill-invoice.md'
description: >-
  The Get bill or invoice details action in the Xero connector lets you retrieve
  detailed information for a specific bill or invoice.
---

# Xero - Get bill or invoice details action

The **Get bill or invoice details** action allows you to retrieve detailed information for a specific bill or invoice in Xero. You can search for an invoice by providing its unique ID or invoice number. For bills, use the invoice ID to obtain the details.

![Get bill or invoice details action](/assets/get-bill-details-action.0ubWAHoT.png)_Xero - Get bill or invoice details action_

## Input

| Input field | Description |
| --- | --- |
| Invoice number | Enter the full invoice number to retrieve the details of the invoice. You can use the invoice ID or invoice number for invoice details, and the invoice ID for bill details. |

## Output

| Output field | Description |
| --- | --- |
| Type | The document type. |
| Invoice ID | The unique identifier for the invoice or bill. |
| Invoice number | The assigned number for the invoice or bill. |
| Payments | Details of payments made towards the invoice. |
| Credit notes | Details of credit notes applied to the invoice. |
| Amount due | Total amount due on the invoice. |
| Amount paid | Total amount paid towards the invoice. |
| Amount credited | Total amount credited towards the invoice. |
| URL | Link to the invoice or bill online. |
| Currency code | Currency code used in the invoice. |
| Currency rate | Exchange rate used if the invoice is in a foreign currency. |
| Has errors | Indicates if there are any errors with the invoice. |
| Is discounted | Indicates if any discounts were applied to the invoice. |
| Has attachments | Indicates if there are any attachments with the invoice. |
| Contact | Details of the contact associated with the invoice. |
| Date | Date the invoice was issued. |
| Due date | Date by which the invoice is due. |
| Status | Current status of the invoice. |
| Branding theme ID | The identifier for the branding theme associated with the invoice. |
| Line amount types | Indicates how amounts are expressed. |
| Line items | The items or services included in the invoice. |
| Sub total | The total amount before tax. |
| Total tax | The total tax amount for the invoice. |
| Total | The total amount of the invoice, including tax. |
| Updated date | The date on which the invoice details were last updated. |
| Paid date | The date on which the invoice was paid in full. |
| Reference | A reference note or identifier for the invoice. |

---
