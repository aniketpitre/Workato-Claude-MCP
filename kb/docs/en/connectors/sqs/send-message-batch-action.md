---
url: 'https://docs.workato.com/en/connectors/sqs/send-message-batch-action.md'
description: Send multiple messages to an Amazon SQS queue.
---

# Amazon SQS – Send messages (batch)

The **Send messages** batch action delivers multiple messages to a specified Amazon SQS queue.

## Input

| Input field | Description |
| --- | --- |
| Queue URL | Enter the **Queue URL** to send messages to. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Batch request entries | Provide a list datapill to define the messages to send. |
| Message body | Enter the contents of the message. The maximum size is 256 KB per message. |
| Message attribute | Enter structured metadata for the message, sent as key-value pairs. |
| Message system attribute | Enter a system-defined attribute. |
| Delivery delay | Enter the number of seconds to delay the first delivery of each message. This field appears for standard queues only. |
| Message group ID | Specify the message group tag to ensure messages are processed in FIFO order. Required for FIFO queues. |
| Message deduplication ID | Enter a unique token to prevent duplicate messages within a 5-minute window. Required for FIFO queues when content-based deduplication isn't enabled. |

> **MESSAGE SIZE LIMITS**
> 
> Amazon SQS quotas each message in a batch to 256 KB and the total size of all messages in the request to 1 MiB (1,048,576 bytes). The request fails if either quota is exceeded.

## Output

| Output field | Description |
| --- | --- |
| Successful | A list of messages that were successfully sent. |
| Failed | A list of messages that failed to send. |

---
