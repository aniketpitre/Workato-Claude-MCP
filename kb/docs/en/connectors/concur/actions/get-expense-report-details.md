---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-expense-report-details.md
description: >-
  The Get expense report details action retrieves detailed information about a
  specific expense report in SAP Concur.
---

# SAP Concur - Get expense report details action

The **Get expense report details** action retrieves detailed information about a specific expense report in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| User ID | Enter the unique identifier of the SAP Concur user. |
| Report ID | Enter the unique identifier of the expense report to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Approval status | The report's approval status in the user's language. |
| Approval status ID | The unique identifier of the approval status. |
| Concur audit status | The audit status for the report in Concur. |
| Custom data | List of custom field values for the report. |
| ID (Custom data) | The unique identifier of the custom field. |
| Value (Custom data) | The value entered in the custom field. |
| Is valid (Custom data) | Indicates whether the custom field value is valid. |
| List item URL (Custom data) | The URL to the list item if the custom field is a list type. |
| Ledger | The ledger code for the report. |
| Ledger ID | The unique identifier of the ledger. |
| Payment status | The payment status of the report in the user's language. |
| Payment status ID | The unique identifier of the payment status. |
| Submit date | The date the report was submitted. |
| Currency code | The currency code for the report. |
| Claimed amount | The total amount of all non-personal expenses in the report. |
| Value (Claimed amount) | The numeric value of the claimed amount. |
| Currency code (Claimed amount) | The currency code for the claimed amount. |
| Amount company paid | The amount paid by the company. |
| Value (Amount company paid) | The numeric value of the amount company paid. |
| Currency code (Amount company paid) | The currency code for the amount company paid. |
| Payment confirmed amount | The confirmed payment amount. |
| Value (Payment confirmed amount) | The numeric value of the payment confirmed amount. |
| Currency code (Payment confirmed amount) | The currency code for the payment confirmed amount. |
| Amount due company | The amount due to the company. |
| Value (Amount due company) | The numeric value of the amount due to the company. |
| Currency code (Amount due company) | The currency code for the amount due to the company. |
| Amount due company card | The amount due on the company card. |
| Value (Amount due company card) | The numeric value of the amount due on the company card. |
| Currency code (Amount due company card) | The currency code for the amount due on the company card. |
| Amount due employee | The amount due to the employee. |
| Value (Amount due employee) | The numeric value of the amount due to the employee. |
| Currency code (Amount due employee) | The currency code for the amount due to the employee. |
| Personal amount | The total amount of personal expenses in the report. |
| Value (Personal amount) | The numeric value of the personal amount. |
| Currency code (Personal amount) | The currency code for the personal amount. |
| Report total | The total amount of the report including all expenses. |
| Value (Report total) | The numeric value of the report total. |
| Currency code (Report total) | The currency code for the report total. |
| Amount not approved | The total amount of expenses not approved in the report. |
| Value (Amount not approved) | The numeric value of the amount not approved. |
| Currency code (Amount not approved) | The currency code for the amount not approved. |
| Is financial integration enabled | Indicates whether financial integration is enabled for the report. |
| Can reopen | Indicates whether the report can be reopened. |
| Is reopened | Indicates whether the report has been reopened. |
| Is receipt image available | Indicates whether a receipt image is available for the report. |
| Is receipt image required | Indicates whether a receipt image is required for the report. |
| Is paper receipts received | Indicates whether paper receipts have been received. |
| Report ID | The unique identifier of the expense report. |
| Expense entries list | List of expense entries within the report. |
| Expense ID (Expense entries list) | The unique identifier of the expense entry. |
| Links | Hypermedia links related to the report. |
| Rel (Links) | The relationship of the link to the current resource. |
| Href (Links) | The URL of the linked resource. |
| Hreflang (Links) | The language of the linked resource. |
| Media (Links) | The media type of the linked resource. |
| Title (Links) | The title of the linked resource. |
| Type (Links) | The type of the linked resource. |
| Deprecation (Links) | Indicates whether the link is deprecated. |
| Method (Links) | The HTTP method to use with the link. |
| Is templated (Links) | Indicates whether the link is a URI template. |
| Report date | The date assigned to the report. |
| Report form ID | The unique identifier of the report form used. |
| Business purpose | The text explaining the business purpose for the expenses. |
| Country code | The country code where the expenses occurred. |
| Country sub division code | The country subdivision code where the expenses occurred. |
| Policy ID | The unique identifier of the expense policy applied to the report. |
| Start date | The start date of the travel or expense period. |
| End date | The end date of the travel or expense period. |
| Name | The name of the expense report entered by the user. |
| Policy | The name of the expense policy applied to the report. |
| Country | The country where the expenses occurred. |
| User ID | The unique identifier of the user who created the report. |
| Report type | The type of expense report. |
| Redirect fund | The redirect fund information for the report. |
| Amount (Redirect fund) | The amount to be redirected. |
| Credit card ID | The unique identifier of the credit card used. |
| Creation date | The date and time when the report was created. |
| Can recall | Indicates whether the report can be recalled. |
| Report version | The version number of the report. |
