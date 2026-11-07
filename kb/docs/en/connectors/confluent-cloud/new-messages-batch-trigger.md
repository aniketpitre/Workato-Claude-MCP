---
url: >-
  https://docs.workato.com/en/connectors/confluent-cloud/new-messages-batch-trigger.md
description: >-
  The New messages in topic trigger (batch) in the Confluent Cloud connector
  picks up new messages from a topic in batches on each poll interval.
---

# Confluent Cloud - New messages in topic trigger (batch)

Configure the Confluent Cloud connector to listen to new messages in batches that are created in your Confluent Cloud topic. This trigger checks for new messages once every poll interval and Workato processes each batch as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Topic | Select a topic from the list or enter the topic name. |
| Message schema source | Select where your message schema is defined from either your [common data models](/en/features/common-data-model) or your schema registry in Confluent Cloud. To retrieve schemas from your schema registry, you must configure your Confluent Cloud connection with your [Stream Governance API credentials](/en/connectors/confluent-cloud#stream-governance-credentials). |
| Message schema | Select a message schema from your common data models or schema registry. |
| Initial offset | Determine the initial offset. This value tells Workato how to handle the operation when there is no initial offset in Kafka or if the current offset no longer exists on the server. If set to **Earliest**, Workato starts fetching messages from the oldest available message in the topic. If set to **Latest**, Workato starts fetching messages from the most recent message. This value defaults to **Earliest**. |
| Batch size | Select the size of the returned events batch. The minimum is 1 and the maximum is 100. The default value is 100. |

## Output

The output datatree contains information about the messages. This includes the key, raw message, partition, offset, timestamp, and size.

| Field | Description |
| --- | --- |
| Records | An array of message records. Each record contains the following fields. |
| Key | The message key. This value is stored with the message. |
| Message | The message content. |
| Raw message | The raw message content. |
| Partition | The partition number. |
| Offset | The offset number. |
| Timestamp | The timestamp of the message. |
| Size | The size of the message in bytes. |
