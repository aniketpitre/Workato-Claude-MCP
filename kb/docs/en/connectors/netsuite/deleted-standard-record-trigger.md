---
url: >-
  https://docs.workato.com/en/connectors/netsuite/deleted-standard-record-trigger.md
description: >-
  The Deleted standard record trigger checks for records deleted after the
  specified date.
---

# NetSuite SOAP - Deleted standard record trigger

The **Deleted standard record** trigger checks for records deleted after the specified date. Subsequently, the recipe checks for deleted records once every polling interval.

> **PREREQUISITES**
> 
> Ensure that you've added the **Deleted Records** and **SOAP Web Services** permissions to the role used in your Workato connection. Refer to [Create an integration role](/en/connectors/netsuite/netsuite-connect#step-3) for detailed steps.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Set how frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |
| When first started, this recipe should pick up events from | Specify the date and time from which to pick up trigger events when you start the recipe for the first time. Defaults to fetching records deleted an hour ago if left blank. You can't change this value after running or testing the recipe. |
| Standard record | Select a NetSuite standard record to monitor for deleted records. |

Supported records

This trigger supports monitoring the following NetSuite standard records for deleted records:

- Accounting Period
- Adv Inter Company Journal Entry
- Assembly Build
- Assembly Item
- Assembly Unbuild
- Billing Account
- Billing Schedule
- Bin
- Bin Transfer
- Bin Worksheet
- Budget
- Calendar Event
- Cash Refund
- Cash Sale
- Charge
- Check
- Contact
- Contact Category
- Contact Role
- Cost Category
- Coupon Code
- Credit Memo
- Custom List
- Custom Purchase
- Custom Record
- Custom Sale
- Custom Transaction
- Customer
- Customer Category
- Customer Deposit
- Customer Message
- Customer Payment
- Customer Refund
- Customer Status
- Deposit
- Deposit Application
- Description Item
- Discount Item
- Download Item
- Employee
- Entity Group
- Estimate
- Expense Category
- Expense Report
- Fair Value Price
- File
- Folder
- Gift Certificate
- Global Account Mapping
- Inter Company Journal Entry
- Inventory Adjustment
- Inventory Cost Revaluation
- Inventory Item
- Inventory Number
- Inventory Transfer
- Invoice
- Issue
- Item Account Mapping
- Item Demand Plan
- Item Fulfillment
- Item Group
- Item Receipt
- Item Supply Plan
- Job
- Job Status
- Job Type
- Journal Entry
- Kit Item
- Lot Numbered Assembly Item
- Lot Numbered Inventory Item
- Manufacturing Cost Template
- Manufacturing Operation Task
- Manufacturing Routing
- Marketing Campaign
- Markup Item
- Nexus
- Non Inventory Purchase Item
- Non Inventory Resale Item
- Non Inventory Sale Item
- Opportunity
- Other Charge Purchase Item
- Other Charge Resale Item
- Other Charge Sale Item
- Other Name Category
- Partner
- Partner Category
- Paycheck Journal
- Payment Item
- Payment Method
- Payroll Item
- Period End Journal
- Phone Call
- Price Level
- Pricing Group
- Project Task
- Promotion Code
- Purchase Order
- Purchase Requisition
- Return Authorization
- Rev Rec Schedule
- Rev Rec Template
- Sales Order
- Sales Role
- Serialized Assembly Item
- Serialized Inventory Item
- Service Purchase Item
- Service Resale Item
- Service Sale Item
- Site Category
- Solution
- Statistical Journal Entry
- Subtotal Item
- Support Case
- Task
- Term
- Time Bill
- Time Entry
- Time Sheet
- Topic
- Transfer Order
- Units Type
- Vendor
- Vendor Bill
- Vendor Category
- Vendor Credit
- Vendor Payment
- Vendor Return Authorization
- Win Loss Reason
- Work Order
- Work Order Close
- Work Order Completion
- Work Order Issue

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the deleted record. |
| Internal ID | The unique internal identifier of the deleted record. |
| Type | The record type of the deleted record. |
| Deleted date | The date and time when the record was deleted. |
