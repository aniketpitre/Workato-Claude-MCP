---
url: >-
  https://docs.workato.com/en/connectors/azure-file-storage/search-files-and-directories-action.md
description: >-
  The Search files and directories action lists the files and directories under
  a directory path in Azure File Storage.
---

# Azure File Storage - Search files and directories action

The **Search files and directories** action lists the files and directories under a directory path in Azure File Storage. You can filter results by name prefix and page through large listings using the returned next page value.

## Input

| Input field | Description |
| --- | --- |
| Directory path | Enter the path to the directory you plan to list. For example, `hrdata/reports`. Leave empty to list the root of the file share. |
| Prefix | Enter a prefix the search to limit files and directories whose names begin with the specified prefix. |
| Page size | Enter the maximum number of files or directories to return. Default and maximum is `5000`. |

## Output

| Output field | Description |
| --- | --- |
| Entries | List of files and directories found under the directory path, including type, name, file ID, content length, timestamps, ETag, attributes, and permission key for each entry. |
| Directory ID | Unique identifier of the searched directory. |
| Next page | Value to use in the **Page** input field to retrieve the next page of results. |
