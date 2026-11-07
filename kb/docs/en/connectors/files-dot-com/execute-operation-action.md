---
url: >-
  https://docs.workato.com/en/connectors/files-dot-com/execute-operation-action.md
description: The Execute operation action executes file operations in Files.com.
---

# Files.com - Execute operation action

The **Execute operation** action executes file operations in Files.com.

## Input

| Input field | Description |
| --- | --- |
| Operation | Select the file operation to execute. Available operations include `Copy file/folder`, `Move file/folder`, `Extract ZIP file`, and `Create ZIP file`. |
| Path | Enter the current path to the file or folder. For example: `folder/file.txt` |
| Destination | Enter the destination path for the file or folder. For example: `folder/file.txt` |
| Overwrite | Select whether to overwrite existing file(s) in the destination file or folder. |
| Structure | Select `Yes` to copy the structure only, without file contents. Select `No` to copy both the structure and file contents. |

## Output

| Output field | Description |
| --- | --- |
| Status | A message indicating the status of the operation, such as `pending`. |
| File migration ID | A unique ID assigned to the file on which the operation was performed. |
