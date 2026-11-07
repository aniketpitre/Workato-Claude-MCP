---
url: 'https://docs.workato.com/en/connectors/xero/update-bill-invoice.md'
description: >-
  The Update bill or invoice with line items action in the Xero connector lets
  you append new lines or overwrite existing line items.
---

# Xero - Update bill or invoice with line items action

The **Update bill or invoice with line items** action allows you modify an existing bill or invoice with line items in Xero. This action allows you to append new line items or overwrite existing line items of the invoice or bill.

![Update bill or invoice header details action](/assets/update-bill-invoice-action.D9DlZIkU.png)_Xero - Update bill or invoice header details action_

## Input

| Input field | Description |
| --- | --- |
| Invoice number | Enter the unique number of the invoice you plan to update. |
| Date | Specify the date of the invoice. |
| Due date | Set the due date for the invoice. This field is required if the invoice status is set to `AUTHORISED` or `SUBMITTED`. |
| Status | Choose the current status of the invoice. |
| Branding theme | Select the branding theme to apply to the invoice. |
| Amounts are | Indicate how amounts are presented on the invoice. |
| Currency code | Enter the currency code for the invoice. |
| URL | Provide the URL to any relevant online resource or document related to the invoice. |
| Reference | Input a reference note or number for the invoice. |

## Output

| Output field | Description |
| --- | --- |
| Reference | A reference note or number for the invoice or bill. |
| Type | The type of document (invoice or bill). |
| Invoice ID | The unique identifier for the invoice or bill. |
| Invoice number | The number of the invoice or bill. |
| Amount due | The total amount due on the invoice or bill. |
| Amount paid | The total amount paid against the invoice or bill. |
| Amount credited | The total amount credited to the invoice or bill. |
| URL | The link to the invoice or bill online. |
| Currency code | The currency code used for the invoice or bill. |
| Currency rate | The exchange rate applied to the invoice or bill. |
| Has errors | Indicates if there are errors associated with the invoice or bill. |
| Is discounted | Indicates if any discounts have been applied. |
| Has attachments | Indicates if there are attachments included with the invoice or bill. |
| Contact | The contact information related to the invoice or bill. |
| Date | The date the invoice or bill was issued. |
| Due date | The due date for payment of the invoice or bill. |
| Branding theme ID | The identifier for the branding theme applied to the invoice or bill. |
| Status | The current status of the invoice or bill. |
| Line amount types | The type of line amounts on the invoice or bill. |
| Line items | Details of each item listed on the invoice or bill. |
| Sub total | The subtotal amount of the invoice or bill before tax. |
| Total tax | The total tax amount for the invoice or bill. |
| Total | The total amount of the invoice or bill, including tax. |
| Updated date | The date on which the invoice or bill was last updated. |
| Paid date | The date when the invoice or bill was paid, if applicable. |

---
