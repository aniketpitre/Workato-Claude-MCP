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
