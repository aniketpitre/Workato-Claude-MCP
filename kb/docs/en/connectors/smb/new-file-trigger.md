---
url: 'https://docs.workato.com/en/connectors/smb/new-file-trigger.md'
description: >-
  The New/updated file in directory trigger in the SMB connector fires when a
  file is created or updated in the first level of a specified directory.
---

# SMB - New/updated file in directory trigger

This trigger monitors the first level of a specified directory for newly created or updated files.

You can use the [Download file action](/en/connectors/smb/download-file-action) to fetch the contents of the new or updated file.

## Input

| Input field | Description |
| --- | --- |
| Folder path | Select the folder that you plan to monitor. You can select a folder from the drop-down menu or enter a folder path directly. Files in this directory are processed in order based on when they were last modified, from oldest to most recent. |
| When first started, this recipe should pick up events from | The recipe will process files created or updated after this time. If left blank, the default date will be set to **1 hour** before the recipe is first started. Once the recipe has been run or tested, the value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output field | Description |
| --- | --- |
| File path (processed) | The file path. |
| File name (processed) | The name of the file. |
| Content | Number of the bytes that was read. |
| File size (bytes) | The size of the file. |
| Attributes | Attributes attached to the file. |
| Creation time | The time the file was created. |
| Change time | The time the file was last changed. |
| Access time | The time the file was accessed. |

---
