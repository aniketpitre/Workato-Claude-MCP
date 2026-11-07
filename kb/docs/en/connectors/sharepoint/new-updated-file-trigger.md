---
url: 'https://docs.workato.com/en/connectors/sharepoint/new-updated-file-trigger.md'
description: >-
  The new or updated file trigger in the SharePoint connector picks up new or
  updated files in a library on each poll interval.
---

# SharePoint - New or updated file trigger

This trigger picks up new or updated files in your SharePoint library. It checks for new or updated files once every poll interval and Workato processes each file as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Document library | Select the specific document library to monitor for new or updated files. |
| Folder | Select the folder to process files. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output datatree contains information about the new or updated file. This includes the file name, server relative URL, and other metadata.

| Field | Description |
| --- | --- |
| Check in comment | The comment provided when checking in the file in SharePoint. |
| Check out type | The type of checkout (for example, online or offline) for the file in SharePoint. |
| Content tag | The tag or label associated with the content of the file in SharePoint. |
| Customized page status | The status of customization for SharePoint pages related to the file. |
| E tag | The entity tag used for versioning and cache validation in SharePoint. |
| Exists | Indicates whether the file exists in SharePoint. |
| Length | The size or length of the file in SharePoint. |
| Level | The security or access level associated with the file in SharePoint. |
| Major version | The major version number of the file in SharePoint. |
| Minor version | The minor version number of the file in SharePoint. |
| Name | The name of the file in SharePoint. |
| Server relative URL | The relative URL of the file within the SharePoint site. |
| Time created | The date and time when the file was created in SharePoint. |
| Time last modified | The date and time when the file was last modified in SharePoint. |
| Title | The title or display name of the file in SharePoint. |
| UI version | The user interface version number associated with the file in SharePoint. |
| UI version label | The label or description associated with the UI version of the file in SharePoint. |
| Unique ID | The unique identifier assigned to the file within SharePoint. |
| Linking URI | The URI used for linking related resources or files within SharePoint. |
| Linking URL | The URL used for linking related resources or files within SharePoint. |
| IRM enabled | Indicates whether Information Rights Management (IRM) is enabled for the file in SharePoint. |
| Metadata | Additional metadata or properties associated with the file in SharePoint. This includes the URI, ID, and Type of metadata. |
| Author | The URI of the author or creator of the file in SharePoint. |
| Checked out by user | The URI of the user who currently has the file checked out for editing in SharePoint. |
| Effective information rights management settings | The URI of the information regarding effective IRM settings for the file in SharePoint. |
| Information rights management settings | The URI of the detailed settings for Information Rights Management (IRM) applied to the file in SharePoint. |
| List item all fields | The URI of all fields associated with the list item where the file is located in SharePoint. |
| Locked by user | The URI of the user who currently has the file locked for editing in SharePoint. |
| Modified by | The URI of the user who last modified the file in SharePoint. |
| Properties | The URI of all properties associated with the file in SharePoint. |
| Version events | The URI of the events related to versioning of the file in SharePoint. |
| Versions | The URI of the different versions of the file available in SharePoint. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/new-updated-file-in-folder-hierarchy-trigger.md
description: >-
  The new or updated file in folder hierarchy trigger in the SharePoint
  connector picks up new or updated files across a folder hierarchy.
---

# SharePoint - New/updated file in folder hierarchy trigger

This trigger picks up new or updated files in your SharePoint folder hierarchy. It checks for new or updated files once every poll interval and Workato processes each file as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Site name | Provide the name of the SharePoint site to which you plan to connect. If left blank, Workato connects to your default home site, as specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. If you plan to connect to a different site, you can provide the absolute URL to override the base URL. For example, if the input is `https://company-name.sharepoint.com/teams/product`, Workato connects to the provided input. Alternatively, you can provide the absolute URL to connect to a different site. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Document library | Select the specific document library to monitor for new or updated files. |
| Folder | Select the folder to monitor for new or updated files. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records created or updated one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output datatree contains information about the new or updated file. This includes the file name, server relative URL, and other metadata.

