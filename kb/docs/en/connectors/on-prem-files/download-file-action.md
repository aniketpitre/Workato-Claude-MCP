---
url: 'https://docs.workato.com/en/connectors/on-prem-files/download-file-action.md'
description: >-
  The Download file action in the On-prem files connector lets you download an
  existing on-prem file and return its raw contents, with file streaming
  support.
---

# On-prem files - Download file action

The **Download file** action downloads an existing on-prem file. The output of this action is the file's raw contents and supports [file streaming](/en/features/file-streaming).

## Input

| Input field | Description |
| --- | --- |
| File | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) to the file to download. Only files can be downloaded. |
| File encoding | Optional. Select the file's encoding type. Select **Auto-Detect** to automatically recognize encoding based on the file's content. |
| Chunk size (KB) | Optional. Define the chunk size for streaming file contents. The minimum value is 32 KB, and the maximum is 10 MB. This field defaults to 32 KB if left blank. |

## Output

| Output field | Description |
| --- | --- |
| File contents | The contents of the file, which can be used in other actions. This datapill supports [file streaming](/en/features/file-streaming) for working with large files. |

---
