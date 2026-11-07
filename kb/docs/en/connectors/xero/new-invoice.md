---
url: 'https://docs.workato.com/en/connectors/xero/new-invoice.md'
description: >-
  The New/updated invoice trigger in the Xero connector fires when an invoice is
  created or updated in your connected Xero organization.
---

# Xero - New/updated invoice trigger

The **New/updated invoice** trigger activates when an invoice is created or updated.

![New/updated invoice trigger](/assets/new-invoice-trigger.m8bj4bvC.png)_Xero - New/updated invoice trigger_

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how often Workato checks for new or updated events. This field defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Determine the starting point for the trigger to fetch events. You cannot change this value after the recipe has been run or tested. |
| Status | Specify the invoice status that triggers the recipe. |
| Sent to contact | Filter invoices sent to a particular contact, applicable to approved invoices only. |

## Output

| Output field | Description |
| --- | --- |
| Type | The type of the invoice. |
| Invoice ID | The unique identifier for the invoice. |
| Invoice number | The invoice number assigned by Xero. |
| Payments | Payment details associated with the invoice. |
| Credit notes | Credit note details applied to the invoice. |
| Amount due | The total amount due on the invoice. |
| Amount paid | The total amount paid against the invoice. |
| Amount credited | The total amount credited to the invoice. |
| URL | The URL link to the invoice in Xero. |
| Currency code | The currency code used for the invoice. |
| Currency rate | The exchange rate applied to the invoice currency. |
| Has errors | Indicates if there are errors associated with the invoice. |
| Is discounted | Indicates if any discounts have been applied to the invoice. |
| Has attachments | Indicates if there are attachments included with the invoice. |
| Contact | Contact details associated with the invoice. |
| Date | The date the invoice was issued. |
| Due date | The due date for payment of the invoice. |
| Status | The current status of the invoice. |
| Branding theme ID | The identifier for the branding theme applied to the invoice. |
| Line amount types | The type of line amounts on the invoice. |
| Line items | Details of each item listed on the invoice. |
| Sub total | The subtotal amount of the invoice before tax. |
| Total tax | The total tax amount for the invoice. |
| Total | The total amount of the invoice, including tax. |
| Updated date | The date on which the invoice was last updated. |
| Paid date | The date when the invoice was paid, if applicable. |
| Reference | A reference note or number for the invoice. |

---
