---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/monitor-changes-entities-trigger.md
description: >-
  The Monitor changes in entities trigger in the Microsoft Dynamics 365
  connector tracks entity changes using delta links for change-tracked objects.
---

# Microsoft Dynamics 365 - Monitor changes in entities trigger

The Monitor Changes in Entities trigger in Microsoft Dynamics 365 monitors changes in entities using delta links. It is recommended to use this trigger for entities that don't have a modified on timestamp.

## Input

| Field | Description |
| --- | --- |
| Entity | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. Only objects eligible for change tracking are supported. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| Fetch only new changes? | Choose `Yes` to return only changes in the records after the recipe has started. Defaults to `Yes`. Recommended to avoid large number of initial jobs. |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |
