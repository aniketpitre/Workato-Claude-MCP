---
url: 'https://docs.workato.com/en/connectors/active_directory/add-group-action.md'
description: >-
  The Add group action in the Active Directory connector lets you create a new
  group, using a reference group's attributes as a template.
---

# Active Directory - Add group action

The **Add group** action creates a new group in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| Sample group DN | Specify the distinguished name (DN) of a reference group. The action uses this group’s attributes as a template to define sub-fields in the **Attributes to add** field. These attributes are then applied to the newly created group and included in the action’s output. |
| Group DN | Provide the distinguished name (DN) to identify the new group in Active Directory. |
| Attributes to add | Enter values for the attributes you plan to add to the new group. This field includes a sub-field for each attribute of the reference group. |

## Output

The **Add group** action's output includes values from the newly created group for each attribute defined by the reference group.

---
