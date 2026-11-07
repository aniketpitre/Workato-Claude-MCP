---
url: 'https://docs.workato.com/en/connectors/csv-by-workato/compose-csv-action.md'
description: >-
  This action converts a list of objects into a CSV-formatted string for export
  or storage.
---

# CSV tools by Workato - Compose CSV action (batch)

The **Compose CSV** batch action converts a list of objects into a CSV-formatted string. You can use this action to prepare structured data for export, transfer, or storage as a CSV file.

## Input

| Input fields | Description |
| --- | --- |
| CSV column names | Enter one column name per line. This defines the order and structure of the CSV. |
| Create header line | Set to **Yes** to include a header line at the top of the CSV using the column names provided. |
| Column delimiter | Select the character used to separate columns in the CSV output. |
| Force quotes | Set to **Yes** to wrap all values in quotes. Set to **No** to quote only when necessary. |
| CSV data lines | Provide the list datapill that contains the rows for the CSV. Then, map the corresponding fields to each column you defined in the **CSV column names** field. |

## Output

| Output fields | Description |
| --- | --- |
| CSV contents | A text string that represents the formatted CSV. Use this value to upload the file or pass it to another system. |

---
