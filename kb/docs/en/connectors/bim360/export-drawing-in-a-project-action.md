---
url: >-
  https://docs.workato.com/en/connectors/bim360/export-drawing-in-a-project-action.md
description: >-
  The export drawing in a project action exports a page from a PDF in BIM 360's
  document management system as a new PDF file.
---

# BIM 360 - Export drawing in a project action

The **Export drawing in a project** action exports a page from a PDF in BIM 360's document management system as a new PDF file.

> **LIMITATIONS**
> 
> The **Export drawing in a project** action can only export documents from the `Plans` folder and its sub-folders. Refer to BIM 360's [Plans and Project Files](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-9B58CB2C-0519-47B0-9199-4535577B594A) guide for more information.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the document you plan to export a page from. |
| Project name | Select the project that contains the document you plan to export a page from. |
| Folder name | Select the folder that contains the document you plan to export a page from. |
| File name | Select the file that contains the document you plan to export a page from. |
| Version number | Select the document's version number. |
| Include markups | Specify whether to export the page's annotations. |
| Include hyperlinks | Specify whether to export the page's hyperlinks. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the page. |
| Project ID | The BIM 360 ID of the project that contains the page. |
| Folder ID | The BIM 360 ID of the folder that contains the page. |
| Item ID | The BIM 360 ID of the page. |
| Status | The status of the export job in BIM 360. |
