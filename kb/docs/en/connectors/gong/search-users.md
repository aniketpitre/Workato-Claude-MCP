---
url: 'https://docs.workato.com/en/connectors/gong/search-users.md'
description: >-
  The Search users action in the Gong connector looks up users by their Gong
  internal IDs and returns their profile details.
---

# Gong - Search users action

This action will search users in Gong. It searches for users in Gong via their Gong internal IDs.

## Input

| Field | Description |
| --- | --- |
| User IDs | List of users to be filtered. If not supplied, all users are returned. |

## Output

User specific output fields will be dynamically rendered base on the users returned. A sample response structure is below.

| Field | Description |
| --- | --- |
| Users _A list of following fields for each user_ | Active | Field indicating whether the user is currently active. |
| Created | Datetime when the user was created. |
| Email address | Email address of the user. |
| Email alias | List of email aliases of the user. |
| First name | First name of user. |
| Last name | Last name of user. |
| Title | Title of the user. |
| ID | UUID of the user. |
| Manager ID | UUID of the manager. |
| Personal meeting urls | List of personal meeting urls of the user. |
| Meeting consent page url | Meeting consent page url of the user. |
| Extension | Extension of the phone number of the user. |
| Phone number | User's phone number. |
| Settings | Object containing the relevant settings of a user's gong account. |
| List Size | The list size of the call transcripts. |
| List Index | An index for each item in the list of call transcripts. |
| Records _Metadata of the response_ | Current page number | Necessary for repeat requests to ensure pagination. |
| Current page size | Number of records on the current page. |
| Cursor | UUID necessary for pagination. |
| Total Records | Total number of records that can be queried. |

---
