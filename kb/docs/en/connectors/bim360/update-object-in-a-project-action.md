---
url: >-
  https://docs.workato.com/en/connectors/bim360/update-object-in-a-project-action.md
description: >-
  The update object in a project action updates an existing object you specify
  in BIM 360.
---

# BIM 360 - Update object in a project action

The **Update object in a project** action updates an existing object you specify in BIM 360.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to update. |
| Project name | Select the project that contains the object you plan to update. |
| Container ID | Provide the BIM 360 container ID where you plan to update an object. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the object. |
| Project ID | The BIM 360 ID of the project that contains the object. |
| ID | The BIM 360 ID of the object. |
| Name | The name of the object. |
| Description | The object's description. |
| Creator ID | The ID of the user that created the object. |
| Changed by | Indicates the user that changed the object. |
| External ID | The ID of the object in an external system. |
| External system | The name of the external system that manages the object. |
| Created at | A timestamp indicating when the object was created. |
| Updated at | A timestamp indicating when the object was last updated. |

> **ADDITIONAL OUTPUT FIELDS**
> 
> The **Update object in a project** action generates additional output fields based on your selected **Object**. Refer to BIM 360's [API guide](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/) for more information on BIM 360 objects.
