---
url: >-
  https://docs.workato.com/en/connectors/bim360/new-or-updated-document-in-a-project-folder-and-subfolders-trigger.md
description: >-
  The new or updated document in a project folder and subfolders trigger
  monitors a BIM 360 project folder and its sub-folders for newly created or
  updated documents.
---

# BIM 360 - New or updated document in a project folder and subfolders trigger

The **New or updated document in a project folder and subfolders** trigger monitors a BIM 360 project folder and its sub-folders for newly created or updated documents.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project folder you plan to monitor. |
| Project name | Select the project that contains the project folder you plan to monitor. |
| Folder | Select the project folder you plan to monitor. This trigger also monitors the folder's sub-folders. |
| When first started, this recipe should pick up events from | Set the date and time to start capturing trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the document. |
| Project ID | The BIM 360 ID of the project that contains the document. |
| Folder ID | The BIM 360 ID of the folder that contains the document. |
| Item ID | The BIM 360 ID of the document. |
| Item type | The document's type. |
| Attributes | Contains information about the document's attributes, such as their `Name` an `Created at` date. |
| Links | Contains information about the document's link, such as its `Href`. |
| Relationships | Contains information about the document's relationships, such as their `Thumbnails` and `Links`. |
