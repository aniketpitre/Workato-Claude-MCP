---
url: 'https://docs.workato.com/en/connectors/excel/add-worksheet-action.md'
description: >-
  The Add a worksheet action in the Excel connector lets you add a new named
  worksheet to a specified Excel file.
---

# Excel - Add a worksheet action

This action adds a worksheet to a specified Excel file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |
| Name | Name of the worksheet to create. |

## Output

| Output field | Description |
| --- | --- |
| `Worksheet` | Metadata describing the Worksheet created |

---
