---
url: 'https://docs.workato.com/en/connectors/ftp/list-files-directories-action.md'
description: >-
  This action retrieves the first level of a directory from the connected
  server.
---

# FTP/FTPS - List files and directories action

The **List files and directories** action retrieves the first level of a directory from the connected server.

## Input

| Input field | Description |
| --- | --- |
| Directory | Provide the full path of the directory to retrieve. For example, `root_directory/sample`. |
| Include files | Optional. Select whether to return files in addition to directories. Defaults to `Yes`. |

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the file or directory. |
| Full path | The full path of the file or directory. |
| Directory | Indicates whether the entry is a directory. This returns `false` for files and `true` for directories. |
| Size | The size of the file in bytes. |
| Permissions | The permissions associated with the file or directory. |
| Owner | The owner of the directory or file. |
| Group | The group associated with the directory or file. |
| Modification time | The time the file or directory was last modified. |

---
