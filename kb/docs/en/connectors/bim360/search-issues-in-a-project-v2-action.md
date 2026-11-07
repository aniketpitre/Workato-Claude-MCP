---
url: >-
  https://docs.workato.com/en/connectors/bim360/search-issues-in-a-project-v2-action.md
description: >-
  The search issues in a project (V2) batch action retrieves a list of the
  issues in a BIM 360 project you specify.
---

# BIM 360 - Search issues in a project (V2) action (batch)

The **Search issues in a project (V2)** batch action retrieves a list of issues from a BIM 360 project you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to search. |
| Project name | Select the project that contains the container you plan to search. |
| Container ID | Provide the BIM 360 container ID you plan to retrieve issues from. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the issues. |
| Project ID | The BIM 360 ID of the project that was searched. |
| Pagination | Contains information about pagination of the returned `Results` list, such as `Limit`, `Offset`, and `Total results`. |
| Results | Contains information about the issues retrieved from BIM 360, such as their `ID`, `Title`, and `Description`. |
