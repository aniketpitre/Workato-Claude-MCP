---
url: 'https://docs.workato.com/en/connectors/authhub/add-member-to-a-group-action.md'
description: The Add member to a group action adds multiple members to a group in AuthHub.
---

# AuthHub - Add member to a group action

The **Add member to a group** action adds multiple members to a group in AuthHub.

## Input

| Input field | Description |
| --- | --- |
| Users | Enter a list of users to add to the group. |
| Username | Enter the username of the member to add to the group. |
| Group ID | Enter the ID of the group in which to add the members. |

## Output

| Output field | Description |
| --- | --- |
| Schemas | A list of object schemas returned by the response. |
| Display name | The display name of the group. |
| ID | The unique ID of the group. |
| Members results | An object containing information about group members, such as `Total results` which lists the number of members in the group. |
| Meta | An object containing information about the group, such as the date and time the group was `Created` and `Last modified`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/authhub/get-record-details-by-id-action.md
description: The Get record details by ID action retrieves a record from AuthHub.
---

# AuthHub - Get record details by ID action

The **Get record details by ID** action retrieves a record from AuthHub. The current version of the AuthHub connector only supports the **User** object for this action.

## Input

| Input field | Description |
| --- | --- |
| ID | Enter the unique ID of the user to fetch. |

## Output

| Output field | Description |
| --- | --- |
| Active | Indicates whether the user is active. |
| Display name | The email address of the user. |
| ID | The unique ID of the user. |
| Locale | The preferred language of the user. |
| Title | The job title of the user. |
| User name | The username of the user. |

---

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

---
