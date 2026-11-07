---
url: 'https://docs.workato.com/en/features/filestorage/delete-directory-action.md'
description: >-
  Reference for the Workato FileStorage Delete directory action, including the
  directory path input field and output fields.
---

# Workato FileStorage - Delete directory action

This action deletes a directory in [Workato FileStorage](/en/features/workato-filestorage).

![Delete directory in FileStorage action](/assets/filestorage-delete-directory.DV_YLtSc.png) _Delete directory in FileStorage action_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| Directory path/Select file | Choose a directory or enter the full path (for example, `samplepath/dirname`) of the directory you plan to delete. |

## Output

| Field | Description |
| --- | --- |
| Directory path | Complete path of the deleted directory. |

---
