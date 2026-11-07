---
url: 'https://docs.workato.com/en/connectors/sqs/send-message-action.md'
description: >-
  The Send Message action allows you to send a single message to a chosen SQS
  queue.
---

# Amazon SQS - Send message action

The **Send Message** action allows you to send a single message to a chosen SQS queue.

## Input

| Input field | Description |
| --- | --- |
| Queue | Enter the Queue URL of the queue. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Message body | Enter the message to send. The maximum string size is 256 KB. This is normally unstructured data. |
| Message attribute | Enter a list of message attributes sent in the message. Use this field for structured data. |
| Message system attribute | Select the message system attribute. The only supported message system attribute is AWSTraceHeader. Select the type `String`. The string value must be a correctly formatted AWS X-Ray trace header string. The size of a message system attribute doesn't count towards the total size of a message. |

## Output

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| MD5 of message attributes | The MD5 hash of the message attribute. |
| MD5 of message body | The MD5 hash of the message body. |
| MD5 of message system attributes | The MD5 hash of the message system attribute. |
| Message ID | The unique ID of the message. |
| Sequence number | This parameter applies only to FIFO (first-in-first-out) queues. The large, non-consecutive number that Amazon SQS assigns to each message. |

---
