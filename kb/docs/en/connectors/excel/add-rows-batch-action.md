---
url: 'https://docs.workato.com/en/connectors/excel/add-rows-batch-action.md'
description: >-
  The Add rows action in the Excel connector lets you add a list of rows to a
  table in a specified Excel file.
---

# Excel - Add rows action

This action adds rows to a table in a specified Excel file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |
| Table name | Name of the table to add rows to. |
| Columns | The column names for this table. These are used to generate the datapills in this action's output. It does not need to match the column names in your worksheet. |
| Rows | List of rows to add. |

## Output

| Output field | Description |
| --- | --- |
| `Rows` | The rows just added to the Excel file. |

---
