---
url: 'https://docs.workato.com/en/connectors/xero/update-bill-details.md'
description: >-
  The Update bill or invoice header details action in the Xero connector lets
  you update the header details of an existing bill or invoice.
---

# Xero - Update bill or invoice header details action

The **Update bill or invoice header details** action allows you to update an existing bill or invoice identified by the invoice ID or number. This action only allows you to update the invoice header details.

![Update bill or invoice header details](/assets/update-bill-action.RAcNSacp.png)_Xero - Update bill or invoice header details_

## Input

| Input field | Description |
| --- | --- |
| Invoice number | Input the invoice number to specify the bill or invoice you plan to update. |
| New status | Choose the new status for the invoice from the provided list. |
| Due date | Enter a new due date for the invoice. This field is required if the invoice status is set to `AUTHORISED` or `SUBMITTED`. |
| Reference | Provide an additional reference number for the bill or invoice. |
| URL | Add a link to an external online document associated with the bill or invoice. This link shows as **Go to Workato** in Xero. |

## Output

| Output field | Description |
| --- | --- |
| Type | The type of document, such as an invoice or bill. |
| Invoice ID | The unique identifier for the invoice or bill. |
| Invoice number | The number of the invoice or bill. |
| Payments | A list of payments associated with the invoice. |
| Credit notes | Details of credit notes applied to the invoice. |
| Amount due | The total amount due on the invoice. |
| Amount paid | The total amount that has been paid on the invoice. |
| Amount credited | The total amount credited against the invoice. |
| URL | The link to the invoice document or related online resource. |
| Currency code | The currency code for the invoice. |
| Currency rate | The exchange rate for the currency used in the invoice. |
| Has errors | Indicates whether any errors are associated with the invoice. |
| Is discounted | Indicates if a discount has been applied to the invoice. |
| Has attachments | Indicates if there are attachments included with the invoice. |
| Contact | The contact information related to the invoice. |
| Date | The date the invoice was issued. |
| Due date | The date by which the invoice is due for payment. |
| Status | The current status of the invoice. |
| Branding theme ID | The identifier for the branding theme associated with the invoice. |
| Line amount types | The type of line amounts on the invoice. |
| Line items | Details of each item listed on the invoice. |
| Sub total | The sub total amount before tax. |
| Total tax | The total tax amount for the invoice. |
| Total | The total amount of the invoice, including tax. |
| Updated date | The date on which the invoice was last updated. |
| Paid date | The date the invoice was paid, if applicable. |
| Reference | A reference number or note associated with the invoice. |

---
