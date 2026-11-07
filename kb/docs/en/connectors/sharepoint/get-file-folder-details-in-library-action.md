---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/get-file-folder-details-in-library-action.md
description: >-
  The get file or folder details action in the SharePoint connector lets you
  retrieve details of a specified file or folder in a library.
---

# SharePoint - Get file or folder details in SharePoint library action

This action retrieves the details of a specified file or folder in a SharePoint library.

## Input

| Field | Description |
| --- | --- |
| File or Folder | Select the file or folder to retrieve details for. |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Folder | Select the folder for which you plan to retrieve the details. Alternatively, you can provide the relative URL of the folder. For example, `/sites/sitename/documentlibrary/foldername`. |
| File name | Select the name of the file for which you plan to retrieve the details. Alternatively, you can provide the relative URL of the file. For example, `/sites/sitename/documentlibrary/foldername/filename`. |

## Output

The output datatree contains the details of the specified file or folder.

| Field | Description |
| --- | --- |
| ID | The identifier of the file or folder in SharePoint. |
| Name | The name of the file or folder. |
| Server relative URL | The server-relative URL of the file or folder location in SharePoint. |
| Exists | Indicates whether the file or folder exists. |
| Type | The type of the file. |
| Edit link | The URL for editing the file or folder. |
| Check in comment | The comment associated with the file's check-in status (if applicable). |
| Check out type | The type of check-out status (if applicable). |
| Content tag | The unique content tag identifying the file's version and state. |
| Customized page status | The status indicating if the page is customized (if applicable). |
| E tag | The ETag value for the file, indicating its current version. |
| IRM enabled | Indicates if Information Rights Management (IRM) is enabled for the file. |
| Length | The size of the file in bytes. |
| Level | The security level of the file or folder. |
| Major version | The major version number of the file or folder. |
| Minor version | The minor version number of the file or folder. |
| Linking URI | The URI providing a link to the file or folder. |
| Linking URL | The URL providing a link to the file or folder. |
| Time created | The date and time when the file or folder was created. |
| Time last modified | The date and time when the file or folder was last modified. |
| Title | The title or display name of the file or folder (if available). |
| UI version | The User Interface (UI) version number associated with the file or folder. |
| UI version label | The label associated with the UI version of the file or folder. |
| Unique ID | The unique identifier of the file or folder in SharePoint. |
