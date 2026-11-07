---
url: 'https://docs.workato.com/en/connectors/baserow/create-record-action.md'
description: >-
  Add a new row to a table using your table's own column names as the input
  fields.
---

# Baserow - Create record action

The **Create record** action creates a new row in a table in Baserow.

## Input

Input fields dynamically generate based on the object you select and the create operation. The following fields are common to all objects. Fields with computed or read-only types, such as formulas, lookups, or auto number, aren't included because Baserow doesn't accept them as input.

| Input field | Description |
| --- | --- |
| Object type | Select the object type, such as **Row**. |
| Table ID | Select the table to create a row in. |

## Output

Output fields dynamically generate based on the object type you select. The following fields are common to all objects.

| Output field | Description |
| --- | --- |
| Row ID | The new row's unique identifier. |
| Order | The row's position among the table's rows. |

---
