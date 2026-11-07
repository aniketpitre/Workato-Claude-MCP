---
url: 'https://docs.workato.com/en/connectors/sharepoint/delete-row-in-list-action.md'
description: >-
  The delete row action in the SharePoint connector lets you delete a row from a
  list you specify.
---

# SharePoint - Delete row in SharePoint list action

This action deletes a row in a SharePoint list you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list in which you plan to delete a row. |
| Row ID | Provide the ID of the row you plan to delete. |

## Output

The output datatree contains the status of the delete operation.

| Field | Description |
| --- | --- |
| Success | The status of the delete operation. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/download-file-from-library-action.md
description: >-
  The download file action in the SharePoint connector lets you download a file
  from a library you specify.
---

# SharePoint - Download file from SharePoint library action (file)

This action downloads a file from a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Folder relative URL | Provide the relative URL of the folder. For example, if you have not specified the **Site name**, enter `/documentlibraryname/foldername`.If you have provided the **Site name**, enter `/sites/sitename/documentlibrary/foldername`. |
| File path | Provide a direct path to the file. For example, `/sites/sitename/documentlibrary/foldername/filename.txt`. |
| File name | Provide the name of the file you plan to download. |
| Encoding of the file content | Specify the encoding of the file to set it explicitly. By default, Workato sets the encoding to UTF-8 if left blank. Learn more about the [encodings Workato supports](https://en.wikibooks.org/wiki/Ruby_Programming/Encoding). |

## Output

The output datatree contains the content of the downloaded file.

| Field | Description |
| --- | --- |
| Content | The content of the downloaded file. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/get-file-folder-permissions-library-action.md
description: >-
  The get file or folder permissions action in the SharePoint connector lists
  all individual and group permissions for a file or folder.
---

# SharePoint - Get file or folder permissions in SharePoint library action (batch)

This action retrieves the permissions of a specific file or folder in a SharePoint library. The specified folder can also be a document library. All associated permissions (both individual and group permissions) are listed.

## Input

| Field | Description |
| --- | --- |
| Document Library/Folder/Files | Select which entity to provide the permissions for. If File or Folder is selected, select the file or folder from the drop-down in addition to selecting the document library. |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Document library | Provide the document library containing the file or folder. |
| Folder | Select the folder for which you plan to retrieve permissions. Alternatively, you can provide the relative URL of the folder. For example, `/sites/sitename/documentlibrary/foldername`. |
| File name | The name of the file for which you plan to retrieve permissions. Alternatively, you can provide the relative URL of the file. For example, `/sites/sitename/documentlibrary/foldername/filename`. |

## Output

The output datatree contains the permissions of the specified file or folder.

| Field | Description |
| --- | --- |
| Odata metadata | Metadata providing details about the OData service endpoint. |
| Value | The specific permissions associated with the file or folder in SharePoint. The metadata is returned in the output. |
| Member | The specific users with permissions to access the file, folder, or document library. |
| Odata type | The type of the OData entity returned. |
| Odata ID | The unique identifier of the OData entity. |
| Odata edit link | The URL for editing the OData entity. |
| Base permissions | The base permissions assigned to the member. |
| Description | Additional descriptive information about the member. |
| Hidden | Indicates if the member is hidden. |
| ID | The identifier of the member. |
| Name | The name or title of the member. |
| Order | The order or sequence related to the member. |
| Role type kind | The kind of role or type of membership for the member. |
| List size | The size or count of items related to the member in a list context. |
| List index | The index position of the member in a list. |
| Principal ID | The principal identifier associated with the member. |

---

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

---

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

---
