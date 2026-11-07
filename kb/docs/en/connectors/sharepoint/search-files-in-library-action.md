---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/search-files-in-library-action.md
description: >-
  The Search files action in the SharePoint connector lets you find files in a
  folder you specify in a library, by file name or by regular search.
---

# SharePoint - Search files in SharePoint library action (batch)

This action searches for files in a folder you specify in a SharePoint library.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| File search method | The method to use to search files. Defaults to **Search by file name**, which searches using the exact file name. Alternatively, you can select **Regular search**. |
| Folder | The folder to search for the files. |
| File name | The name of the file for which you plan to search. |
| Search text | The text to search for in the file content or metadata. This field is only available when you search using **Regular search**. |
| Author | The author of the file. This field is only available when you search using **Regular search**. |
| Last Modified Time | The last modified time of the file. This field is only available when you search using **Regular search**. |
| File size | The size of the file. This field is only available when you search using **Regular search**. |

## Output

The output datatree contains the details of the files that match the search criteria.

| Field | Description |
| --- | --- |
| ID | The unique identifier of the file. |
| Name | The name of the file. |
| Server relative URL | The server-relative URL of the file. |
| Exists | Indicates if the file exists in the library. |
| Type | The type or file extension of the file. |
| Edit link | URL for editing the file. |
| Check in comment | Comments associated with the file check-in. |
| Check out type | The type of check-out (for example, online or offline). |
| Content tag | The tag associated with the content of the file. |
| Customized page status | Indicates if the file's page is customized. |
| E tag | The entity tag (ETag) for the file's version. |
| IRM enabled | The information Rights Management (IRM) status. |
| Length | The size or length of the file. |
| Level | The security level of the file. |
| Major version | The major version number of the file. |
| Minor version | The minor version number of the file. |
| Linking URI | The URI linking to the file. |
| Linking URL | The URL linking to the file. |
| Time created | The date and time the file was created. |
| Time last modified | The date and time the file was last modified. |
| Title | The title or display name of the file. |
| UI version | The user Interface (UI) version of the file. |
| UI version label | The label for the UI version of the file. |
| Unique ID | The unique identifier of the file. |
| List size | The size of the SharePoint list containing the file. |
| List index | The index position of the file within the SharePoint list. |
