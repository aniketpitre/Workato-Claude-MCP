---
url: 'https://docs.workato.com/en/connectors/egnyte/download-file-action.md'
description: >-
  The Download file action in the Egnyte connector lets you download a file from
  a specified path in Egnyte using a configurable chunk size.
---

# Egnyte - Download file action

The **Download file** action allows you to download a file from Egnyte.

![Download file action](/assets/download-file-action.BqLvjC3S.png)_Download file action_

## Input

| Input field | Description |
| --- | --- |
| File path | Select the file path of the file you plan to download. |
| Chunk size | Enter the chunk size to determine the units of information to be processed in a given amount of time. The default chunk size is 10MB. Accepted chunk sizes range from 32KB to 10MB. |

## Output

| Output field | Description |
| --- | --- |
| Content | The content description, indicating how content is read. For example: `content read 10485760 bytes at a time`. |

---
