---
url: 'https://docs.workato.com/en/connectors/google-drive/action-list-permissions.md'
description: Lists all permissions associated with a file you specify in Google Drive.
---

# Google Drive - List file permissions action (batch)

This action lists all permissions associated with a given file in Google Drive. Permission details include the file's ownership and whether the file is shared with additional users, groups, or domains, or is accessible to anyone.

![Google Drive List file permissions action](/assets/google-drive-list-permissions.CW2ZCksP.png) _Google Drive List file permissions action_

## Input

| Input field | Description |
| --- | --- |
| File | The file with the permissions you plan to retrieve. Select a file or enter its ID. To find the file ID, right-click the file and select **Share > Copy link**. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file ID in the output of other Google Drive triggers and actions. |
| Maximum results | The maximum number of results to be returned per page. Default is `100`. |
| Page token | Token to specify the next page of results. Use the `nextPageToken` value from the output of a previous **List permissions** action. If the page token is `null`, there are no further pages of results. |
| Use domain admin access? | Issues the request as a domain administrator, if the connected user is the admin of the domain owning a shared drive. This setting allows the domain admin to [retrieve permissions for shared drive files](https://developers.google.com/drive/api/guides/manage-shareddrives#manage_shared_drives_for_domain_administrators) owned by their domain even if they aren't a member of the given shared drive. Default is set to **No**. |

## Output

| Output field | Description |
| --- | --- |
| Type | The type of grantee: `user`, `group`, `domain`, or `anyone`. |
| Permission ID | The ID of this permission. |
| Email address | The email address of the user or group that was granted this permission. |
| Domain | The domain this permission refers to. |
| Role | The role granted by this permission. |
| View | The view for this permission. |
| Allow file discovery | Indicates whether this permission allows the file to be discovered through search. This is only applicable to permissions granted to `domain` or `anyone`. |
| Display name | The human-readable name for the permission grantee. `user`: User's full name. `group`: Name of the Google Group. `domain`: Domain owning the shared drive. Not applicable to the type `anyone`. |
| Photo link | A link to the user's profile photo, if available. |
| Team Drive permission details | A list of permission details for the Team Drive. Contains the following output fields, in addition to **List size** and **List index**: Team Drive permission type: The permission type for this user. Only applies to Team Drives., Role: The primary role for this user. Only applies to Team Drives., Inherited from: The ID of the item from which this permission is inherited. Only applies to Team Drives., Inherited: Indicates whether this permission is inherited. Only applies to Team Drives. |
| Permission details | A list of permission details for the shared drive. Contains the following output fields, in addition to **List size** and **List index**: Permission type: The permission type for this user. Only applies to shared drives., Role: The primary role for this user. Only applies to shared drives., Inherited from: The ID of the item from which this permission is inherited. Only applies to shared drives., Inherited: Indicates whether this permission is inherited. Only applies to shared drives. |
| Deleted | Indicates whether the account associated with this permission has been deleted. This field only applies to user and group permissions. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-drive/action-remove-permissions.md
description: Removes a permission associated with a file you specify in Google Drive.
---

# Google Drive - Remove file permission action

This action removes a permission associated with a given file in Google Drive. Permission details include the file's ownership and whether the file is shared with additional users, groups, or domains, or is accessible to anyone.

![Google Drive Remove file permission action](/assets/google-drive-remove-permission.Qqca5RhN.png) _Google Drive Remove file permission action_

## Input

| Input field | Description |
| --- | --- |
| File | The file with the permission you plan to remove. Select a file or enter its ID. To find the file ID, right-click the file and select **Share > Copy link**. For example, if the URL is `https://drive.google.com/file/d/123nyR2IjW_Rq84d3qEYRoq1/view`, the file ID is `123nyR2IjW_Rq84d3qEYRoq1`. Alternatively, you can find the file ID in the output of other Google Drive triggers and actions. |
| Permission | The permission you plan to remove. Select a permission or enter its ID. The permission ID can be obtained from the [List permissions](/en/connectors/google-drive/action-list-permissions) action. |

## Output

| Output field | Description |
| --- | --- |
| Success | **True** if the permission was successfully removed. |

---
