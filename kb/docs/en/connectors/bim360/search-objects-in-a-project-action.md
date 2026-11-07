---
url: >-
  https://docs.workato.com/en/connectors/bim360/search-objects-in-a-project-action.md
description: >-
  The search objects in a project action searches a BIM 360 project and returns
  a list of objects matching the type you specify.
---

# BIM 360 - Search objects in a project action

The **Search objects in a project** action searches a BIM 360 project and returns a list of objects matching the type you specify.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of object you plan to search for. |
| Hub name | Select the hub that contains the project you plan to search. |
| Project name | Select the project you plan to search. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the object. |
| Project ID | The BIM 360 ID of the project that contains the object. |
| Pagination | Contains information about pagination of the returned `Results` list, such as `Limit`, `Offset`, and `Total results`. |
| Results | Contains information about the objects retrieved from BIM 360, such as their `ID`, `Title`, and `Description` |

> **COST FILE PACKAGE OBJECT OUTPUT FIELDS**
> 
> The `Cost file package` object doesn't generate output fields.
