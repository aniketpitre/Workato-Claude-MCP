---
url: 'https://docs.workato.com/en/connectors/active_directory/add_entry.md'
description: >-
  The Add entry action in the Active Directory connector lets you create a new
  entry, using a reference entry's attributes as a template.
---

# Active Directory - Add entry action

The **Add entry** action creates a new entry in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| Sample entry DN | Specify the distinguished name (DN) of a reference entry. The action uses this entry's attributes as a template to define sub-fields in the **Attributes to add** field. These attributes are then applied to the newly created entry and included in the action’s output. |
| Entry DN | Provide the distinguished name (DN) to identify the new entry in Active Directory. |
| Attributes to add | Enter values for the attributes you plan to add to the new entry. This field includes a sub-field for each attribute of the reference entry. |

## Output

The **Add entry** action's output includes values from the newly created entry for each attribute defined by the reference entry.

---
