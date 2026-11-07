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
