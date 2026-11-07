---
url: 'https://docs.workato.com/en/connectors/box/trigger-new-csv-line.md'
description: >-
  The New line in CSV file trigger starts a recipe when a new line is added to a
  specified CSV file in Box.
---

# Box - New line in CSV file trigger

The **New line in CSV file** trigger starts a recipe when a CSV file in Box adds a new line. The trigger processes all existing lines in the selected file. Each line runs as a separate event. You must append new lines at the end of the CSV file. Removing or editing lines causes the trigger to stop tracking correctly.

## Input

| Input field | Description |
| --- | --- |
| File | Select the CSV file to process. You can select from the drop-down menu or enter a file ID. |
| Column separator | Select the character used to separate column values. For example, a comma. |
| Add column names manually | Select **Yes** to define column names manually. Select **No** to use the first row of the CSV file as column names. |

## Output

| Output field | Description |
| --- | --- |
| Line number | Number of the line the trigger processes. The first non-header line has the value `1`. |
| Columns | Contains the CSV columns and their data. If you configured custom values, this is an object datapill with the defined columns. If you selected from the option list, the output shows the configured column names. |

---
