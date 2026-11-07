---
url: 'https://docs.workato.com/en/connectors/kickflow/new-event-trigger.md'
description: >-
  The New event trigger starts a recipe when a subscribed ticket event occurs in
  Kickflow.
---

# Kickflow - New event trigger

The **New event** trigger starts a recipe when a subscribed ticket event occurs in Kickflow.

## Input

| Input field | Description |
| --- | --- |
| Event | Select one or more ticket events to trigger on, such as `Ticket created` or `Ticket approved`. |
| Workflow | Optional. Select the ticket's workflow to include the ticket's formatted workflow inputs in the output. |
| Signature | Optional. Enter the secret you set when you registered the webhook in Kickflow. This verifies that events originate from Kickflow. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Kickflow](https://developer.kickflow.com/rest/spec) documentation for a complete list of output fields.

---
