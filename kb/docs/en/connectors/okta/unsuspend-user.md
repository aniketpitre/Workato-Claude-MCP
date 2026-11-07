---
url: 'https://docs.workato.com/en/connectors/okta/unsuspend-user.md'
description: >-
  The Un-suspend an existing user action in the Okta connector returns a
  suspended user to active status, and requires an administrator role.
---

# Okta - Un-suspend an existing user action

This action is used to un-suspend an existing user in Okta. This operation can only be performed on users with an SUSPENDED status. The user has a status of ACTIVE when the process is complete. Requires Organization Administrator or Super Administrator roles to use this action.

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |

## Output

| Field | Description |
| --- | --- |
| Unsuspended | Returns true if the user is successfully un-suspended. |

---
