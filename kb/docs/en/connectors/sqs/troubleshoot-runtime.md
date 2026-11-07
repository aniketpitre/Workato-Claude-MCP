---
url: 'https://docs.workato.com/en/connectors/sqs/troubleshoot-runtime.md'
description: >-
  Use this guide to troubleshoot errors that occur at runtime when you use the
  Amazon SQS connector in Workato.
---

# Troubleshoot Amazon SQS runtime errors

Use this guide to troubleshoot errors that occur at runtime when you use the Amazon SQS connector in Workato.

## SQS processes duplicate messages

You may notice that Amazon SQS processes the same message twice. This happens when you use a standard queue. Standard queues deliver each message at least once, but duplicates and out-of-order delivery can occur due to the distributed system design.

Complete the following steps to resolve this error:

- Use a First-In-First-Out (FIFO) queue type. Refer to [Amazon SQS FIFO queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html) for more information.
- Configure exactly-once processing in Amazon SQS. Refer to [Exactly-once processing in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html) in the Amazon documentation for instructions.

---
