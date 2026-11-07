---
url: 'https://docs.workato.com/en/connectors/excel/list-worksheets-action.md'
description: >-
  The List worksheets action in the Excel connector lets you retrieve all
  worksheets and their metadata from a specified Excel file.
---

# Excel - List Worksheets action

This action list all Worksheet objects found in a specified excel file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |

## Output

| Output field | Description |
| --- | --- |
| `Worksheets` | An array of worksheets within the excel file and associated metadata. |

---
