---
url: 'https://docs.workato.com/en/features/filestorage/search-files-action.md'
description: >-
  Use the Search files action to find files matching a name condition across
  directories and subdirectories in Workato FileStorage.
---

# Workato FileStorage - Search files action

This action searches directories and subdirectories in [Workato FileStorage](/en/features/workato-filestorage) and returns a list of files with names that match a specified condition. This is useful for grouping and processing files. The action supports pagination to retrieve large lists of files.

If you select a directory but do not specify a condition to match, the action lists all files under a directory and its subdirectories.

![Search files in FileStorage action](/assets/filestorage-search-files.2qxRBLRb.png) _Search files in FileStorage action_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| Directory path/File path | Choose or enter the path of the directory to search for matching files (for example: `samplepath/path1/`). Subdirectories are also included in the search. |
| File name | Choose the criteria by which matching filenames are returned: **Condition:** The condition used to match a provided value. Defaults to **Equals** if not specified., **Value:** The value to match (for example: `invoices`). For example, to return a list of files whose names begin with `2024`, set **Condition** to `Starts with` and set **Value** to `2024`. |
| Page size | Specify the number of files to fetch in a single set. Defaults to `50` if not specified. Maximum is `100`. |
| Page offset | Specify the page number to fetch file records from. Defaults to `0`, which represents the first page. |

## Output

| Field | Description |
| --- | --- |
| Page offset | The current page number. |
| Size of the page | Number of records in the current page. |
| Files | A list of files with the following metadata: File name, File path, File size (bytes), File creation time, Last modified time, List size, List index |

---
