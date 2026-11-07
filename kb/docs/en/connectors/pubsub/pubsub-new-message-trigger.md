---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-new-message-trigger.md'
description: >-
  The New message trigger monitors a specific topic in real-time. The trigger
  picks up all messages published to that topic as a single trigger event.
---

# Workato Event Streams - New message trigger

The **New message** trigger monitors a specific topic in real-time. The trigger picks up all messages published to that topic as a single trigger event.

## Input

| Input field | Description |
| --- | --- |
| Message topic | Select an existing message topic or click **Create a new one** to open the event stream creation modal in a new page. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. You can't change this value after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

Refer to [Trigger conditions](/en/recipes/triggers#trigger-conditions) to only process trigger events matching specific conditions.

## Output

The output of this trigger is the contents of the published message in the format defined by the [event stream](/en/connectors/pubsub/pubsub-creating-new).

---
