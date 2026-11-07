---
url: 'https://docs.workato.com/en/connectors/sharepoint/copy-file-action.md'
description: >-
  The copy file action in the SharePoint connector lets you copy a file to a
  specific folder in SharePoint.
---

# SharePoint - Copy file in SharePoint action

This action copies a file to a specific folder in SharePoint.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Parent folder | Specify the parent folder containing the file. |
| File name | Specify the name of the file you plan to copy. |
| Destination folder | Specify the folder where you plan to move the copied file. |
| Destination file name | Provide the name for the copied file in the destination folder. If you leave this field empty, Workato uses the original file name. |
| Overwrite existing file? | Determine whether to overwrite the existing file in the destination folder. |

## Output

The output datatree contains the status of the move operation.

| Field | Description |
| --- | --- |
| Status | Indicates the status of the copy operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/create-folder-in-library-action.md
description: >-
  The create folder action in the SharePoint connector lets you create a folder
  in a library you specify.
---

# SharePoint - Create folder in SharePoint library action

This action creates a folder in a SharePoint library you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Parent folder | Provide the parent folder where the new folder is created. |
| Folder name | Provide the name of the new folder you plan to create. |

## Output

The output datatree contains the details of the newly created folder.

| Field | Description |
| --- | --- |
| Metadata | Metadata about the file. This object contains the ID, URI, Etag, and Type of the file. |
| Activities | Activities related to the folder. |
| Files | The URL of the files contained within the folder. |
| List item all fields | The URL of all fields associated with list items in the folder. |
| Parent folder | The URL of the folder that contains the current folder. |
| Properties | The URL of additional properties or attributes of the folder. |
| Storage metrics | The URL of metrics related to the storage usage of the folder. |
| Folders | The URL of subfolders within the current folder. |
| Unique ID | The unique identifier for the folder. |
| Name | The name of the folder. |
| Server Relative URL | The relative URL of the folder within the SharePoint site. |
| Exists | Indicates whether the folder exists. |
| Item count | The number of items (files, subfolders, and more) in the folder. |
| Time created | The timestamp indicating when the folder was created. |
| Time last modified | The timestamp indicating when the folder was last modified. |
| Prog ID | The programmatic identifier associated with the folder. |
| Welcome page | The URL or path to the welcome page associated with the folder. |
| Is WOPI enabled | Indicates whether Web Application Open Platform Interface (WOPI) is enabled. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/create-rows-in-list-action-batch.md
description: >-
  The create rows action in the SharePoint connector lets you create multiple
  rows at once in a list you specify.
---

# SharePoint - Create rows in SharePoint list action (batch)

This action creates multiple rows in a SharePoint list you specify.

## Input

| Field | Description |
| --- | --- |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| List | Specify the list where you plan to create rows. |
| Batch | Specify the batch of rows you plan to create. Each row should contain the fields you plan to populate. |

## Output

The output datatree contains the details of the newly created rows.

