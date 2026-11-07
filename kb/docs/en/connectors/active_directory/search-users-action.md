---
url: 'https://docs.workato.com/en/connectors/active_directory/search-users-action.md'
description: >-
  The Search users batch action in the Active Directory connector retrieves user
  accounts matching your criteria and processes them in batches.
---

# Active Directory - Search users action (Batch)

The **Search users** batch action retrieves a list of Active Directory user accounts matching the criteria you specify and processes them in batches.

## Input

| Input field | Description |
| --- | --- |
| Sample user DN | Specify the distinguished name (DN) of a reference user account. The action uses this account’s attributes as a template to define sub-fields in the **Search users by** field and retrieve values from matching users. |
| Limit | Enter the maximum number of user accounts you plan to retrieve for each action. The maximum is 1,000 entries. |
| Batch size | Optional. Enter the maximum number of entries to return in each batch. Defaults to `1000`. |
| Batch cookie | Optional. Enter the `Batch cookie` from a previous iteration of this action to retrieve the next batch of results. Leave this field blank to retrieve the first batch. |
| Search users by | Enter values for each attribute you plan to filter by. Only user accounts that match all the provided values are processed. This field includes sub-fields for each attribute of the reference user account. |
| Advanced search filter | Enter [LDAP filters](https://ldap.com/ldap-filters/) to define search conditions. For example, enter `(ou=Dev)(objectClass=Person)` to retrieve only `Person` entries from the `Dev` organization unit. |

## Output

| Output field | Description |
| --- | --- |
| Batch cookie | A pagination token for the next batch of results. |
| Users | Returns the user accounts that match your search criteria, including values for each attribute defined by the sample user. |

---

---
url: >-
  https://docs.workato.com/en/connectors/active_directory/add-user-to-group-action.md
description: >-
  The Add user to group action in the Active Directory connector lets you add a
  user account to a group you specify.
---

# Active Directory - Add user to group action

The **Add user to group** action adds a user account to a group you specify in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| User DN | Specify the distinguished name (DN) of the user account you plan to add to the group. |
| Group DN | Specify the distinguished name (DN) of the group to which you plan to add the user account. |

## Output

The **Add user to group** action does not have any output fields.

---
