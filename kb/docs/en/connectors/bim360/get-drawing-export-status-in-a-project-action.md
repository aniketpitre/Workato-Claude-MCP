---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-drawing-export-status-in-a-project-action.md
description: >-
  The get drawing export status in a project action retrieves data about a PDF
  export job in BIM 360.
---

# BIM 360 - Get drawing export status in a project action

The **Get drawing export status in a project** action retrieves the status and details of a PDF export job in BIM 360.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the export job you plan to retrieve. |
| Project name | Select the project that contains the export job you plan to retrieve. |
| Folder name | Select the folder that contains the export job you plan to retrieve. |
| File name | Select the file that contains the export job you plan to retrieve. |
| Version number | Select the version number for the export job. |
| Export ID | Provide the BIM 360 ID of the export job. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the drawing. |
| Project ID | The BIM 360 ID of the project that contains the drawing. |
| Item ID | The BIM 360 ID of the drawing. |
| Export job ID | The BIM 360 ID of the export job. |
| Status | The status of the export job in BIM 360. |
| Data | Contains data information about the drawing, such as its `Version URN`, `Resource ID`, and `Link`. |
