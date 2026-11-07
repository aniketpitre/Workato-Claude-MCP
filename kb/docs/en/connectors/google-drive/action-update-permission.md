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
