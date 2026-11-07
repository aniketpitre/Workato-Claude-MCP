---
url: 'https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers.md'
description: >-
  Browse the triggers available in the Oracle Fusion Cloud connector for Workato
  to start recipes from events on Fusion Cloud objects.
---

# Oracle Fusion Cloud - Triggers

The Oracle Fusion Cloud connector supports the following triggers:

- [New business event trigger](/en/connectors/oracle-fusion-cloud/triggers/new-business-event)
- [New employee atom feed entry trigger](/en/connectors/oracle-fusion-cloud/triggers/new-employee-atom-feed-entry)
- [New organization atom feed entry trigger](/en/connectors/oracle-fusion-cloud/triggers/new-organization-atom-feed-entry)
- [New record trigger](/en/connectors/oracle-fusion-cloud/triggers/new-record)
- [New record trigger (batch)](/en/connectors/oracle-fusion-cloud/triggers/new-record-batch)
- [New/updated record trigger](/en/connectors/oracle-fusion-cloud/triggers/new-updated-record)
- [New/updated record trigger (batch)](/en/connectors/oracle-fusion-cloud/triggers/new-updated-record-batch)

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-business-event.md
description: >-
  The New business event trigger monitors Oracle Fusion Cloud for new business
  events and triggers immediately when they occur.
---

# Oracle Fusion Cloud - New business event trigger

The **New business event** trigger monitors Oracle Fusion Cloud for new business events in real time.

## Input

| Input field | Description |
| --- | --- |
| Event | Select the business event to monitor. |

What event types are supported?

This trigger supports the following event types:

