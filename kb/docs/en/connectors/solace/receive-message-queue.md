---
url: 'https://docs.workato.com/en/connectors/solace/receive-message-queue.md'
description: Receives a message from the specified Solace queue.
---

# Solace - Receive message from queue action

The **Receive message from queue** action receives a single message from a `Solace` queue you specify.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue, or toggle to enter it manually. |
| Message format | Select the message format. Options are **Binary** and **Text**. |
| Timeout (ms) | Optional. Enter the maximum wait time for a message, in milliseconds. The minimum value is `1` and the maximum is `300,000`. Defaults to `30,000`. |
| Selector | Optional. Enter a filter expression to select specific messages. For example, `property='value'`. Property names are case-sensitive. |
| Manual acknowledgement | Optional. Specify whether to hold the message until the **Acknowledge message** action settles it. Defaults to `No`, which acknowledges the message as soon as its output is produced. The job persists and you can rerun it, but the broker won't redeliver the message. |
| Acknowledgement timeout (ms) | Optional. Enter the number of milliseconds to wait for the **Acknowledge message** action before the message is redelivered. Solace treats the message as failed, redelivers it to the queue for a future receive attempt, and fails the original acknowledgement if the recipe doesn't finish acknowledging within this window. Defaults to `30,000`. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying this message for manual acknowledgement. Pass it to the **Acknowledge message** action's **Acknowledgement handle** field to settle the message. |
| Message type | The format of the received message payload, for example, `text`. |
| Delivery mode | The delivery mode the message was sent with, for example, `PERSISTENT`. |
| Priority | The message's priority. |
| Class of service | The message's class of service. |
| Destination | The queue the message was delivered to. |
| Reply to | The destination to send replies to, if the sender set one. |
| Application ID | The sending application's ID, if set by the sender. |
| Application type | The sending application's message type, if set by the sender. |
| HTTP content type | The message's HTTP content type, if set by the sender. |
| Correlation ID | An identifier for tracking related messages, if set by the sender. |
| Sender ID | The identifier of the client that sent the message, if set. |
| Replication group ID | The message's replication group ID, used for Solace data replication (DR). |
| Sequence number | The message's sequence number, if set by the sender. |
| Sender time | The sender's timestamp, in milliseconds, if set. |
| Receive time | The timestamp when the message was received, in milliseconds. |
| Time to live | The broker-enforced time-to-live for the message, in milliseconds. `0` means the message doesn't expire. |
| Expiration | The informational expiration timestamp header, in milliseconds, if set. |
| Delivery count | The number of times this message has been delivered. |
| Is reply | Whether the message is a reply message. |
| Dead message queue eligible | Whether the message is eligible to be routed to the dead message queue if it can't be delivered. |
| Discard indication | Whether one or more messages were discarded before this one, for example, due to a full buffer. |
| Eliding eligible | Whether the message is eligible for eliding, a broker-side feature that reduces message rate for matching subscribers. |
| User data | Arbitrary user data, base64-encoded, if set by the sender. |
| Properties | The message's custom properties. |

---

---
url: >-
  https://docs.workato.com/en/connectors/solace/receive-messages-batch-from-queue.md
description: Receives up to Batch size messages from the specified Solace queue.
---

# Solace - Receive messages batch from queue action

The **Receive messages batch from queue** action receives up to a batch size of messages from a `Solace` queue you specify. Messages are acknowledged automatically.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue to receive messages from. |
| Message format | Select the message format. Options are **Binary** and **Text**. |
| Batch size | Optional. Enter the maximum number of messages to receive. The minimum value is `1` and the maximum is `100`. Defaults to `10`. |
| Timeout (ms) | Optional. Enter the maximum wait time for a message, in milliseconds. The minimum value is `1` and the maximum is `300,000`. Defaults to `30,000`. |
| Selector | Optional. Enter a filter expression to select specific messages. For example, `property='value'`. Property names are case-sensitive. |

## Output

| Output field | Description |
| --- | --- |
| Message count | The number of messages received. |
| Messages | A list of received messages. |

---
