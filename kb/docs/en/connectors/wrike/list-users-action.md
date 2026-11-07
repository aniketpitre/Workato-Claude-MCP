---
url: 'https://docs.workato.com/en/connectors/wrike/list-users-action.md'
description: >-
  The List users batch action in the Wrike connector retrieves all users and
  their IDs from the connected Wrike instance for use in later actions.
---

# Wrike - List users action (batch)

The **List users** batch action retrieves all users in the connected Wrike instance. You can use user IDs in subsequent Wrike actions.

## Input

This action doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Users | List of retrieved users. |
| ID | Unique identifier for the user. |
| First name | First name of the user. |
| Last name | Last name of the user. |
| Type | Type of user account. |
| Title | Job title of the user, if applicable. |
| Phone | Phone number of the user, if available. |
| Profiles | List of user profiles associated with the account. |
| Avatar URL | URL of the user’s avatar image. |
| Timezone | Time zone set in the user’s profile. |
| Locale | Language and region settings of the user. |
| Deleted | Indicates whether the user is deleted. |
| Member ID | Unique identifier for the user's membership in a Wrike workspace. |
| My team | Indicates whether the user is part of the **My team** group. |
| Custom fields | List of retrieved custom fields. |
| List size | Total number of users retrieved in the batch. |
| List index | Position of the current user in the batch. |

---
