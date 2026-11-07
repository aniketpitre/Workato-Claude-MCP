---
url: 'https://docs.workato.com/en/connectors/solace/new-message-topic-trigger.md'
description: Triggers when a new message is available in the specified Solace topic.
---

# Solace - New message in topic trigger

The **New message in topic** trigger monitors one or more `Solace` topic subscriptions you specify for new messages.

## Input

| Input field | Description |
| --- | --- |
| Topics | Enter one or more topic subscriptions to listen on, for example, `['orders/created', 'orders/updated']`. This field supports wildcards for single level (`*`) and remaining levels (`>`). |
| Message format | Select the message format. Options are **Binary** and **Text**. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying this message for manual acknowledgement. |
| Message type | The format of the received message payload, for example, `text`. |
| Delivery mode | The delivery mode the message was sent with, for example, `PERSISTENT`. |
| Priority | The message's priority. |
| Class of service | The message's class of service. |
| Destination | The topic the message was delivered to. |
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
