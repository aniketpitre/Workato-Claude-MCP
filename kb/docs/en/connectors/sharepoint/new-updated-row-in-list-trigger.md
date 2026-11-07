---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/new-updated-row-in-list-trigger.md
description: >-
  The new or updated row trigger in the SharePoint connector picks up new or
  updated rows in a list you specify on each poll interval.
---

# SharePoint - New/updated row in SharePoint list trigger

This trigger picks up new or updated rows in your SharePoint list. It checks for new or updated rows once every poll interval and Workato processes each row as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Site name | The name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site. Use the site name as found in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. |
| List | Select the specific list to monitor for new or updated rows. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output datatree contains the details of the newly added or updated row. This output is dynamic and is determined by the list you select. A typical list generates something similar to the following output.

| Field | Description |
| --- | --- |
| Content type ID (ContentTypeId) | The identifier for the content type of the item. |
| Title (Title) | The title or name of the item. |
| Name | The name or title of the item (similar to Title). |
| Approver comments (OData\_\_ModerationComments) | Comments added during the approval process. |
| File type (File\_x0020\_Type) | The type of file (document, spreadsheet, etc.). |
| Color (OData\_\_ColorHex) | The color code associated with the item. |
| Color tag (OData\_\_ColorTag) | The tag or label indicating a specific color. |
| Emoji (OData\_\_Emoji) | The emoji associated with the item. |
| Compliance asset ID (ComplianceAssetId) | The identifier for compliance purposes. |
| Profile picture (ProfilePicture) | The URL or reference to the profile picture. |
| ID (ID) | The unique identifier of the item. |
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
| Sort T\\type (SortBehavior) | The sorting behavior applied to the item. |
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
| Comment settings (OData\_\_CommentFlags) | The comment settings associated with the item. |
| Comment count (OData\_\_CommentCount) | The number of comments associated with the item. |
