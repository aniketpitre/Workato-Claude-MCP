---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/delete-file-folder-from-library-action.md
description: >-
  The delete file or folder action in the SharePoint connector lets you delete a
  file or folder from a library you specify.
---

# SharePoint - Delete file or folder from SharePoint library action

This action deletes a file or a folder from a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| File or Folder | Select the file or folder you plan to delete. |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Folder | Select the folder you plan to delete. Alternatively, you can provide the site relative URL. For example, `/sites/sitename/documentlibrary/foldername`. |
| File name | Select the file to delete. |

## Output

The output datatree contains the status of the delete operation.

| Field | Description |
| --- | --- |
| Status | Indicates the status of the delete operation. |
