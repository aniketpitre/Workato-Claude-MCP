---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/update-file-in-library-action.md
description: >-
  The update file using file contents action in the SharePoint connector lets
  you replace the content of a file in a library you specify.
---

# SharePoint - Update file in SharePoint using file contents action

This action updates the file content of a file in a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Parent folder | Specify the parent folder containing the file you plan to update. |
| File name | Provide the name of the file you plan to update. |
| File contents | The content of the file to be updated. |

## Output

The output datatree contains the status of the update operation.

| Field | Description |
| --- | --- |
| Status | Indicates the status of the update operation. |
