---
url: >-
  https://docs.workato.com/en/connectors/zendesk/search-organization-member-action.md
description: >-
  The Search organization member action in the Zendesk connector lets you
  retrieve a list of all members in a specified organization.
---

# Zendesk - Search organization member action (batch)

A membership links a user to an organization - An organization can have many users, and a users can be in many organizations.

This action retrieves a list of all members in a specified organization. Only records in your Zendesk instance that matches all the criteria will be returned.

![Search organization member action](/assets/search-organization-member-action.UIloclKm.png)_Search organization member action_

## Input

| Input field | Description |
| --- | --- |
| Organization ID | The unique Zendesk ID of the organization. |
| Name | The name of the member. |
| Email | The email of the member. |

## Output

The output of this action contains a list of members with their respective outputs. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | Unique Zendesk user ID. This is automatically assigned when the user is created. |
| Role | The role of the user. Permitted values are `End-user`, `Agent`, or `Administrator`. |
| Email | The primary email of the user. |
| Organization ID | The unique Zendesk ID of the user's organization. If the user has more than one organization membership, it will display the user's default organization. |
| User custom fields | Includes data of user custom fields. |
| List size | The size of the list, corresponding to the number of members retrieved. |

Click here for a full list of [user outputs](/en/connectors/zendesk/user-fields#user-output-fields).
