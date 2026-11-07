---
url: 'https://docs.workato.com/en/connectors/zendesk/create-user-action.md'
description: >-
  The Create user action in the Zendesk connector creates a single new user
  record in your Zendesk instance, including standard and custom fields.
---

# Zendesk - Create user action

This action creates a single user in your Zendesk instance.

![Create user action](/assets/create-user-action.BEApAKfN.png)_Create user action_

## Input

Here are some commonly used inputs.

| Input field | Description |
| --- | --- |
| Name | The name of the user. |
| Role | The role of the user. Permitted values are `End-user`, `Agent`, or `Administrator`. |
| Email | Mandatory if the user's role is designated as `Agent`. The primary email of the user. |
| User custom fields | Provide data for user custom fields. |

Click here for a full list of [user inputs](/en/connectors/zendesk/user-fields#user-input-fields).

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

---
