---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/upload-file-action.md
description: >-
  The Upload file action enables you to upload a file by providing the file
  contents. If a file with the same name already exists in the folder, this
  action overwrites the file contents.
---

# Microsoft Graph API - Upload file action

The **Upload file** action enables you to upload a file by providing the file contents. If a file with the same name already exists in the folder, this action overwrites the file contents.

## Input

| Input field | Description |
| --- | --- |
| Drive ID | The unique identifier of the OneDrive or SharePoint drive. |
| Folder ID | The unique identifier of the destination folder in the drive. |
| File name | The name of the file to be uploaded. |
| File content | The actual data or content of the file. |
| Mime type | The format of the file. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the item within the Drive. |
| Created by | Identity of the user, device, and application that created the item. |
| Created date time | Timestamp when the file was created. |
| Description | User-provided description of the file. |
| E tag | eTag for the entire item (metadata + content). |
| Last modified by | Identity of the user, device, and application that last modified the item. |
| Last modified date time | Date and time the item was last modified. |
| Name | The name of the item (filename and extension). |
| Parent reference | Parent information, if the item has a parent. |
| Web URL | URL that displays the resource in the browser. |
| Created by user | Identity of the user who created the item. |
| Last modified by user | Identity of the user who last modified the item. |
| Audio | Audio metadata, if the item is an audio file. |
| Bundle | Bundle metadata, if the item is a bundle. |
| Content | The content stream, if the item represents a file. |
| C tag | An eTag for the content of the item. This eTag isn't changed if only the metadata is changed. Note This property isn't returned if the item is a folder. |
| Deleted | Information about the deleted state of the item. |
| File | File metadata, if the item is a file. |
| File system info | File system information on client. |
| Folder | Folder metadata, if the item is a folder. |
| Image | Image metadata, if the item is an image. |
| Location | Location metadata, if the item has location data. |
| Malware | Malware metadata, if the item was detected to contain malware. |
| Package | If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. |
| Pending operations | If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. |
| Photo | Photo metadata, if the item is a photo. |
| Publication | Provides information about the published or checked-out state of an item, in locations that support such actions. This property isn't returned by default. |
| Remote item | Remote item data, if the item is shared from a drive other than the one being accessed. |
| Root | If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive. |
| Search result | Search metadata, if the item is from a search result. |
| Shared | Indicates that the item was shared with others and provides information about the shared state of the item. |
| Sharepoint IDs | Returns identifiers useful for SharePoint REST compatibility. |
| Special folder | If the current item is also available as a special folder, this facet is returned. |
| Size | Size of the item in bytes. |
| Video | Video metadata, if the item is a video. |
| Web dav URL | WebDAV compatible URL for the item. |
| Workbook | For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. |
| Analytics | Analytics about the view activities that took place on this item. |
| Children | Collection containing Item objects for the immediate children of Item. Only items representing folders have children. |
| List item | For drives in SharePoint, the associated document library list item. |
| Permissions | The set of permissions for the item. |
| Retention label | Information about retention label and settings enforced on the driveItem. |
| Subscriptions | The set of subscriptions on the item. Only supported on the root of a drive. |
| Thumbnails | Collection of [thumbnailSet](https://learn.microsoft.com/en-us/graph/api/resources/thumbnailset?view=graph-rest-1.0) objects associated with the item. For more information, see [getting thumbnails](https://learn.microsoft.com/en-us/graph/api/driveitem-list-thumbnails?view=graph-rest-1.0). |
| Versions | The list of previous versions of the item. For more info, see [getting previous versions](https://learn.microsoft.com/en-us/graph/api/driveitem-list-versions?view=graph-rest-1.0). |

Please refer to the [Properties](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0#properties) for detailed schema.
