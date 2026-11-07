---
url: 'https://docs.workato.com/en/connectors/excel/get-cells-action.md'
description: >-
  The Get cells action in the Excel connector lets you retrieve a range of cell
  values from a worksheet using cell notation or a named range.
---

# Excel - Get cells action

The **Get cells** action retrieves a range of cell values in your Excel spreadsheet. You can provide the **Worksheet** and **Range** (for example, `A1:D100` or a named range). This action doesn't infer the used range. The maximum file size supported is 50MB.

Use the [Get rows action](/en/connectors/excel/get-rows-action) and enter the exact **Table name** to return rows from an Excel table.

![Get cells action](/assets/get-cells-action.DO5_jVJt.png)_Get cells action_

## Input

| Input field | Description |
| --- | --- |
| File source | File source of the spreadsheet, either from `OneDrive` or `SharePoint document library` |
| Site _Only if file source is Sharepoint_ | The SharePoint site that spreadsheet belongs in. |
| Folder | The spreadsheet's folder within the selected file source. Either select from the generated picklist or provide the drive and folder ID manually. |
| File name | File name of the spreadsheet to read from. |
| Worksheet | The worksheet to read from within the spreadsheet. Provide either the worksheet name or the sheet position. |
| Range | The range address of the worksheet to retrieve cells from, either with cell notation, e.g. `B5:C20`, or with a [named range](https://support.microsoft.com/en-us/office/define-and-use-names-in-formulas-4d0f13ac-53b7-422e-afd2-abd7ff379c64) |
| Range contains header line? | Set to `Yes` if the range address contains a header line in the first row that should not be returned as an output row. |
| Columns | The column names for this range of cells. These are used to generate the datapills in this action's output. It does not to match the column names in your worksheet. |

## Output

| Output field | Description |
| --- | --- |
| `Rows` | An array of rows of the cells extracted. The datapills within the row is determined the **Columns** input. |

---
