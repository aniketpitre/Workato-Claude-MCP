---
url: 'https://docs.workato.com/en/connectors/xero/create-transaction.md'
description: >-
  The Create bank transaction action in the Xero connector lets you create a new
  bank transaction in your connected Xero organization.
---

# Xero - Create bank transaction action

The **Create bank transaction** action allows you to create a bank transaction in Xero.

![Create bank transaction](/assets/create-transaction-action.RncJ6tGc.png)_Xero - Create bank transaction action_

## Input

| Input field | Description |
| --- | --- |
| Contact | The contact associated with the bank transaction. Provide either the **Contact ID**, **Name**, or **Email address** to complete this required field. |
| Contact ID (contact) | Enter the unique identifier for the contact. |
| Name (contact) | Enter the contact's name. |
| Email address (contact) | Provide the contact's email address. |
| Bank account | The bank account details that record the transaction. Provide either the **Account ID**, **Code**, or **Name** to complete this required field. |
| Account ID (bank account) | The unique identifier for the bank account. |
| Code (bank account) | The code of the bank account. |
| Name (bank account) | The name of the bank account. |
| Bank transaction types | Specify the type of bank transaction. |
| Is reconciled | Indicate whether the transaction is reconciled. |
| Reference | Include a reference for the transaction. This is required only for `SPEND` and `RECEIVE` transactions. |
| Currency code | Enter the currency code for the transaction. This is required only for `OVERPAYMENT` transactions. |
| Currency rate | Specify the exchange rate for the transaction. This is required only for `OVERPAYMENT` transactions. |
| Bank transaction status | Set the status of the bank transaction. |
| Amounts are | Indicate whether the amounts are tax inclusive, exclusive, or no tax. This field defaults to `Tax exclusive` if left blank. |
| URL | Include a link to an external document related to the bank transaction. |
| Sub total | Enter the subtotal amount for the bank transaction before tax. |
| Total tax | Input the total tax amount on the bank transaction. |
| Total | Input the total amount of the bank transaction, including tax. |
| Date of transaction | Input the date of the bank transaction. |
| Line items source list | Input a list datapill representing the line items. |
| Description (line items) | Enter a description for the line items. Ensure it is at least one character and a maximum of four thousand characters. |
| Item name (line items) | Specify the name of the line items. Click **Products and services** to retrieve the item name. If both the item name and item code are provided, the item code takes precedence. |
| Quantity (line items) | Enter the quantity of the line items. Provide at least two fields out of **Quantity**, **Unit price** or **Line amount**. |
| Unit price (line items) | Set the unit price for the line items. Provide at least two fields out of **Quantity**, **Unit price** or **Line amount**. |
| Line amount (line items) | Enter the total amount for the line items. Provide at least two fields out of **Quantity**, **Unit price** or **Line amount**. |
| Discount rate (line items) | Apply a discount rate to the line items if applicable. |
| Account code (line items) | Assign an account code from your **Chart of accounts** to the line items. |
| Tax type name (line items) | Specify the tax type. Click **Settings > General settings > Tax rates** to find the tax type name. |
| Tax amount (line items) | Enter the tax amount for the line items. This field is auto-calculated as a percentage of the line amount based on the tax rate. |
| Item code (line items) | Provide the item code. Click **Products and services** to retrieve the item code. If both the item name and code are provided, the item code takes precedence. |

## Output

| Output field | Description |
| --- | --- |
| Bank transaction ID | The unique identifier for the bank transaction. |
| Updated date UTC | The date and time the transaction was last updated, in UTC. |
| Line items | Details of each item in the transaction. |
| Bank account | The bank account associated with the transaction. |
| Contact | Information about the contact associated with the transaction. |
| Bank transaction types | The type of the bank transaction. |
| Is reconciled | Indicates whether the transaction has been reconciled. |
| Reference | A reference number or note associated with the transaction. |
| Currency code | The currency code used for the transaction. |
| Currency rate | The exchange rate for the currency used in the transaction. |
| Bank transaction status | The current status of the bank transaction. |
| Amounts are | Indicates whether the amounts are tax inclusive, exclusive, or no tax. |
| URL | A link to an external document or resource related to the bank transaction. |
| Sub total | The subtotal amount of the bank transaction before tax. |
| Total tax | The total tax amount for the bank transaction. |
| Total | The total amount of the bank transaction, tax inclusive. |
| Date of transaction | The date when the bank transaction occurred. |

---
