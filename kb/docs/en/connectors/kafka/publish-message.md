---
url: 'https://docs.workato.com/en/connectors/kafka/publish-message.md'
description: The Publish message action publishes a new message to a selected Kafka topic.
---

# Apache Kafka - Publish message action

The **Publish message** action publishes a new message to a selected Kafka topic. You can select schemas in AVRO or Protobuf format for the Kafka message body and message key.

For publishing multiple messages in a single batch operation, use the [Publish messages action (batch)](/en/connectors/kafka/publish-messages-batch).

> **MESSAGE SIZE LIMITATION**
> 
> The maximum message size is 50 MB.

## Input

| Input field | Description |
| --- | --- |
| Topic | Select or enter the name of the topic where you plan to publish a message. |
| Message schema source | Define your message schema source. Options include: **Common data model** - Use the schema defined in Workato, **Schema registry** - Use the schema defined in your Kafka cluster. Requires the `schema.registry.url` property to be configured, **Common data model – Protobuf** - Use Protobuf schemas defined in Workato Workato supports schemas in AVRO and Protobuf format. |
| Message schema | Select the message schema based on the **Message schema source** selection. |
| Protobuf message schema | Select the Protobuf message schema from the schema registry. This field appears when **Common data model – Protobuf** is selected as the message schema source. |
| Key schema type | Configure the schema type for your message keys. Options include: **Plaintext** - Use simple string keys, **Schema registry** - Use schemas from your Kafka cluster. Requires the `schema.registry.url` property to be configured Workato supports schemas in AVRO and Protobuf format. |
| Key schema | Select the key schema from your available schemas. This field appears when **Schema registry** is selected as the key schema type. |
| Partition | Specify a topic partition (index starts from 0) to explicitly publish to. If not specified, Kafka selects the partition automatically. |
| Message | Provide the message content. |
| Key | Provide the message key to be stored with the message. |
| Message headers | Provide a list of key-value pairs to be stored with the message as headers. Header keys may be duplicated. |
| Key (Message headers) | Enter the header key name. |
| Value (Message headers) | Enter the header value. |

## Output

The output contains useful information after a successful action. To use the output in downstream steps, map in the relevant datapill.

| Output field | Description |
| --- | --- |
| Size | Size of the published message. |
| Timestamp | Timestamp of the published message. |
| Partition | Partition ID where the message was added. |
| Offset | The message offset, which is a unique message identifier in Kafka. |

---
