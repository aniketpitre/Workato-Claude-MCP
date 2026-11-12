---
url: 'https://docs.workato.com/en/connectors/solace/new-message-topic-trigger.md'
description: Triggers when a new message is available in the specified Solace topic.
---

# Solace - New message in topic trigger

The **New message in topic** trigger monitors one or more Solace topic subscriptions you specify for new messages.

## Input

| Input field | Description |
| --- | --- |
| Topics | Enter one or more topic subscriptions to listen on, for example, `['orders/created', 'orders/updated']`. This field supports wildcards for single level (`*`) and remaining levels (`>`). |
| Message format | Select the message format. Options are **Binary** and **Text**. |

## Output

| Output field | Description |
| --- | --- |
| Acknowledgement handle | An opaque handle identifying this message for manual acknowledgement. |
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
