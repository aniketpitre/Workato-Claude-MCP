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
