---
url: 'https://docs.workato.com/en/connectors/smb/download-file-action.md'
description: >-
  The Download file action in the SMB connector lets you download a file from
  your network share in binary mode using file streaming for use downstream.
---

# SMB - Download file action

This action downloads a file from your SMB network share in binary mode. The file contents can be used in downstream recipe steps. This action cannot be used to download entire folders.

To process this action, Workato splits the file contents into chunks and downloads them across separate requests in a technique called [file streaming](/en/features/file-streaming). The time it takes to process the action depends on the file size and the download speed.

The default chunk size is set to 5 MB. You can change the chunk size to increase the download speed if your connection is stable. The maximum chunk size is 100 MB.

## Input

| Input field | Description |
| --- | --- |
| File | Provide the full path of the file, including the file name and extension, for example: `/folder1/folder2/filename.csv` |
| Chunk size | Select the chunk size. The default is 5 MB and the maximum is 100 MB. |

## Output

| Output field | Description |
| --- | --- |
| File content | The size of the file in bytes. |
| Path | The full path of the file, including the file name and extension, for example: `/folder1/folder2/filename.csv`. |
| Directory name | The complete path of the file, for example: `/folder1/folder2/`. |
| File name | The name of the downloaded file. |
| Size | The size of the downloaded file. |
| Attributes | Attributes of the downloaded file. |
| Kind | Indicates whether this item is a file. |
| Creation time | The time the file was created. |
| Change time | The time the file was last changed. |
| Access time | The time the file was accessed. |

---
