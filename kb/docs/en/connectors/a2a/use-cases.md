---
url: 'https://docs.workato.com/en/connectors/a2a/use-cases.md'
description: >-
  This document includes common use cases for the A2A Protocol connector in
  Workato.
---

# A2A Protocol - Common use cases

The A2A Protocol actions are commonly used together in the following ways:

## Asynchronous polling

Complete the following steps to use A2A Protocol with **Asynchronous polling**:

1. Run **Send task** with **Wait for result?** set to `No`.
   
2. Store the returned task ID.
   
3. Use the **Get task status** action in a later recipe to check whether the task has completed.
   

## Branching on task state

Complete the following steps to use A2A Protocol with **Branching on task state**:

1. Add a conditional step after **Get task status** that uses the `status.state` output datapill.
   
2. Configure the following in your recipe:
   
   - Route `COMPLETED` tasks to a result handler
   - Route `FAILED` tasks to an alert
   - Route `WORKING` tasks to a wait step

## Auditing past tasks

Complete the following steps to use A2A Protocol with **Auditing past tasks**:

Retrieve a historical task by ID and its message history to log or report on the conversation.

> **TASK ID RETENTION**
> 
> The agent must recognize the supplied task ID. Some agents retain task records for a limited time. Refer to the connected agent's documentation for retention details.

---