| Field | Description |
| --- | --- |
| Content type ID (ContentTypeId) | The identifier for the content type of the item. |
| Name (title) | The name or title of the item. |
| Approver comments (OData\_\_ModerationComments) | Comments added during the approval process. |
| File type (File\_x0020\_Type) | The type of file (document, spreadsheet, etc.). |
| Color (OData\_\_ColorHex) | The color code associated with the item. |
| Color tag (OData\_\_ColorTag) | The tag or label indicating a specific color. |
| Emoji (OData\_\_Emoji) | The emoji associated with the item. |
| Compliance asset ID (ComplianceAssetId) | The identifier for compliance purposes. |
| Profile picture (ProfilePicture) | The URL or reference to the profile picture. |
| ID (ID) | The unique identifier or title of the item. |
| Content type (ContentType) | The content type of the item (document, list item, and more). |
| Modified (Modified) | The date and time when the item was last modified. |
| Created (Created) | The date and time when the item was created. |
| Created by (Author) | The user who created the item. |
| Modified by (Editor) | The user who last modified the item. |
| Has copy destinations (…\_\_HasCopyDestinations) | Indicates if the item has copy destinations. |
| Copy source (OData\_\_CopySource) | The source from which the item was copied. |
| Ows hidden version (owshiddenversion) | The hidden version number of the item. |
| Workflow Version (WorkflowVersion) | The version of the workflow associated with the item. |
| UI Version (OData\_\_UIVersion) | The user interface version of the item. |
| Version (OData\_\_UIVersionString) | The version of the item (string representation). |
| Attachments (Attachments) | Indicates if the item has attachments. |
| Approval Status (OData\_\_ModerationStatus) | The approval status of the item. |
| Edit (Edit) | The edit link for the item. |
| Title (LinkTitleNoMenu) | The title of the item without a menu link. |
| Title (LinkTitle) | The title of the item with a menu link. |
| Title (LinkTitle2) | The alternative title of the item with a menu link. |
| Select (SelectTitle) | The select title of the item. |
| Instance ID (InstanceID) | The unique identifier of the instance. |
| Order (Order) | The order of the item. |
| GUID (GUID) | The globally unique identifier of the item. |
| Workflow Instance ID (WorkflowInstanceID) | The identifier of the workflow instance associated with the item. |
| URL Path (FileRef) | The server-relative URL path of the item. |
| Path (FileDirRef) | The server-relative path of the folder containing the item. |
| Modified (Last\_x0020\_Modified) | The date and time when the item was last modified. |
| Created (Created\_x0020\_Date) | The date and time when the item was created. |
| Item type (FSObjType) | The type of the item in the document library (file, folder, and more). |
| Sort type (SortBehavior) | The sorting behavior applied to the item. |
| Effective permissions mask (PermMask) | The permissions mask indicating effective permissions for the item. |
| Principal count (PrincipalCount) | The number of principals with permissions on the item. |
| Name (FileLeafRef) | The leaf name of the file (name without path). |
| Unique ID (UniqueId) | The unique identifier of the item. |
| Document parent identifier (ParentUniqueId) | The identifier of the parent document in a document set. |
| Client ID (SyncClientId) | The identifier used for synchronization purposes. |
| ProgId (ProgId) | The programmatic identifier of the file type. |
| ScopeId (ScopeId) | The identifier of the scope of the item. |
| HTML file type (HTML\_x0020\_File\_x0020\_Type) | The HTML file type associated with the item. |
| Edit menu table start (…a\_\_EditMenuTableStart) | The start of the edit menu table. |
| Edit menu table start (…\_\_EditMenuTableStart2) | The alternative start of the edit menu table. |
| Edit menu table end (OData\_\_EditMenuTableEnd) | The end of the edit menu table. |
| Name (LinkFilenameNoMenu) | The filename without a menu link. |
| Name (LinkFilename) | The filename with a menu link. |
| Name (LinkFilename2) | The alternative filename with a menu link. |
| Type (DocIcon) | The icon representing the document type. |
| Server relative URL (ServerUrl) | The server-relative URL of the item. |
| Encoded absolute URL (EncodedAbsUrl) | The encoded absolute URL of the item. |
| File name (BaseName) | The base name of the file (filename without extension). |
| Property bag (MetaInfo) | The metadata information associated with the item. |
| Level (OData\_\_Level) | The level of the item in a hierarchy. |
| Is current version (OData\_\_IsCurrentVersion) | Indicates if the item is the current version. |
| Item child count (ItemChildCount) | The number of child items associated with the item. |
| Folder child count (FolderChildCount) | The number of child folders associated with the item. |
| Restricted (Restricted) | Indicates if the item is restricted. |
| Originator ID (OriginatorId) | The identifier of the originator of the item. |
| NoExecute (NoExecute) | Indicates if the item should not be executed. |
| Content version (ContentVersion) | The version of the content. |
| Label setting (OData\_\_ComplianceFlags) | The compliance flags associated with the item. |
| Retention label (OData\_\_ComplianceTag) | The retention tag applied to the item. |
| Retention label (Applie…plianceTagWrittenTime) | The date and time when the retention tag was applied. |
| Label applied by (OData\_\_ComplianceTagUserId) | The user who applied the retention tag. |
| Item is a record (OData\_\_IsRecord) | Indicates if the item is a record. |
| Access policy (AccessPolicy) | The access policy applied to the item. |
| VirusStatus (OData\_\_VirusStatus) | The virus scan status of the item. |
| VirusVendorID (OData\_\_VirusVendorID) | The identifier of the virus scanning vendor. |
| VirusInfo (OData\_\_VirusInfo) | The information related to the virus scan. |
| App created by (AppAuthor) | The application that created the item. |
| App modified by (AppEditor) | The application that last modified the item. |
| Total size (SMTotalSize) | The total size of the item. |
| Last modified date (SMLastModifiedDate) | The date and time when the item was last modified. |
| Total file stream size (SMTotalFileStreamSize) | The total size of the file stream. |
| Total file count (SMTotalFileCount) | The total number of files. |
| \-Comment settings (OData\_\_CommentFlags) | The comment settings associated with the item. |
| \-Comment count (OData\_\_CommentCount) | The number of comments associated with the item. |
| Success | Indicates the success of the operation. |
| Error | Indicates whether the operation resulted in an error. |
| List size | The list size. |
| List index | The list index. |

---

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

---
