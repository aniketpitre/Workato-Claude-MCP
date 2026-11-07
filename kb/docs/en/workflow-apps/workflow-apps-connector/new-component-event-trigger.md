---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-component-event-trigger.md
description: >-
  Configure the New component event trigger to run a recipe when a Run recipe
  action is invoked and return data to a Workflow app component.
---

# New component event trigger

The **New component event** trigger runs when a [Run recipe action](/en/workflow-apps/component-actions/run-recipe) is invoked in the Workflow apps portal. Use this trigger in combination with the **Return data to component** action to send data back to a page component in a Workflow app.

## Input

| Input field | Description |
| --- | --- |
| Input parameters | Use input parameters to receive data from the Workflow apps page for use in your recipe. For example, you can use page data to search for relevant records in a third-party app. |
| Output schema | Specify output fields to send data obtained in this recipe back to your Workflow apps page. |

* * *

## Output

| Output field | Description |
| --- | --- |
| Context | The context object contains information about the Workflow apps user using the page, including app-user details and group membership. |
| Workflow apps user | This object is nested within the `Context` object and contains the following available attributes: `User ID`: The ID of the user., `User name`: The user's name., `User email`: The user's email address., `Status`: The user's status., `Groups`: An object nested within the `Workflow apps user` object and contains information about user group membership. |
| Parameters | The parameters object is nested within the `Context` object and contains input parameters defined in the trigger. This object is empty if you haven't defined any input parameters. |
