---
url: 'https://docs.workato.com/en/connectors/jms/publish-message-to-queue-action.md'
description: >-
  The Publish message to queue action creates a new message in a queue you
  specify.
---

# JMS tools by Workato - Publish message to queue action

The Publish message to queue action creates a new message in a queue you specify.

> **PREREQUISITES**
> 
> You must define the queue name, message format, and message schema in a [common data model](/en/features/common-data-model) before you can use this action.
> 
> Additionally, some input fields are only available in OPA [version 30](/en/on-prem/agents/versions#v30) or higher.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Enter the name of the queue to create a message in. This must exactly match the queue name defined in your common data model. |
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
