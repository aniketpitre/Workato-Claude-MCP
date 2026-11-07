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
