---
url: >-
  https://docs.workato.com/en/connectors/bim360/new-or-updated-object-in-a-project-trigger.md
description: >-
  The new or updated object in a project trigger monitors a BIM 360 project
  folder you specify for newly created or updated objects.
---

# BIM 360 - New or updated object in a project trigger

The **New or updated object in a project** trigger monitors a BIM 360 project folder you specify for newly created or updated objects.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the type of object you plan to monitor. |
| Hub name | Select the hub that contains the project you plan to monitor. |
| Project name | Select the project you plan to monitor. |
| When first started, this recipe should pick up events from | Set the date and time to start capturing trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The **New or updated object in a project** trigger's output fields vary based on your selected **Object** type. Refer to BIM 360's [API guide](https://aps.autodesk.com/en/docs/bim360/v1/reference/http/) for more information on BIM 360 objects.
