---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/rename-directory-action.md
description: >-
  The Rename directory action renames an existing directory within the same file
  share in Azure File Storage.
---

# Azure File Storage - Rename directory action

The **Rename directory** action renames an existing directory within the same file share in Azure File Storage. The source directory must exist, and the destination directory must not already exist unless you enable **Replace if exists**.

## Input

| Input field | Description |
| --- | --- |
| Source path | Enter the path of the existing directory to rename. For example, `hrdata/old_reports`. |
| Destination path | Enter the new path for the directory. For example, `hrdata/new_reports`. The destination must not already exist unless **Replace if exists** is enabled. |
| Replace if exists | Enable to overwrite the existing destination. |
| Ignore read-only | Enable to rename only if the destination has the read-only attribute. Requires **Replace if exists** to also be true. |
| Metadata | Specify key-value metadata pairs to set on the renamed directory. Each call replaces all existing metadata. Keys must follow C# identifier naming rules. |
| Headers | Specify HTTP request headers to customize file permissions, attributes, timestamps, lease validation, client request tracking, and trailing dot behavior. |

## Output

| Output field | Description |
| --- | --- |
| Status code | HTTP status code of the operation. |
| Response headers | HTTP response headers including ETag, last modified, file creation time, last write time, permission key, attributes, file ID, parent ID, and request ID. |
