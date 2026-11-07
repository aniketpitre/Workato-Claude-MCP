---
url: 'https://docs.workato.com/en/connectors/zendesk/create-organization-action.md'
description: >-
  The Create organization action in the Zendesk connector creates a single new
  organization record in your Zendesk instance.
---

# Zendesk - Create organization action

This action creates a single organization in your Zendesk instance.

![Create organization action](/assets/create-organization-action.Dwbe_ybf.png)_Create organization action_

## Input

| Input field | Description |
| --- | --- |
| Name | The name of the organization. |
| External ID | A unique identifier from another system. |
| Domain name | The domain name associated with this organization. |
| Details | Details about the organization. |
| Notes | Notes about the organization. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Shared tickets | Select `Yes` if the end-users in this organization are able to see each other's tickets, otherwise select `No`. |
| Shared comments | Select `Yes` if the end-users in this organization are able to see each other's comments on tickets, otherwise select `No`. |
| Tags | The tags applied to this organization. You can add multiple tags with the `,` separator. |
| Organization custom fields | Provide data for organization custom fields. |

Click here for a full list of [organization inputs](/en/connectors/zendesk/organization-fields#organization-input-fields).

## Output

The output of this trigger contains the full set of columns from the selected organization. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| ID | The unique Zendesk ID of the organization. This is automatically assigned when the organization is created. |
| Group ID | The unique Zendesk ID of the group of this organization. |
| Organization custom fields | Includes data of organization custom fields. |

Click here for a full list of [organization outputs](/en/connectors/zendesk/organization-fields#organization-output-fields).

---

---
url: >-
  https://docs.workato.com/en/connectors/zendesk/create-organization-membership-action.md
description: >-
  The Create organization membership action in the Zendesk connector connects an
  existing user to an existing organization by their Zendesk IDs.
---

# Zendesk - Create organization membership action

A membership links a user to an organization - An organization can have many users, and a users can be in many organizations.

This action connects an existing user to an existing organization. Both the user and the organization are identified by their Zendesk ID.

![Create organization membership action](/assets/create-organization-membership.CYRHz47S.png)_Create organization membership action_

## Input

| Input field | Description |
| --- | --- |
| User ID | The Zendesk ID of the user to be connected. |
| Organization ID | The Zendesk ID of the organization to be connected. |

## Output

| Output field | Description |
| --- | --- |
| User ID | The unique Zendesk ID of the user of this membership. |
| Organization ID | The unique Zendesk ID of the organization of this membership. |
| ID | The unique Zendesk ID of the organization membership. This is automatically assigned when the membership is created. |
| URL | The API URL of this membership. |
| Default | Is `True` if this is the default organization membership of the user, otherwise it will display `False`. |
| Created at | The time the organization membership was created. |
| Updated at | The time the organization membership was updated. |

---
