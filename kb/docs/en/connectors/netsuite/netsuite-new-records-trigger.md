---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-new-records-trigger.md
description: >-
  The new standard object and new custom object triggers in the NetSuite SOAP
  connector pick up newly created records of the selected object type.
---

# NetSuite SOAP - New standard object and new custom object trigger

The new standard object and new custom object triggers are very similar.

> **Limited support**
> 
> Because of API limitations, Workato does not support [some types of records](/en/connectors/netsuite/netsuite-unsupported-records).

## Configure the trigger

To use this trigger, first, we must select the standard object or the custom object to monitor. We also must input the datetime in the **From** field to pinpoint the exact date from which the recipe should start processing records.

![Unconfigured NetSuite new object trigger](/assets/unconfigured-netsuite-new-trigger.CF9Wj014.png)_NetSuite new object trigger - unconfigured. Select the object to monitor for newly created records._

When the recipe starts for the first time, it picks up all existing instances of the selected object created after the datetime in the **From** field. Subsequently, it processes only the new instances.

Consider the selected sales order and 1 Jan, 2017 midnight trigger:

![Configured NetSuite new object trigger](/assets/configured-netsuite-new-trigger.Ds-tMDTh.png)_NetSuite new object trigger - configured_

On first run, the recipe processes all sales orders from or after 1 Jan, 2017 midnight. Subsequently, if the recipe continues to run, the recipe picks up only new sales.

> **Trigger behavior when you stop and restart a recipe**
> 
> If you stop the recipe, the recipe processes all new sales orders created during the stoppage interval when restarted.
