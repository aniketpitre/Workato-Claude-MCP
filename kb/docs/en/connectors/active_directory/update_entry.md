---
url: 'https://docs.workato.com/en/connectors/active_directory/update_entry.md'
description: >-
  The Update entry action in the Active Directory connector lets you update the
  attributes of an existing entry you specify by distinguished name.
---

# Active Directory - Update entry action

The **Update entry** action updates an existing entry you specify in Active Directory.

## Input

| Input field | Description |
| --- | --- |
| Sample entry DN | Specify the distinguished name (DN) of a reference entry. The action uses this entry’s attributes as a template to define sub-fields in the **Attributes to update** field and retrieve values from the updated entry. |
| Entry DN | Specify the distinguished name (DN) of the entry you plan to update. |
| Attributes to update | Enter new values for the attributes you plan to update. This field includes a sub-field for each attribute of the reference entry. |

## Output

The **Update entry** action's output includes values from the updated entry for each attribute defined by the reference entry.

---
