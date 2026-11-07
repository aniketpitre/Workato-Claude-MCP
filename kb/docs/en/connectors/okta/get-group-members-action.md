---
url: 'https://docs.workato.com/en/connectors/okta/get-group-members-action.md'
description: >-
  The Get user group members action in the Okta connector retrieves the list of
  users belonging to a specified group, with status and profile data.
---

# Okta - Get user group members action

This action retrieves a list of users of a specified group in your Okta instance.

![Get group members action](/assets/get-group-members.CKiHa_Zc.png)_Get group members action_

## Input

| Field | Description |
| --- | --- |
| Group ID | The unique ID of the group. |
| Page size | The maximum number of records to return in a single response. Default to 1000. |
| Next page token | The token for continuing a previous list request on the next page. Provide the token from a previous response here. |
| Group ID | The unique ID of the group. |

## Output

The output datatree contains a list of members. Each member contains information like the user ID and status.

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
| List size | The number of members in the group. |
| List index | The index of this user in the list of members. |

---

---
url: >-
  https://docs.workato.com/en/connectors/okta/get-recent-events-by-user-action.md
description: >-
  The Get recent log on events by user action in the Okta connector lets you
  retrieve up to 100 log events from the last 12 hours for a specific user.
---

# Okta - Get recent log on events by user action

This action retrieves a log on recent events for a specific user. This action uses the email address to identify the user.

This action will retrieve up to 100 actions from the last 12 hours.

![Get recent log on events by user ction](/assets/get-recent-log-on-events-by-user.BpQC--eJ.png)_Get recent log on events by user action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |

## Output

The output datatree contains a list of logs on events. Each log event contains information about the event like the timestamp, the actor, the client used, the authentication and security contents.

Refer to [Event outputs](/en/connectors/okta/events-output-datatree) for the full list of output fields.

---
