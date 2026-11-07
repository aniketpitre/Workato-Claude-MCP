---
url: >-
  https://docs.workato.com/en/connectors/okta/expire-an-existing-user-password.md
description: >-
  The Expire an existing user password action in the Okta connector expires a
  user password and can optionally return a temporary password.
---

# Okta - Expire an existing user password action

This action expires an existing user’s password in Okta and optionally returns a temporary password. Requires Organization Administrator or Super Administrator roles to use this action.

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |
| Return temporary password | Choose whether to return a temporary password in the response of the action or not. Useful when the temporary password is needed by downstream actions. Defaults to false. |

## Output

| Field | Description |
| --- | --- |
| Temporary password | Temporary password is returned if return temporary password is set to true. |
