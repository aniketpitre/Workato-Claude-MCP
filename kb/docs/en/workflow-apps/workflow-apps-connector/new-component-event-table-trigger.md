---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-component-event-table-trigger.md
description: >-
  Configure the New component event (Table widget) trigger to send data back to
  a table component when a Workflow app page loads.
---

# New component event (Table widget) trigger

The **New component event (Table widget)** trigger runs when a page is loaded in a Workflow app. Use this trigger in combination with the **Return data to component** action to send data back to a table component in a Workflow app.

## Input

| Input field | Description |
| --- | --- |
| Input parameters | Use input parameters to receive data from the Workflow apps page for use in your recipe. For example, you can use page data to search for relevant records in a third-party app. |
| Table schema | Enter fields to define the table's schema. |

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
