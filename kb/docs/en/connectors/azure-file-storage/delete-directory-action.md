---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/delete-directory-action.md
description: >-
  The Delete directory action deletes an empty directory from Azure File
  Storage.
---

# Azure File Storage - Delete directory action

The **Delete directory** action deletes an empty directory from Azure File Storage. The directory must be empty before you can delete it.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the path to the directory you plan to delete. For example, `hrdata/reports/2025`. The directory must be empty. |
| Headers | Enter HTTP request headers to customize client request tracking and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including content length, server, request ID, version, and date. |
