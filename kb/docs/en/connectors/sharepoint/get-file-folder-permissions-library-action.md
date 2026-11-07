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
