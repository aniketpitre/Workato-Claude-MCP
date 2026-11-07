---
url: 'https://docs.workato.com/en/connectors/zendesk/updated-ticket-trigger.md'
description: >-
  The New/updated ticket trigger in the Zendesk connector picks up tickets in
  real time as soon as they are created or updated.
---

# Zendesk - New/updated ticket trigger (real time)

This trigger picks up tickets as soon they are created or updated. Each ticket is processed as a separate job.

This trigger picks up tickets in real time. If you want to process tickets from a designated time, you can use the [polling trigger](/en/connectors/zendesk/new-ticket-trigger).

> **Role privileges**
> 
> You need a Zendesk account with the Administrator role to use this trigger in your recipe.

![New/updated ticket trigger](/assets/updated-ticket-trigger.D6KCzTZB.png)_New/updated ticket trigger_

## Input

There are no input fields for this trigger.

> **AUTOMATIC TRIGGER CREATION IN ZENDESK**
> 
> This Workato trigger automatically creates a Zendesk trigger. You can find the trigger in your Zendesk account under **Admin > Business rules > Triggers**.

## Output

The output of this action contains the full set of columns from the selected ticket. Here are some commonly used outputs.

| Output field | Description |
| --- | --- |
| Ticket ID | The unique Zendesk ID of the ticket. This is automatically assigned when the ticket is created. |
| Subject | The subject of the ticket. |
| Type | The type of ticket. Permitted values are `problem`, `incident`, `question`, or `task`. |
| Priority | The priority of the ticket. Permitted values are `urgent`, `high`, `normal`, or `low`. |
| Ticket custom fields | Includes data of ticket custom fields. |

Click here for a full list of [ticket outputs](/en/connectors/zendesk/ticket-fields#ticket-output-fields).

---
