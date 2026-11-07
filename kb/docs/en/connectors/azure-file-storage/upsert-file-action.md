---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/upsert-file-action.md
description: >-
  The upsert file action enables you to create a new file or update an existing
  one with the specified content.
---

# Azure File Storage - Upsert file action

The **Upsert file** action creates a new file or updates an existing file with content you specify in Azure File Storage. The action searches your files and replaces your file content if it finds an existing file. The action creates a new file with the content if it doesn't find an existing file. This action supports files up to **300 MB**.

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the path to the file you plan to upsert. For example, `hrdata/test.csv` |
| File contents | Enter the contents you plan to write to the file. |
| Request headers (create file) | Enter HTTP request headers for the create file operation, such as content length, content type, cache control, and metadata. |
| Request headers (put range) | Select HTTP request headers for the put range operation, such as content MD5, lease ID, file last write time. |

## Output

| Output field | Description |
| --- | --- |
| Create file response | Output of the create file operation. |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, last modified, ETag, and request ID. |
| Put range response | Output of the put range operation. |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, content MD5, last modified, ETag, and request ID. |
