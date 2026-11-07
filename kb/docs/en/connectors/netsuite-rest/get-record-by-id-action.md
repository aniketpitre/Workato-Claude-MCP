---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/get-record-by-id-action.md
description: >-
  The Get record by ID action retrieves a record from NetSuite using its
  internal ID.
---

# NetSuite REST - Get record by ID action

The **Get record by ID** action retrieves a record from NetSuite using its internal ID.

## Input

| Input fields | Description |
| --- | --- |
| Record | Select a [NetSuite record](#record-types) to retrieve, or toggle this field to enter a custom record type ID. |
| Internal ID | Enter the internal ID of the record to retrieve. |

### Record types

This action supports the following record types:

- Account
- Accounting period
- Advanced intercompany journal entry
- Assembly item
- Billing account
- Billing schedule
- Bin
- Bin transfer
- Cash refund
- Cash sale
- Change order
- Charge
- Check
- Class
- Commerce category
- Consolidated exchange rate
- Contact
- Contact category
- Contact role
- Cost category
- Credit card charge
- Credit card refund
- Credit memo
- Currency
- Customer
- Customer category
- Customer deposit
- Customer payment
- Customer refund
- Customer subsidiary relationship
- Department
- Deposit
- Deposit application
- Description item
- Discount item
- Email template
- Employee
- Estimate
- Event
- Expense category
- Expense report
- Fulfillment request
- Inbound shipment
- Intercompany journal entry
- Intercompany transfer order
- Inventory adjustment
- Inventory cost revaluation
- Inventory count
- Inventory item
- Inventory number
- Inventory transfer
- Invoice
- Item fulfillment
- Item group
- Item receipt
- Job
- Job status
- Job type
- Journal entry
- Kit item
- Location
- Markup item
- Message
- Nexus
- Non-inventory purchase items
- Non-inventory resale item
- Non-inventory sale item
- Opportunity
- Other charge for purchase item
- Other charge for resale item
- Other name
- Other name category
- Payment item
- Phone call
- Price book
- Price level
- Price plan
- Pricing group
- Project task
- Purchase order
- Requisition
- Return authorization
- Sales order
- Sales tax item
- Service purchase item
- Service resale item
- Service sale item
- Ship item
- Statistical journal entry
- Subscription
- Subscription line
- Subscription plan
- Subscription term
- Subsidiary
- Subtotal item
- Task
- Tax type
- Time bill (track time)
- Transfer order
- Unit of measure
- Usage
- Vendor
- Vendor bill
- Vendor category
- Vendor credit
- Vendor prepayment
- Vendor prepayment application
- Vendor return authorization
- Vendor subsidiary relationship

Refer to the NetSuite [REST Web Services Supported Records](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1558962745.html) documentation for more information.

## Output

The output fields depend on the record you select. Each record returns a unique set of fields based on its type.
