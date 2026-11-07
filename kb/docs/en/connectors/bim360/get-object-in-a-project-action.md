---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-object-in-a-project-action.md
description: >-
  The get object in a project action retrieves data about a BIM 360 object you
  specify.
---

# BIM 360 - Get object in a project action

The **Get object in a project** action retrieves data about a BIM 360 object you specify.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of object you plan to retrieve. |
| Hub name | Select the hub that contains the object you plan to retrieve. |
| Project name | Select the project that contains the object you plan to retrieve. |

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
