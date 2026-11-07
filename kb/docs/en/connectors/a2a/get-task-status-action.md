---
url: 'https://docs.workato.com/en/connectors/a2a/get-task-status-action.md'
description: >-
  The Get task status action retrieves the current state and available artifacts
  of an A2A Protocol task.
---

# A2A Protocol - Get task status action

The **Get task status** action retrieves the current state and available artifacts of a task sent to the connected agent in A2A Protocol. Use this action to check on a task that was sent asynchronously, or to inspect the result of any task.

This action performs a single point-in-time read. It doesn't poll or wait for the task to reach a terminal state. Use the **Send task** action with **Wait for result?** set to `Yes` to wait for a task to complete in a single recipe step.

Refer to the [A2A Protocol specification](https://a2a-protocol.org/latest/topics/what-is-a2a/) for more information about the A2A Protocol task lifecycle.

## How it works

The recipe runs and the action sends a single JSON-RPC `tasks/get` request to the connected agent with the supplied task ID and returns the current task object.

The action requests up to 50 messages from the task's history when **Include message history?** is selected. The action doesn't request history if you don't select **Include message history?**.

## Input

| Input field | Description |
| --- | --- |
| Task ID | Required. Enter the ID of the task to retrieve. This is the `id` value returned by a previous **Send task** action. |
| Include message history? | Optional. Select to include up to 50 messages exchanged on the task. Unselect to omit message history from the response. Defaults to unselected. |

## Output

The action returns the JSON-RPC `result` object from the agent. The shape matches the A2A Protocol `Task` object defined in the [A2A Protocol specification](https://a2a-protocol.org/latest/topics/what-is-a2a/).

| Output field | Description |
| --- | --- |
| Task ID | The unique identifier of the task. |
| Kind | The type of object to get the status for. Typically, `task`. |
| Context ID | The conversation context identifier assigned by the agent. |
| Status | The current state of the task. Including the timestamp, status message, and status state, such as `SUBMITTED`, `WORKING`, `INPUT_REQUIRED`, `COMPLETED`, `FAILED`, or `CANCELED`. |
| Artifacts | An array of artifacts produced by the agent. Populated when the task reaches `COMPLETED`. Each artifact contains an array of `parts`, where each part has a `kind` of `text`, `file`, or `data`. |
| Message history | An array of messages exchanged on the task. Populated only when **Include message history?** is selected. |

---
