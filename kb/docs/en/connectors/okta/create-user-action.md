---
url: 'https://docs.workato.com/en/connectors/okta/create-user-action.md'
description: >-
  The Create user action in the Okta connector creates a new user, with profile,
  credentials, and an option to activate the user on creation.
---

# Okta - Create user action

This action creates a new user.

![Create user action](/assets/create-user.CsvhxPFf.png)_Create user action_

## Input

The input configuration contains the full set of user properties. Refer to the Okta [user object](https://developer.okta.com/docs/reference/api/users/#user-object) documentation for more information on user properties.

Below are the commonly used user properties.

| Input field | Description |
| --- | --- |
| Profile | First name | First name for the new user. |
| Last name | Last name for the new user. |
| Primary email ID | Primary email address of the new user. |
| Username | A unique identifier for the user. This must be an email. |
| Title | Title of the new user. |
| Employee number | An organization assigned identifier for the new user. |
| Manager ID | The Okta ID of the user's manager. |
| Manager | The display name of the user's manager |
| Credentials | Password | The password for the new user. The password must be a minimum of 8 characters, contain an uppercase, lowercase, and digit character. Refer to the Okta [default password policy](https://developer.okta.com/docs/reference/api/users/#default-password-policy) documentation for more information. |
| Recovery question | The secret question and answer that is validated when a user forgets their password. |
| Activate user | Executes the activation lifecycle when creating the user. If set to **False**, you can activate the user at a later time with the [Activate user action](/en/connectors/okta/activate-user-action.md). |

## Output

The output datatree contains information about the user like the ID and status.

| Field | Description |
| --- | --- |
| ID | The unique ID for the user. |
| Status | The current status of the user. |
| Created time | The timestamp when the user was created. |
| Activated time | The timestamp when the user's status was updated to `Active`. |
| Status changed time | The timestamp when the status was last changed. |
| Last login time | The timestamp when the user was last logged in. |
| Last updated time | The timestamp when the user was last updated. |
| Password changed time | The timestamp when the password was last changed. |
| Profile | This object contains information about the user's profile, including first and last name, email, organization, and title. Refer to the Okta [user profile object](https://developer.okta.com/docs/reference/api/users/#profile-object) documentation for more information. |
| Credentials | This object specifies the primary authentication and recovery credentials for the user. It includes the recovery question and credentials provider. |
| Links | This object contains a collection of link relations for the user. It includes lifecycle operations and credentials operations. Refer to the Okta [user links object](https://developer.okta.com/docs/reference/api/users/#links-object) documentation for more information. |

---
