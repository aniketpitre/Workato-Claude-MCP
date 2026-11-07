---
url: 'https://docs.workato.com/en/connectors/sqs/receive-messages-action.md'
description: The Receive messages action pulls up to 10 messages from a chosen SQS queue.
---

# Amazon SQS - Receive messages action

The **Receive messages** action pulls up to 10 messages from a chosen SQS queue. Use this action when you have a recipe that pulls messages midway through a recipe workflow.

## Input

| Input field | Description |
| --- | --- |
| Queue | Enter the Queue URL of the queue. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Select attributes | Enter a list of attributes to return with each message. |
| Max number of messages | Enter the maximum number of messages to return. Amazon SQS doesn't return more messages than this value, however SQS may return fewer messages. The value must be between `1` and `10`. The default is `1`. |
| Visibility timeout | Enter the duration (in seconds) of the visibility timeout. This hides messages retrieved by a ReceiveMessage request from subsequent retrieve requests for a specified amount of time. Maximum value is 12 hours. Refer to [Visibility timeout](/en/connectors/sqs#visibility-timeout) for more information |
| Wait time (seconds) | Enter the duration (in seconds) that the call waits for a message to arrive in the queue before returning. The value must be between `0` and `20`. If a message is available, the call returns sooner than `WaitTimeSeconds`. If no messages are available and the wait time expires, the call returns successfully with an empty list of messages. |

## Output

The output to this action is a list of messages.

| Field name | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| MD5 of message attributes | The MD5 hash of the message attribute. |
| MD5 of message body | The MD5 hash of the message body. |
| MD5 of message system attributes | The MD5 hash of the message system attribute. |
| Message ID | The unique ID of the message. |
| Message body | The message's contents. |
| Sequence number | This parameter applies only to FIFO (first-in-first-out) queues. The large, non-consecutive number that Amazon SQS assigns to each message. |

---
