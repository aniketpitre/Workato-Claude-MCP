---
url: 'https://docs.workato.com/en/connectors/sqs/new-message-trigger.md'
description: >-
  The Amazon SQS connector supports the New message and New message (Batch)
  triggers.
---

# Amazon SQS - New message trigger

The SQS connector supports the following triggers:

- [New message](#new-message)
- [New messages (Batch)](#new-message-batch)

## New message

The **New message** trigger checks your SQS queue at regular polls to retrieve messages. Use the [New message (Batch) trigger](#new-message-batch) for high volume queues.

### Input

| Input field | Description |
| --- | --- |
| Queue | Enter the Queue URL to pull messages from. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Automatically delete message | Select **Yes** to automatically delete messages after the trigger processes them. If set to **No**, your recipe must explicitly delete messages using a [Delete message](/en/connectors/sqs/delete-message-action) action. |
| Visibility timeout | Enter the duration (in seconds) of the visibility timeout. This hides messages retrieved by a `ReceiveMessage` request from subsequent retrieve requests for a specified amount of time. Maximum value is 12 hours. Refer to [Visibility timeout](/en/connectors/sqs#visibility-timeout) for more information. |

### Output

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| MD5 of message attributes | The MD5 hash of the message attribute. |
| MD5 of message body | The MD5 hash of the message body. |
| MD5 of message system attributes | The MD5 hash of the message system attribute. |
| Message ID | The unique ID of the message. |
| Message body | The message's contents. |
| Sequence number | The large, non-consecutive number that Amazon SQS assigns to each message. This parameter applies only to FIFO (first-in-first-out) queues. |

## New message (Batch)

The **New message (Batch)** trigger regularly polls your specified SQS queue to retrieve messages. Workato recommends the batch trigger for high volume queues.

### Input

| Input field | Description |
| --- | --- |
| Queue | Enter the Queue URL to pull messages from. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Automatically delete message | Select **Yes** to automatically delete messages after the trigger processes them. If set to **No**, your recipe must explicitly delete messages using a [Delete message](/en/connectors/sqs/delete-message-action) action. |
| Visibility timeout | Enter the duration (in seconds) of the visibility timeout. This hides messages retrieved by a ReceiveMessage request from subsequent retrieve requests for a specified amount of time. Maximum value is 12 hours. Refer to [Visibility timeout](/en/connectors/sqs#visibility-timeout) for more information. |
| Batch size (Only for batch trigger) | Enter the maximum number of messages for each trigger event. The minimum is 10, maximum is 2000, default is 2000. The input must be a multiple of 10. |

> **FIFO QUEUE MESSAGE LIMITS**
> 
> When using the **New message** batch trigger with a FIFO queue, Amazon SQS limits the number of messages returned per **Message group ID**, not the total batch size.
> 
> Amazon SQS enforces strict ordering by **Message group ID**, which groups related messages together. SQS processes messages with the same **Message group ID** one at a time, in the order they were sent.
> 
> As a result, even if you configure a higher batch size in your recipe, the trigger retrieves up to **10 messages** from each message group at a time. This is an Amazon SQS API limitation that Workato can't override.
> 
> To process more messages concurrently, distribute messages across multiple **Message group IDs** or run several recipes that connect to the same queue.
> 
> Refer to the [FIFO queue delivery logic in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html) documentation for more information.

### Output

The output to this trigger is a list of messages.

| Output field | Description |
| --- | --- |
| Request ID | The unique id of the request. |
| MD5 of message attributes | The MD5 hash of the message attribute. |
| MD5 of message body | The MD5 hash of the message body. |
| MD5 of message system attributes | The MD5 hash of the message system attribute. |
| Message ID | The unique ID of the message. |
| Message body | The message's contents. |
| Sequence number | This parameter applies only to FIFO (first-in-first-out) queues. The large, non-consecutive number that Amazon SQS assigns to each message. |

---
