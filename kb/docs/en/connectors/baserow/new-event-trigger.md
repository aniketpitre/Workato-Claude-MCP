---
url: 'https://docs.workato.com/en/connectors/baserow/new-event-trigger.md'
description: >-
  Fire a recipe on row changes in a Baserow table using a webhook you register
  in Baserow.
---

# Baserow - New event trigger

The **New event** trigger monitors a Baserow table for newly created, updated, or deleted rows.

> **REGISTER THE WEBHOOK IN BASEROW**
> 
> This trigger uses a static webhook URL. Save the recipe, then copy the webhook URL from the trigger step. In Baserow, open the table's menu, go to **Webhooks**, and create a webhook pointing at that URL. Select the events you want to send, such as **rows.created**, **rows.updated**, and **rows.deleted**.

## Input

| Input field | Description |
| --- | --- |
| Object type | Select the object type, such as **Row**. |
| Table ID | Select the table to receive events from. Register the webhook for this table in Baserow, as shown in the tip above. |
| Event type | Select the event to listen for. Options are **Rows created**, **Rows updated**, or **Rows deleted**. |

## Output

Output fields dynamically generate based on the object type you select. The following fields are common to all objects.

| Output field | Description |
| --- | --- |
| Event type | The event that invoked the trigger. Options are `rows.created`, `rows.updated`, or `rows.deleted`. |
| Event ID | The event's unique identifier. |
| Table ID | The ID of the table the event occurred in. |
| Database ID | The ID of the database the table belongs to. |
| Workspace ID | The ID of the workspace the database belongs to. |
| Old item | The row's previous field values before the update. The **Old item** field is only available for `rows.updated` events. |
| Row ID | The row's unique identifier. |
| Order | The row's position among the table's rows. |

---
