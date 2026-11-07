---
url: >-
  https://docs.workato.com/en/connectors/google-drive/action-remove-permissions.md
description: Removes a permission associated with a file you specify in Google Drive.
---

# Google Drive - Remove file permission action

This action removes a permission associated with a given file in Google Drive. Permission details include the file's ownership and whether the file is shared with additional users, groups, or domains, or is accessible to anyone.

![Google Drive Remove file permission action](/assets/google-drive-remove-permission.Qqca5RhN.png) _Google Drive Remove file permission action_

## Input

| Input field | Description |
| --- | --- |
| File | The file with the permission you plan to remove. Select a file or enter its ID. To find the file ID, right-click the file and select **Share > Copy link**. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file ID in the output of other Google Drive triggers and actions. |
| Permission | The permission you plan to remove. Select a permission or enter its ID. The permission ID can be obtained from the [List permissions](/en/connectors/google-drive/action-list-permissions) action. |

## Output

| Output field | Description |
| --- | --- |
| Success | **True** if the permission was successfully removed. |
