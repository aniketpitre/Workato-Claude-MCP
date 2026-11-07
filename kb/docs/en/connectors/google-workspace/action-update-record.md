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
