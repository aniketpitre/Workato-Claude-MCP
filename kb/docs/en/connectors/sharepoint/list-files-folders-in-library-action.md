---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/list-files-folders-in-library-action.md
description: >-
  The list files and folders action in the SharePoint connector lets you list
  all files and folders within a folder you specify in a library.
---

# SharePoint - List files and folders within a folder in SharePoint library action (batch)

This action lists all files and folders within a specified folder in SharePoint library.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Folder | Specify the folder to list files and folders from. |

## Output

The output datatree contains the details of the files and folders within the specified folder.

| Field | Description |
| --- | --- |
| ID | The unique identifier for the file or item. |
| Name | The name of the file or item, including its extension. |
| Server relative URL | The URL of the file or item relative to the SharePoint site collection root. |
| Exists | Indicates whether the file or item exists (true/false). |
| Type | The type of the file or item. |
| Edit link | The URL to edit the file or item. |
| Check in comment | Comment associated with the last check-in operation. |
| Check out type | Type of check-out (if checked out). |
| Content tag | Tag associated with the content of the file or item. |
| Customized page status | Status indicating if the page is customized. |
| E tag | Entity tag for the file or item. |
| IRM enabled | Indicates whether Information Rights Management (IRM) is enabled. |
| Length | Size of the file in bytes. |
| Level | Security level of the file or item. |
| Major version | Major version number of the file or item. |
| Minor version | Minor version number of the file or item. |
| Linking URI | URI used for linking to the file or item. |
| Linking URL | URL used for linking to the file or item. |
| Time created | Date and time when the file or item was created. |
| Time last modified | Date and time when the file or item was last modified. |
| Title | Title or name of the file or item. |
| UI version | User Interface (UI) version of the file or item. |
| UI version label | Label associated with the UI version. |
| Unique ID | Unique identifier of the file or item. |
| Name | The name of the file or item (repeated). |
| Server Relative URL | The URL of the file or item relative to the SharePoint site collection root (repeated). |
| Exists | Indicates whether the file or item exists (true/false) (repeated). |
| Item count | Number of items in the list or library. |
| Time created | Date and time when the item was created (repeated). |
| Time last modified | Date and time when the item was last modified (repeated). |
| Prog ID | Programmatic identifier (ProgID) of the file or item. |
| Welcome page | Status indicating if the page is a welcome page. |
| Is WOPI enabled | Indicates whether Web Application Open Platform Interface (WOPI) is enabled. |
| List size | Size of the list in bytes. |
| List index | Index position of the item in the list. |
