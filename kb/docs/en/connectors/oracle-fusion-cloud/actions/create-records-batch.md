---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/create-records-batch.md
description: >-
  The Create records batch action creates new records for a specified object in
  Oracle Fusion Cloud in batches.
---

# Oracle Fusion Cloud - Create records action (batch)

The **Create records** batch action creates multiple new records for a specified object in Oracle Fusion Cloud. For example, it can create multiple receivable invoices for a specific customer account.

All attributes and child objects appear as input fields after you select the object. Provide the required fields and populate required child objects to create the records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the records to create. |
| Records | Expand this section to enter the field values for the records. |
| Records source list | Input a list datapill. |

Additional fields load dynamically based on the selected object.

## Output

| Output field | Description |
| --- | --- |
| Items | A list of the created records. |

Additional fields return based on the selected object.
