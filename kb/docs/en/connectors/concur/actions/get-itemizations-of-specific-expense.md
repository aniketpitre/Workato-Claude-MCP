---
url: >-
  https://docs.workato.com/en/connectors/concur/actions/get-itemizations-of-specific-expense.md
description: >-
  The Get itemizations of specific expense action retrieves a list of
  itemization summaries for a specific expense in SAP Concur.
---

# SAP Concur - Get itemizations of specific expense action

The **Get itemizations of specific expense** action retrieves a list of itemization summaries for a specific expense in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| User ID | Enter the unique identifier of the SAP Concur user. |
| Report ID | Enter the unique identifier of the report. |
| Expense ID | Enter the unique identifier of the expense. |

## Output

| Output field | Description |
| --- | --- |
| Itemizations | List of itemization details for the expense. |
| Expense ID (Itemizations) | The unique identifier of the parent expense entry. |
| Approver adjusted amount (Itemizations) | The amount adjusted by the approver. |
| Value (Approver adjusted amount) | The numeric value of the approver adjusted amount. |
| Currency code (Approver adjusted amount) | The currency code for the approver adjusted amount. |
| Allocation state (Itemizations) | The type of allocation for the itemization. |
| Allocation set ID (Itemizations) | The unique identifier of the allocation set. |
| Approved amount (Itemizations) | The approved amount of the itemization in the report currency. |
| Value (Approved amount) | The numeric value of the approved amount. |
| Currency code (Approved amount) | The currency code for the approved amount. |
| Business purpose (Itemizations) | The text describing the business purpose of the itemization. |
| Claimed amount (Itemizations) | The total claimed amount for the itemization. |
| Value (Claimed amount) | The numeric value of the claimed amount. |
| Currency code (Claimed amount) | The currency code for the claimed amount. |
| Ereceipt image ID (Itemizations) | The unique identifier of the electronic receipt image. |
| Exchange rate (Itemizations) | The exchange rate applied to the itemization. |
| Value (Exchange rate) | The numeric value of the exchange rate. |
| Currency code (Exchange rate) | The currency code for the exchange rate. |
| Expense source identifiers (Itemizations) | List of source identifiers for the expense. |
| Expense type (Itemizations) | The expense type information for the itemization. |
| ID (Expense type) | The unique identifier of the expense type. |
| Name (Expense type) | The name of the expense type in the user's language. |
| Code (Expense type) | The code for the expense type. |
| Is deleted (Expense type) | Indicates whether the expense type has been deleted. |
| Has blocking exceptions (Itemizations) | Indicates whether the itemization has blocking exceptions. |
| Has exceptions (Itemizations) | Indicates whether the itemization has exceptions. |
| Has missing receipt declaration (Itemizations) | Indicates whether a missing receipt declaration is present. |
| Is auto created (Itemizations) | Indicates whether the itemization was automatically created. |
| Is image required (Itemizations) | Indicates whether a receipt image is required for the itemization. |
| Is paper receipt required (Itemizations) | Indicates whether a paper receipt is required for the itemization. |
| Is personal expense (Itemizations) | Indicates whether the itemization is a personal (non-reimbursable) expense. |
| Image certification status (Itemizations) | The certification status of the receipt image. |
| Location (Itemizations) | The location information for the itemization. |
| ID (Location) | The unique identifier of the location. |
| Name (Location) | The name of the location. |
| City (Location) | The city where the expense occurred. |
| Country sub division code (Location) | The country subdivision code (state/province) where the expense occurred. |
| Country code (Location) | The two-letter ISO country code where the expense occurred. |
| Payment type (Itemizations) | The payment type information for the itemization. |
| ID (Payment type) | The unique identifier of the payment type. |
| Name (Payment type) | The name of the payment type in the user's language. |
| Code (Payment type) | The code for the payment type. |
| Posted amount (Itemizations) | The amount converted to the report currency. |
| Value (Posted amount) | The numeric value of the posted amount. |
| Currency code (Posted amount) | The currency code for the posted amount. |
| Transaction date (Itemizations) | The date when the expense transaction occurred. |
| Receipt image ID (Itemizations) | The unique identifier of the receipt image. |
| Ticket number (Itemizations) | The ticket or reference number associated with the itemization. |
| Transaction amount (Itemizations) | The amount in the original transaction currency. |
| Value (Transaction amount) | The numeric value of the transaction amount. |
| Currency code (Transaction amount) | The currency code for the transaction amount. |
| Travel allowance (Itemizations) | Travel allowance information for the itemization. |
| Daily limit amount (Travel allowance) | The daily quota amount for the travel allowance. |
| Daily travel allowance ID (Travel allowance) | The unique identifier of the daily travel allowance. |
| Is expense part of travel allowance (Travel allowance) | Indicates whether the expense is part of a travel allowance. |
| Vendor (Itemizations) | The vendor information for the itemization. |
| ID (Vendor) | The unique identifier of the vendor. |
| Name (Vendor) | The name of the vendor. |
| Description (Vendor) | The description of the vendor. |
| Attendee count (Itemizations) | The number of attendees associated with the itemization. |
| Links (Itemizations) | Hypermedia links related to the itemization. |
| Rel (Links) | The relationship of the link to the current resource. |
| Href (Links) | The URL of the linked resource. |
| Method (Links) | The HTTP method to use with the link. |
| Is templated (Links) | Indicates whether the link is a URI template. |
