---
url: 'https://docs.workato.com/en/connectors/active_directory/update-user-action.md'
description: >-
  The Update user action in the Active Directory connector lets you update the
  attributes of an existing user account you specify.
---

# Active Directory - Update user action

The **Update user** action updates an existing user account you specify in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| Sample user DN | Specify the distinguished name (DN) of a reference user account. The action uses this account’s attributes as a template to define sub-fields in the **Attributes to update** field and retrieve values from the updated user. |
| User DN | Specify the distinguished name (DN) of the user account you plan to update. |
| Attributes to update | Enter new values for the attributes you plan to update. This field includes a sub-field for each attribute of the reference user account. |

## Output

The **Update user** action's output includes values from the updated user account for each attribute defined by the reference user account.

---
