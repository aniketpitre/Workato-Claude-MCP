---
url: 'https://docs.workato.com/en/connectors/onedrive/new-line-csv-file-trigger.md'
description: >-
  The New line in CSV file trigger in the OneDrive connector picks up new lines
  added to a specified CSV file in Microsoft OneDrive as separate events.
---

# OneDrive - New line in CSV file trigger

The **New line in CSV file** trigger detects new lines added to a specified CSV file in your OneDrive account. This trigger processes each new line as a separate event.

## Input

| Input fields | Description |
| --- | --- |
| File path | Provide the full path of the CSV file, including folder structure and file extension. For example, `folder-one/file-name.csv`. |
| Column separator | Specify the character used to separate values in the CSV file. |

## Output

The output fields provide information about the new line added to the CSV file, including its line number and column values.

| Output field | Description |
| --- | --- |
| Line | The line number of the new line in the CSV file. |

---
