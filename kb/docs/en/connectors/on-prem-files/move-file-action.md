---
url: 'https://docs.workato.com/en/connectors/on-prem-files/move-file-action.md'
description: >-
  The Move file action in the On-prem files connector lets you move an existing
  on-prem file to a destination folder you specify.
---

# On-prem files - Move file action

The **Move file** action moves an on-prem file to a folder you specify. The file and destination folder must already exist for this action to work.

## Input

| Input field | Description |
| --- | --- |
| File | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the file to move. Only files can be moved. |
| Destination folder | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the destination folder to move the file to. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the file, including its extension. |
| File path (original) | The original path of the file, relative to the [base path](/en/connectors/on-prem-files#relative-path) defined in your connection profile. |
| File path (new) | The new path of the file, relative to the [base path](/en/connectors/on-prem-files#relative-path) defined in your connection profile. |
| File size (bytes) | The size of the file in bytes. |
| Created time | The time the file was created. This value is set by your OS. |
| Last modified time | The time the file was last modified. This value is set by your OS. |

---
