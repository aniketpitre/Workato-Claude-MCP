---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/get-user-data-action.md
description: >-
  Configure the Get user data (batch) action to retrieve user details from the
  Workflow apps portal by email, user group, and sort options.
---

# Get user data action (batch)

Get user data from the Workflow apps portal.

## Input

| Input field | Description |
| --- | --- |
| Email address | Provide the user email to retrieve the user data. |
| User groups | Select user groups from the list to retrieve user data for all users in each group. |
| Sort by | Specify how to sort the results. Available options include `Name`, `Email`, and `Status`. |
| Sort direction | Determine whether to sort the results in `Ascending` or `Descending` order. |
| Entries per page | Limit the number of users returned in this action. The default value is 500 and the maximum value is 500. |
| Next page token | Get users starting with the given offset. |

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
