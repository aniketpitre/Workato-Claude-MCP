---
url: 'https://docs.workato.com/en/connectors/shopware/new-record-trigger.md'
description: >-
  The New record trigger runs when a new object record, such as a customer, is
  created.
---

# Shopware - New record trigger

The **New record** trigger runs when a new object record, such as a customer, is created. It checks for new events once every polling interval.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to monitor events for. |
| Trigger poll interval | Specify how frequently to check for new events. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get events created one hour ago. |

## Output

The output schema depends on the selected object. Use the output fields to map datapills to downstream steps.

For example, if you select the **Order** object, the output includes the following:

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the order. |
| Active | Indicates whether the order is active or not. |
| Customer number | The unique number of customer who placed the order. |
| Company | The company that placed the order. |
| Email | The email address of the company/customer that placed the order. |

---
