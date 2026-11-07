---
url: >-
  https://docs.workato.com/en/connectors/oracle-ebs/triggers/new-business-event.md
description: >-
  The New business event trigger monitors business events in Oracle E-Business
  Suite such as invoice creation, order status changes, or employee updates.
---

# Oracle E-Business Suite - New business event trigger

The **New business event** trigger monitors business events in Oracle E-Business Suite, such as invoice creation, order status changes, or employee updates.

This trigger creates a subscription in Oracle's Business Event System for the specified event, which uses Oracle Advanced Queuing (AQ) infrastructure for reliable event notifications.

> **TIP**
> 
> Oracle E-Business Suite includes over 900 preconfigured business events—use [Oracle Integration Repository](https://docs.oracle.com/cd/E18727_01/doc.121/e12064/T291171T329891.htm) to discover available events.

## Input

| Input field | Description |
| --- | --- |
| Product family | Select the Oracle E-Business Suite product family that publishes the event. |
| Product | Select the specific product within the product family. |
| Event name | Select the business event to monitor. |
| System name | Enter the name of the system where the subscription executes. The default is `DEV.US.ORACLE.COM` if left blank. |
| Description | Enter text describing the subscription's purpose. |
| Priority | Select the priority for processing deferred subscriptions. Options include `Normal`, `High`, and `Low`. |

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
