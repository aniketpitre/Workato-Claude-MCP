---
url: 'https://docs.workato.com/en/connectors/kafka/new-message-trigger.md'
description: >-
  The New message trigger picks up new Kafka messages for a selected Kafka
  topic.
---

# Apache Kafka - New message in topic trigger

The **New message in topic** trigger picks up new Kafka messages for a selected Kafka topic. Each message creates a single job. You can select Kafka message and key schemas in AVRO or Protobuf format.

The initial offset can be configured to define where to start consuming Kafka messages. For batch processing where multiple messages are processed in a single job, use the [New messages in topic trigger (batch)](/en/connectors/kafka/new-messages-trigger-batch).

> **UPDATED TRIGGER VERSION**
> 
> **This trigger requires on-prem agent version 2.20.0 or later.** Previous versions of this trigger are deprecated.
> 
> If you're using an older version, [upgrade your agent](/en/on-prem/agents/upgrade) and update your recipes to use this trigger. This version provides:
> 
> - Improved reliability when recipes are stopped with queued messages
> - Better handling of message consumption after recipe downtime

## Input

| Input field | Description |
| --- | --- |
| Topic | Select a Kafka topic to subscribe to. The trigger consumes all messages from the selected topic and all its partitions. You can filter the messages by partition in the recipe. |
| Message schema source | Define your message schema source. Options include: **Common data model** - Use the schema defined in Workato, **Schema registry** - Use the schema defined in your Kafka cluster. Requires the `schema.registry.url` property to be configured, **Common data model – Protobuf** - Use Protobuf schemas defined in Workato Workato supports schemas in AVRO and Protobuf format. |
| Message schema | Select the message schema based on the **Message schema source** selection. |
| Protobuf message schema | Select the Protobuf message schema from the schema registry. This field appears when **Common data model – Protobuf** is selected as the message schema source. |
| Key schema type | Configure the schema type for your message keys. Options include: **Plaintext** - Use simple string keys, **Schema registry** - Use schemas from your Kafka cluster. Requires the `schema.registry.url` property to be configured Workato supports schemas in AVRO and Protobuf format. |
| Key schema | Select the key schema from your available schemas. This field appears when **Schema registry** is selected as the key schema type. |
| Initial offset | Choose the starting point for consuming Kafka messages from the selected topic. Options include: **Earliest** - Retrieves all available messages in the Kafka cluster, **Latest** - Ignores all historical messages and only consumes new messages from the selected Kafka topic |

> **INITIAL OFFSET ONLY APPLIES ONCE PER TOPIC**
> 
> The **Initial offset** field only applies when you run a recipe for the first time for a selected **Topic**.
> 
> For example, to stop a recipe and ignore all messages produced during downtime:
> 
> 1. Stop the recipe.
>    
> 2. Change the **Topic** or clone the recipe.
>    
> 3. Select **Latest** in the **Initial offset** field.
>    
> 4. Start the edited or cloned recipe.
>    

## Output

The output of this trigger is a single Kafka message. To use the output in downstream steps, map in the relevant datapill.

| Output field | Description |
| --- | --- |
| Message | Message fields with data consumed from the selected Kafka topic. |
| Message headers | A list of key-value pairs stored with the message as headers. |
| Size | Size of the consumed Kafka message. |
| Timestamp | Timestamp of the Kafka message. |
| Key | Kafka message key fields with data. |
| Partition | Partition ID from which the Kafka message was consumed. |
| Offset | The message offset, which is a unique message identifier in Kafka. |

---
