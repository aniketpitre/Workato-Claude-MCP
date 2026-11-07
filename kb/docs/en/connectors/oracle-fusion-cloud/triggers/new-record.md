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
