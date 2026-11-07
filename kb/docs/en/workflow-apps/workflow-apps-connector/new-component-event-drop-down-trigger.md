---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-component-event-drop-down-trigger.md
description: >-
  Configure the New component event (drop-down) trigger to populate Workflow app
  drop-down components with data from a third-party app.
---

# New component event (drop-down) trigger

The **New component event (drop-down)** real-time trigger runs when a drop-down component is opened in a Workflow app. This trigger enables you to populate drop-down components with data from a third-party app. Use this trigger in combination with the **Return data to component** action to send data back to a drop-down component in a Workflow app.

## Input

| Input field | Description |
| --- | --- |
| Input parameters | Use input parameters to receive data from the Workflow apps page for use in your recipe. For example, you can use page data to search for relevant records in a third-party app. |
| Use recipe to find search results? | Select `Yes` and use the Search Query datapill in the recipe to enable typeahead search in drop-down components. Select `No` if the drop-down contains fewer than 1,000 options and all records can be retrieved at once. |
| Minimum search characters to trigger the recipe | Specify the minimum number of characters to trigger the recipe. The default value is `3`. Alternatively, enter `0` to trigger recipe immediately when the drop-down opens without requiring user input. |

## Output

| Output field | Description |
| --- | --- |
| Context | This object contains information about the Workflow apps user accessing the page, including app-user details and group membership. |
| Workflow apps user (Context) | An object nested within the `Context` object containing information about the user who accesses the application. |
| User ID (Workflow apps user) | The user's unique identifier. |
| User name (Workflow apps user) | The user's name. |
| User email (Workflow apps user) | The user's email address. |
| Status(Workflow apps user) | The user's status, such as `active` or `inactive`. |
| Groups (Workflow apps user) | An object nested within the `Workflow apps user` object containing information about the user's group membership. |
| Parameters | Contains input parameters defined in the trigger. This object is empty if you haven't defined any input parameters. |
| Search query | The search term used in the drop-down component on the Workflow apps page. Map this datapill into other actions if you are using the recipe to find search results. |
