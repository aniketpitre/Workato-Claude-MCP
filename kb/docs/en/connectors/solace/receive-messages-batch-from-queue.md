---
url: >-
  https://docs.workato.com/en/connectors/solace/receive-messages-batch-from-queue.md
description: Receives up to Batch size messages from the specified Solace queue.
---

# Solace - Receive messages batch from queue action

The **Receive messages batch from queue** action receives up to a batch size of messages from a `Solace` queue you specify. Messages are acknowledged automatically.

## Input

| Input field | Description |
| --- | --- |
| Queue name | Select a queue to receive messages from. |
| Message format | Select the message format. Options are **Binary** and **Text**. |
| Batch size | Optional. Enter the maximum number of messages to receive. The minimum value is `1` and the maximum is `100`. Defaults to `10`. |
| Timeout (ms) | Optional. Enter the maximum wait time for a message, in milliseconds. The minimum value is `1` and the maximum is `300,000`. Defaults to `30,000`. |
| Selector | Optional. Enter a filter expression to select specific messages. For example, `property='value'`. Property names are case-sensitive. |

## Output

| Output field | Description |
| --- | --- |
| Message count | The number of messages received. |
| Messages | A list of received messages. |
