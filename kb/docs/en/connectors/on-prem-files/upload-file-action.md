---
url: 'https://docs.workato.com/en/connectors/on-prem-files/upload-file-action.md'
description: >-
  The Upload file action in the On-prem files connector lets you upload a file
  to an existing on-prem folder, with support for large file sizes.
---

# On-prem files - Upload file action

The **Upload file** action uploads a file to an existing on-prem folder.

> **LEGACY ACTION**
> 
> The On-prem files connector has both **Upload file** and **Upload file (Legacy)** actions:
> 
> - The **Upload file** action supports large file sizes and requires an agent version 2.10.2 or later.
> - The **Upload file (Legacy)** action does not support large file sizes and requires an agent version 2.4.2 or later.

## Input

| Input field | Description |
| --- | --- |
| Folder | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the folder to upload the file to. |
| File name | Enter the name of the file to upload, including its extension. |
| File contents | Input a File contents datapill or enter the file contents directly. This input field supports [streaming](/en/features/file-streaming). |
| Overwrite existing file? | Select whether to replace the contents of existing files with the same name and extension. If you select **No**, a new file is created with an incremental number appended to the filename, for example: `report_1.csv`, `report_2.csv`, `report_3.csv`. |

## Output

| Output field | Description |
| --- | --- |
| File path | The path of the file, relative to the [base path](/en/connectors/on-prem-files#relative-path) defined in your connection profile. For example: `/my-profile/path/uploaded-file.csv`. |
| File name | The name of the file, including its extension. |
| File size (bytes) | The size of the file contents in bytes. |
| Created time | The time the file was created. This value is set by your OS. |
| Last modified time | The time the file was last modified. This value is set by your OS. |
| File existed before upload? | Indicates whether the action replaced the contents of a file with the same name and extension in the selected folder. |

---
