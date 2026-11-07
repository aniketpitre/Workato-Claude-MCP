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
