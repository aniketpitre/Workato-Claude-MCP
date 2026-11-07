---
url: 'https://docs.workato.com/en/connectors/google-workspace/action-get-record.md'
description: >-
  The Get record action allows you to get details of an object in the Google
  Workspace.
---

# Google Workspace - Get record action

The **Get record** action retrieves details about an object in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection.

The **Get record** action supports the following **Object** types:

- [User](#get-user)
- [User alias](#get-user-alias)
- [Group](#get-group)
- [Organizational unit](#get-organizational-unit)
- [Member from group](#get-member-from-group)
- [Role assignment](#get-role-assignment)
- [App specific passwords](#get-app-specific-passwords)
- [Verification code](#get-verification-code)
- [Access token](#get-access-token)
- [License](#get-license-assigned-to-a-user)

## Get user

The `Get user` **Object** selection retrieves user details in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user primary or alias email address. |
| Projection type | Select the projection type as `Full` or `Basic`. The default is `Basic`. |
| View type | Select the view type as `admin_view` or `domain_public`. The default is `admin_view`. |
| Custom Field schemas | Select the custom field schemas. The default is `all fields`. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get user alias

The `Get user alias` **Object** selection gets user alias email address details in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | The user primary email address, alias email address, or unique user ID. |
| Alias | The user alias email address. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get group

The `Get group` **Object** selection gets group details in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | The group email address or alias email address. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get organizational unit

The `Get organizational unit` **Object** selection gets organizational unit details in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Organizational unit | Select the organizational unit in Google Workspace. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get member from group

The `Get member from group` **Object** selection gets member details from a group in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group email address | Enter the group email address, group alias, or unique group ID. |
| Group member email address | Enter user or group email address that is part of the selected group. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get role assignment

The `Get role assignment` **Object** selection retrieves user role assignment details in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Role | Select the role assignment to retrieve details. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get App specific passwords

The `Get App specific passwords` **Object** selection retrieves details of the user app-specific password in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address, including primary, alias, or a unique user ID. |
| Code ID | Enter the app-specific password unique ID to be retrieved. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get verification code

The `Get verification code` **Object** selection retrieves verification code details associated with a user email address in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter user email address, such as the primary or alias. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get access token

The `Get access token` **Object** selection retrieves access token details issued to a client under a user.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address, such as primary, alias, or a unique user ID. |
| Client ID | Enter the client ID of the application to which the token is issued to. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

## Get license assigned to a user

The `Get license assigned to a user` **Object** selection retrieves product license details assigned to a user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Product ID | Enter the product name associated with the user license. |
| SKU to update | Enter the product SKU unique identifier number. |
| Email ID | Provide the user email ID associated with the license. Use the updated email ID if email ID updates have been applied. |

### Output

The **Get record** action generates output fields relevant to the newly added user objects, including any custom fields defined in the **Custom fields schema**.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-mobile-device.md
description: >-
  The Mobile device action performs certain action on the mobile device resource
  enlisted in the Google Workspace.
---

# Google Workspace - Mobile device action

The **Mobile device** action performs certain action on the mobile device resource enlisted in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection. Refer to the [Google Workspace Directory API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-mobile-devices) for more information about the configuration.

### Input

| Input field | Description |
| --- | --- |
| Resource ID | Enter the mobile device Google Workspace ID. |
| Action | Select the action you plan to perform on the device. |

### Output

| Output field | Description |
| --- | --- |
| Success | A boolean (`true` or `false`) value indicating whether the action was successful or not. |
| Error message | Displays an error message if the action was not successful. |

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-search-record.md
description: >-
  Search record action allows you to search for specific objects in the Google
  Workspace.
---

# Google Workspace - Search record action (batch)

The **Search record** action searches for specific objects in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection.

The **Search record** action supports the following **Object** types:

- [User](#search-user)
- [User alias](#search-user-alias)
- [Group](#search-group)
- [Organizational unit](#search-org-unit)
- [Member to group](#search-member)
- [Role assignment](#search-role-assign)
- [App specific passwords](#app-specific-password)
- [Access token](#search-access-token)
- [License](#search-license)
- [Mobile device resources](#search-mobile-device)
- [Roles](#search-roles)

## Search user

The `Search User` **Object** selection searches for users in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Domain | Provide the domain name where you plan to search for users. |
| Projection type | Select the fields subset type to display for the user list. |
| Fields | Provide the user given name, family name, and the primary email. |
| Custom query | Set matching attributes in a custom query to search for users. |
| Max result | Enter maximum results value to return. |
| Custom fields schema | Select customer fields which can be passed on to search for the users. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search user alias

The `Search user alias` **Object** selection searches for alias email addresses in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user primary email address, alias email address, or unique user ID. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search group

The `Search group` **Object** selection searches for groups in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group name | Enter the group name. |
| Group email | Enter the group email address. |
| Group member email | Enter the group member email address. Don't provide this value if **Group name** or **Group email** is already provided. |
| Custom Query | Set matching attributes in a custom query to search for groups. |
| Maximum Result | Provide the maximum results value to return. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search organizational unit

The `Search organizational unit` **Object** selection searches for an organizational unit in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Organizational unit | Select the organizational unit. |
| Type | Select to return all organizations or only the child organizations. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search members of a group

The `Search members of a group` **Object** selection searches for group members in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group email | Enter the group email address, group alias, or unique group ID. |
| Include derived membership | Select if indirect memberships must be included in the results. |
| Max results | Select the maximum results to return in the response. |
| Page token | Provide the next page token in the list. |
| Role | Select a role to return results based on user roles. Options include `owner`, `manager`, and `member`. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search role assignment

The `Search role assignment` **Object** selection searches for role assignments in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Role ID | Enter the `Role ID` to only return assignments related to the selected role. |
| Email address | Enter the user email address, alias address, or unique ID to return role assignments related to a user. |
| Max results | Select the maximum results to return in the response. |
| Page token | Provide the next page token in the list. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search app specific passwords

The `Search app specific passwords` **Object** selection searches for information relating to a user app-specific password in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address, such as primary, alias, or unique user ID. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search access token

The `Search access token` **Object** selection searches for action tokens relating to a user email address in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user primary or alias email address or their unique user ID. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search licenses assigned

The `Search licenses assigned` **Object** selection searches for product licenses assigned to a user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Product ID | Enter the product name to search for licenses. |
| Domain Name | Enter the domain name where the licenses reside. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search mobile device resources

The `Search mobile device resources` **Object** selection searches for user mobile device resources in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Max results | Select the maximum results to return in the response. |
| Query | Add a search string if required for retrieving results. |
| Page token | Provide the next page token in the list. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

## Search roles

The `Search roles` **Object** selection searches for roles in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Max results | Select the maximum results to return in the response. |
| Page token | Provide the next page token in the list. |

### Output

The **Search record** action generates output fields relevant to the newly added group object.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-transfer-data.md
description: >-
  Transfer data action allows you to transfer data from one user ID to another
  in the Google Workspace.
---

# Google Workspace - Transfer data action

The **Transfer data** action transfers data from one user ID to another in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection. You can use this action to transfer ownership from one user to another when off-boarding a user.

### Input

| Input field | Description |
| --- | --- |
| Old owner user ID | Enter the old owner user ID. |
| New owner user ID | Enter the new owner user ID. |
| Application data transfers source list | Select the source list for the transfer. Accepts list datapill as input. This list contains data transfer details of the applications associated with this transfer resource. |
| Application ID | Select the data transfer application. |
| Application transfer params source list | Select the parameters list for the transfer. Accepts list datapill as input. These parameters are used to select the data that gets transferred in context of this application. |
| Transfer parameter values | Select the parameter values to transfer. |
| Application transfer status | Select the application transfer status. |

### Output

The **Transfer data** action generates output fields relevant to the newly added group object.

---

---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-update-record.md
description: Update record action allows you to update an object in the Google Workspace.
---

# Google Workspace - Update record action

The **Update record** action updates an object in Google Workspace. You must select the **Object** type you plan to add before you can configure the action. The recipe editor generates additional fields based on your selection.

The **Update record** action supports the following **Object** types:

- [User](#update-a-user)
- [User to admin](#update-user-to-admin)
- [Group](#update-a-group)
- [Organizational unit](#update-org-unit)
- [Member to group](#update-group)
- [License](#update-license)

## Update a user

The `Update a user` **Object** selection updates a user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address to update. |
| Generate Password | Select `yes` to generate randomized password, or provide a custom password in the **custom password** field. |
| Organizational unit | Enter a new organizational unit name or select from the list. |
| Custom fields schema | Provision to add customer fields which can be passed on to update the user. |

> **ADDITIONAL INPUT FIELDS**
> 
> The recipe editor generates additional optional fields based on your Google Workspace configuration.

### Output

The **Update record** action generates output fields relevant to the newly added user object, including any custom fields defined in the **Custom fields schema**.

## Update user to admin

The `Update user to admin` **Object** selection updates a user to an admin in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user primary email address. |
| Admin Status | Select the user admin status to update. |

### Output

The **Update record** action generates output fields relevant to the newly added user object, including any custom fields defined in the **Custom fields schema**.

## Update a Group

The `Update a Group` **Object** selection updates a group in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group email address/Group ID | Enter the current group email address to update. |
| Description | Enter a group description. |
| Email address | Enter the group email address to update. |
| Group display name | Enter the group display name. |

### Output

The **Update record** action generates output fields relevant to the newly added user object, including any custom fields defined in the **Custom fields schema**.

## Update an organizational unit

The `Update an organizational unit` **Object** selection updates an organizational unit in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Organizational unit | Select the organizational unit. |
| Description | Enter the organizational unit description. |
| Organizational unit name | Enter the organizational unit path name. |
| Block inheritance | Select to inherit the settings of parent organizational unit or not. |
| Parent organizational path | Select or enter the parent organizational unit path. |

### Output

The **Update record** action generates output fields relevant to the newly added user object, including any custom fields defined in the **Custom fields schema**.

## Update a member of a group

The `Update a member of a group` **Object** selection updates a group member in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group email address | Enter the group email address, group alias, or unique group ID. |
| Group member email address | Enter the user or another group email address to update. |
| Mail delivery preferences | Select mail delivery frequency or disable mail delivery. |
| Group member role | Select the group member type. Options include `manager`, `member`, or `owner`. |

### Output

The **Update record** action generates output fields relevant to the newly added user object, including any custom fields defined in the **Custom fields schema**.

## Update a license

The `Update a license` **Object** selection updates a user product license in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Product ID | Enter the product name for which the user license needs an update. |
| SKU | Enter the product SKU unique identifier number. |
| User ID | Enter the user ID. Use the updated user email ID if the user email address has been updated. |
| SKU to update | Enter the product SKU unique identifier number to update. |

### Output

The **Update record** action generates output fields relevant to the newly added user object, including any custom fields defined in the **Custom fields schema**.

---
