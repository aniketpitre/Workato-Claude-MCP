---
url: 'https://docs.workato.com/en/connectors/vercel/new-deployment-event-trigger.md'
description: >-
  The New deployment event trigger monitors Vercel in real time for deployment
  events and starts a recipe when they occur.
---

# Vercel - New deployment event (real-time) trigger

The **New deployment event (real-time)** trigger monitors Vercel in real time for deployment events and starts a recipe when they occur. Workato creates the webhook in Vercel when the recipe starts and deletes it when the recipe stops.

## Input

| Input field | Description |
| --- | --- |
| Events | Optional. Select the events you plan to listen for. Options include `deployment.created`, `deployment.succeeded`, `deployment.error`, `deployment.canceled`, `deployment.promoted`, and `deployment.rollback`. Defaults to all events if left blank. |
| Project IDs | Optional. Select projects or enter a comma-separated list of project IDs to limit events to those projects. |

## Output

| Output field | Description |
| --- | --- |
| ID | The event ID. |
| Type | The event type. For example, `deployment.succeeded`. |
| Created at | When the event was created, in ISO 8601 format. |
| Payload | The event details, such as user ID, team ID, deployment, project ID, alias, links, plan, and regions. |
| Region | The Vercel region that sent the event. |

---
