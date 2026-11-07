---
url: 'https://docs.workato.com/en/connectors/concur/actions/get-invoice-details.md'
description: >-
  The Get invoice details action retrieves detailed information about a specific
  invoice in SAP Concur.
---

# SAP Concur - Get invoice details action

The **Get invoice details** action retrieves detailed information about a specific invoice in SAP Concur.

## Input

| Input field | Description |
| --- | --- |
| Invoice ID | Enter the unique identifier of the invoice to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the invoice. |
| URI | The URI to the invoice resource. |
| Employee name | The name of the employee associated with the invoice. |
| Currency code | The three-letter ISO 4217 currency code for the invoice currency. |
| Invoice number | The vendor's invoice identifier. |
| Data source | The creation method code for the invoice. |
| Ledger code | The journal assignment code. |
| Country code | The country identifier. |
| Name | The invoice name. |
| Description | The description of the invoice. |
| OB 10 transaction ID | The OB 10 transaction identifier. |
| OB 10 buyer ID | The OB 10 buyer identifier. |
| Buyer cost center | The buyer's cost center. |
| Check number | The check number for the payment. |
| Payment terms days | The number of days for payment terms. |
| Payment method | The payment method code. |
| Payment adjustment notes | Notes regarding payment adjustments. |
| Receipt confirmation type | The type of receipt confirmation. |
| Is invoice confirmed | Indicates whether the invoice has been confirmed. |
| Submitted by delegate | Indicates whether the invoice was submitted by a delegate. |
| Approved by delegate | Indicates whether the invoice was approved by a delegate. |
| Is assigned | Indicates whether the invoice has been assigned. |
| Payment request created by test user | Indicates whether the payment request was created by a test user. |
| Is payment request deleted | Indicates whether the payment request has been deleted. |
| Is test transaction | Indicates whether this is a test transaction. |
| Is payment request duplicate | Indicates whether the payment request is a duplicate. |
| Notes to vendor | Notes to send to the vendor. |
| Discount terms | The discount terms for the invoice. |
| Approval status | The approval status code of the invoice. |
| Created by username | The username of the user who created the invoice. |
| Assigned by username | The username of the user who assigned the invoice. |
| Payment request deleted by | The username of the user who deleted the payment request. |
| User creation date | The date when the invoice was created by the user. |
| Invoice date | The date the vendor issued the invoice. |
| Posting date | The date when the invoice was posted. |
| First submit date | The date when the invoice was first submitted. |
| Last submit date | The date when the invoice was last submitted. |
| Payment due date | The date when payment is due. |
| Workflow complete date | The date when the workflow was completed. |
| Extract date | The date when the invoice was extracted. |
| Paid date | The date when the invoice was paid. |
| First approval date | The date when the invoice was first approved. |
| Assigned date | The date when the invoice was assigned. |
| Deleted date | The date when the invoice was deleted. |
| Invoice received date | The date when the invoice was received. |
| Payment status | The payment status code. |
| Invoice amount | The user-entered value representing the total invoice amount. |
| Calculated amount | The calculated total amount of the invoice. |
| Total approved amount | The total amount approved for the invoice. |
| Shipping amount | The shipping cost. |
| Tax amount | The total tax value. |
| Line item total amount | The total amount of all line items. |
| Paid amount | The amount that has been paid. |
| Discount percentage | The supplier discount percentage if terms are met. |
| Line item vat amount | The total VAT amount for line items. |
| Delivery slip number | The delivery slip number. |
| Purchase order number | The associated purchase order number. |
| Amount without vat | The net amount excluding VAT. |
| Vat amount one | The first VAT amount. |
| Vat amount two | The second VAT amount. |
| Vat amount three | The third VAT amount. |
| Vat amount four | The fourth VAT amount. |
| Vat rate one | The first VAT rate applied. |
| Vat rate two | The second VAT rate applied. |
| Vat rate three | The third VAT rate applied. |
| Vat rate four | The fourth VAT rate applied. |
| Tax code | The primary tax code. |
| Provincial tax ID | The provincial tax identifier. |
| Vendor tax ID | The vendor's tax identifier. |
| External policy ID | The external policy reference. |
| Tax code 2 | The second tax code. |
| Tax code 3 | The third tax code. |
| Tax code 4 | The fourth tax code. |
| Vendor remit address | The vendor location for payment remittance. |
| Name (Vendor remit address) | The name of the vendor remit location. |
| Discount terms (Vendor remit address) | The discount terms for the vendor. |
| Address code (Vendor remit address) | The unique identifier of the vendor address. |
| Vendor code (Vendor remit address) | The unique identifier of the vendor. |
| Address 1 (Vendor remit address) | The first line of the vendor address. |
| Address 2 (Vendor remit address) | The second line of the vendor address. |
| Address 3 (Vendor remit address) | The third line of the vendor address. |
| City (Vendor remit address) | The city of the vendor address. |
| State (Vendor remit address) | The state of the vendor address. |
| Postal code (Vendor remit address) | The postal code of the vendor address. |
| Country code (Vendor remit address) | The country code of the vendor address. |
| Vendor ship from address | The vendor's shipping origin address. |
| Company bill to address | The company's billing address. |
| Company ship to address | The company's shipping address. |
| Line items | The collection of line items on the invoice. |
| Line item (Line items) | Individual line item details. |
| Line item ID (Line item) | The unique identifier of the line item. |
| Expense type code (Line item) | The expense type code for the line item. |
| Request line item number (Line item) | The line item number in the request. |
| Quantity (Line item) | The quantity of items. |
| Description (Line item) | The description of the line item. |
| Allocation status (Line item) | The allocation status of the line item. |
| Ship to postal code (Line item) | The postal code for the shipping destination. |
| Ship from postal code (Line item) | The postal code for the shipping origin. |
| Line item is test user (Line item) | Indicates whether the line item was created by a test user. |
| Is matched (Line item) | Indicates whether the line item has been matched to a purchase order. |
| Purchase order number (Line item) | The purchase order number associated with the line item. |
| Matched purchase order line item ID (Line item) | The identifier of the matched purchase order line item. |
| Supplier part ID (Line item) | The supplier's part identifier. |
| Unit of measure (Line item) | The unit of measure for the line item. |
| Unit price (Line item) | The price per unit. |
| Total price (Line item) | The total price for the line item. |
| Requested line item amount (Line item) | The requested amount for the line item. |
| Approved line item amount (Line item) | The approved amount for the line item. |
| Tax (Line item) | The tax amount for the line item. |
| Amount without vat (Line item) | The line item amount excluding VAT. |
| Vat amount (Line item) | The VAT amount for the line item. |
| Vat amount two (Line item) | The second VAT amount for the line item. |
| Vat amount three (Line item) | The third VAT amount for the line item. |
| Vat amount four (Line item) | The fourth VAT amount for the line item. |
| Vat rate (Line item) | The VAT rate applied to the line item. |
| Vat rate two (Line item) | The second VAT rate applied to the line item. |
| Vat rate three (Line item) | The third VAT rate applied to the line item. |
| Vat rate four (Line item) | The fourth VAT rate applied to the line item. |
| Tax code (Line item) | The tax code for the line item. |
| Tax code 2 (Line item) | The second tax code for the line item. |
| Tax code 3 (Line item) | The third tax code for the line item. |
| Tax code 4 (Line item) | The fourth tax code for the line item. |
| Delivery slip number (Line item) | The delivery slip number for the line item. |
| Allocations (Line item) | The allocations for the line item. |
| Allocation (Allocations) | Individual allocation details. |
| Percentage (Allocation) | The allocation percentage. |
| Allocation account code (Allocation) | The account code for the allocation. |
| Is test user (Allocation) | Indicates whether the allocation was created by a test user. |
| Custom 1-20 (Allocation) | Custom field values 1 through 20 for the allocation. |
| List size (Allocation) | The size of the allocation list. |
| List index (Allocation) | The index of the allocation in the list. |
| Matched purchase order receipts (Line item) | The purchase order receipts matched to the line item. |
| Matched purchase order receipt (Matched purchase order receipts) | Individual matched purchase order receipt details. |
| Goods receipt number (Matched purchase order receipt) | The goods receipt number. |
| List size (Matched purchase order receipt) | The size of the matched purchase order receipts list. |
| List index (Matched purchase order receipt) | The index of the matched purchase order receipt in the list. |
| Custom 1-20 (Line item) | Custom field values 1 through 20 for the line item. |
| List size (Line item) | The size of the line items list. |
| List index (Line item) | The index of the line item in the list. |
| Org unit 1 | Organization unit field 1. |
| Org unit 2 | Organization unit field 2. |
| Org unit 3 | Organization unit field 3. |
| Org unit 4 | Organization unit field 4. |
| Org unit 5 | Organization unit field 5. |
| Org unit 6 | Organization unit field 6. |
| Custom 1-24 | Custom field values 1 through 24 for the invoice. |

---

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

---
