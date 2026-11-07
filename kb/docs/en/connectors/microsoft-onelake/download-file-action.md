---
url: >-
  https://docs.workato.com/en/connectors/microsoft-onelake/download-file-action.md
description: >-
  The Download file action downloads the contents of an existing file from
  Microsoft OneLake storage.
---

# Microsoft OneLake - Download file action

The **Download file** action downloads the contents of an existing file from Microsoft OneLake storage. Subsequent recipe steps can use the file contents to upload the file into another app.

There is no fixed limit on file size. The maximum file size depends on whether the download can finish within the [job timeout limit](/en/recipes/jobs#timeouts).

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the ID of the workspace where the lakehouse is located. |
| Lakehouse ID | Enter the ID of the lakehouse where the file is located. |
| File path | Specify the path of the file. |

## Output

| Output field | Description |
| --- | --- |
| Contents | File contents of the downloaded file. |
| Name | Name of the file with its extension. |
| File size | Size of the file. |
