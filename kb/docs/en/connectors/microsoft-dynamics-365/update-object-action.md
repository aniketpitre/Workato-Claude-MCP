---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/update-object-action.md
description: >-
  The Update object action in the Microsoft Dynamics 365 connector lets you
  update an existing record for a specified object using its ID.
---

# Microsoft Dynamics 365 - Update object action

This action updates an existing record for a specified object in Microsoft Dynamics 365 using its ID.

## Input

| Field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| ID | Dynamics ID of the record to update. |
| Object Fields | Fields of the object that you plan to update. |

## Output

The output datatree contains the version number and details of the updated object. Each field corresponds to the attributes of the object in Microsoft Dynamics 365.

| Field | Description |
| --- | --- |
| Version number | Version number of the updated object. |
