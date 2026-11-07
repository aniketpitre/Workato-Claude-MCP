---
url: >-
  https://docs.workato.com/en/connectors/authhub/remove-member-from-a-group-action.md
description: >-
  The Remove member from a group action removes multiple members from an AuthHub
  group.
---

# AuthHub - Remove member from a group action

The **Remove member from a group** action removes multiple members from an AuthHub group.

## Input

| Input field | Description |
| --- | --- |
| Users | Enter a list of users to remove from the group. |
| Username | Enter the username of the member to remove from the group. |
| Group ID | Enter the unique ID of the group from which to remove members. |

## Output

| Output field | Description |
| --- | --- |
| Schemas | A list of object schemas returned by the response. |
| Display name | The display name of the group from which members were removed. |
| ID | The unique ID of the group. |
| Members results | An object containing information about group members, such as `Total results` which lists the number of members in the group. |
| Meta | An object containing information about the group, such as the date and time the group was `Created` and `Last modified`. |
