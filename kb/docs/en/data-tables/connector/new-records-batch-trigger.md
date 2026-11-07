---
url: 'https://docs.workato.com/en/data-tables/connector/new-records-batch-trigger.md'
description: >-
  The new records trigger checks for new records in a data table you specify in
  batches.
---

# New records trigger (batch)

The **New records** trigger checks for new records in a data table you specify in batches. This trigger supports the following maximum batch size:

| Description | Quota |
| --- | --- |
| Maximum batch size for all Data table connector batch triggers | 1,000 |

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select a data table to monitor for newly created records. Click the link in this field's description to view the selected data table in the [data tables interface](/en/data-tables/data-table-interface). |
| When first started, this recipe should pick up events from | Get new records starting at a specific date/time. This enables your recipe to capture past events from up to 30 days ago. The trigger retrieves new records from one hour ago if you leave this field empty. You cannot change this value after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Choose the desired output format | Optional. Specify how to map the new record data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |

## Output

| Output fields | Description |
| --- | --- |
| Range | Timestamps of the first and last new records in the retrieved batch. |
| First record ID | ID of the first record in the batch. |
| Last record ID | ID of the last record in the batch. |
| Records | A list of all the new records, including information such as its `Record ID`, `Created at` date, `Updated at` timestamp, and data from any of the data table's custom columns. |

---
