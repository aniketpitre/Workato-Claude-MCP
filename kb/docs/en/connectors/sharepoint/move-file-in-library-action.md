---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/move-file-in-library-action.md
description: >-
  The move file action in the SharePoint connector lets you move a file to a
  specific folder in a library.
---

# SharePoint - Move file in SharePoint library action

This action moves a file to a specific folder in a SharePoint library.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Parent folder | Specify the parent folder containing the file. |
| File name | Specify the name of the file you plan to move. |
| Destination folder | Specify the folder where you plan to move the file. |
| Destination file name | Provide the name for the file in the destination folder. If you leave this field empty, Workato uses the original file name. |
| Overwrite existing file? | Determine whether to overwrite the existing file in the destination folder. |

## Output

The output datatree contains the status of the move operation.

| Field | Description |
| --- | --- |
| Status | Indicates the status of the move operation. |
