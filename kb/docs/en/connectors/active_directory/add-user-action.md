---
url: 'https://docs.workato.com/en/connectors/active_directory/add-user-action.md'
description: >-
  The Add user action in the Active Directory connector lets you create a new
  user account, using a reference user's attributes as a template.
---

# Active Directory - Add user action

The **Add user** action creates a new user account in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| Sample user DN | Specify the distinguished name (DN) of a reference user. The action uses this user's attributes as a template to define sub-fields in the **Attributes to add** field. These attributes are then applied to the newly created user account and included in the action’s output. |
| User DN | Provide the distinguished name (DN) to identify the new user account in Active Directory. |
| Attributes to add | Enter values for the attributes you plan to add to the new user account. This field includes a sub-field for each attribute of the reference user account. |

## Output

The **Add user** action's output includes values from the newly created user account for each attribute defined by the reference user account.

---
