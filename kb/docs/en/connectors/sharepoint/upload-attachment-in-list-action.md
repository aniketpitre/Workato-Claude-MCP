---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/upload-attachment-in-list-action.md
description: >-
  The upload attachment action in the SharePoint connector lets you upload an
  attachment to an item you specify in a list.
---

# SharePoint - Upload attachment in SharePoint list action (file)

This action uploads an attachment to a specified item in a SharePoint list.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list to which to upload the attachment. |
| Item ID | Provide the ID of the item to which the attachment is uploaded. |
| File name | Provide the name of the file you plan to upload. |
| Content | Provide the content of the file you plan to upload. |

## Output

The output datatree contains the details of the uploaded attachment.

| Field | Description |
| --- | --- |
| File name | The name of the uploaded file. |
| File name as path | The path of the uploaded file. |
| Server relative path | The server relative path of the uploaded file. |
| Server relative URL | The server relative URL of the uploaded file. |
