---
url: 'https://docs.workato.com/en/connectors/okta/reset-user-password.md'
description: >-
  The Okta connector action resets an active user's forgotten password and can
  optionally email a one-time token link to the user.
---

# Okta - Reset an existing user's forgotten password action

This action resets an existing user’s forgotten password and optionally sends them the one-time token (OTT) link via email. Please note that the user must be in ACTIVE state and will be required to validate their security question's answer when visiting the reset link. User’s state will still remain ACTIVE in this case. Requires Organization Administrator or Super Administrator roles to use this action.

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |
| Send forgotten password email to user | Choose whether to send the forgotten password email automatically to user. User needs to validate by answering the security question before setting the new password. If set to false, returns a link for the user to reset their password in the response. Allowed values are: true or false. Default is true. |

## Output

| Field | Description |
| --- | --- |
| Sent forgotten password email | Shows whether the email was sent successfully or not if "Send forgotten password email to user" is set to true. |
| Forgotten password reset URL | Returns reset URL if "Send forgotten password email to user" is set to false. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/okta/list-applications-assigned-to-user.md
description: >-
  The List applications assigned to user action in the Okta connector returns
  the applications assigned to a user with their metadata.
---

# Okta - List applications assigned to user action

This lists the applications that are assigned under a user with the associated metadata information.

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |
| Page size | The maximum number of records to return in a single response. Default to 50. |
| Next page token | The token for continuing a previous list request on the next page. Provide the token from a previous response here. |

## Output

The output datatree contains a list of user applications. Each user application contains information like the application ID and application name. Refer to the Okta [Apps API response parameters](https://developer.okta.com/docs/reference/api/apps/#response-parameters-14) documentation for more details on the output fields.

| Field | Description |
| --- | --- |
| ID | The unique ID for the application. |
| Name | The name of the application. |
| Label | The label added to the application. |
| Status | Current status of the user's application. |
| Creation | The timestamp when the application was created. |
| Last updated | The timestamp when the application was last updated. |
| Accessibility | Object containing details such as whether the application is self service or not, the login URL, etc. |
| Visibility | Object containing visibility details about the application. |
| Links | Object containing specific links to users, groups and so on. |
| Credentials | Object containing credential-related details such as whether the password is revealed or not. |
| Embedded | Object containing user details. |
| List size | The number of groups in the list. |
| List index | The index of this group in the list of groups. |

---
