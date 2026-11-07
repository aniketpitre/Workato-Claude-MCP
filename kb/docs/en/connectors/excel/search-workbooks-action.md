---
url: 'https://docs.workato.com/en/connectors/excel/search-workbooks-action.md'
description: >-
  The Search workbooks action in the Excel connector lets you find workbooks in
  a OneDrive or SharePoint file source by query.
---

# Excel - Search Workbooks action

This action searches for workbooks in a specific file source.

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| Drive | The drive within the selected file source. e.g. `Documents` for `SharePoint document library` |
| Query | The free test query that will be matched across various fields including filename, metadata, and file content. |

## Output

| Output field | Description |
| --- | --- |
| `Workbooks` | An array of workbooks that match your query. |

---
