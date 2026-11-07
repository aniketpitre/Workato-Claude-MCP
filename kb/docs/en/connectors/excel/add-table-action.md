---
url: 'https://docs.workato.com/en/connectors/excel/add-table-action.md'
description: >-
  The Add a table action in the Excel connector lets you create a table over a
  cell range in a specified worksheet of an Excel file.
---

# Excel - Add a table action

This action adds a table in a specified Excel file.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| File | The file within the selected file source. Either select from the generated picklist or provide the file ID manually. |
| Worksheet | Name of the worksheet where the table will be added to. |
| Range from | The top left cell address where the table will start from. For example, A1 |
| Range to | The bottom right cell address where the table will end. e.g. B2 |
| Has headers? | Boolean value that indicates whether the range has column labels. If the source does not contain headers (i.e. when this property set to No), Excel will automatically generate header shifting the data down by one row. |

## Output

| Output field | Description |
| --- | --- |
| `Table` | Metadata describing the table created |

---
