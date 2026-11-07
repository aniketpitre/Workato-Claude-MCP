---
url: 'https://docs.workato.com/en/connectors/okta/deactivate-user-action.md'
description: >-
  The Deactivate user action in the Okta connector deactivates a user and sets
  the status to deprovisioned, a destructive, unrecoverable operation.
---

# Okta - Deactivate user action

This action deactivates an existing user and sets the user status to `Deprovisioned`.

> **Warning!**
> 
> Deactivating a user is a destructive operation. The user is deprovisioned from all assigned applications which may destroy their data such as email or files. This action cannot be recovered! Refer to the Okta [Deactivate user](https://developer.okta.com/docs/reference/api/users/#deactivate-user) documentation for more information.

![Deactivate user action](/assets/deactivate-user.BwrlIMyQ.png)_Deactivate user action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |

## Output

There are no outputs for this action.

---
