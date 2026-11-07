---
url: 'https://docs.workato.com/en/features/filestorage/rename-move-file-action.md'
description: >-
  Use the Rename/move file action to rename a file or move it to a new
  destination directory in Workato FileStorage.
---

# Workato FileStorage - Rename/move file action

This action allows you to rename a file or move a file to a new destination in [Workato FileStorage](/en/features/workato-filestorage).

![Rename/move file in FileStorage action](/assets/filestorage-rename-move-file.BUfkQJtN.png) _Rename/move file in FileStorage action_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| Source file path | Choose or enter the full path of the source file you plan to move or rename (for example: `directory1/directory2/filename`). Note that the file must exist in the path, or the action returns an error. |
| Destination directory path | Choose or enter the directory path where you plan to move the file. To rename the file, provide the same directory path as in the source (for example: `directory1/directory2`). |
| Destination file name | Enter the destination file name. To move the file, you can provide either the same name or a different name for the destination file. |

## Output

| Field | Description |
| --- | --- |
| Source file path | The complete path of the original file. |
| Destination file path | The complete path of the newly renamed or moved file. |

---
