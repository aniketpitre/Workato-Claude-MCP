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
