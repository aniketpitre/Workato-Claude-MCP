---
url: 'https://docs.workato.com/en/connectors/okta/get-user-groups-action.md'
description: >-
  The Get user groups action in the Okta connector retrieves the group
  memberships of a specific user, including group ID and profile details.
---

# Okta - Get user groups action

This action retrieves the group memberships of a specific user.

![Get user groups action](/assets/get-user-groups.BxA3D9SI.png)_Get user groups action_

## Input

| Field | Description |
| --- | --- |
| User ID | The unique ID of the target user. |
| Page size | The maximum number of records to return in a single response. Default to 10000. |
| Next page token | The token for continuing a previous list request on the next page. Provide the token from a previous response here. |

## Output

The output datatree contains a list of group memberships. Each group membership contains information like the group ID and group profile properties.

| Field | Description |
| --- | --- |
| ID | The unique ID for the group. |
| Creation time | The timestamp when the group was created. |
| Last modification time | The timestamp when the group was last modified. |
| Last membership updated time | The timestamp when the group's membership was last updated. |
| Object class | An array of strings. This determines the group profile. |
| Type | This determines how a group's profile and membership are managed. |
| Profile | Information about the group, including name and description of the group. |
| Links | This object contains a collection of link relations for the group. It includes lifecycle operations and related resources. Refer to the Okta [group links object](https://developer.okta.com/docs/reference/api/groups/#links-object) documentation for more information. |
| List size | The number of groups in the list. |
| List index | The index of this group in the list of groups. |

---
