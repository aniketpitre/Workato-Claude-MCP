---
url: 'https://docs.workato.com/en/connectors/excel/list-tables-action.md'
description: >-
  The List tables action in the Excel connector lets you retrieve all tables and
  their metadata found in a specified Excel file.
---

# Excel - List tables action

This action list all tables objects found in a specified file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |

## Output

| Output field | Description |
| --- | --- |
| `Tables` | An array of tables and associated metadata. |

---
