---
url: 'https://docs.workato.com/en/connectors/jms/publish-message-to-topic-action.md'
description: >-
  The Publish message to topic action creates a new message in a topic you
  specify.
---

# JMS tools by Workato - Publish message to topic action

The Publish message to topic action creates a new message in a topic you specify.

> **PREREQUISITES**
> 
> You must define the topic name, message format, and message schema in a [common data model](/en/features/common-data-model) before you can use this action.
> 
> Additionally, some input fields are only available in OPA [version 30](/en/on-prem/agents/versions#v30) or higher.

## Input

| Input field | Description |
| --- | --- |
| Topic name | Enter the name of the topic to create a message in. This must exactly match the topic name defined in your common data model. |
| Delivery Mode | Optional. Select the delivery mode for the message. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Priority | Optional. Enter the message priority as an integer between `0` and `9`. A higher value number represents a higher priority. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Delivery delay | Optional. Enter the number of milliseconds to delay the message before delivery. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Time to live | Optional. Enter the lifetime of the message in milliseconds. Enter `0` or leave this field blank to set messages to not expire. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Correlation ID | Optional. Enter the identifier for tracking related messages. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Type (ReplyTo) | Optional. Select the type of destination to send replies to. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Name (ReplyTo) | Optional. Enter the name of the destination to send replies to. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Type | Optional. Enter the classification of the message. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Properties | Optional. Define custom properties to include in the message schema. Requires OPA [version 30](/en/on-prem/agents/versions#v30) or higher. |
| Message | Define the message payload. Messages have a maximum size of 30 MB. |

## Output

The output of this action varies based on the message schema.

---

---
url: >-
  https://docs.workato.com/en/connectors/jms/receive-message-from-queue-action.md
description: >-
  The Receive message from queue action receives a message from a JMS queue you
  specify.
---

# JMS tools by Workato - Receive message from queue action

The Receive message from queue action receives a message from a JMS queue you specify.

> **PREREQUISITES**
> 
> The following prerequisites are required for this action:
> 
> - A queue name, message format, and message schema defined in a [common data model](/en/features/common-data-model)
> - OPA [version 30.1](/en/on-prem/agents/versions#v30-1) or higher

## Input

| Input field | Description |
| --- | --- |
| Queue name | Enter the name of the queue to receive a message from. This must exactly match the queue name defined in your common data model. |
| Message type | Select the message format to receive. |
| Timeout | Enter the maximum wait time for a message in milliseconds. Defaults to `30000` (30 seconds) when left blank. |
| Selector | Optional. Enter a JMS selector expression to filter the messages this action receives. |
| Properties | Optional. Define custom properties to expect in the message schema. |

## Output

| Output field | Description |
| --- | --- |
| ID | A unique identifier for the message. |
| Priority | A numeric value indicating the message's priority. |
| Mode | The delivery mode of the message. For example: `PERSISTENT`. |
| Destination | Contains information about the target destination for the message, including `Type` and `Topic`. |
| ReplyTo | Contains information about the target destination for replies, including `Type` and `Topic`. |
| Timestamp | A timestamp indicating when the message was created. |
| Delivery time | A timestamp indicating when the message was delivered. |
| Expiration | A timestamp indicating when the message expires. |
| Correlation | An identifier for tracking related messages. |
| Redelivered | Indicates whether the message was redelivered. |
| Properties | Contains the message's properties. |
| Message | Contains the message content. |

---
