---
url: >-
  https://docs.workato.com/en/features/filestorage/generate-shareable-link-action.md
description: >-
  Reference for the Workato FileStorage Generate shareable file link action,
  including scope, file path, and expiry input and output fields.
---

# Workato FileStorage - Generate shareable file link action

This action allows you to create a temporary authenticated URL that you can share externally for a file in [Workato FileStorage](/en/features/workato-filestorage). A third party can use this URL to download, upload, or append contents to the file for a duration you specify.

![Generate shareable link to file in FileStorage action](/assets/filestorage-generate-shareable-link.CrBURNN3.png) _Generate shareable link to file in FileStorage action_

> **FILE AND DIRECTORY ACCESS**
> 
> Currently, all users in a workspace can access all FileStorage files and directories in the workspace when they use the [FileStorage connector](/en/features/filestorage/filestorage-connector). Workato does not restrict access based on role unless the files are accessed from the [FileStorage UI](/en/features/filestorage/filestorage-console#rbac).

## Input

| Field | Description |
| --- | --- |
| Scope | Choose the action that users can execute: **Upload**: Allow users to upload data to create a new file. Does not work on an existing file., **Download**: Allow users to download an existing file., **Append**: Allow users to append data to an existing file. |
| File name | Required if **Scope** is set to **Upload**. Enter the name of the file to be created. |
| File path | Choose a file or enter the full path of the file to be shared (for example: `samplepath/path1`). If the path does not exist, the action returns an error. |
| Expires in | Specify the length of time after which the shareable link expires. Defaults to `900` seconds (15 minutes) if not specified. Maximum is `604800` seconds (7 days). |

## Output

| Field | Description |
| --- | --- |
| Shareable link | The URL from which the file can be uploaded, downloaded, or appended, depending on the scope you select. |
| File path | The complete path of the file being shared. |
| Expires in (seconds) | The length of time in seconds after which the shareable link expires. |
