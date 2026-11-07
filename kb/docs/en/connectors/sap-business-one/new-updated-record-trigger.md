---
url: >-
  https://docs.workato.com/en/connectors/sap-business-one/new-updated-record-trigger.md
description: >-
  The New/updated record trigger in the SAP Business One connector runs your
  recipe when a selected object, such as an order, is created or updated.
---

# SAP Business One - New/updated record trigger

The **New/updated record** trigger runs the recipe when you create or update a specific SAP Business One object, such as an order.

![SAP Business One - New/Updated record trigger](/assets/new-update-record-trigger.PNIT8OGs.png)_SAP Business One New/updated record trigger_

## Input

| Input Field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. Defaults to every 10 minutes if left blank. |
| Object | Select a SAP Business One object from the drop-down list. |
| Object key | Select the ID that the recipe uses to identify the monitored object. |
| When first started, this recipe should pick up events from | Objects created after this date and time will be processed in the trigger. If left blank, the trigger will pick up entries created one hour before the recipe is first started. |
| Set trigger condition | Defines further guidelines added to a specific trigger to filter the type of trigger events selected for processing. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps.
