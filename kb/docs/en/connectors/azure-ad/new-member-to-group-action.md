---
url: 'https://docs.workato.com/en/connectors/azure-ad/new-member-to-group-action.md'
description: Adds member to a group in Microsoft Entra ID.
---

# Microsoft Entra ID - Add member to group action

The **Add member to group** action adds a member to a group in Microsoft Entra ID.

## Input

| Input fields | Description |
| --- | --- |
| Group | Choose a group from the drop-down menu. Alternatively, enter a custom value if the group is not listed. |
| User | Choose a user from the drop-down menu. Alternatively, enter a custom value if the user is not listed. |

## Output

This action has no output.

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-ad/remove-member-from-group-action.md
description: >-
  Removes a member from a group. You will not be able to remove a member from
  groups with dynamic memberships.
---

# Microsoft Entra ID - Remove member from group action

The **Remove member from group** action removes a member from a group. You can't remove members from groups with dynamic memberships.

## Input

| Input fields | Description |
| --- | --- |
| Group | Choose a group from the drop-down menu. Alternatively, enter a custom value if the group is not listed. |
| User | Choose a user from the drop-down menu. Alternatively, enter a custom value if the user is not listed. |

## Output

This action has no output.

---

---
url: >-
  https://docs.workato.com/en/connectors/azure-ad/revoke-user-sign-in-session-action.md
description: Revokes user sign-in session.
---

# Microsoft Entra ID - Revoke sign-in session action

The **Revoke sign-in session** action invalidates a user’s refresh tokens to prevent unauthorized access to organization data. It resets the `signInSessionsValidFromDateTime` user property to the current date-time, which forces the user to sign in again to all previously authorized applications, regardless of the device. [Learn more](https://learn.microsoft.com/en-us/graph/api/user-revokesigninsessions).

## Input

| Input field | Description |
| --- | --- |
| Revoke current user sign-in session? | Choose whether to revoke the current user’s sign-in session. |
| User ID or user principal name | Enter the user ID or user principal name. |

## Output

| Output field | Description |
| --- | --- |
| Value | Returns `true` if the user’s session is revoked. |

---
