---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/get-file-contents-action.md
description: >-
  The Get file contents action enables you to download the contents of an
  existing file from Azure File Storage.
---

# Azure File Storage - Get file contents action

The **Get file contents** action enables you to download the contents of an existing file from Azure File Storage.

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the path to the file in the share, including the file name. For example, `hrdata/test.csv`. |
| Timeout | Specify the timeout in seconds to wait for the server to complete the operation. |
| Headers | Specify HTTP request headers to customize range, content integrity checks, lease validation, request tracking, and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| File contents | Contents of the file. |
| Response headers | HTTP response headers including cache control, content length, content type, last modified, ETag, and request ID. |
