---
url: 'https://docs.workato.com/en/connectors/baserow/update-records-action-batch.md'
description: >-
  Update up to 200 existing rows in a single request instead of calling Update
  record repeatedly.
---

# Baserow - Update records action (batch)

The **Update records (batch)** action updates up to 200 rows in one request in Baserow.

## Input

Input fields dynamically generate based on the object you select and the update operation. The following fields are common to all objects. Fields with computed or read-only types, such as formulas, lookups, or auto number, aren't included because Baserow doesn't accept them as input.

| Input field | Description |
| --- | --- |
| Object type | Select the object type, such as **Row**. |
| Table ID | Select the table the rows belong to. |
| Items | Add up to 200 rows to update. Each item needs a **Row ID** and the fields to update. |

## Output

Output fields dynamically generate based on the object type you select. The following fields are common to all objects.

| Output field | Description |
| --- | --- |
| Items | The updated rows. Each item includes a **Row ID**, **Order**, and the table's fields. |

---
