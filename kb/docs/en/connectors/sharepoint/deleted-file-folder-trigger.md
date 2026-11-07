---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/deleted-file-folder-trigger.md
description: >-
  The Deleted file or folder trigger monitors the SharePoint Recycle Bin for
  newly deleted items.
---

# SharePoint - Deleted file or folder trigger

The **Deleted file or folder** trigger monitors the SharePoint Recycle Bin for newly deleted items. This trigger requires the [Authorization code grant](/en/connectors/sharepoint#authentication-auth-code-grant) connection type.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. Minimum value is five minutes. |
| Site name | Provide the SharePoint site name to connect to. Use the site name from the URL. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, enter `product`. Workato uses the site name from your connection setup if the field is left blank. The base URL is `https://company-name.sharepoint.com/sites`. Enter an absolute URL to override the base URL, such as `https://company-name.sharepoint.com/teams/product`. |
| When first started, this recipe should pick up events from | Specify the timestamp to start monitoring deletions from. Leave blank to start from one hour ago. You can't change this value after running or testing the recipe. |

## Output

| Output field | Description |
| --- | --- |
| Item ID | The unique ID of the deleted file or folder. |
| Title | The title of the deleted file or folder. |
| Deleted Date | The date the file or folder was deleted. |
| Deleted By | The user who deleted the file or folder. |
| Item Type | Indicates whether the item was a file or folder. |
| Directory Name | The name of the directory where the file or folder was located. |
| File/Folder Name | The name of the deleted file or folder. |
| Size (bytes) | The size in bytes of the deleted file or folder. |
