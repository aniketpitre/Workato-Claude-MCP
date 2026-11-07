---
url: >-
  https://docs.workato.com/en/data-tables/connector/new-updated-record-trigger.md
description: >-
  The new/updated record trigger monitors a data table you specify in real-time
  for newly created or updated records.
---

# New/updated record trigger (real-time)

The **New/updated record** trigger monitors a data table you specify in real-time for newly created or updated records.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select a data table to monitor for newly created or updated records. Click the link in this field's description to view the selected data table in the [Data tables interface](/en/data-tables/data-table-interface). |
| When first started, this recipe should pick up events from | Get new or updated records starting at a specific date/time. This enables your recipe to capture past events from up to 30 days ago. The trigger retrieves newly created or updated records from one hour ago if you leave this field empty. You cannot change this value after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Choose the desired output format | Optional. Specify how to map the new or updated record data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |

> **TRIGGER CONDITIONS**
> 
> This trigger supports [trigger conditions](/en/recipes/triggers#trigger-conditions) that you can use to filter incoming trigger events.

## Output

| Output fields | Description |
| --- | --- |
| Change ID | The ID number that corresponds to the change in the data table. |
| Record | Contains information about the new or updated record, such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of the data table's custom columns. |
| Old record | Contains information about the original record, such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of the data table's custom columns. |
