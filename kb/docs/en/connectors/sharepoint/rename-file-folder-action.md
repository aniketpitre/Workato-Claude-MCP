---
url: 'https://docs.workato.com/en/connectors/sharepoint/rename-file-folder-action.md'
description: >-
  The rename a file or folder action in the SharePoint connector lets you give a
  file or folder a new name in SharePoint.
---

# SharePoint - Rename a file or folder in SharePoint action

This action renames a file or folder in SharePoint.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Parent folder | Specify the parent folder containing the file. |
| File name | Specify the name of the file you plan to rename. |
| New file name | Provide a new name for the file or folder. |

## Output

The output datatree contains the status of the move operation.

| Field | Description |
| --- | --- |
| Status | Indicates the status of the operation. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/search-list-items-in-library-action.md
description: >-
  The search list items action in the SharePoint connector lets you search for
  list items in a library you specify.
---

# SharePoint - Search list items in SharePoint library action

This action searches for list items in a specified SharePoint library.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list to search for items. |
| Filter | Provide a filter condition to use to search for items. |
| Search by | Specify the how you plan to search for items. This section of the UI includes options to Search by list or specify search fields individually. |
| Page size | Specify the maximum number of records to return in a single response. |
| Next page link | Provide the link to the next page of results. |

## Output

The output datatree contains the details of the list items that match the search criteria.

| Field | Description |
| --- | --- |
| \[List fields\] | The fields of the list with their respective values. |
| Next page link | The link to the next page of results. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/search-users-in-library-action.md
description: >-
  The search users action in the SharePoint connector lets you search for users
  on a SharePoint site by filter and pagination criteria.
---

# SharePoint - Search users in SharePoint library action (batch)

This action searches for users in a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Filter | Provide a filter condition to use to search for the user. For example, `Email eq xyz@microsoft.com and Id eq 6`. |
| Search by | Specify the how you plan to search for users. You can search by a fixed list or a dynamic list using a list datapill. |
| Search by source list | Input a list datapill to search for users using a list. Learn more about [list input](/en/features/list-management#list-batch-action). |
| ID | Search by the unique identifier assigned to the user. |
| Is hidden in UI? | Search by whether this field is hidden in the user interface. |
| Title | Search by the title or name associated with the user. |
| Login name | Search by the user's login name used for authentication. |
| Expiration | Search by the date when the user's account or access expires. |
| User principal name | Search by the principal name of the user in the domain. |
| Is email authentication guest user? | Search by whether the user is authenticated as a guest via email. |
| Is shared by email guest user? | Search by whether the user account is shared as a guest user via email. |
| Is site Admin? | Search by whether the user has administrative privileges on the site. |
| Principal type | Search by the type of principal, such as user or group, associated with the user. Refer to the Microsoft [SharePoint principal types](https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee541430\(v=office.15\)#members) documentation for more information. |
| Email | Search by the email address associated with the user. |
| OData ID | Search by the unique identifier in the OData format for the user. |
| OData type | Search by the type of data as per OData specifications. |
| Pagination | Specify how you plan for Workato to handle the search results. This section of the UI includes input fields allowing you to specify the **Page size**, **Offset**, and **Order by** |
| Page size | The maximum number of records to return in a single response. |
| Offset | The number of records to skip. |
| Order by | The field to order the results by. |

## Output

The output datatree contains the details of the users that match the search criteria.

| Field | Description |
| --- | --- |
| ID | The unique identifier assigned to the user in Sharepoint. |
| Is hidden in UI? | Indicates whether the user's profile is hidden in the user interface (UI). |
| Title | The display name or title associated with the user. |
| Login name | The login name or identifier used by the user to access SharePoint. |
| Expiration | The date or status indicating when the user's account or access expires. |
| User principal name | The user's principal name, typically in the format of an email address, used for identification purposes. |
| Is email authentication guest user? | Indicates whether the user is authenticated through email as a guest user. |
| Is shared by email guest user? | Indicates whether the user account is shared via email as a guest user. |
| Is site Admin? | Indicates whether the user has administrative privileges on the site. |
| Principal type | The type of principal, such as user or group, associated with the user. Refer to the Microsoft [SharePoint principal types](https://learn.microsoft.com/en-us/previous-versions/office/sharepoint-csom/ee541430\(v=office.15\)#members) documentation for more information. |
| Email | The primary email address associated with the user account. |
| User ID | The unique identifier assigned to the user within the system. |
| Odata ID | The unique identifier assigned to the user's data entry in the OData format. |
| Odata type | The type or category of data represented by the OData entry related to the user. |
| Odata edit link | A link or URL that allows editing of the user's data entry in OData format. |
| List size | The size or number of items in a list associated with the user. |
| List index | The index or position of the user's entry within a list. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/update-file-metadata-in-library-action.md
description: >-
  The update file metadata action in the SharePoint connector lets you update
  the metadata fields of a file in a library you specify.
---

# SharePoint - Update file metadata in SharePoint library action

This action updates the metadata of a file in a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Document library | Select the document library containing the file. |
| Parent folder | Specify the parent folder containing the file. |
| File name | Provide the name of the file whose metadata you plan to update. For example, `sample file.docx`. Select the **Encoded file name** option to use the URL encoded file name instead. |
| Additional fields | Provide input for the metadata fields you plan to update. These fields are dynamic and are determined by the file you select. |

## Output

The output datatree contains the status of the update operation.

| Field | Description |
| --- | --- |
| Status | Indicates the status of the update operation. |

---

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

---
