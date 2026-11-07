---
url: 'https://docs.workato.com/en/connectors/on-prem-files/new-lines-trigger.md'
description: >-
  The New lines in CSV file batch trigger in the On-prem files connector picks
  up newly added lines from an on-prem CSV file each poll interval.
---

# On-prem files - New lines in CSV file trigger (Batch)

The **New lines in CSV file** batch trigger monitors an on-prem CSV file you specify for new lines.

The trigger detects all existing lines in the CSV file when you start the recipe for the first time. Only newly added lines are processed on subsequent runs. This trigger checks for new lines once every poll interval.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Define how frequently the recipe checks for new lines. The minimum and default value is `5` minutes. |
| CSV file | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the CSV file to monitor for new lines. This CSV file must have a header line. The value of each column in the header is used to generate the output schema of the trigger. |
| Column delimiter | Select the character used to separate column values within each CSV row. |
| Quote character | Select the character used to quote cell values. Set to **None** if no quote character is used. |
| File encoding | Select the encoding for the CSV file. This field defaults to **UTF-8**. |
| Batch size | Enter the number of CSV rows to process in each batch. Refer to [Batch processing](/en/features/batch-processing) for more information. This field defaults to 100 and supports a maximum of 2,000 lines. |

## Output

| Output field | Description |
| --- | --- |
| First line number in batch | The line number of the first line in the batch currently being processed. Header lines aren't counted. |
| Last line number in batch | The line number of the last line in the batch currently being processed. Header lines aren't counted. |
| CSV lines | Contains information about the contents of the new lines, such as the `List size`, `List index`, and the column names. |

---
