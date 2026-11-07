---
url: 'https://docs.workato.com/en/connectors/on-prem-files/list-files-action.md'
description: >-
  The List files in folder batch action in the On-prem files connector lets you
  list all files in an on-prem folder, sorted alphabetically by path.
---

# On-prem files - List files in folder action (Batch)

The **List files in folder** batch action lists all files in the on-prem folder you select. Files are returned in a flat list and sorted in alphabetical order by file path.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the parent folder to list files from. |
| Include files in sub-folders? | Select an option to determine whether files in sub-folders are included or not. Note that files are returned in a flat alphabetical list, instead of a directory. |
| Filter files by name | Optional. Define a [naming pattern](/en/connectors/on-prem-files#naming-pattern) that files must use to trigger a job. |

## Output

| Output field | Description |
| --- | --- |
| File path | The path of the current file, relative to the [base path](/en/connectors/on-prem-files#relative-path) defined in your connection profile. For example: `/my-profile/path/report.csv`. |
| File name | The name of the file, including its extension. |
| File size (bytes) | The size of the file contents in bytes. |
| Created time | The time the file was created. This value is set by your OS. |
| Last modified time | The time the file was last modified. This value is set by your OS. |
| List size | The total number of files in the list. |
| List index | The index of the current file within the list. |

---
