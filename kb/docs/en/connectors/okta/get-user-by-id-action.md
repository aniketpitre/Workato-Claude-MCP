---
url: 'https://docs.workato.com/en/connectors/okta/get-user-by-id-action.md'
description: >-
  The Get user by ID action in the Okta connector retrieves the account details
  of a specific user, including status, profile, and credentials.
---

# Okta - Get user by ID action

This action retrieves account details of a specific user.

![Get user by ID action](/assets/get-user-by-id.CdWJm5R9.png)_Get user by ID action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |

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
