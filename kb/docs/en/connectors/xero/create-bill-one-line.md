---
url: 'https://docs.workato.com/en/connectors/xero/create-bill-one-line.md'
description: >-
  The Create bill with one line item action in the Xero connector lets you
  create a bill with a single line item.
---

# Xero - Create bill with one line item action

The **Create bill with one line item** action allows you to create a bill with a single line item in Xero.

![Create bill with one line item](/assets/create-bill-one-action.Dk_v33az.png)_Xero - Create bill with one line item action_

## Input

| Input field | Description |
| --- | --- |
| Contact name | Enter the exact name of the contact you plan to invoice. |
| First name | Specify the contact's first name. |
| Last name | Specify the contact's last name. |
| Email | Provide the contact's email address. |
| Reference | Provide a code to identify the bill. |
| Date | Set the issue date for the bill. |
| Due date | Define the due date for the bill. This field is required if the invoice status is set to `AUTHORISED` or `SUBMITTED`. |
| Currency code | Enter the currency code for the bill amounts. |
| Status | Select the initial status of the bill. This field defaults to `DRAFT` if left blank. |
| Branding theme | Choose a branding theme to apply to the bill. |
| Amounts are | Indicate whether the amounts are tax inclusive, exclusive, or no tax. This field defaults to `Tax exclusive` if left blank. |
| URL | Include a link to an external document related to the bill. |
| Planned payment date | Set the planned payment date for the bill. |
| Description | Enter a description for the line item. Ensure it is at least one character and a maximum of four thousand characters. |
| Item name | Specify the name of the line item. Click **Products and services** to retrieve the item name. If you provide both the item name and code, the item code takes precedence. |
| Quantity | Enter the quantity of the line item. Provide at least two fields out of **Quantity**, **Unit price** or **Line amount**. |
| Unit price | Set the unit price for the line item. Provide at least two fields out of **Quantity**, **Unit price** or **Line amount**. |
| Line amount | Enter the total amount for the line item. Provide at least two fields out of **Quantity**, **Unit price** or **Line amount**. |
| Discount rate | Apply a discount rate to the line item if applicable. |
| Account code | Assign an account code from your **Chart of accounts** to the line item. |
| Tax type name | Specify the tax type. Click **Settings > General settings > Tax rates** to find the tax type name. |
| Tax amount | Enter the tax amount for the line item. This field is auto-calculated as a percentage of the line amount based on the tax rate. |
| Item code | Provide the item code. Click **Products and services** to retrieve the item code. If you provide both the item name and code, the item code takes precedence. |

## Output

| Output field | Description |
| --- | --- |
| Type | The type of the document (bill). |
| Invoice ID | The unique identifier for the invoice. |
| Reference | A reference number or note associated with the bill. |
| Payments | A list of payments that includes details related to the bill's payments. |
| Credit Notes | A list of credit notes that includes details related to the bill's credit notes. |
| Payments | A list of payments that includes details related to the bill's payments. |
| Credit Notes | A list of credit notes that includes details related to the bill's credit notes. |
| Amount due | The total amount due on the bill. |
| Amount paid | The total amount paid on the bill. |
| Amount credited | The total amount credited to the bill. |
| URL | The link to the bill or associated online resource. |
| Currency code | The currency code for the bill. See [ISO 4217 Currency Codes](http://www.xe.com/iso4217.php) for more information. |
| Currency rate | The exchange rate for the currency used. |
| Has errors | Indicates if there are errors related to the bill. |
| Is discounted | Indicates if a discount has been applied to the bill. |
| Has attachments | Indicates if there are attachments included with the bill. |
| Contact | Contact information for the bill. |
| Date | The issue date of the bill. |
| Due date | The due date for payment of the bill. |
| Status | The current status of the bill. |
| Branding theme ID | The identifier for the branding theme used in the bill. |
| Line amount types | The type of line amounts on the bill. |
| Line items | Detailed information about each line item on the bill. |
| Sub total | The subtotal amount of the bill before tax. |
| Total tax | The total tax amount for the bill. |
| Total | The total amount for the bill, including tax. |
| Updated date | The date when the bill details were last updated. |
| Paid date | The date when the bill was paid, if applicable. |
| Planned payment date | The planned payment date for the bill. |

---
