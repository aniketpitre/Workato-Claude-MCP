---
url: >-
  https://docs.workato.com/en/connectors/supabase/insert-or-upsert-rows-action.md
description: >-
  Insert one or more rows into a Supabase table, with an optional upsert when a
  unique key already exists.
---

# Supabase - Insert or upsert rows action

The **Insert or upsert rows** action inserts one or more rows into a table in Supabase, with an optional upsert when a unique key already exists.

## Input

Input fields dynamically generate based on the table you select.

| Input field | Description |
| --- | --- |
| Table | Select the table or view in the Supabase project. |
| Rows | Enter one or more rows to insert or upsert. |
| Resolution | Optional. Select whether to merge new values into the existing row or ignore the insert on a conflict. Requires **On conflict** columns. |
| On conflict | Optional. Select the unique column(s) for upsert conflicts. The **On conflict** field is required when **Resolution** is set. |
| Apply defaults for missing columns | Optional. Select **Yes** to use database defaults for blank columns, or **No** to leave blank columns unset. Defaults to **No** if left blank. |
| Select | Optional. Select the columns to return. Leave blank to return all columns. |

## Output

Output fields dynamically generate based on the table you select.

| Output field | Description |
| --- | --- |
| Rows | The inserted or upserted rows. |
| Location | The inserted row's URL. The **Location** field is only available when Supabase's response doesn't include row data. |
