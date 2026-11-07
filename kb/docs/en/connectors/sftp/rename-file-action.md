---
url: 'https://docs.workato.com/en/connectors/sftp/rename-file-action.md'
description: >-
  The Rename/move file action in the SFTP connector renames a file or moves it
  to a new destination on your SFTP server.
---

# SFTP - Rename/move file action

This action renames a file or moves it to a new destination on the SFTP server. If the file path provided is invalid, the job will fail.

![Rename/move file action](/assets/rename-file-action.p-IddCOd.png)_Rename/move file action_

## Input

| Input field | Description |
| --- | --- |
| Source path | Provide the current full path of the file, including the file name and extension. Example: `/folder1/folder2/filename.csv` |
| Destination path | Provide the new full path of the file, including the file name and extension. To **rename** a file: Provide the same source path with a new file name. Example: `/folder1/folder2/new_filename.csv`, To **move** a file: Make sure the folders in the new path exist. Example: `/folder1/new_folder/filename.csv` |

## Output

| Output field | Description |
| --- | --- |
| Source path | The old full path of the file. |
| Destination path | The new full path of the file. |

To retrieve more details about the file you've just renamed or moved, use the [Get file information](/en/connectors/sftp/get-file-information-action) action.

---
