---
url: >-
  https://docs.workato.com/en/connectors/oracle-ebs/triggers/new-custom-business-event.md
description: >-
  The New custom business event trigger monitors custom business events in
  Oracle E-Business Suite.
---

# Oracle E-Business Suite - New custom business event trigger

The **New custom business event** trigger monitors custom business events in Oracle E-Business Suite. Provide the event name and optional subscription details to receive Oracle EBS events in real-time.

This trigger creates a subscription in Oracle's Business Event System for the specified event, which uses Oracle Advanced Queuing (AQ) infrastructure for reliable event notifications.

## Input

| Input field | Description |
| --- | --- |
| Event name | Provide the name of the business event to monitor. |
| System name | Enter the name of the system where the subscription executes. The default is `DEV.US.ORACLE.COM` if left blank. |
| Description | Enter text describing the subscription's purpose. |
| Priority | Select the priority for processing deferred subscriptions. Options include `Normal`, `High`, and `Low`. The default is `Normal`. |

## Output

| Output field | Description |
| --- | --- |
| Event name | The name of the business event that occurred. |
| Event key | Unique identifier for this specific event instance. |
| Event data | Event-specific information in XML format. Structure varies by event type. |
| Message (Event data) | The XML payload containing event details. |
| Correlation ID | Identifier linking related events together. |
| Parameter list | Collection of key-value pairs providing event context. |
| Parameter (Parameter list) | Individual parameter within the list. |
| Name (Parameter) | The name of the parameter. |
| Value (Parameter) | The value of the parameter. |
