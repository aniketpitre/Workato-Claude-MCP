---
url: 'https://docs.workato.com/en/connectors/zoho-crm/triggers/new-invoice.md'
description: >-
  The New invoice trigger checks for new invoices in Zoho CRM once every polling
  interval.
---

# Zoho CRM - New invoice trigger

The **New invoice** trigger checks for new invoices in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| Invoice ID | The unique identifier of the invoice. |
| Tax | The total tax amount for the invoice. |
| Invoice number | The invoice identification number. |
| Sales order ID | The unique identifier of the related sales order. |
| Account ID | The unique identifier of the related account. |
| Subject | The name of the invoice. |
| Sales order | The reference sales order. |
| Sub total | The subtotal amount before taxes and adjustments. |
| Account name | The name of the related account. |
| Invoice owner | The user to whom the invoice is assigned. |
| Adjustment | Any adjustments such as discounts or extra charges. |
| Grand total | The total amount including taxes and adjustments. |
| Excise duty | The excise duty for the shipment. |
| Sales commission | The commission to the sales person. |
| Status | The status of the invoice. |
| Contact name | The name of the related contact. |
| Discount | The discount amount or percentage. |
| Purchase order | The reference purchase order. |
| Invoice date | The date on which the invoice was created. |
| Due date | The invoice due date. |
| Terms and conditions | The terms and conditions associated with the invoice. |
| Billing street | The billing street address. |
| Billing city | The billing city. |
| Billing state | The billing state or province. |
| Billing zip | The billing postal code. |
| Billing country | The billing country. |
| Shipping street | The shipping street address. |
| Shipping city | The shipping city. |
| Shipping state | The shipping state or province. |
| Shipping zip | The shipping postal code. |
| Shipping country | The shipping country. |
| Description | Additional details about the invoice. |
| Product details | The line item details for products in the invoice. |
| Product ID (Product details) | The unique identifier of the product. |
| Product code (Product details) | The product identification code. |
| Product name (Product details) | The name of the product. |
| Product description (Product details) | Additional details about the product. |
| Unit price (Product details) | The unit price of the product. |
| Quantity in stock (Product details) | The stock quantity available. |
| Quantity (Product details) | The quantity for the line item. |
| Amount (Product details) | The amount for the line item. |
| Discount (Product details) | The discount for the line item. |
| Total after discount (Product details) | The total amount after applying the discount. |
| List price (Product details) | The product list price from the price book. |
| Total (Product details) | The total amount of the line item. |
| Product tax (Product details) | The tax component for the product. |
| Book (Product details) | The price book reference. |
| Line tax (Product details) | The tax details for the line item. |
| Percentage (Line tax) | The tax percentage. |
| Name (Line tax) | The name of the tax. |
| Value (Line tax) | The tax value. |
| Contact ID | The unique identifier of the related contact. |
| SM owner ID | The ID of the user who owns the invoice. |
| SM creator ID | The ID of the user who created the invoice. |
| Created by | The user who created the invoice. |
| Modified by (ID) | The ID of the user who last modified the invoice. |
| Modified by | The user who last modified the invoice. |
| Created time | The timestamp when the invoice was created. |
| Modified time | The timestamp when the invoice was modified. |
| Currency symbol | The currency symbol for monetary values. |
| Process flow | The process flow associated with the invoice. |
| Approved | Indicates if the invoice has been approved. |
| Editable | Indicates if the invoice record is editable. |
| Approval | The approval details for the invoice. |
| Delegate (Approval) | Indicates if approval can be delegated. |
| Approve (Approval) | Indicates if the invoice can be approved. |
| Reject (Approval) | Indicates if the invoice can be rejected. |
| Resubmit (Approval) | Indicates if the invoice can be resubmitted. |
| Line tax | Additional tax details for line items. |
| Percentage (Line tax) | The tax percentage for additional taxes. |
| Name (Line tax) | The name of the additional tax. |
| Value (Line tax) | The value of the additional tax. |

---

---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/triggers/new-standard-object.md
description: >-
  The New standard object trigger checks for new standard objects in Zoho CRM
  once every polling interval.
---

# Zoho CRM - New standard object trigger

The **New standard object** trigger checks for new standard objects in Zoho CRM once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| Module name | Select the name of the module to monitor for new records. Options include: `Accounts`, `Contacts`, `Deals`, `Vendors`, `Leads`, `Campaigns`, `Products`, `Invoices`, `Price Books`, `Quotes`, `Sales Orders`, `Purchase Orders`, `Cases`, `Solutions`, and `Appointments`. |
| When first started, this recipe should pick up events from | Specify the date and time from which the recipe picks up trigger events. You can't change this value after running or testing the recipe. |

## Output

Output fields are dynamically generated based on the selected module.

---
