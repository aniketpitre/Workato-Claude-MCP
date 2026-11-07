---
url: >-
  https://docs.workato.com/en/connectors/bim360/create-object-in-a-project-action.md
description: The create object in a project action creates a new object in BIM 360.
---

# BIM 360 - Create object in a project action

The **Create object in a project** action creates a new object in BIM 360.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of object you plan to create. |
| Hub name | Select the hub where you plan to create a new object. |
| Project name | Select the project where you plan to create a new object. |

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

> **OUTPUT FIELDS**
> 
> The `Cost attachment` and `Cost document` objects don't generate output fields.
> 
> Other objects may generate additional output fields. Refer to BIM 360’s [API guide](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/) for more information.
