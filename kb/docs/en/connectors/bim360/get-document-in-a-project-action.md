---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-document-in-a-project-action.md
description: >-
  The get document in a project action retrieves data about a BIM 360 document
  you specify.
---

# BIM 360 - Get document in a project action

The **Get document in a project** action retrieves data about a BIM 360 document you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the document you plan to retrieve. |
| Project name | Select the project that contains the document you plan to retrieve. |
| Folder | Select the folder that contains the document you plan to retrieve. |
| File name | Select the file that contains the document you plan to retrieve. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the document. |
| Project ID | The BIM 360 ID of the project that contains the document. |
| Jsonapi | Contains information about the API such as its `Version`. |
| Links | Contains information about the document's associated links, such as their `Type` and `Data`. |
| Data | Contains metadata information about the document, such as its `Type`, `Item ID`, and `Relationships`. |
| Included | Contains information about the document, such as its `Attributes`, `Links`, and `List size`. |