- Item Create Event
- Item Update Event
- Item Bulk Load Event
- Item Publication Event
- Oracle Health Publication Event
- Item CrossReference Relationship Create Event
- Item CrossReference Relationship Update Event
- Item CrossReference Relationship Delete Event
- Trading Partner Item Relationship Create Event
- Trading Partner Item Relationship Update Event
- Trading Partner Item Relationship Delete Event
- Related Item Relationship Create Event
- Related Item Relationship Update Event
- Related Item Relationship Delete Event
- Source System Item Relationship Create Event
- Source System Item Relationship Update Event
- Source System Item Relationship Delete Event
- GTIN Item CrossReference Relationship Create Event
- GTIN Item CrossReference Relationship Update Event
- GTIN Item CrossReference Relationship Delete Event
- Data Pool Subscription Confirmation Sent Event
- Data Pool Subscription Event
- Product Upload Status Change Event
- Item Catalog Category Assignment Change Event
- Item Category Assignment Delete Event
- New Item Request Opened
- New Item Request Status Changed To Definition
- New Item Request Status Changed To Approval
- New Item Request Scheduled
- New Item Request Completed
- Bulk Delete Event
- Item Level Multi Row EFF Delete Event
- Item Revision Level Multi Row EFF Delete Event
- Item Supplier Level Multi Row EFF Delete Event
- Item Import Job Complete Event
- Shipment Request Generate Event
- Manifest Request Event
- Advanced Shipment Notice Event
- Pick Confirm Event
- Create Transfer Order Line
- Modify Transfer Order Line
- Create Movement Request
- Outbound Direct Work Order Transactions
- ASN creation event
- ASN cancellation event
- Create Inbound ASN
- Cancel Inbound ASN
- Create Receiving Receipt event
- Create Deliver Transaction event
- Create Correction Transaction event
- Create Return Transaction event
- Receipt Advice Event Notification
- Outbound Receipt Advice
- Print Label Request Event
- Work Order Create
- Work Order Update
- Print Product Label Event
- Order Status Updated
- Sales Order Notification
- Sales Order Transportation Planning
- Sales Order Trade Compliance Screening
- Item Structure Create Event
- Item Structure Update Event
- Item Structure Component Create Event
- Item Structure Component Update Event
- Change Order Scheduled Event
- Change Order Open Event
- Change Order Interim Approval Event
- Change Order Approval Event
- Change Order Completed Event
- Change Order Scheduled Event V2
- Change Order Open Event V2
- Change Order Interim Approval Event V2
- Change Order Approval Event V2
- Change Order Completed Event V2
- Shipment Advice Event
- Trade Screening Request Event
- Backorder Line Event
- Outbound Shipment Request
- Standard Cost Published Event
- Standard Cost Exported Event
- Transfer Price Published Event
- Financial Orchestration Transfer Price Business Event
- Customer Asset Created
- Customer Asset Updated
- Customer Asset Relationship Created
- Customer Asset Relationship Deleted
- Maintenance Asset Created
- Maintenance Asset Updated
- Inspection Business Event
- B2B Message Created
- Manufacturer Create Event
- Manufacturer Update Event
- Debrief Header Updated
- Estimate Header Created
- Estimate Header Updated
- Project Status Event
- Publish Progress Event
- Plan Change Event
- Project Task Progress Status Changed
- Project Milestone Completion
- Project Deliverable Status Changed
- Project Resource Request Status Changed
- Project Gate Status Changed
- Project Gate Approver Status Changed
- Unplanned Project Cost Event
- Project Change Order Status Changed
- Project Work Plan Baseline Creation
- Project Issue Status Changed
- Plan Status Changed Event
- Purchase Order Event
- Supplier Created Event
- Supplier Updated Event
- Supplier Negotiation Invitation Event
- Activity Created Event
- Activity Updated Event
- Activity Deleted Event
- Recurrence Activity Created Event
- Recurrence Activity Updated Event
- Recurrence Activity Deleted Event
- Activity Note Created Event
- Activity Note Updated Event
- Activity Note Deleted Event
- Account Created Event
- Account Updated Event
- Account Deleted Event
- Contact Created Event
- Contact Updated Event
- Contact Deleted Event
- BusinessPlan Created Event
- BusinessPlan Updated Event
- BusinessPlan Deleted Event
- Business Plan Note Created Event
- Business Plan Note Updated Event
- Business Plan Note Deleted Event
- Opportunity Created Event
- Opportunity Updated Event
- Opportunity Deleted Event
- Opportunity Note Created Event
- Opportunity Note Updated Event
- Opportunity Note Deleted Event
- Lead Created Event
- Lead Updated Event
- Lead Deleted Event
- Lead Note Created Event
- Lead Note Updated Event
- Lead Note Deleted Event
- Deal Created Event
- Deal Updated Event
- Deal Note Created Event
- Deal Note Updated Event
- Deal Note Deleted Event
- Service Request Created Event
- Service Request Updated Event
- Service Request Selected Attribute value Changed Event
- Service Request Deleted Event
- Service Request Message Created Event
- Partner Created Event
- Partner Updated Event
- Partner Note Created Event
- Partner Note Updated Event
- Partner Note Deleted Event
- Partner Contact Created Event
- Partner Contact Updated Event
- Work Order Created Event
- Work Order Updated Event
- Asset Created Event
- Asset Updated Event
- Asset Deleted Event
- Resolution Request Updated
- Loyalty Member Created Event
- Loyalty Member Updated Event
- Loyalty Member Voucher Created Event
- Loyalty Member Voucher Updated Event
- Contract Created Event
- Contract Updated Event
- Contract Deleted Event
- Contract Status Changed Event
- Loyalty Member Referral Event
- Loyalty Transaction Created Event
- Loyalty Transaction Updated Event
- Loyalty Member Card Created Event
- Loyalty Member Card Updated Event
- Loyalty Member Tier Change Event
- Loyalty Attribute Created Event
- Loyalty Attribute Updated Event
- Subscription Created Event
- Subscription Updated Event
- Subscription Deleted Event
- Subscription AR Integration Event
- Loyalty Member Promotion Enrollment Event
- Loyalty Promotion Attribute Created Event
- Loyalty Promotion Attribute Updated Event
- ERP Integration Inbound event
- ERP Integration Outbound event
- Credit Case Folder Closure Event
- Credit Case Folder Created
- Credit Case Folder Refresh Requested
- Receivables Invoice Completed
- Receivables Invoice Paid
- Standard Receipt Created
- Standard Receipt Reversed
- Standard Receipt Applied
- Standard Receipt Unapplied
- Standard Receipt Deleted
- Receivables Invoice Incompleted
- Receivables Credit Memo Applied
- Receivables Credit Memo Completed
- Receivables Credit Memo Incompleted
- Receivables Lockbox Batch Completed
- Receivables Autoinvoice Completed
- Invoice Hold Applied
- Invoice Hold Released
- Payables Payment Created
- Payables Invoice Approved
- Payables Invoice Created
- Payables Invoice Validated
- Payables Invoice Cancelled
- Payables Payment Voided
- Strategy External Task opened
- Strategy Closed
- Payment File Created
- Journal Batch Approved
- Journal Batch Posting Completed
- Accounting Period Opened
- Accounting Period Closed
- Accounting Period Reopened
- Expenses Expense Report Submitted
- Expenses Expense Report Manager Approved
- Expenses Expense Report Auditor Approved
- Expenses Expense Report Held
- Expenses Expense Report Hold Released
- Expenses Expense Report Paid
- Revenue Contract Batch Created
- CustomPO\_c\_Standard\_Create
- CustomPO\_c\_Standard\_Update
- CustomCustomer\_c\_Standard\_Create
- CustomCustomer\_c\_Standard\_Update

