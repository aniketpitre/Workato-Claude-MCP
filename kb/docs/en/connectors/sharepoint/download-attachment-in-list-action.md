---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/download-attachment-in-list-action.md
description: >-
  The download attachment action in the SharePoint connector lets you download
  an attachment from an item you specify in a list.
---

# SharePoint - Download attachment in SharePoint list action (file)

This action downloads an attachment from a specified item in a SharePoint list.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list to download the attachment from. |
| Item ID | Provide the ID of the item from which the attachment is downloaded. This can be found in the url of items page. |
| File name | Provide the name of the file you plan to download. |
| Encoding of the file content | Specify the encoding of the file to set it explicitly. By default, Workato sets the encoding to UTF-8 if left blank. Learn more about the [encodings Workato supports](https://en.wikibooks.org/wiki/Ruby_Programming/Encoding). |

## Output

The output datatree contains the content of the downloaded attachment.

| Field | Description |
| --- | --- |
| Content | The content of the downloaded file. |
