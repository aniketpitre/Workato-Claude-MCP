---
url: 'https://docs.workato.com/en/connectors/solace/acknowledge-message.md'
description: >-
  Settles a message received from a trigger or the receive action in manual
  acknowledgement mode.
---

# Solace - Acknowledge message received from Solace action

The **Acknowledge message received from Solace** action settles a message received from a trigger or the **Receive message from queue** action in manual acknowledgement mode.

## Input

| Input field | Description |
| --- | --- |
| Acknowledgement handle | Enter the acknowledgement handle from the output of a trigger or receive action. |
| Outcome | Select the acknowledgement outcome. Options include: **ACCEPTED**: Consumes the message., **FAILED**: Redelivers the message., **REJECTED**: Routes the message to the dead-message queue. |

## Output

There is no output for this action.

---
