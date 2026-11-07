---
url: 'https://docs.workato.com/en/connectors/solace/new-message-queue-trigger.md'
description: The New message in queue trigger monitors a Solace queue for new messages.
---

# Solace - New message in queue trigger

The **New message in queue** trigger monitors a `Solace` queue for new messages.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue to monitor. |
| Message format | Select a message format. Options are **Binary** and **Text**. |
| Manual acknowledgement | Optional. Select whether to hold each message until the recipe settles it with the **Acknowledge message** action. Defaults to `No`, which acknowledges each message as soon as its trigger event is created. The job persists and you can rerun it, but the broker won't redeliver the message. |
| Acknowledgement timeout (ms) | Optional. Enter the number of milliseconds to wait for the **Acknowledge message** action before the message is redelivered. Solace treats the message as failed and redelivers it, spawning a duplicate job, and failing the original acknowledgement if the recipe doesn't finish acknowledging within this window. Defaults to `30,000`. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying this message for manual acknowledgement. Pass it to the **Acknowledge message** action's **Acknowledgement handle** field to settle the message. |
| Message type | The format of the received message payload, for example, `text`. |
| Delivery mode | The delivery mode the message was sent with, for example, `PERSISTENT`. |
| Priority | The message's priority. |
| Class of service | The message's class of service. |
| Destination | The queue the message was delivered to. Contains: Type, Name |
| Reply to | The destination to send replies to, if the sender set one. Contains: Type, Name |
| Application ID | The sending application's ID, if set by the sender. |
| Application type | The sending application's message type, if set by the sender. |
| HTTP content type | The message's HTTP content type, if set by the sender. |
| Correlation ID | An identifier for tracking related messages, if set by the sender. |
| Sender ID | The identifier of the client that sent the message, if set. |
| Replication group ID | The message's replication group ID, used for Solace data replication (DR). |
| Sequence number | The message's sequence number, if set by the sender. |
| Sender time | The sender's timestamp, in milliseconds, if set. |
| Receive time | The timestamp when the message was received, in milliseconds. |
| Time to live | The broker-enforced time-to-live the message was sent with, in milliseconds. `0` means the message doesn't expire. |
| Expiration | The informational expiration timestamp header, in milliseconds, if set. |
| Delivery count | The number of times this message has been delivered. |
| Is reply | Whether the message is a reply message. |
| Dead message queue eligible | Whether the message is eligible to be routed to the dead message queue if it can't be delivered. |
| Discard indication | Whether one or more messages were discarded before this one, for example, due to a full buffer. |
| Eliding eligible | Whether the message is eligible for eliding, a broker-side feature that reduces message rate for matching subscribers. |
| User data | Arbitrary user data, base64-encoded, if set by the sender. |
| Properties | The message's custom properties. Contains: Name, Type, Value |
| Manual acknowledgement | The **Manual acknowledgement** setting used for this trigger. |

---
