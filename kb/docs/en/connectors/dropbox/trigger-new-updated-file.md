---
url: 'https://docs.workato.com/en/connectors/dropbox/trigger-new-updated-file.md'
description: >-
  The New/updated file in directory trigger in the Dropbox connector fires when
  a file is added or updated in a folder or its subfolders.
---

# Dropbox - New/updated file in directory trigger

Triggers when a new file is added or existing file is updated in a specified folder. New and updated files in subfolders will also be picked up.

When recipe is first started, picks up files created or updated an hour ago.

![New/updated file in directory](/assets/updated-file-trigger.CxeV8ivQ.png)_New/Updated file in directory trigger_

## Input

| Field name | Description |
| --- | --- |
| Folder / Folder path | The folder to monitor for new/updated files. Sub-folders of this folder will also be monitored. |
| Obtain a direct URL to file | Generate a public URL that lives for 4 hours. This URL can be obtained from the URL datapill in the trigger output. |
| Timestamp | The trigger picks up files on this timestamp. Option between server modified and client modified, defaults to client modified. This value should not be changed once the recipe is tested or run. |

## Output

| Field name | Description |
| --- | --- |
| Path | File path. |
| Bytes | File size in bytes. |
| Size | File size in string format. |
| Mime type | The Mime type of this file. |
| URL | File's public URL. Can be used to download file using the [Workato file connector](/en/features/handling-binary-files#download-file-content-from-public-url). |
| URL expires | Date/time the file's public URL will expire. |
| Rev | A unique identifier for the current revision of the file. |
| Modified | Date/time the file was last modified. |
| Client modified time | This is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not. |

---
