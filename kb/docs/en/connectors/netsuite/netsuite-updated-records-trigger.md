---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-updated-records-trigger.md
description: >-
  The new/updated standard object and custom object triggers in the NetSuite
  SOAP connector pick up records created or updated after a set date and time.
---

# NetSuite SOAP - New/Updated standard object and new/updated custom object triggers

The new/updated standard object and new/updated custom object triggers are very similar.

> **Limited support**
> 
> Because of API limitations, Workato does not support [some types of records](/en/connectors/netsuite/netsuite-unsupported-records).

When a recipe that updates records starts for the first time, it processes all instances of the selected object created or updated after the datetime in the **From** field.

Subsequently, the recipe processes all newly created instances or updated instances.

## Configure the trigger

To use this trigger, follow these steps:

1. Select the standard object or the custom object to monitor.
   
2. Identify the datetime in the **From** field so the recipe starts processing the correct records.
   
   ![Unconfigured NetSuite new/updated object trigger](/assets/unconfigured-netsuite-new-updated-trigger.Ci6wvg7K.png)_NetSuite new/updated object trigger - unconfigured. Select the object to monitor for newly created or updated records._
   

## Example

Consider the selected sales order and 1 Jan, 2017 midnight trigger:

![Configured NetSuite new/updated object trigger](/assets/configured-netsuite-new-updated-trigger.DJnRXlp5.png)_NetSuite new/updated object trigger - configured_

On the first run, the recipe processes all sales orders from or after 1 Jan. 2017 at midnight. Subsequently, if the recipe continues to run, the recipe picks up only new sales.

> **Trigger behavior when the recipe stops and restarts**
> 
> If you stop the recipe, it processes all new sales orders created during the stoppage interval when you restart it.
> 
> The recipe only picks up the most recent version of the search record. So, if a record updates three (3) times during the outage interval, the recipe only picks up the last version of the record when it restarts.
