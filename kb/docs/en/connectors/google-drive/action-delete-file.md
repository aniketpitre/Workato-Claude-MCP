---
url: 'https://docs.workato.com/en/connectors/google-drive/action-delete-file.md'
description: Deletes a file from Google Drive
---

# Google Drive - Delete file action

Delete a file from Google Drive. Note that this action deletes the file **permanently**. The file is _not_ placed in trash where it can be restored for a set period of time.

![Google Drive Delete file action](/assets/google-drive-delete-file.CSINTegc.png) _Google Drive Delete file action_

## Input

| Output field | Description |
| --- | --- |
| File | The file you plan to delete. Select a file or enter its ID. To find the file ID, right-click the file and select **Share > Copy link**. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file ID in the output of other Google Drive triggers and actions. |

## Output

| Output field | Description |
| --- | --- |
| Success | **True** if the file was successfully deleted. |

---
