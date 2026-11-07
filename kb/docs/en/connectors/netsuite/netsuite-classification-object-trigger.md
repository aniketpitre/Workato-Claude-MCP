---
url: >-
  https://docs.workato.com/en/connectors/netsuite/netsuite-classification-object-trigger.md
description: >-
  The Classification object trigger in the NetSuite SOAP connector monitors
  classification objects such as departments, locations, and classifications.
---

# NetSuite SOAP - Classification object trigger

Some objects in NetSuite are classification objects: departments, locations, and classifications.

Select the classification object to monitor.

When the recipe runs for the first time, it picks up all existing instances of the selected object. Subsequently, the recipe processes only newly created instances.

![New classification object trigger](/assets/new-classification-object-trigger.4nlRkXuk.png)_New classification object trigger_

For example, if I select **departments** as the triggering object, the trigger picks up all existing department objects when the recipe runs for the first time. Subsequently, if the recipe keeps running, it only picks up newly created departments.

> **Stopping and re-starting recipes**
> 
> If the recipe stops and then starts again, it picks up all new departments that you create during the stoppage interval.
