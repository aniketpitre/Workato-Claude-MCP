---
url: 'https://docs.workato.com/en/connectors/on-prem-files/new-line-trigger.md'
description: >-
  The New line in CSV file trigger in the On-prem files connector picks up newly
  added lines from an on-prem CSV file each poll interval.
---

# On-prem files - New line in CSV file trigger

The **New line in CSV file** trigger monitors an on-prem CSV file you specify for new lines.

The trigger detects all existing lines in the CSV file when you start the recipe for the first time. Only newly added lines are processed on subsequent runs. This trigger checks for new lines once every poll interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Define how frequently the recipe checks for new lines. The minimum and default value is `5` minutes. |
| CSV file | Select a CSV file to monitor for new lines. This CSV file must have a header line. The value of each column in the header is used to generate the output schema of the trigger. |
| Column delimiter | Select the character used to separate column values within each CSV row. |
| Quote character | Select the character used to quote cell values. Set to **None** if no quote character is used. |
| File encoding | Select the encoding for the CSV file. This field defaults to **UTF-8**. |

## Output

| Output field | Description |
| --- | --- |
| Line number | The line number of the line currently being processed. Header lines are not counted. |
| CSV line | Contains information about the contents of the new line, such as the column names and their values. |

---
