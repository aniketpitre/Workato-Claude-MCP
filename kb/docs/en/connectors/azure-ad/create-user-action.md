---
url: 'https://docs.workato.com/en/connectors/azure-ad/create-user-action.md'
description: >-
  Creates a new security group anonymously. Groups created without specifying
  owners will not be modifiable.
---

# Microsoft Entra ID - Create user action

The **Create user** action creates a user in Microsoft Entra ID.

## Input

| Input field | Description |
| --- | --- |
| Display name | Enter a display name for the user. This appears in lists, searches, and communication interfaces. |
| Mail nickname | Enter an alias for the user’s email address. This forms the local part of the email before the domain. |
| User principal name | Enter the user’s sign-in name in Microsoft Entra ID. |
| Password | Enter a password for the user. |
| Force change password next sign in | Select **YES** to require the user to change their password at next sign-in. |
| Account enabled | Select the boolean value (YES/NO) from the drop-down. |

Refer to the [User schema](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0#properties) documentation for more information about optional fields.

## Output

Refer to the [User schema](https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0#properties) documentation for more information about output fields.

---
