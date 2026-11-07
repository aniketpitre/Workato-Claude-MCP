---
url: 'https://docs.workato.com/en/connectors/jira/get-user-details-action.md'
description: >-
  This action retrieves a user from Jira. This action fails if the user doesn't
  exist.
---

# Jira - Get user details action

The **Get user details** action retrieves a user from Jira. This action fails if the user doesn't exist.

## Input

| Input field | Description |
| --- | --- |
| Username | Enter the username to search for in Jira. For example, enter `johndoe` if the user's email address is `johndoe@workato.com`. |
| Email | Enter the email to search for in Jira. For example: `johndoe@workato.com` |

## Output

| Output field | Description |
| --- | --- |
| Self | The API URL of the user. |
| Key | The human-readable Jira identifier for the user. |
| Name | The login username of the user. |
| Account ID | The Atlassian account identifier for the user. |
| Email address | The email address of the user. |
| Avatar URLs | URLs of the user's avatar images. |
| Display name | The display name of the user. |
| Active | Indicates whether the user's account is active. |
| Time zone | The timezone of the user. |
| Locale | The language and formatting preferences of the user. |
| Expand | Fields expanded in the response, such as groups and application roles the user is a member of. |

---

---
url: >-
  https://docs.workato.com/en/connectors/jira/search-assignable-users-batch-action.md
description: >-
  This action retrieves a list of all users that can be assigned to a specific
  issue.
---

# Jira - Search assignable users action (batch)

The **Search assignable users (batch)** action retrieves a list of all users that can be assigned to a specific issue. You can provide the user's login username to narrow the list down to a single user.

## Input

| Input field | Description |
| --- | --- |
| Project ID or key | Enter the ID or key of the project to search within. |
| Issue ID or key | Enter the ID or key of the issue to find assignable users for. |
| Username | Optional. Enter a specific username to search for in Jira. For example, enter `johndoe` if the user's email address is `johndoe@workato.com`. The action returns an empty list if the specified user can't be assigned or the username is invalid. Leave this blank to retrieve all assignable users. |

## Output

| Output field | Description |
| --- | --- |
| Self URL | The API URL of the user. |
| Key | The human-readable Jira identifier for the user. |
| Name | The login username of the user. |
| Account ID | The Atlassian account identifier for the user. |
| Email address | The email address of the user. |
| Avatar URLs | URLs of the user's avatar images. |
| Display name | The display name of the user. |
| Active | Indicates whether the user's account is active. |
| Time zone | The timezone of the user. |
| Locale | The language and formatting preferences of the user. |
| Groups | Contains information about groups the user is a member of, including `Size` and `Items`. |
| Application roles | Contains information about the application roles assigned to the user, including `Size` and `Items`. |
| Expand | Fields expanded in the response, such as groups and application roles the user is a member of. |
| Last login time | The date and time the user last logged in. |
| List size | The total number of retrieved users. |
| List index | The position of the current user in the results list. |

---
