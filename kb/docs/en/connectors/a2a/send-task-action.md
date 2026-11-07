---
url: 'https://docs.workato.com/en/connectors/a2a/send-task-action.md'
description: >-
  The Send task action sends a message to the connected agent in the A2A
  Protocol connector. The action either returns with the new task ID, or waits
  until the agent reaches a terminal state to return artifacts.
---

# A2A Protocol - Send task action

The **Send task** action sends a message to the connected A2A Protocol agent in A2A Protocol. The action either returns with the new task ID, or waits until the agent reaches a terminal state to return artifacts.

You can invoke an agent in a recipe in the following ways:

- **Synchronous**: Send a message and wait for the completed result in a single step.
- **Asynchronous**: Send a message, immediately return a task ID, and check the result later with the **Get task status** action.
- **Resume**: Resume a task that previously returned the `INPUT_REQUIRED` state by passing the task ID with the new message. Refer to [Resume a task](/en/connectors/a2a/resume-task) for more information about resuming a task.

> **ONLY USE SYNCHRONOUS MODE FOR SHORT TASKS**
> 
> Set **Wait for result?** to `Yes` only when the agent is expected to complete within the configured timeout. Use asynchronous mode and check the result with the **Get task status** action for long-running tasks.

Refer to the [A2A protocol specification](https://a2a-protocol.org/latest/topics/what-is-a2a/) for more information about the A2A Protocol task lifecycle.

## How it works

A2A Protocol fetches the connected agent's Agent Card from `/.well-known/agent.json` and lists the agent's declared skills in the hint text on the **Message** field when you use this action. The A2A Protocol specification can't route a message to a specific skill. The agent selects the appropriate skill from your message content. The action sends a JSON-RPC `message/send` request to the agent when the recipe runs.

## Input

| Input field | Description |
| --- | --- |
| Wait for result? | Required. Select `No – return task ID immediately` to return the task object as soon as the agent accepts the task. Select `Yes – block until complete` to wait until the agent finishes and return the completed task. The action checks whether the agent's Agent Card declares `capabilities.pushNotifications: true`. The action polls every minute for task completion. When the task reaches a terminal state, the action returns the result. |
| Message | Required. Enter the text prompt to send to the agent. The hint lists the skills declared by the connected agent. A generic hint is shown if Workato can't access the Agent Card. |
| Task ID (resume only) | Optional. Enter the ID of an existing task to continue a previous task that returned `INPUT_REQUIRED`. The agent treats the message as a continuation of the existing task. Leave this field empty to start a new task. |
| Timeout (seconds) | Optional. The maximum number of seconds the action waits for the task to reach a terminal state. Defaults to `300`. The minimum value is `60` seconds. Only visible when **Wait for result?** is set to `Yes`. The action fails with an error if the request exceeds the timeout. |
| Push notification webhook URL | Choose whether to enable push notifications for a webhook URL. Only visible when when **Wait for result?** is `Yes` and the connected agent has `pushNotifications: true` in its Agent Card. |

## Output

The action returns the JSON-RPC `result` object from the agent. The shape matches the A2A Protocol `Task` object defined in the [A2A Protocol specification](https://a2a-protocol.org/latest/topics/what-is-a2a/).

| Output field | Description |
| --- | --- |
| Task ID | The unique identifier of the task. |
| Kind | The type of object to get the status for. Typically, `task`. |
| Context ID | The conversation context identifier assigned by the agent. |
| Status | The current state of the task. Including the timestamp, status message, and status state, such as `SUBMITTED`, `WORKING`, `INPUT_REQUIRED`, `COMPLETED`, `FAILED`, or `CANCELED`. |
| Artifacts | An array of artifacts produced by the agent. Populated when the task reaches `COMPLETED`. Each artifact contains an array of `parts`, where each part has a `kind` of `text`, `file`, or `data`. |
| Message history | An array of messages exchanged on the task. Populated when the agent returns message history. |

---
