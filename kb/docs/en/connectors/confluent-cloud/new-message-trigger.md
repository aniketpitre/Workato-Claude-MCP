---
url: 'https://docs.workato.com/en/connectors/confluent-cloud/new-message-trigger.md'
description: >-
  The New message in topic trigger in the Confluent Cloud connector fires for
  each new message created in a topic, processing every message as a separate
  job.
---

# Confluent Cloud - New message in topic trigger

Use this trigger to listen to new messages that are created in your Confluent Cloud topic. This trigger checks for new messages once every poll interval and Workato processes each message as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Determine how frequently to check for new events. This defaults to five minutes if left blank. The minimum value allowed is five minutes. |
| Topic | Select a topic from the list or enter the topic name. |
| Message schema source | Select where your message schema is defined from either your [common data models](/en/features/common-data-model) or your schema registry in Confluent Cloud. To retrieve schemas from your schema registry, you must configure your Confluent Cloud connection with your [Stream Governance API credentials](/en/connectors/confluent-cloud#stream-governance-credentials). |
| Message schema | Select a message schema from your common data models or schema registry. |
| Initial offset | Determine the initial offset. This value tells Workato how to handle the operation when there is no initial offset in Kafka or if the current offset no longer exists on the server. If set to **Earliest**, Workato starts fetching messages from the oldest available message in the topic. If set to **Latest**, Workato starts fetching messages from the most recent message. This value defaults to **Earliest**. |

## Output

The output datatree contains information about the message. This includes the key, raw message, partition, offset, timestamp, and size.

| Field | Description |
| --- | --- |
| Key | The message key. This value is stored with the message. |
| Message | The message content. |
| Raw message | The raw message content. |
| Partition | The partition number. |
| Offset | The offset number. |
| Timestamp | The timestamp of the message. |
| Size | The size of the message in bytes. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/confluent-cloud/publish-message-action.md
description: >-
  The Publish message action in the Confluent Cloud connector lets you send a
  message to a topic you specify, with optional key and partition settings.
---

# Confluent Cloud - Publish message action

This action publishes a message to a Confluent Cloud topic you specify.

## Input

| Field | Description |
| --- | --- |
| Topic | Select a topic from the list or enter the topic name. |
| Message schema source | Select where your message schema is defined from either your [common data models](/en/features/common-data-model) or your schema registry in Confluent Cloud. To retrieve schemas from your schema registry, you must configure your Confluent Cloud connection with your [Stream Governance API credentials](/en/connectors/confluent-cloud#stream-governance-credentials). |
| Message schema | Select a message schema from your common data models or schema registry. |
| Message | Provide the message you plan to publish. The available fields are dependent on the message schema you selected. |
| Key | Provide the message key. This value is stored with the message. Kafka uses the key to select an appropriate topic partition when the partition is not assigned explicitly. Only string keys are supported. |
| Partition | Determine a partition for your message. You can explicitly publish a message to the specific topic partition. The index starts at 0. Otherwise, Kafka selects the partition automatically. |

## Output

| Field | Description |
| --- | --- |
| Key | The key of the message. |
| Message | The message content. |
| Raw message | The raw message content. |
| Partition | The partition where the message was published. |
| Offset | The offset of the message in the partition. |
| Timestamp | The timestamp when the message was created. |
| Size | The size of the message in bytes. |

---
