---
url: 'https://docs.workato.com/en/connectors/smb/metadata-action.md'
description: >-
  The Get metadata of resource action in the SMB connector lets you retrieve
  basic details about a file or folder, such as its name, path, and size.
---

# SMB - Get metadata of resource

This action retrieves basic information about a specific file or folder in your SMB location, such as its `name`, `path`, and `size`.

## Input

| Input field | Description |
| --- | --- |
| Path | Provide the full path of the resource including the file name and extension, for example: `/folder1/folder2/filename.csv` |

## Output

| Output field | Description |
| --- | --- |
| Path | The path of the resource, including the file name and extension, for example: `/folder1/folder2/filename.csv`. |
| Size | The size of the resource. |
| Attributes | Attributes of the resource. |
| Kind | Indicates whether this item is a file or folder. |
| Name | Name of the resource. |
| Directory name | The complete path of the resource, for example: `/folder1/folder2/`. |
| Creation time | The time the resource was created. |
| Change time | The time the resource was last changed. |
| Access time | The time the resource was accessed. |

---
