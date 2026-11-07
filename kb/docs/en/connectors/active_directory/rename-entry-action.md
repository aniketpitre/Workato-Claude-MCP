---
url: 'https://docs.workato.com/en/connectors/active_directory/rename-entry-action.md'
description: >-
  The Rename entry action in the Active Directory connector lets you change the
  distinguished name (DN) of an entry you specify.
---

# Active Directory - Rename entry action

The **Rename entry** action changes the distinguished name (DN) of an entry you specify in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| Existing entry DN | Specify the distinguished name (DN) of the entry you plan to rename. |
| New entry DN | Provide a new distinguished name (DN) for the entry. |

## Output

The **Rename entry** action does not have any output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/active_directory/search-groups-action.md
description: >-
  The Search group batch action in the Active Directory connector retrieves
  groups matching your criteria and processes them in batches.
---

# Active Directory - Search group action (Batch)

The **Search group** batch action retrieves a list of Active Directory groups matching the criteria you specify and processes them in batches.

## Input

| Input field | Description |
| --- | --- |
| Sample group DN | Specify the distinguished name (DN) of a reference group. The action uses this group’s attributes as a template to define sub-fields in the **Search groups by** field and retrieve values from matching groups. |
| Limit | Enter the maximum number of entries you plan to retrieve each trigger event. The maximum value is 1,000 entries. |
| Batch size | Optional. Enter the maximum number of entries to return in each batch. Defaults to `1000`. |
| Batch cookie | Optional. Enter the `Batch cookie` value from a previous iteration of this action to retrieve the next batch of results. Leave this field blank to retrieve the first batch. |
| Search groups by | Enter values for each attribute you plan to filter by. Only groups that match all the provided values are processed. This field includes sub-fields for each attribute of the reference group. |
| Advanced search filter | Enter [LDAP filters](https://ldap.com/ldap-filters/) to define search conditions. For example, enter `(ou=Dev)(objectClass=Group)` to retrieve only `Group` objects from the `Dev` organization unit. |

## Output

| Output field | Description |
| --- | --- |
| Batch cookie | A pagination token for the next batch of results. |
| Groups | Contains groups that match your search criteria, including values for each attribute defined by the sample group. |

---

---
url: >-
  https://docs.workato.com/en/connectors/active_directory/set-password-to-user-action.md
description: >-
  The Set password to user action in the Active Directory connector sets a new
  password for a user account over a secure LDAP connection.
---

# Active Directory - Set password to user action

The **Set password to user** action sets a new password for an Active Directory user account you specify. This action requires a secure LDAP connection.

## Input

| Input field | Description |
| --- | --- |
| User DN | Specify the distinguished name (DN) of the user account you plan set a new password for. |
| Password | Enter a new password for the user account. |
| Change password on the next login? | Specify whether to change the password on the user's next login. |

## Output

The **Rename entry** action does not have any output fields.

---
