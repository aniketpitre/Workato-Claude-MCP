---
url: 'https://docs.workato.com/en/connectors/excel/delete-rows-action.md'
description: >-
  The Delete row action in the Excel connector lets you delete a row from a
  table in a specified Excel file by its row index.
---

# Excel - Delete row action

This action deletes a row in a table in a specified Excel file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |
| Table name | Name of the table to add rows to. |
| Index | The index of the row to be deleted. |

## Output

| Output field | Description |
| --- | --- |
| `Rows` | The rows just added to the Excel file. |

---
