---
url: 'https://docs.workato.com/en/connectors/ftp/get-file-information-action.md'
description: >-
  The Get file information action retrieves information about a file in the
  connected server.
---

# FTP/FTPS - Get file information action

The **Get file information** action retrieves information about a file in the connected server. This action fails if the file isn't found.

## Input

| Input field | Description |
| --- | --- |
| File name | Enter the full path, including the file extension, of the file to retrieve. For example, `/user/personal_folder/file name.txt`. This field is case-sensitive. |

## Output

| Output field | Description |
| --- | --- |
| Size | The size of the file in bytes. |
| Type | The type of the file, such as `file` or `directory`. |
| Last modified | The time the file was last modified. |

---
