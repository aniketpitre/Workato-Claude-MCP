---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/invite-user-action.md
description: >-
  Configure the Invite user action to send an email invitation to the Workflow
  apps portal and add the user to one or more user groups.
---

# Invite user

Invite a user by email to the Workflow apps portal. The user must accept the invitation before using the portal.

## Input

| Input field | Description |
| --- | --- |
| Name | The name of the user you plan to invite to the portal. |
| Email address | Provide the email address to send the invite to. |
| User groups | Add the user to one or more user groups. If left blank, the user is added to the **Everyone** group by default. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Users | An object containing information about the user. |
| User ID (Users) | The ID of the user. |
| User name (Users) | The user's name. |
| User email (Users) | The user's email address. |
| Status (Users) | The user's status. |
| Groups (Users) | An object nested within the `Users` object. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Continuation token | The token used to paginate through entries. |
| Entries per page | The number of entries per page. |
