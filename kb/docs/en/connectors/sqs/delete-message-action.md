---
url: 'https://docs.workato.com/en/connectors/sqs/delete-message-action.md'
description: >-
  The SQS connector supports the Delete message and Delete messages (batch)
  action.
---

# Amazon SQS - Delete messages

The SQS connector supports two kinds of delete message actions:

- [Delete message](#delete-message-action)
- [Delete messages (Batch)](#delete-messages-batch)

## Delete message action

The **Delete message** action deletes a single message in a queue defined by the message's receipt handle.

### Input

| Input field | Description |
| --- | --- |
| Queue | Enter the Queue URL of the queue. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Receipt handle | Enter the receipt handle associated with the message to delete. You can find receipt handles from trigger output or actions that retrieve messages. |

### Output

| Field name | Description |
| --- | --- |
| Request ID | The unique ID of the request. |

## Delete messages (batch)

The **Delete messages (Batch)** action deletes a batch of messages in a queue defined by the message receipt handles.

### Input

| Output field | Description |
| --- | --- |
| Queue | Enter the Queue URL of the queue. Avoid selecting from the list in production environments. Selecting from the list stores the full Queue URL, including the AWS account ID, which may not update correctly when deploying across environments. |
| Receipt handle | Enter a list of receipt handles of messages to delete. You can find receipt handles from trigger output or actions that retrieve messages. |

### Output

| Output field | Description |
| --- | --- |
| Successful | A list of successfully deleted messages. |
| Failed | A list of messages that failed to deleted. You can store these messages or attempt to delete them again. |

---
