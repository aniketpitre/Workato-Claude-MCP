---
url: 'https://docs.workato.com/en/connectors/ftp/download-large-file-action.md'
description: The Download large file action retrieves a large file from your server.
---

# FTP/FTPS - Download large file action

The **Download large file** action retrieves a file from your server. This action uses [file streaming](/en/features/file-streaming) to support files larger than those supported by the [Download file action](/en/connectors/ftp/download-file-action).

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the full path of the file, including the file extension. For example, `/directory1/file1.txt`. This field is case-sensitive. |
| Encoding of file content | Optional. Select how the file is encoded. If left blank, the encoding is detected automatically. |

## Output

| Output field | Description |
| --- | --- |
| File contents | The contents of the file in binary format. |
| Detected encoding | The detected encoding of the file content. |
| Size | The size of the file in bytes. |

---
