---
url: 'https://docs.workato.com/en/connectors/solace/new-message-batch-trigger.md'
description: >-
  The New message batch in queue trigger monitors a Solace queue for a batch of
  new messages.
---

# Solace - New message batch in queue trigger

The **New message batch in queue** trigger monitors a Solace queue for a batch of new messages. The trigger buffers messages until the batch reaches the **Batch size** you specify or the **Batch timeout** elapses, whichever comes first.

> **ON-PREM AGENT VERSION**
> 
> This trigger requires on-prem agent version [34](/en/on-prem/agents/versions#v34-0) or later. Refer to [Upgrade your agent](/en/on-prem/agents/upgrade) to update an agent from an earlier version.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a Solace queue to monitor. |
| Message format | Select the message format. Options include **Binary** and **Text**. |
| Batch size | Optional. Enter the maximum number of messages to aggregate into a single trigger event. The minimum value is `1` and the maximum is `1000`. Defaults to `10`. |
| Batch timeout (ms) | Optional. Enter the maximum number of milliseconds to wait before triggering from a batch smaller than the specified **Batch size**. The minimum value is `1` and the maximum is `300,000`. Defaults to `30,000`. |
| Manual acknowledgement | Optional. Select whether to keep the whole batch unacknowledged at the broker until the recipe settles it with the **Acknowledge message** action, which accepts, fails, or rejects every message in the batch as one unit. Defaults to `No`, which accepts the batch automatically, permanently removing all its messages from the queue even if the recipe job later fails. The job persists and you can rerun it, but the broker won't redeliver any message in the batch. |
| Acknowledgement timeout (ms) | Optional. Enter the number of milliseconds the broker waits for the **Acknowledge message** action to settle the batch before giving up. Solace treats the whole batch as failed, redelivers every message in it, spawns a duplicate job, and fails the original acknowledgement attempt if the recipe doesn't finish acknowledging within this window. Defaults to `60,000`. |
| Max pending acknowledgements | Optional. Enter the maximum number of batches the agent holds unacknowledged at once before it stops pulling more messages from the queue. Only relevant in **Manual acknowledgement** mode. Set this to your recipe's **Concurrency** value, or lower if the recipe acknowledges a batch before the job finishes. A higher value increases memory use and the chance of acknowledgement timeouts without added throughput. Defaults to `5`. |
| Additional subscription properties | Optional. Click **Add parameter** to pass extra Solace session properties for this subscription only, overriding any value set in the connection's **Additional connection properties** section. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying the whole batch for manual acknowledgement. Pass it to the **Acknowledge message** action's **Acknowledgement handle** field to settle every message in the batch. |
| Manual acknowledgement | The **Manual acknowledgement** setting used for this trigger. |
| Message count | The number of messages in the batch. |
| Messages | The messages in the batch. Each message contains the fields in [Messages](#messages). |

### Messages

| Output field | Description |
| --- | --- |
| Acknowledgement handle | The same **Acknowledgement handle** as the trigger's top-level field, repeated here for convenience when iterating over **Messages**. |
| Message type | The format of the received message payload. For example: `text`. |
| Delivery mode | The delivery mode the message was sent with. `PERSISTENT` messages are stored by the broker until delivered, acknowledged, or expired. `DIRECT` messages aren't stored and can be dropped if no subscriber is ready to receive them. |
| Priority | The message's delivery priority. This only affects delivery order if the queue has priority ordering enabled. |
| Class of service | The message's class of service, which determines how readily the broker discards the message if its destination queue is congested. |
| Destination | The queue or topic the message was delivered to. Contains: Type, Name |
| Reply to | The destination to send replies to, if the sender set one. Contains: Type, Name |
| Application ID | The sending application's ID, if set by the sender. |
| Application type | The sending application's message type, if set by the sender. |
| HTTP content type | The message's HTTP content type, if set by the sender. |
| Correlation ID | An identifier for tracking related messages, if set by the sender. |
| Sender ID | The identifier of the client that sent the message, if set. |
| Replication group ID | The message's replication group ID, used for Solace data replication. |
| Sequence number | The message's sequence number, if set by the sender. |
| Sender time | The sender's timestamp, in milliseconds, if set. |
| Receive time | The timestamp when the message was received, in milliseconds. |
| Time to live | The broker-enforced time-to-live the message was sent with, in milliseconds. This is what actually expires the message, and routes it to the dead message queue if it's eligible. `0` means the message doesn't expire. |
| Expiration | The informational expiration timestamp header, in milliseconds, if set. Unlike **Time to live**, it doesn't expire the message on the broker. |
| Delivery count | The number of times this message has been delivered. |
| Is reply | Whether this message is a reply to an earlier request, as used in Solace's request-reply messaging pattern. |
| Dead message queue eligible | Whether the message is eligible to be routed to the dead message queue if it can't be delivered. |
| Discard indication | Whether one or more messages were discarded before this one, for example, due to a full buffer. |
| Eliding eligible | Whether the message is eligible for eliding, where the broker thins a rapid series of updates to a topic down to only the latest value for a slow subscriber. Applies to direct messages only. |
| User data | Arbitrary user data, base64-encoded, if set by the sender. |
| Properties | The message's custom properties. Contains: Name, Type, Value, List size: The number of properties., List index: The property's position in the list. |
| Message | The message payload. |
| List size | The number of messages in the batch. |
| List index | The message's position in the batch. |

---
