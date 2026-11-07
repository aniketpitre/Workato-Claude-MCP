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
