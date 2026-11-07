---
url: 'https://docs.workato.com/en/connectors/kafka/publish-messages-batch.md'
description: >-
  The Publish messages batch action publishes multiple messages to a selected
  Kafka topic in a single batch operation.
---

# Apache Kafka - Publish messages action (batch)

The **Publish messages** batch action publishes multiple messages to a selected Kafka topic in a single batch operation. You can select schemas in AVRO or Protobuf format for the Kafka message body and message key.

> **REQUIREMENTS AND LIMITATIONS**
> 
> This action requires on-prem agent [version 31](/en/on-prem/agents/versions#v31) or later.
> 
> Batch limitations:
> 
> - **Maximum batch size**: 50 MB
> - **Maximum message count**: 100 messages per batch

## Input

| Input field | Description |
| --- | --- |
| Topic | Select or enter the name of the topic where you plan to publish messages. |
| Message schema source | Select where your message schema is defined. Options include: **Common data model** - Use the schema defined in Workato, **Schema registry** - Use the schema defined in your Kafka cluster. Requires the `schema.registry.url` property to be configured, **Common data model – Protobuf** - Use Protobuf schemas defined in Workato Workato supports schemas in AVRO and Protobuf format. |
| Message schema | Select the message schema based on the **Message schema source** selection. |
| Protobuf message schema | Select the Protobuf message schema from the schema registry. This field appears when **Common data model – Protobuf** is selected as the message schema source. |
| Key schema type | Configure the schema type for your message keys. Options include: **Plaintext** - Use simple string keys, **Schema registry** - Use schemas from your Kafka cluster. Requires the `schema.registry.url` property to be configured Workato supports schemas in AVRO and Protobuf format. |
| Key schema | Select the key schema from your available schemas. This field appears when **Schema registry** is selected as the key schema type. |
| Partition | Specify a topic partition (index starts from 0) to explicitly publish to. If not specified, Kafka selects the partition automatically. |
| Records | Provide a list of records to publish to the Kafka topic. Expand this section to configure the records source and individual message details. |
| Records source list (Records) | Provide a list datapill that contains the records to publish. Each item in the list represents one message to publish to Kafka. [Learn more about list input](/en/features/list-management). |
| Records fields (Message) | Provide the message content for each record. |
| Key (Records) | Provide the message key to be stored with each message. |
| Message headers (Records) | Provide a list of key-value pairs to be stored with each message as headers. Header keys may be duplicated. |

## Output

The output contains information about successfully published messages and any failures that occurred during batch publishing. To use the output in downstream steps, map in the relevant datapill.

| Output field | Description |
| --- | --- |
| Successful | A list containing the results for each successfully published message. |
| Index (Successful) | The index of the message in the original input batch (starting from 0). |
| Key (Successful) | The message key that was published with the message. |
| Size (Successful) | Size of the published message. |
| Timestamp (Successful) | Timestamp of the published message. |
| Partition (Successful) | Partition ID where the message was added. |
| Offset (Successful) | The message offset, which is a unique message identifier in Kafka. |
| Failed | A list containing details for each message that failed to publish. |
| Index (Failed) | The index of the failed message in the original input batch (starting from 0). |
| Key (Failed) | The message key of the failed message. |
| Error (Failed) | The error message describing why the message failed to publish. |

---
