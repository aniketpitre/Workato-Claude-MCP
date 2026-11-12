---
url: 'https://docs.workato.com/en/connectors/solace/receive-message-queue.md'
description: Receives a message from the specified Solace queue.
---

# Solace - Receive message from queue action

The **Receive message from queue** action receives a single message from a Solace queue you specify.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue, or toggle to enter it manually. |
| Message format | Select the message format. Options are **Binary** and **Text**. |
| Timeout (ms) | Optional. Enter the maximum wait time for a message, in milliseconds. The minimum value is `1` and the maximum is `300,000`. Defaults to `30,000`. |
| Selector | Optional. Enter a filter expression to select specific messages. For example, `property='value'`. Property names are case-sensitive. |
| Manual acknowledgement | Optional. Specify whether to hold the message until the **Acknowledge message** action settles it. Defaults to `No`, which acknowledges the message as soon as its output is produced. The job persists and you can rerun it, but the broker won't redeliver the message. |
| Acknowledgement timeout (ms) | Optional. Enter the number of milliseconds to wait for the **Acknowledge message** action before the message is redelivered. Solace treats the message as failed, redelivers it to the queue for a future receive attempt, and fails the original acknowledgement if the recipe doesn't finish acknowledging within this window. Defaults to `60,000`. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying this message for manual acknowledgement. Pass it to the **Acknowledge message** action's **Acknowledgement handle** field to settle the message. |
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

---

---
url: >-
  https://docs.workato.com/en/connectors/solace/receive-messages-batch-from-queue.md
description: Receives a batch of messages from the Solace queue you specify.
---

# Solace - Receive messages batch from queue action

The **Receive messages batch from queue** action receives a batch of messages from a Solace queue you specify.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue to receive messages from. |
| Message format | Select the message format. Options are **Binary** and **Text**. |
| Batch size | Optional. Enter the maximum number of messages to receive. The minimum value is `1` and the maximum is `1000`. Defaults to `10`. |
| Timeout (ms) | Optional. Enter the maximum wait time for a message, in milliseconds. The minimum value is `1` and the maximum is `300,000`. Defaults to `30,000`. |
| Selector | Optional. Enter a filter expression to select specific messages. For example, `property='value'`. Property names are case-sensitive. |
| Manual acknowledgement | Optional. Select whether to keep the whole batch unacknowledged at the broker until the recipe settles it with the **Acknowledge message** action, which accepts, fails, or rejects every message in the batch as one unit. Defaults to `No`, which acknowledges (accepts) the batch as soon as its output is produced, permanently removing all its messages from the queue even if the recipe job later fails. The job persists and you can rerun it, but the broker won't redeliver any message in the batch. Requires on-prem agent version [34](/en/on-prem/agents/versions#v34-0) or later. Refer to [Upgrade your agent](/en/on-prem/agents/upgrade) to update an agent from an earlier version. |
| Acknowledgement timeout (ms) | Optional. Enter the number of milliseconds the broker waits for the **Acknowledge message** action to settle the batch before giving up. Solace treats the whole batch as failed, redelivers it to the queue for a future receive attempt, and fails the original acknowledgement attempt if the recipe doesn't finish acknowledging within this window. Defaults to `60,000`. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying the whole batch for manual acknowledgement. Pass it to the **Acknowledge message** action's **Acknowledgement handle** field to settle every message in the batch. |
| Message count | The number of messages received. |
| Messages | The messages received. Each message contains the fields in [Messages](#messages). |

### Messages

| Output field | Description |
| --- | --- |
| Acknowledgement handle | The same **Acknowledgement handle** as the action's top-level field, repeated here for convenience when iterating over **Messages**. |
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
| List size | The number of messages received. |
| List index | The message's position in the list. |

---
