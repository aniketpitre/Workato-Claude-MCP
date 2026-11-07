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
