---
url: 'https://docs.workato.com/en/connectors/zendesk/search-users-action.md'
description: >-
  The Search users action in the Zendesk connector lets you retrieve a list of
  users in your instance that match your search criteria.
---

# Zendesk - Search users action (batch)

This action retrieves a list of all users that matches your search criteria. Only records in your Zendesk instance that matches all the criteria will be returned.

![Search user action](/assets/search-user-action.Cxxgdgy_.png)_Search user action_

## Input

| Input field | Description |
| --- | --- |
| Name | The name of the user. |
| Email | The email of the user. |
| Organization | The name of the user's organization. |
| External ID | A unique identifier from another system. |
| Tags | The tags applied to this user. You can query multiple tags with the `,` separator. |
| Notes | Notes about the user. |

## Output

The output of this action contains a list of user with their respective outputs. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the user. This is automatically assigned when the user is created. |
| Role | The role of the user. Permitted values are `End-user`, `Agent`, or `Administrator`. |
| Email | The primary email of the user. |
| Organization ID | The unique Zendesk ID of the user's organization. If the user has more than one organization membership, it will display the user's default organization. |
| User custom fields | Includes data of user custom fields. |
| List size | The size of the list, corresponding to the number of users retrieved. |

Click here for a full list of [user outputs](/en/connectors/zendesk/user-fields#user-output-fields).

---