## Output

| Output field | Description |
| --- | --- |
| Data | A SOAP-formatted XML payload that includes metadata such as the event destination, tracking identifiers, and user context in the header and event-specific details in the body. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-employee-atom-feed-entry.md
description: >-
  The New employee atom feed entry trigger detects and retrieves new
  employee-related events from Oracle Fusion Cloud's atom feed.
---

# Oracle Fusion Cloud - New employee atom feed entry trigger

The **New employee atom feed entry** trigger detects and retrieves new employee-related events from Oracle Fusion Cloud's atom feed.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |
| Feed Title | Select the atom feed title to monitor for new employee events. Options include: New Hire, Termination, Person Basic Information Changed, Person Assignment Changed, Work Relationship Update, Work Relationship Cancellation, Workstructure Organization Changed, Workstructure Location Changed, Workstructure Job Changed, Workstructure Grade Changed, Workstructure Position Changed |
| When first started, this recipe should pick up events from | Specify the starting date and time from which to begin retrieving events. |
| Trigger on date field | Choose the date field (**Published** or **Updated**) to determine when the trigger fires for new or updated feed entries. The default is **Published**. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the atom feed entry event. |
| Title | The title of the atom feed entry, usually describing the nature of the employee event (for example, Update, Hire). |
| Summary | A brief summary of the event or change detected. |
| Content | Detailed event data including employee context, changed attributes, and flex fields. |
| Context (Content) | Employee context information such as Person ID, Person Name, Assignment, Dates, and other HR attributes. |
| Changed Attributes | List of fields that have changed, showing old and new values. |
| Flex Fields | Additional flex field data, including custom or extended HR attributes. |
| Updated | The timestamp when the atom feed entry was last updated. |
| Published | The timestamp when the atom feed entry was published. |
| Authors | Array of authors, typically listing the system or user that performed the change. |
| Links | Array of hyperlinks to related resources (for example, employee record URL). |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-organization-atom-feed-entry.md
description: >-
  The New organization atom feed entry trigger detects and retrieves new
  organization-related events from Oracle Fusion Cloud's atom feed.
---

# Oracle Fusion Cloud - New organization atom feed entry trigger

The **New organization atom feed entry** trigger detects and retrieves new organization-related events from Oracle Fusion Cloud's atom feed.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |
| Feed Title | Select the atom feed title to monitor for new organization events. Options include: Workstructure Organization Changed, Workstructure Location Changed, Workstructure Job Changed, Workstructure Grade Changed, Workstructure Position Changed |
| When first started, this recipe should pick up events from | Specify the starting date and time from which to begin retrieving events. |
| Trigger on date field | Choose the date field (**Published** or **Updated**) to determine when the trigger fires for new or updated feed entries. The default is **Published**. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the atom feed entry event. |
| Title | The title of the atom feed entry, usually describing the nature of the organization event (for example, `Update`). |
| Summary | A brief summary of the event or change detected. |
| Content | Detailed event data including organization context, changed attributes, and flex fields. |
| Context (Content) | Organization context information such as `Organization ID`, `Organization Name`, `Location`, `Dates`, and other attributes. |
| Changed Attributes | List of fields that have changed, showing old and new values. |
| Flex Fields | Additional flex field data, including custom or extended attributes. |
| Updated | The timestamp when the atom feed entry was last updated. |
| Published | The timestamp when the atom feed entry was published. |
| Authors | Array of authors, typically listing the system or user that performed the change. |
| Links | Array of hyperlinks to related resources (for example, organization record URL). |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-record.md
description: >-
  The New record trigger detects when a new record is created in Oracle Fusion
  Cloud and can be configured to monitor any supported object type.
