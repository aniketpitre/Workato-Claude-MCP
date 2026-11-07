---
url: 'https://docs.workato.com/en/connectors/creatio/new-event-trigger.md'
description: The New event trigger runs when a new event is detected in Creatio.
---

# Creatio - New event trigger

The **New event** trigger runs when a new event is detected in Creatio, for example, when a record is created.

![Creatio trigger](/assets/creatio-new-event-trigger.CEBZ8sJi.png)_Creatio trigger_

## Input

| Input field | Description |
| --- | --- |
| Event | Enter the event you plan the trigger to pick up jobs for. It should be the same as in the UI. For example, `account.created` or `account.updated`. |

## Output

The output fields are determined by the output fields defined in the input. Map the relevant datapill from the data tree to subsequent steps.

---
