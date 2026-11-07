---
url: 'https://docs.workato.com/en/connectors/on-prem-files/rename-file-action.md'
description: >-
  The Rename file action in the On-prem files connector lets you rename an
  existing on-prem file to a new name you specify.
---

# On-prem files - Rename file action

The **Rename file** action renames an existing on-prem file. You can't rename folders with this action.

## Input

| Input field | Description |
| --- | --- |
| File | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the file to rename. Only files can be renamed. |
| New file name | Enter a new name for the file, including its extension. |

## Output

| Output field | Description |
| --- | --- |
| File name | The new name of the file, including its extension. |
| File path | The path of the file, relative to the [base path](/en/connectors/on-prem-files#relative-path) defined in your connection profile. For example: `/my-profile/path/renamed-file.csv`. |
| File size (bytes) | The size of the file contents in bytes. |
| Created time | The time the file was created. This value is set by your OS. |
| Last modified time | The time the file was last modified. This value is set by your OS. |

---
