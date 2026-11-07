---
url: 'https://docs.workato.com/en/connectors/google-drive/action-search-files.md'
description: Retrieves a list of files or folders that match your search criteria
---

# Google Drive - Search files or folders action

This action retrieves a list of files or folders that match your search criteria.

![Google Drive Search files or folders action](/assets/google-drive-search-files.CgLJ48pK.png) _Google Drive Search files or folders action_

## Input

| Input field | Description |
| --- | --- |
| Files or folders | Select whether to search for files or folders. |
| Folder | Narrow down the search to within this folder. Does not include matching files and folders in subfolders. Leave blank to search through My Drive. |
| Name | Search for files or folders whose names partially match the given name. |
| Modified after | Search for files modified after this date. |
| Trashed files? | Set to **Yes** to search for files that have been trashed. |
| Starred files? | Set to **Yes** to search for files that have been starred. |
| Owner email | Search for files or folders belonging to this user. |
| Writer email | Search for files or folders that this user has permissions to edit. |
| Reader email | Search for files or folders that this user has permissions to read. |
| Shared with me? | Search for files or folders shared with the connected user. |
| Query | Filter the search results by an exact query. Refer to the [Google Drive documentation](https://developers.google.com/drive/api/guides/search-files) for the supported syntax. To filter by **Name**, **Modified after**, **Trashed files?**, **Starred files?**, **Owner email**, **Writer email**, **Reader email**, and/or **Shared with me?**, you can use the **Query** field with the [appropriate syntax](https://developers.google.com/drive/api/guides/search-files), or you can use the preceding fields in this table, but not both. Adding any entry twice will lead to query errors. For example, if you enter the **Name** field, do not enter a `name` query. |
| Next page token | Specify the `nextPageToken` from a previous search request to retrieve the next page of search results. |
| Page size | The maximum number of files or folders to return per page. Partial or empty result pages are possible even before the end of the files list has been reached. Acceptable values are `1` to `100`, inclusive. Default is `100`. |

## Output

Note that in Google Drive API, the terms `folder` and `file` are used interchangeably. A `folder` is technically a special `file`. As a result, whenever the field name or field description mentions `file`, it also applies to `folder`.

| Output field | Description |
| --- | --- |
| Next page token | Specify this token in the **Next page token** field to retrieve the next page of search results. |
| Incomplete search | Indicates whether the search is incomplete. |
| Files | List of files or folders found from the search. Each file/folder contains the following output fields, in addition to **List size** and **List index**: ID: ID of the file.; Name: Name of the file or folder.; MIME type: MIME type of this file, as stated in [Google Drive's documentation](https://developers.google.com/drive/api/v3/mime-types).; Description: A short description of the file.; Starred: Whether the user has starred the file.; Trashed: Indicates whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner may trash a file, and other users cannot see files in the owner's trash.; Explicitly trashed: Indicates whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder (for example, when you trash an entire parent folder). |
| Parents | The list of the parent folders that contain the file. Each parent folder in the list contains the following output field, in addition to **List size** and **List index**: ID: The ID of the parent folder containing the file. |
| Version | A version number for the file. This reflects every change made to the file on the server, even those not visible to the user. |
| Web content link | A link for downloading the content of the file in a browser. This is only available for files with binary content in Google Drive. |
| Web view link | A link for opening the file in a relevant Google editor or viewer in a browser. |
| Icon link | A static, unauthenticated link to the file's icon. |
| Thumbnail link | A short-lived link to the file's thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file's content. |
| Viewed by me | Indicates whether the file has been viewed by this user. |
| Viewed by me time | The last time the file was viewed by this user (RFC 3339 date-time). |
| Created time | The time at which the file was created (RFC 3339 date-time). |
| Modified time | The last time the file was modified by anyone (RFC 3339 date-time). |
| Modified by me time | The last time the file was modified by this user (RFC 3339 date-time). |
| Sharing user | The user who shared the file with the requesting user, if applicable. Each user contains the following output fields: Display name: A plain text displayable name for this user.; Email address: The email address of the user.; Permission ID: The user's ID as visible in Permission resources.; Photo link: A link to the user's profile photo, if available. |
| Owners | The list of owners of the file. Currently, only certain legacy files may have more than one owner. Not populated for shared drive files. Each owner contains the following fields, in addition to **List size** and **List index**: Display name: A plain text displayable name for this user.; Email address: The email address of the user.; Permission ID: The user's ID as visible in Permission resources.; Photo link: A link to the user's profile photo, if available.; Me: Indicates whether this user is the requesting user. |
| Shared | Indicates whether the file has been shared. Not populated for shared drive files. |
| Owned by me | Indicates whether the user owns the file. Not populated for shared drive files. |
| Viewers can copy content | Indicates whether users with **View** access can copy the file contents. |
| Writers can share | Indicates whether users with **Edit** access can share the file. Not populated for shared drive files. |
| Original filename | The original filename of the file if available, or else the original value of the name field. This is only available for files with binary content in Google Drive. |
| Full file extension | The full file extension extracted from the name field. May contain multiple concatenated extensions (for example, `tar.gz`). This is only available for files with binary content in Google Drive. It is automatically updated when the name field changes, but it is not cleared if the new name doesn't contain a valid extension. |
| File extension The final component of the full file extension (for example, `gz`). This is only available for files with binary content in Google Drive. |  |
| MD5 checksum | The MD5 checksum for the content of the file. This is only applicable to files with binary content in Google Drive. |
| Size | The size of the file's content in bytes. This is only applicable to files with binary content in Google Drive. |
| Quota bytes used | The number of storage quota bytes used by the file. This includes the head revision as well as previous revisions with [Keep Forever](https://developers.google.com/drive/api/guides/change-overview) enabled. |
| Head revision ID | The ID of the file's most current version. This is currently only available for files with binary content in Google Drive. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-drive/action-update-permission.md
description: Updates a permission associated with a file you specify in Google Drive.
---

# Google Drive - Update file permission action

This action updates a permission associated with a given file in Google Drive. Permissions are useful to transfer file ownership or to share a file with specific users, groups, or domains, or to make it accessible to anyone.

![Google Drive Update file permission action](/assets/google-drive-update-permission.gYmvoR46.png) _Google Drive Update file permission action_

## Input

| Input field | Description |
| --- | --- |
| File | The file with the permission you plan to update. Select a file or enter its ID. To find the file ID, right-click the file and select **Share > Copy link**. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file ID in the output of other Google Drive triggers and actions. |
| Permission | The permission you plan to update. Select a permission or enter its ID. The permission ID can be obtained from the [List permissions](/en/connectors/google-drive/action-list-permissions) action. |
| Role | The role granted by this permission. Select a role or use a custom value. Allowed role values are `owner`, `organizer`, `fileOrganizer`, `writer`, `commenter`, `reader`. |
| Use domain admin access? | Issues the request as a domain administrator, if the connected user is the admin of the domain owning a shared drive. This setting allows the domain admin to [set permissions for shared drive files](https://developers.google.com/drive/api/guides/manage-shareddrives#manage_shared_drives_for_domain_administrators) owned by their domain even if they aren't a member of the given shared drive. Default is set to **No**. |
| Transfer ownership | Transfer ownership of the file to the user email provided. The file must have been shared with the user and the **Role** must be set to `owner`. Defaults to **No**. |
| Remove expiration | Whether to remove the expiration date. |

## Output

| Input field | Description |
| --- | --- |
| Kind | The kind of resource this is: **drive#permission**. |
| Type | The type of grantee: **user**, **group**, **domain**, or **anyone.** |
| Permission ID | The ID of this permission. |
| Email address | The email address of the user or group that was granted this permission. |
| Domain | The domain this permission refers to. |
| Role | The role granted by this permission. |
| View | The view for this permission. |
| Allow file discovery | Indicates whether this permission allows the file to be discovered through search. This is only applicable to permissions granted to **domain** or **anyone**. |
| Display name | The human-readable name for the permission grantee. **user**: User's full name. **group**: Name of the Google Group. **Domain**: Domain owning the shared drive. Not applicable to the type **anyone**. |
| Photo link | A link to the user's profile photo, if available. |
| Team Drive permission details | A list of permission details for the Team Drive. Contains the following output fields, in addition to **List size** and **List index**: Team Drive permission type: The permission type for this user. Only applies to Team Drives., Role: The primary role for this user. Only applies to Team Drives., Inherited from: The ID of the item from which this permission is inherited. Only applies to Team Drives., Inherited: Indicates whether this permission is inherited. Only applies to Team Drives. |
| Permission details | A list of permission details for the shared drive. Contains the following output fields, in addition to **List size** and **List index**: Permission type: The permission type for this user. Only applies to Shared drives., Role: The primary role for this user. Only applies to Shared drives., Inherited from: The ID of the item from which this permission is inherited. Only applies to Shared drives., Inherited: Indicates whether this permission is inherited. Only applies to Shared drives. |
| Deleted | Indicates whether the account associated with this permission has been deleted. This field only applies to user and group permissions. |

---
