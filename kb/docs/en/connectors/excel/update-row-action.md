---
url: 'https://docs.workato.com/en/connectors/excel/update-row-action.md'
description: >-
  The Update row action in the Excel connector lets you update the values of a
  row in a table within a specified Excel file by index.
---

# Excel - Update row action

This action updates a row in a table in a specified Excel file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |
| Table name | Name of the table to add rows to. |
| Index | The index of the row to be deleted. |
| Columns | The column names for this table. These are used to generate the datapills in this action's output. It does not need to match the column names in your worksheet. |
| Row values | The row values to update. |

## Output

| Output field | Description |
| --- | --- |
| `Rows` | The rows just added to the Excel file. |

---
