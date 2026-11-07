---
url: 'https://docs.workato.com/en/connectors/baserow/update-record-action.md'
description: >-
  Change one existing row's field values, identified by its row ID, in a Baserow
  table.
---

# Baserow - Update record action

The **Update record** action updates an existing row in a table in Baserow. Use the [Update records (batch)](/en/connectors/baserow/update-records-action-batch) action instead to update up to 200 rows in one request.

## Input

Input fields dynamically generate based on the object you select and the update operation. The following fields are common to all objects. Fields with computed or read-only types, such as formulas, lookups, or auto number, aren't included because Baserow doesn't accept them as input.

| Input field | Description |
| --- | --- |
| Object type | Select the object type, such as **Row**. |
| Table ID | Select the table the row belongs to. |
| Row ID | Enter the unique identifier of the row to update. |

## Output

Output fields dynamically generate based on the object type you select. The following fields are common to all objects.

| Output field | Description |
| --- | --- |
| Row ID | The updated row's unique identifier. |
| Order | The row's position among the table's rows. |

---
