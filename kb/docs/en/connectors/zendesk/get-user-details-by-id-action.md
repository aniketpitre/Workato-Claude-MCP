---
url: >-
  https://docs.workato.com/en/connectors/zendesk/get-user-details-by-id-action.md
description: >-
  The Get user details by ID action in the Zendesk connector lets you retrieve
  details about a specific user that matches a search by user ID.
---

# Zendesk - Get user details by ID action

This action retrieves details about a specific user that matches a search by user ID. Only records in your Zendesk instance that matches the criteria will be returned.

![Get user details by ID action](/assets/get-user-by-id.CJ7LtXoL.png)_Get user details by ID action_

## Input

| Input field | Description |
| --- | --- |
| User ID | The unique Zendesk ID of the user. |

## Output

The output of this action contains the full set of columns from the selected user. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the user. This is automatically assigned when the user is created. |
| Role | The role of the user. Permitted values are `End-user`, `Agent`, or `Administrator`. |
| Email | The primary email of the user. |
| Organization ID | The unique Zendesk ID of the user's organization. If the user has more than one organization membership, it will display the user's default organization. |
| User custom fields | Includes data of user custom fields. |

Click here for a full list of [user outputs](/en/connectors/zendesk/user-fields#user-output-fields).
