---
url: >-
  https://docs.workato.com/en/connectors/bim360/get-folder-info-in-a-project-action.md
description: >-
  The get folder info in a project action retrieves data about a BIM 360 folder
  you specify.
---

# BIM 360 - Get folder info in a project action

The **Get folder info in a project** action retrieves data about a BIM 360 folder you specify.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the folder you plan to retrieve. |
| Project name | Select the project that contains the folder you plan to retrieve. |
| Folder | Select the folder you plan to retrieve. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the folder. |
| Project ID | The BIM 360 ID of the project that contains the folder. |
| Folder ID | The BIM 360 ID of the folder. |
| Item ID | The BIM 360 ID of the item associated with the folder. |
| Item type | The type of item associated with the folder. |
| Attributes | Contains information about the folder's attributes, such as their `Name` an `Created at` date. |
| Links | Contains information about the folder's link, such as its `Href`. |
| Relationships | Contains information about the folder's relationships, such as their `Links` and `Parent`. |
