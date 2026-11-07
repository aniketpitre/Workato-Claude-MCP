---
url: 'https://docs.workato.com/en/connectors/supabase/query-rows-action.md'
description: >-
  Query rows from a Supabase table with filters, sorting, pagination, and an
  optional total row count.
---

# Supabase - Query rows action

The **Query rows** action retrieves rows from a table in Supabase that match the configured filters, with support for sorting and pagination.

## Input

| Input field | Description |
| --- | --- |
| Table | Select the table or view in the Supabase project. |
| Filters | Optional. Choose which rows to include. Each filter is a column, an operator, and a value. |
| Column (Filters) | Select the column to filter on. Picklist values are the actual table column names as defined in Supabase, for example `cust_id`. |
| Operator (Filters) | Select the operator to compare the column to the value. |
| Value (Filters) | Enter the value to compare against. For `in`, use `(1,2,3)`. For `is`, use `null`, `true`, or `false`. |
| Order | Optional. Sort by column and direction. |
| Column (Order) | Select the column to sort by. |
| Direction (Order) | Select the sort direction. |
| Limit | Optional. Enter the maximum number of rows to return. The default is `1000`. To return a single row, enter `1` and set **Order** so the row is deterministic. |
| Offset | Optional. Enter the number of rows to skip for pagination. The default is `0`. |
| Count | Optional. Select a method to request a total row count with the results. |
| Select | Optional. Select the columns to return. Leave blank to return all columns. |

## Output

Output fields dynamically generate based on the table you select.

| Output field | Description |
| --- | --- |
| Rows | The matching rows. |
| Count | The total number of matching rows. The **Count** field is only available when the **Count** input field is set. |

---
