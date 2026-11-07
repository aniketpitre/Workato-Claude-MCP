---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/create-directory-action.md
description: >-
  The Create directory action creates a new directory in Azure File Storage
  under a specified share or parent directory.
---

# Azure File Storage - Create directory action

The **Create directory** action creates a new directory in Azure File Storage under a specified share or parent directory. The parent directory must already exist, and you can't create a directory hierarchy in a single action.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the path to the directory you plan to create. For example, `hrdata/reports/2025`. The parent directory must already exist. |
| Creation time | Enter the UTC creation time for the directory. Leave empty to use the current time. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including ETag, last modified, file creation time, last write time, permission key, attributes, file ID, parent ID, and request ID. |
