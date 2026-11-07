---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-updated-object-trigger-real-time.md
description: >-
  The New or updated object real-time trigger in the Microsoft Dynamics 365
  connector runs immediately when a record is created or updated.
---

# Microsoft Dynamics 365 - New or updated object trigger (real-time)

The New or updated object trigger (real-time) runs immediately when a record is created or updated in Microsoft Dynamics 365.

## Input

| Field | Description |
| --- | --- |
| Event name | Use a unique name to generate webhook URL. |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |
| When first started, this recipe should pick up events from | Specify the date and time to start processing events. This value can't be changed after you run or test the recipe. |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the changed object, including the fields specified in the output fields. |
