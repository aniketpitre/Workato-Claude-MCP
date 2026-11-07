---
url: 'https://docs.workato.com/en/connectors/supabase/delete-rows-action.md'
description: >-
  Delete rows from a Supabase table that match one or more required filters,
  with the deleted rows returned in the output.
---

# Supabase - Delete rows action

The **Delete rows** action deletes rows from a table in Supabase that match the configured filters. At least one filter is required, so the action can't clear a whole table by mistake.

## Input

| Input field | Description |
| --- | --- |
| Table | Select the table or view in the Supabase project. |
| Filters | Choose which rows to delete. Each filter is a column, an operator, and a value. |
| Column (Filters) | Select the column to filter on. Picklist values are the actual table column names as defined in Supabase, for example `cust_id`. |
| Operator (Filters) | Select the operator to compare the column to the value. |
| Value (Filters) | Enter the value to compare against. For `in`, use `(1,2,3)`. For `is`, use `null`, `true`, or `false`. |
| Select | Optional. Select the columns to return. Leave blank to return all columns. |

## Output

Output fields dynamically generate based on the table you select.

| Output field | Description |
| --- | --- |
| Rows | The deleted rows. |
| Location | The deleted row's URL. The **Location** field is only available when Supabase's response doesn't include row data. |

---
