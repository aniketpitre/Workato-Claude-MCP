---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/new-object-trigger-real-time.md
description: >-
  The New object real-time trigger in the Microsoft Dynamics 365 connector fires
  immediately when a record is created in Microsoft Dynamics 365.
---

# Microsoft Dynamics 365 - New object trigger (real-time)

The New Object trigger (real-time) in Microsoft Dynamics 365 triggers immediately when a record is created in Microsoft Dynamics 365.

## Input

| Field | Description |
| --- | --- |
| Event name | Use a unique name to generate webhook URL. |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| From | Fetch object from the specified time. |
| Output fields | Select the fields of the selected objects you plan to use in your recipe. All fields are returned if left blank. |

## Output

| Field | Description |
| --- | --- |
| Change details | This contains information about the new object, including the fields specified in the output fields. |
