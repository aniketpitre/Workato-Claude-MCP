---
url: 'https://docs.workato.com/en/features/filestorage/new-file-trigger.md'
description: >-
  Trigger Workato recipes in real time when a new file is created or uploaded to
  a monitored directory in Workato FileStorage.
---

# Workato FileStorage - New file trigger (real-time)

This trigger is initiated immediately, in real time, when a new file is created or uploaded to a specified directory in [Workato FileStorage](/en/features/workato-filestorage). The trigger can be paired with both streaming and non-streaming actions (for small volume data).

![New file in FileStorage trigger](/assets/filestorage-new-file.2CDNo3-b.png) _New file in FileStorage trigger_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it retrieves files created after the specified date and time. Leave this field empty to retrieve files created one hour ago. After you test or run the recipe, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Directory path to monitor | Choose or enter the directory path to monitor (for example, `directory1/directory2/`). |
| Include subdirectories? | Whether to monitor subdirectories within the specified directory path. By default, the recipe monitors only the specified directory. |

## Output

| Field | Description |
| --- | --- |
| File name | Name of the new file. |
| File path | Path of the new file. |
| File contents | Full contents of the new file. This is a [streaming object](/en/features/file-streaming). |
| File size (bytes) | Size of the new file in bytes. |

---
