---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/delete-file-action.md
description: The Delete file action deletes an existing file from Azure File Storage.
---

# Azure File Storage - Delete file action

The **Delete file** action deletes an existing file from Azure File Storage.

## Input

| Input field | Description |
| --- | --- |
| File path | Enter the path to the file in the share, including the file name. For example, `hrdata/test.csv`. |
| Timeout | Enter the timeout in seconds to wait for the server to complete the operation. |
| Headers | Enter HTTP request headers to customize lease validation, request tracking, and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, server, request ID, version, and date. |
