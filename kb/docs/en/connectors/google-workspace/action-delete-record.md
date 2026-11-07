---
url: >-
  https://docs.workato.com/en/connectors/google-workspace/action-delete-record.md
description: >-
  The Delete record action allows you to delete an object in the Google
  Workspace.
---

# Google Workspace - Delete record action

The **Delete record** action deletes an object in Google Workspace. To configure the action, you must first select the type of **Object** you plan to add. The recipe editor generates additional fields based on your selection.

The **Delete record** action supports the following **Object** types:

- [User](#delete-a-user)
- [User alias](#delete-a-user-alias)
- [Group](#delete-a-group)
- [Organizational unit](#delete-org-unit)
- [Member to group](#delete-member)
- [Role assignment](#delete-role-assign)
- [Verification code](#delete-code)
- [Delete access token](#delete-token)
- [Delete mobile device resource assigned to a user](#delete-mobile)
- [License](#delete-license)

## Delete a user

The `Delete a user` **Object** selection deletes a user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user primary or alias email address you plan to delete. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the user was successfully deleted. |

## Delete a user alias

The `Delete a user alias` **Object** selection deletes an alias email address of the user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user primary email address, alias email address, or unique user ID. |
| Alias | Enter the user alias email address. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the user alias was successfully deleted. |

## Delete a group

The `Delete a group` **Object** selection deletes a group in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group email address | Enter the group email address you plan to delete. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the group was successfully deleted. |

## Delete an organizational unit

The `Delete an organizational unit` **Object** selection deletes an organizational unit in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Organizational unit | Enter the organizational unit you plan to delete. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the organizational unit was successfully deleted. |

## Delete a member of a group

The `Delete a member of a group` **Object** selection deletes a member of a group in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Group email address | Enter the group email address, group alias, or unique group ID. |
| Group member email address | Select the user or group email address to delete from this group. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the group member was successfully deleted. |

## Delete a role assignment

The `Delete a role assignment` **Object** action deletes a user role assignment in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Role | Select the role to be deleted in Google Workspace. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the role assignment was successfully deleted. |

## Delete app specific passwords

The `Delete app specific passwords` **Object** selection deletes the user app specific passwords in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address, including primary, alias, or a unique user ID. |
| Code ID | Select the app-specific password unique ID to be deleted. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the app specific password was successfully deleted. |

## Delete verification code

The `Delete verification code` **Object** selection deletes the verification code associated with a user email address in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the verification code was successfully deleted. |

## Delete access token

The `Delete access token` **Object** selection deletes the access token issued to a client under a user.

### Input

| Input field | Description |
| --- | --- |
| Email address | Enter the user email address, including primary, alias, or a unique user ID. |
| Client ID | Enter the client ID of the application to which the token is issued. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the access token was successfully deleted. |

## Delete license assigned to a user

The `Delete license assigned to a user` **Object** selection deletes a product license assigned to a user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Product ID | Enter the product name for which you plan to delete the user license. |
| SKU to update | Enter the product SKU unique identifier. |
| Email ID | Enter the user email ID that's associated with the license you plan to delete. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the license was successfully deleted. |

## Delete mobile device resource assigned to a user

The `Delete mobile device resource assigned to a user` **Object** selection deletes a mobile device resource assigned to a user in Google Workspace.

### Input

| Input field | Description |
| --- | --- |
| Resource ID | Enter the API service unique ID used to identify the mobile device. |

### Output

| Output field | Description |
| --- | --- |
| Deleted | A boolean (`true` or `false`) value indicating whether the mobile device resource was successfully deleted. |
