---
url: 'https://docs.workato.com/en/connectors/okta/activate-user-action.md'
description: >-
  The Activate user action in the Okta connector activates a staged user, with
  an option to send an activation email or return activation credentials.
---

# Okta - Activate user action

This action activates an existing user. Additionally, choose whether to send an activation email to the user.

> **User status restriction**
> 
> This operation can only be performed on users with a `Staged` status. Refer to the Okta [Reactivate user](https://developer.okta.com/docs/reference/api/users/#reactivate-user) documentation for more information.

![Activate user action](/assets/activate-user.-gMzEUWc.png)_Activate user action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |
| Send activation email to user | Specify if you want to send an activation email to the user. If set to **False**, the activation credentials will be returned as an output to this action. |

## Output

| Field | Description |
| --- | --- |
| Activation URL | The activation URL. |
| Activation Token | The activation token. |

---
