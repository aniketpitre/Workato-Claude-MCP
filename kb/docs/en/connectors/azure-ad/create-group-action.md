---
url: 'https://docs.workato.com/en/connectors/azure-ad/create-group-action.md'
description: >-
  Creates a new security group anonymously. Groups created without specifying
  owners will not be modifiable.
---

# Microsoft Entra ID - Create group action

The **Create group** action creates a security group without assigned owners. If the group has no owners, no one can modify it.

## Input

| Input field | Description |
| --- | --- |
| Display name | Enter a display name for the group. This appears in lists, searches, and communication interfaces. |
| Mail nickname | Enter an alias for the group’s email address. This forms the local part of the email before the domain. |
| Mail enabled | Select **YES** to enable email for this group. |
| Security enabled | Select the boolean value (YES/NO) from the drop-down. |

## Output

Refer to the [New group trigger](/en/connectors/azure-ad/new-group-trigger#output) for output fields.

---
