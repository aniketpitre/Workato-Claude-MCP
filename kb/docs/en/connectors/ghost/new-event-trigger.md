---
url: 'https://docs.workato.com/en/connectors/ghost/new-event-trigger.md'
description: The New event trigger monitors a Ghost post or member for webhook events.
---

# Ghost - New event trigger

The **New event** trigger monitors Ghost for the webhook event you select. Starting the recipe registers a webhook in Ghost, and stopping the recipe removes it.

## Input

| Input field | Description |
| --- | --- |
| Event | Select the Ghost webhook event to listen for. You can select `Post published`, `Published post edited`, `Post unpublished`, `Post scheduled`, `Member added`, or `Member edited`. Defaults to `Post published` if left blank. |

## Output

Output fields dynamically generate based on the event you select: post fields for post events, member fields for member events. Refer to the [Ghost Admin API](https://docs.ghost.org/admin-api) documentation for more information on available output fields.

---
