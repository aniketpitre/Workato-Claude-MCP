---
url: 'https://docs.workato.com/en/connectors/box/action-download-file.md'
description: >-
  The Download file action downloads the contents of a file from Box. You can
  use the file contents in subsequent steps, such as uploading to another
  application.
---

# Box - Download file action

The **Download file** action downloads the contents of a file from Box. You can use the downloaded file contents in later steps of a recipe, such as uploading the file into another application.

## Input

| Input field | Description |
| --- | --- |
| File ID | Enter the ID of the file to download. You can find the file ID in the output of other Box triggers and actions, or at the end of the file URL in Box. |
| Chunk size | Enter the size of the chunks to stream the file contents. Valid units are `B`, `KB`, and `MB`. The default is **10 MB**. The minimum is **32 KB** and the maximum is **10 MB**. A larger chunk size increases throughput but may exceed API quotas. |
| Encoding of the file content | Select the encoding for the file content. By default, the encoding is **UTF-8**. |

## Output

| Output field | Description |
| --- | --- |
| File contents | Binary contents of the file. You can upload this output to other applications. File contents stream in chunks when used in subsequent steps. |

---
