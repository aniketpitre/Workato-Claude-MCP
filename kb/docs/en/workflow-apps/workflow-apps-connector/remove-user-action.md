---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/remove-user-action.md
description: >-
  Configure the Remove user action to remove a user from the Workflow apps
  portal by email using the Workflow apps connector.
---

# Remove user action

Remove a user from the Workflow apps portal. Refer to the [App-user and group management](/en/workflow-apps/app-user-groups) guide to manage app-users in the UI.

## Input

| Input field | Description |
| --- | --- |
| User email | Provide the email of the user you plan to remove from the Workflow apps portal. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Success | Whether the user is deleted successfully. Available values include `True` or `False`. |
