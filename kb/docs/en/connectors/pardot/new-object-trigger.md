---
url: 'https://docs.workato.com/en/connectors/pardot/new-object-trigger.md'
description: >-
  Invoke a recipe when a user creates a new object in Salesforce Account
  Engagement (Pardot).
---

# Salesforce Account Engagement (Pardot) - New object trigger

The **New object** trigger invokes when a user creates a new object in Salesforce Account Engagement (Pardot).

## Input

| Input field | Description |
| --- | --- |
| Object name | Select the object to monitor. |
| When first started, this recipe should pick up events from | Optional. When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get events created one hour ago. You can't change this value after you run or test the recipe. |

## Output

Output fields dynamically generate based on the object you select. Refer to the Salesforce [Account Engagement API](https://developer.salesforce.com/docs/marketing/pardot/overview) documentation for more information on available output fields. The following field is common to all objects.

| Output field | Description |
| --- | --- |
| ID | The object's unique ID. |

---
