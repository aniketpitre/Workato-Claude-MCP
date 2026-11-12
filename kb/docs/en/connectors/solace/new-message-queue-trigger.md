---
url: 'https://docs.workato.com/en/connectors/solace/new-message-queue-trigger.md'
description: The New message in queue trigger monitors a Solace queue for new messages.
---

# Solace - New message in queue trigger

The **New message in queue** trigger monitors a Solace queue for new messages.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue to monitor. |
| Message format | Select a message format. Options are **Binary** and **Text**. |
| Manual acknowledgement | Optional. Select whether to hold each message until the recipe settles it with the **Acknowledge message** action. Defaults to `No`, which acknowledges each message as soon as its trigger event is created. The job persists and you can rerun it, but the broker won't redeliver the message. |
| Acknowledgement timeout (ms) | Optional. Enter the number of milliseconds to wait for the **Acknowledge message** action before the message is redelivered. Solace treats the message as failed and redelivers it, spawning a duplicate job, and failing the original acknowledgement if the recipe doesn't finish acknowledging within this window. Defaults to `60,000`. |
| Max pending acknowledgements | Optional. Enter the maximum number of received messages the agent holds unacknowledged at once before it stops pulling more from the queue. Only relevant in **Manual acknowledgement** mode. Set this to your recipe's **Concurrency** value, or lower if the recipe acknowledges a message before the job finishes. A higher value increases memory use and the chance of acknowledgement timeouts without added throughput. Defaults to `5`. |
| Additional subscription properties | Optional. Click **Add parameter** to pass extra Solace session properties for this subscription only, overriding any value set in the connection's **Additional connection properties** section. |

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
| Manual acknowledgement | The **Manual acknowledgement** setting used for this trigger. |

---
