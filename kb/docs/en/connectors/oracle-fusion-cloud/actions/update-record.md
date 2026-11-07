---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/update-record.md
description: The Update record action updates an existing record.
---

# Oracle Fusion Cloud - Update record action

The **Update record** action updates an existing record. Select an object to load its input fields. The object's primary key is required to identify the record.

For example, to update a receivables invoice, select **Receivables invoice** and provide the **Customer transaction ID**. You can use the [Search records action](/en/connectors/oracle-fusion-cloud/actions/search-records-batch) to retrieve the ID, then map it into the update input.

To update a child object, provide the IDs of both the main object and the child object. For example, provide the **Line number ID** to update an invoice line.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the record you plan to update. |
| Object ID | Select the ID of the record you plan to update. |

Additional fields load dynamically depending on the object you select.

## Output

The output of this action contains details about the updated record.
