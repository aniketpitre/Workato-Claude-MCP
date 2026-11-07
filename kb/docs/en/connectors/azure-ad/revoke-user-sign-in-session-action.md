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
