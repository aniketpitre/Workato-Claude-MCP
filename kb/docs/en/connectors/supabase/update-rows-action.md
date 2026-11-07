---
url: 'https://docs.workato.com/en/connectors/supabase/update-rows-action.md'
description: >-
  Update rows in a Supabase table that match one or more required filters, with
  the updated rows returned in the output.
---

# Supabase - Update rows action

The **Update rows** action updates rows in a table in Supabase that match the configured filters. At least one filter is required, so the action can't affect a whole table by mistake.

## Input

Input fields dynamically generate based on the table you select.

| Input field | Description |
| --- | --- |
| Table | Select the table or view in the Supabase project. |
| Values | Enter the columns to change on rows matched by **Filters**. Primary key and read-only columns are omitted. When **Apply defaults for missing columns** is **No**, leave a field blank to keep its current value. |
| Filters | Choose which rows to update. Each filter is a column, an operator, and a value. |
| Column (Filters) | Select the column to filter on. Picklist values are the actual table column names as defined in Supabase, for example `cust_id`. |
| Operator (Filters) | Select the operator to compare the column to the value. |
| Value (Filters) | Enter the value to compare against. For `in`, use `(1,2,3)`. For `is`, use `null`, `true`, or `false`. |
| Apply defaults for missing columns | Optional. Select **Yes** to replace blank **Values** fields with the column's database default value. Select **No** to keep the current value of blank **Values** fields. Defaults to **No** if left blank. |
| Select | Optional. Select the columns to return. Leave blank to return all columns. |

## Output

Output fields dynamically generate based on the table you select.

| Output field | Description |
| --- | --- |
| Rows | The updated rows. |
| Location | The updated row's URL. The **Location** field is only available when Supabase's response doesn't include row data. |

---
