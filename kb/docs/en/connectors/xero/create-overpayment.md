---
url: 'https://docs.workato.com/en/connectors/xero/create-overpayment.md'
description: >-
  The Create overpayment action in the Xero connector lets you create an
  overpayment with a line item in your connected Xero organization.
---

# Xero - Create overpayment action

The **Create overpayment** action allows you to create an overpayment with a line item in Xero.

![Create overpayment action](/assets/create-overpayment-action.btiOFs3C.png)_Xero - Create overpayment action_

## Input

| Input field | Description |
| --- | --- |
| Bank transaction types | Select the type of bank transaction. |
| Contact ID (contact) | Enter the unique identifier for the contact in Xero. |
| Name (contact) | Specify the name of the contact. |
| Email address (contact) | Provide the email address of the contact. |
| Account ID (bank account) | Select the ID of the bank account where the overpayment is recorded. |
| Code (bank account) | Enter the code of the bank account. |
| Reference | Add a reference for the transaction, such as an invoice number or note. |
| Bank transaction status | Set the status of the bank transaction. |
| URL | Optionally include a link to an external document related to the overpayment. |
| Date of transaction | Specify the date when the overpayment occurred. |
| Description (line items) | Provide a description for each overpayment line item. |
| Unit price (line items) | Enter the unit price for each item in the overpayment. |
| Line amount (line items) | Specify the line amount for each item in the overpayment. |

## Output

| Output field | Description |
| --- | --- |
| Bank transaction ID | The unique identifier for the bank transaction in Xero. |
| Updated date UTC | The UTC date and time when the transaction was last updated. |
| Line items | Details of each line item in the transaction. |
| Bank account | Details of the bank account associated with the transaction. |
| Remaining credit | The remaining credit amount from the overpayment. |
| Contact | Information about the contact related to the overpayment. |
| Bank transaction types | The type of bank transaction. |
| Is reconciled | Indicates whether the transaction has been reconciled. |
| Reference | A reference note or number for the transaction. |
| Currency code | The currency code used for the transaction. |
| Currency rate | The exchange rate for the currency used in the transaction. |
| Bank transaction status | The current status of the bank transaction. |
| Amounts are | Indicates how amounts are reported. |
| URL | A link to an external document or resource related to the overpayment. |
| Sub total | The subtotal amount of the transaction before tax. |
| Total tax | The total tax amount for the transaction. |
| Total | The total amount of the transaction, including tax. |
| Date of transaction | The date on which the transaction occurred. |
| Overpayment ID | The unique identifier for the overpayment in Xero. |

---
