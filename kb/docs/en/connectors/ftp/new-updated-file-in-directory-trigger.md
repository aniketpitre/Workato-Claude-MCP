---
url: >-
  https://docs.workato.com/en/connectors/ftp/new-updated-file-in-directory-trigger.md
description: This trigger monitors a server directory for new or updated files.
---

# FTP/FTPS - New/updated file in directory trigger

The **New/updated file in directory** trigger monitors an FTP or FTPS directory for new or updated files. Jobs are only triggered from CSV files located at the first level of the directory.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the full path of the directory to monitor. For example, `/user/personal_folder/`. |
| From | Select the date and time from which to start monitoring for new or updated files. Defaults to one hour ago if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Name | The name of the file. |
| Full path | The full path of the file. |
| Directory | Indicates whether the entry is a directory. This returns `false` for files and `true` for directories. |
| Size | The size of the file in bytes. |
| Permissions | The permissions associated with the directory or file. |
| Owner | The owner of the directory or file. |
| Group | The group associated with the directory or file. |
| Modification time | The time the file or directory was last modified. |
