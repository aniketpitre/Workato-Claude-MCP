---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-genie-connector/actions/send-business-event.md
description: >-
  Send a business event to a genie and deliver a notification to a specified
  user.
---

# Workato Genie connector - Send business event action

The **Send business event** action sends a business event to a genie and delivers a notification to a specified user. The recipe continues immediately after sending the event without waiting for the genie to finish processing.

Use this action when a user needs to be informed of an event and may need to take action. Use the [Assign task to genie](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-genie) action for automated tasks that don't require a user. Refer to [App Events vs Agent orchestration](/en/agentic/agent-studio/app-events-vs-agent-orchestration) for a full comparison.

## Input

| Input field | Description |
| --- | --- |
| Genie | Select the genie to send the business event to. |
| User email | Enter the email address of the user who should receive the event. The user must be active and have assigned access to this genie. The action fails if the user doesn't exist in Workato or doesn't have access to the genie. |
| Notification to user | Enter the message to send to the user before the genie begins processing the event. |
| Business event data | Enter a prompt describing what the genie should do in response to this event. Include all context the genie needs to complete the task. |
| Conversation ID | Enter the ID of an existing conversation to continue that thread rather than starting a new one. Refer to [Continue conversation](/en/agentic/agent-studio/app-events/conversations#continue-conversation) for more information. |

## Output

| Output field | Description |
| --- | --- |
| Conversation ID | The ID of the conversation created or continued by this event. |
