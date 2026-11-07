---
url: 'https://docs.workato.com/en/connectors/jms/new-message-in-queue-trigger.md'
description: >-
  The New message in queue trigger monitors a queue in real-time for a message
  type you specify.
---

# JMS tools by Workato - New message in queue (real-time) trigger

The New message in queue trigger monitors a queue in real-time for a message type you specify.

> **PREREQUISITES**
> 
> You must define the queue's name, format, and schema in a [common data model](/en/features/common-data-model) before you can use this trigger.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Enter the name of the queue to monitor. This must exactly match the queue name defined in your common data model. |
| Message type | Select the message format to monitor. The trigger ignores messages that aren't in this format. |
| Properties schema | Optional. Define custom properties to include in the message schema. |

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the message. |
| Priority | A numeric value indicating the message's priority. |
| Mode | The mode of message delivery or processing. |
| Destination | Contains information about the target destination for the message, including `Type` and `Queue`. |
| ReplyTo | Contains information about the target destination for replies, including `Type` and `Queue`. |
| Timestamp | A timestamp indicating when the message was created. |
| Delivery time | A timestamp indicating when the message was delivered. |
| Expiration | A timestamp indicating the when the message expires. |
| Correlation | An identifier for tracking related messages. |
| Type | The classification of the message. |
| Properties | Contains the message's properties. |
| Message | Contains the message content. |

---
