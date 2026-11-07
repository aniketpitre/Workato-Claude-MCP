---
url: 'https://docs.workato.com/en/connectors/box/trigger-new-folder-in-folder.md'
description: >-
  The New/updated folder in folder trigger starts a recipe when a new folder is
  added or an existing folder is updated in a specified Box folder.
---

# Box - New/updated folder in folder trigger

The **New/updated folder in folder** trigger starts a recipe when a new folder is added, or when an existing folder is updated, deleted, restored, moved, or copied in a specified Box folder. The trigger also detects modifications to folder contents, such as when a new file is added or an existing file is updated.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Select the date and time to begin monitoring the folder. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Folder | Select the folder to monitor. You can select from the drop-down menu or enter a folder ID. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique ID of the folder. |
| Name | Folder name. |
| Type | The object type. |
| Description | Folder description. |
| Size | Folder size in bytes. |
| Shared link | Shared link details for the folder. |
| Created at | Date and time the folder was created. |
| Modified at | Date and time the folder was last modified. |

---
