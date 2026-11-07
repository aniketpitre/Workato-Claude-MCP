---
url: 'https://docs.workato.com/en/features/filestorage/create-directory-action.md'
description: >-
  Reference for the Workato FileStorage Create directory action, including
  directory name and path input fields and output fields.
---

# Workato FileStorage - Create directory action

This action creates a new directory in [Workato FileStorage](/en/features/workato-filestorage). Directories are useful for grouping similar files. For example, you could group all marketing files under one directory called `marketing` or store all August sales data files within the directory path `sales/august`.

![Create directory in FileStorage action](/assets/filestorage-create-directory.DmxyfKrf.png) _Create directory in FileStorage action_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| Directory name | Enter the name of the directory that you plan to create. |
| Directory path | Choose or enter the path where this directory resides. If the path contains missing parent directories, they are created automatically. |

## Output

| Field | Description |
| --- | --- |
| Directory path | The full path of the created directory. |

---