| Field | Description |
| --- | --- |
| Metadata | Metadata about the file. This object contains the ID, URI, Etag, and Type of the file. |
| First unique ancestor securable object | The nearest parent object in SharePoint that defines security settings for the file. |
| Role assignments | Assignments of specific permissions or roles within SharePoint for accessing the file. |
| Attachment files | Files attached or uploaded as attachments to the item (e.g., emails with attachments). |
| Content type | The type or category of content that defines metadata and behavior for SharePoint items. |
| Get DLP policy tip | Retrieve data loss prevention (DLP) policy tips associated with the uploaded file. |
| Field values as html | Field values formatted as HTML content within SharePoint for the uploaded file. |
| Field values as text | Field values in plain text format within SharePoint for the uploaded file. |
| Field values for edit | Initial field values intended for editing when creating or updating the file in SharePoint. |
| File | A document or binary object uploaded or created within a SharePoint document library. |
| Folder | The specific folder within SharePoint where the new or updated file is located. |
| Liked by information | Information about users who have liked or favorited the file within SharePoint. |
| Parent list | The list or document library where the file is stored in SharePoint. |
| Properties | Metadata or attributes associated with the file in SharePoint. |
| Versions | Different iterations or revisions of the file within SharePoint's version history. |
| File system object type | The type of file object as classified within SharePoint's document management system. |
| Server redirected embed URI | URI used by SharePoint to embed external resources in documents or pages. |
| Server redirected embed URL | URL used by SharePoint to redirect to embedded resources like videos or images. |
| Content type ID | Unique identifier for the content type associated with the file in SharePoint. |
| File leaf ref | The file name or leaf reference within SharePoint's document library structure. |
| Compliance asset ID | Identifier used within SharePoint for compliance tracking or auditing purposes. |
| Id | Unique identifier assigned to the file within SharePoint. |
| ID | Another identifier commonly used within SharePoint for uniquely identifying files. |
| Created | Date and time when the file was initially created in SharePoint. |
| Author ID | Unique identifier of the user who originally created the file in SharePoint. |
| Modified | Date and time when the file was last modified in SharePoint. |
| Editor ID | Unique identifier of the user who last modified the file in SharePoint. |
| O data copy source | Source from which data is copied using the OData protocol within SharePoint. |
| File ref | Reference or link to the file within SharePoint's document management system. |
| FS obj type | Type of object within SharePoint's file system (e.g., file, folder). |
| Checkout user ID | Unique identifier of the user who has checked out the file for editing in SharePoint. |
| Unique ID | Globally unique identifier (GUID) assigned to the file within SharePoint. |
| O data UI version string | Version string used in the OData user interface within SharePoint. |
| GUID | Globally unique identifier used to reference the file or object within SharePoint. |

---

---
url: >-
  https://docs.workato.com/en/connectors/sharepoint/new-updated-file-in-folder-hierarchy-trigger-large-site.md
description: >-
  The New/updated file in folder hierarchy (large site) trigger detects new or
  modified files within your SharePoint folder hierarchy. Use this trigger when
  monitoring a folder within a large SharePoint site containing more than 5,000
  files.
---

# SharePoint - New/updated file in folder hierarchy trigger (large site)

The **New/updated file in folder hierarchy (large site)** trigger detects new or modified files within your SharePoint folder hierarchy. It checks for changes at each polling interval and processes each file as a separate job.

Use this trigger when monitoring a folder within a large SharePoint site that has more than 5,000 files.

> **TRIGGER DOESN'T RETRIEVE PAST EVENTS**
> 
> This trigger doesn't retrieve updates made before the recipe starts. It only detects changes from the moment the recipe begins running. If your folder isn't in a large site, consider using the [New/updated file in folder hierarchy trigger](/en/connectors/sharepoint/new-updated-file-in-folder-hierarchy-trigger) instead.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Specify how frequently to check for new events. Defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Site name | Provide the name of the SharePoint site you plan to connect to. If left blank, Workato connects to the default home site specified in your connection settings. The site name is located in the URL of the site page. For example, if the URL is `https://company-name.sharepoint.com/sites/product`, the site name is `product`. Alternatively, to connect to a different site, you can provide an absolute URL to override the base URL. For example, entering `https://company-name.sharepoint.com/teams/product` connects Workato to the specified site directly. |
| Document library | Select the specific document library to monitor for new or updated files. |
| Folder | Select the folder to monitor for new or updated files. |
| Time zone | Select the timezone used in SharePoint. To [access and change regional settings](https://support.microsoft.com/en-us/office/change-regional-settings-for-a-site-e9e189c7-16e3-45d3-a090-770be6e83c1a) in SharePoint, go to **Settings > Site Settings > Site Administration > Regional Settings > Time Zone**. |

## Output

| Output field | Description |
| --- | --- |
| Created by | The name or identifier of the user who created the file. |
| Base name | The main name of the file without the extension. |
| Checked out user ID | The unique identifier of the user who checked out the file. |
| Compliance asset ID | The identifier used within SharePoint for compliance tracking or auditing purposes. |
| Content type | The type or category of content that defines metadata and behavior for SharePoint items. |
| Content type ID | The unique identifier associated with the content type of the file. |
| Created | The date and time when the file was initially created in SharePoint. |
| Modified by | The name or identifier of the user who last modified the file. |
| Encoded absolute URL | The fully qualified URL of the file, encoded to ensure special characters are properly represented. |
| Item type | The classification of the item. |
| Path | The file path within the SharePoint hierarchy. |
| Name | The name of the file including the extension. |
| URL path | The URL path of the file within SharePoint. |
| File size | The size of the file in bytes or kilobytes. |
| Folder child count | The number of child items (files or subfolders) inside the folder. |
| GUID | The globally unique identifier used to reference the file or object within SharePoint. |
| ID | The unique identifier assigned to the file within SharePoint. |
| Item child count | The number of child items within the current item, applicable to folders. |
| Modified | The date and time when the file was last modified in SharePoint. |
| Document parent identifier | The unique identifier of the parent folder or document set that contains the file. |
| Server relative URL | The relative URL of the file based on the URL for the server. |
| Title | The display name of the file. |
| Unique ID | Another globally unique identifier (GUID) assigned to the file within SharePoint. |
| Copy source | The original source location of the file if it was copied from another location. |
| Version | The version number of the file. |

---
