---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/change-workflow-stage-action.md
description: >-
  Configure the Change workflow stage action to transition a request through
  stages in a Workflow app, such as marking it Done or Invalid.
---

# Change workflow stage action

**Change workflow stage** is an action you can use to transition a request in a Workflow app through the workflow.

Typical use cases for this action include the following scenarios:

- If the input provided does not pass validation, mark the request as **Invalid**.
- If the request does not need user approval, mark it as **Done** automatically.
- If the manager approval task is approved, mark the request as **Completed**.

* * *

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select an App from the list of available Apps. |
| Record ID | The ID of the record whose workflow stage you plan to change. You can map this in using a datapill from a trigger or action from the Workato Data Tables or Workflow apps connector. |
| Workflow stage | The new workflow stage for the record. Select one of the stages defined in your [application settings](/en/workflow-apps/interface#pages-assign). |

## Output

There is no output for this action.
