---
url: 'https://docs.workato.com/en/connectors/smb/delete-action.md'
description: >-
  The Delete resource action in the SMB connector lets you delete a file or
  folder you specify in your network location, including files in subfolders.
---

# SMB - Delete resource action

This action deletes a file or folder you specify in your SMB network location.

## Input

| Input field | Description |
| --- | --- |
| Resource to delete | Provide the full path of the folder or file to delete, for example: `/folder1/folder2` |
| Include files in sub-folders? | Select whether to also delete files in sub-folders. |

## Output

| Output field | Description |
| --- | --- |
| Path | The name of the deleted file or folder, including the file name and extension, for example: `/folder1/folder2/filename.csv`. |
| Kind | Indicates whether this item is a folder. |
| Size | The size of the deleted resource. |
| Attributes | Attributes attached to the deleted resource. |
| Name | The name of the deleted resource. |
| Directory | The complete path of the deleted resource, for example: `/folder1/folder2/`. |
| Creation time | The time the resource was deleted. |
| Change time | The time the resource was last changed. |
| Access time | The time the resource was accessed. |

---
