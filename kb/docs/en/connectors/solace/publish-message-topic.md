---
url: 'https://docs.workato.com/en/connectors/solace/publish-message-topic.md'
description: Publishes a message to the specified Solace topic.
---

# Solace - Publish message to topic action

The **Publish message to topic** action publishes a message to a `Solace` topic you specify.

## Input

| Input field | Description |
| --- | --- |
| Topic name | Enter the topic name. |
| Message format | Select the message format. Options are **Binary** and **Text**. |
| Delivery mode | Optional. Select a delivery mode. Messages are `PERSISTENT` by default. `DIRECT` is only supported for topics. |
| Priority | Optional. Specify a message priority. The minimum value is `0` and the maximum is `255`. Defaults to `4`. |
| Correlation ID | Optional. Enter an identifier for tracking related messages. |
| Class of service | Optional. Select the message's class of service. |
| Reply to | Optional. Define the destination to send replies to. |
| Application ID | Optional. Enter an identifier for the sending application. |
| Application type | Optional. Enter a classification for the message. |
| HTTP content type | Optional. Enter the message's HTTP content type, for example, `application/json`. |
| Sender ID | Optional. Enter an identifier for the client sending the message. |
| Sequence number | Optional. Enter a sequence number for the message. |
| Sender time | Optional. Enter the sender timestamp in milliseconds. |
| Time to live | Optional. Enter the broker-enforced time-to-live in milliseconds. This is what actually expires the message, and routes it to the dead message queue when eligible. `0` means the message doesn't expire. |
| Expiration | Optional. Enter an informational expiration timestamp header, in milliseconds. **Expiration** doesn't expire the message on the broker. Use **Time to live** to expire the message on the broker. |
| Is reply | Optional. Select whether to mark this message as a reply to another message. |
| Dead message queue eligible | Optional. Select whether the message can be moved to the queue's dead message queue if it can't be delivered, for example, if its **Time to live** expires or it's rejected using the **Acknowledge message** action. |
| Eliding eligible | Optional. Select whether the message is eligible for eliding, a broker-side feature that reduces message rate for subscribers configured to receive only the latest value from a rapid burst of messages. |
| User data | Optional. Enter an arbitrary user data header, sent base64-encoded. |
| Properties | Optional. Define custom message properties, either by mapping a list datapill in the **Properties source list** field, or by adding rows individually. Each row defines a `Name`, `Type`, and `Value`. |

## Output

There is no output for this action.

---
