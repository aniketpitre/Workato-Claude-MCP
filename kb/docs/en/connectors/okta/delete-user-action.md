---
url: 'https://docs.workato.com/en/connectors/okta/delete-user-action.md'
description: >-
  The Delete user action in the Okta connector permanently deletes a
  deprovisioned user, an operation that cannot be recovered.
---

# Okta - Delete user action

This action deletes an existing user permanently.

This action only works on a user whose status is `Deprovisioned`. You can set a user to `Deprevisioned` with the [Deactivate user action](/en/connectors/okta/deactivate-user-action).

> **Warning!**
> 
> This action cannot be recovered! Refer to the Okta [Delete user](https://developer.okta.com/docs/reference/api/users/#delete-user) documentation for more information.

![Delete user action](/assets/delete-user.L3ytcFs7.png)_Delete user action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. If an invalid user ID is provided, it will cause a job error. |

## Output

There are no outputs for this action.

---
