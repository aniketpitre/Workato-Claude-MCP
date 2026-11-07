---
url: 'https://docs.workato.com/en/connectors/pubsub/pubsub-batch-trigger.md'
description: >-
  The new batch of messages trigger in Workato Event streams polls batches of
  new messages from a topic at a specified time interval.
---

# Workato Event Streams - New batch of messages trigger

The new message batch trigger enables you to poll batches of new messages from a specific topic in Workato. The trigger picks up all messages published to that topic in a single batch, at the specified time interval. See [Batch triggers](/en/features/batch-processing#batch-triggers) for more information.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Optional. Specify how frequently to check for new events. The default and minimum value is `5 minutes` and the maximum value is `30 days`. |
| Message topic | Select an existing message topic or click **Create a new one** to open the event stream creation modal in a new page. |
| When first started, this recipe should pick up events from | Set the date and time to start picking up trigger events. This enables your recipe to capture past events. You can't change this value after you run or test the recipe. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Batch size | Enter the number of events to return in each batch. The default and maximum value is `100`. The minimum value is `1`. |

Refer to [Trigger conditions](/en/recipes/triggers#trigger-conditions) to only process trigger events matching specific conditions.

> **BATCH SIZE IS A MAXIMUM**
> 
> The batch size you set is the maximum number of messages the trigger returns in a single batch. Workato also caps each batch at 50 MB of total payload. The trigger returns fewer messages than the configured maximum when individual payloads are large, so each batch stays within the size cap. Workato returns the remaining messages in later batches, so no messages are lost.

## Output

The output of this trigger is the contents of the published messages in the format defined by the [event stream](/en/connectors/pubsub/pubsub-creating-new).

---
