---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/return-data-component-action.md
description: >-
  Configure the Return data to component action to send data back to a Workflow
  app component, paired with a New component event trigger.
---

# Return data to component action

Use the **Return data to component** action to return data back to a component in a Workflow app. This action must be used in combination with the **New component event**, **New component event (Table widget)**, or **New component event (drop-down)** trigger. The recipe job stops immediately after this action.

## Input

| Input field | Description |
| --- | --- |
| Consider action as successful? | Use the **Consider action as successful?** drop-down to determine whether the action was completed successfully. |
| Output | Map in recipe datapills to return data to a page component. The fields in this section are dynamic and determined by the **Output schema** defined in the trigger. |
| Successful toast message | Optional. Provide a successful toast message to display to end-users if the action completes successfully. If left blank, no toast message is displayed to users. |
| Error message | Optional. Provide a custom error message to display to end-users if the action fails. If left blank, no error message is displayed to users. |

## Output

| Output field | Description |
| --- | --- |
| Successful toast message | The message that displays to end-users when the action completes successfully. |
| Error message | The message that displays to end-users when the action fails. |
| Output | The data returned to the Workflow app component. This object is dynamic and the output depends on the datapills mapped into the action input. |
