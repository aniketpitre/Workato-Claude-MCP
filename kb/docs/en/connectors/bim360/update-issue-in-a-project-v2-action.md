---
url: >-
  https://docs.workato.com/en/connectors/bim360/update-issue-in-a-project-v2-action.md
description: >-
  The update issue in a project (V2) action updates an existing issue you
  specify in BIM 360.
---

# BIM 360 - Update issue in a project (V2) action

The **Update issue in a project (V2)** action updates an existing issue you specify in BIM 360.

> **REQUIRED PERMISSIONS**
> 
> Users must have one of the following permissions in BIM 360 to update issues:
> 
> - The project admin role. Refer to BIM 360's [Roles](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-7E2C374B-DADC-4E13-AEA7-C8DCF6838A31) guide for more information.
> - The `create`, `view and create`, or `full control` field management permissions. Refer to BIM 360's [Permissions: Field Management](https://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-7E2C374B-DADC-4E13-AEA7-C8DCF6838A31) guide for more information.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to update. |
| Project name | Select the project that contains the issue you plan to update. |
| Container ID | Provide the BIM 360 container ID where you plan to update an issue. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the issue. |
| Project ID | The BIM 360 ID of the project that contains the issue. |
| Pagination | Contains information about pagination of the returned `Results` list, such as `Limit`, `Offset`, and `Total results`. |
| Results | Contains information about the issues retrieved from BIM 360, such as their `ID`, `Title`, and `Description` |
