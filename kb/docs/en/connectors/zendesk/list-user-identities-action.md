---
url: 'https://docs.workato.com/en/connectors/zendesk/list-user-identities-action.md'
description: >-
  The List user identities action in the Zendesk connector lets you retrieve the
  list of identities for a specific user found by user ID.
---

# Zendesk - List user identities action (batch)

User identity is something that can be used to identify an individual. For example, an email address or a phone number.

This action selects a specific user and returns a list of user identities. It retrieves the user through a search by user ID. Only records in your Zendesk instance that matches the criteria will be returned.

![List user identities action](/assets/list-user-identities-action.DzSaecfx.png)_List user identities action_

## Input

| Input field | Description |
| --- | --- |
| User ID | The unique Zendesk ID of the user. |

## Output

The output of this action contains the full set of user identities from the selected user.

| Output field | Description |
| --- | --- |
| ID | Unique Zendesk user identity ID. This is automatically assigned when the user identity is created. |
| User ID | Unique Zendesk User ID. This is automatically assigned when the user is created. |
| Type | The type of user identity. Some possible values are `email`, `phone_number`, `sdk` etc. |
| Value | The value of the user identity. It is stored as a `string`. |
| Verified | Is `True` if the identity has been verified, otherwise it will display `False`. |
| Primary | Is `True` if the identity is marked as the primary identity, otherwise it will display `False`. For more information on primary user identity, please see the Zendesk documentation on this [topic](https://developer.zendesk.com/rest_api/docs/support/user_identities#make-identity-primary). |
| Created at | The time the identity was created. |
| Updated at | The time the identity was last updated. |
| List size | The size of the list, corresponding to the number of user identities retrieved. |

---

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

---
