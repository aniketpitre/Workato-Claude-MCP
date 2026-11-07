---
url: 'https://docs.workato.com/en/connectors/apify/new-finished-actor-run-trigger.md'
description: >-
  The New finished actor run trigger starts a recipe when a run of an Actor you
  select finishes in Apify.
---

# Apify - New finished actor run trigger

The **New finished actor run** trigger starts a recipe when a run of an Actor you select finishes in Apify.

The trigger registers a webhook in Apify when you start the recipe. Start the recipe first, then run the Actor.

## Input

| Input field | Description |
| --- | --- |
| Actor | Select the Actor to monitor for finished runs from the drop-down menu, or use a custom value. A custom value is an Actor ID, or the username and Actor name joined with a tilde. For example, `apify~hello-world`. |

## Output

| Output field | Description |
| --- | --- |
| User ID | The ID of the Apify user that owns the webhook event. |
| Created at | When the webhook event was created. |
| Event type | The webhook event type, for example `ACTOR.RUN.SUCCEEDED`. |
| Event data | The event payload, which contains the Actor ID, Actor task ID, and Actor run ID. |
| Resource | The finished Actor run object. |

---
