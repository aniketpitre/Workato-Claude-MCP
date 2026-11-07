---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/deleted-object-trigger.md
description: >-
  The Deleted object trigger in the Microsoft Dynamics 365 connector picks up
  deleted objects each polling interval when auditing is enabled.
---

# Microsoft Dynamics 365 - Deleted object trigger

This trigger checks for deleted objects in Microsoft Dynamics 365 after a specified interval lapses and processes each deleted object as a single trigger event. You must enable **Auditing** for Lead to use this trigger. You can enable auditing by visiting **Lead view page > Customize Entity > Enable Auditing**.

## Input

| Field | Description |
| --- | --- |
| Object | Select a standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| When first started, this recipe should pick up events from | Specify the date and time to start processing events. This value can't be changed after you run or test the recipe. |

## Output

| Field | Description |
| --- | --- |
| ID | The ID of the deleted object. |
| Deleted time | The time when the object was deleted. |