---

# Oracle Fusion Cloud - New record trigger

The **New record** trigger detects when a new record is created in Oracle Fusion Cloud. Configure this trigger by selecting an object, such as invoices or products, to monitor for new entries.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new records. Defaults to five minutes if left blank. Minimum is five minutes. |
| Object | Select the object (such as Invoice, Product, Supplier) to monitor for new records. |
| When first started, this recipe should pick up records from | Specify the starting date and time from which to begin retrieving records. |
| Expand | Select child and grandchild objects to include. By default, child objects are included. You can also select grandchild objects under parent objects (for example, include **Attachments** for each line in **Credit memo lines** within the **Receivable credit memo** object). |

## Output

The output of this trigger varies based on the type of object you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-record-batch.md
description: >-
  The New record batch trigger detects when new records are created in Oracle
  Fusion Cloud, processing multiple records at once for any supported object
  type.
---

# Oracle Fusion Cloud - New record trigger (batch)

The **New record** batch trigger detects when new records are created in Oracle Fusion Cloud and processes them in batches.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new records. Defaults to five minutes if left blank. Minimum is five minutes. |
| Object | Select the object to monitor (for example, **Invoice**, **Product**, **Supplier**). |
| When first started, this recipe should pick up records from | Specify the starting date and time from which to begin retrieving records. |
| Expand | Select child and grandchild objects to include. By default, child objects are included. You can also select grandchild objects under parent objects (for example, include **Attachments** for each line in **Credit memo lines** within the **Receivable credit memo** object). |
| Batch size | Specify the number of records to retrieve and process at a time. Minimum is 1, maximum is 100. |

## Output

Returns an array of records for each batch. Each record contains all fields from the selected object, including child and selected grandchild objects.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-updated-record.md
description: >-
  The New/updated record trigger detects when a new record is created or an
  existing record is updated in Oracle Fusion Cloud and can be configured to
  monitor any supported object type.
---

# Oracle Fusion Cloud - New/updated record trigger

The **New/updated record** trigger detects when a new record is created or an existing record is updated in Oracle Fusion Cloud. Configure this trigger by selecting an object (for example, Invoice, Product, Supplier) to monitor.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new or updated records. Defaults to five minutes if left blank. Minimum is five minutes. |
| Object | Select the object (such as **Invoice**, **Product**, **Supplier**) to monitor for new or updated records. |
| When first started, this recipe should pick up records from | Specify the starting date and time from which to begin retrieving records. |
| Expand | Select child and grandchild objects to include. By default, child objects are included. You can also select grandchild objects under parent objects (for example, include **Attachments** for each line in **Credit memo lines** within the **Receivable credit memo** object). |

## Output

The output of this trigger varies based on the type of object you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/triggers/new-updated-record-batch.md
description: >-
  The New/updated record batch trigger detects when new records are created or
  existing records are updated in Oracle Fusion Cloud, processing multiple
  records at once for any supported object type.
---

# Oracle Fusion Cloud - New/updated record trigger (batch)

The **New/updated record** batch trigger detects when new records are created or existing records are updated in Oracle Fusion Cloud. The trigger processes records in batches. Select an object (for example, **Invoice**, **Product**, **Supplier**) to monitor.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new or updated records. Defaults to five minutes if left blank. Minimum is five minutes. |
| Object | Select the object (such as **Invoice**, **Product**, **Supplier**) to monitor for new or updated records. |
| When first started, this recipe should pick up records from | Specify the starting date and time from which to begin retrieving records. |
| Expand | Select child and grandchild objects to include. By default, child objects are included. You can also select grandchild objects under parent objects (for example, include **Attachments** for each line in **Credit memo lines** within the **Receivable credit memo** object). |
| Batch size | Specify the number of records to retrieve and process at a time. Minimum is 1, maximum is 100. |

## Output

The output of this trigger varies based on the type of object you select. For each batch, you receive an array of records, each containing all fields from the selected object, including child and selected grandchild objects.

---
