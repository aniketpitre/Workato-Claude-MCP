---
url: 'https://docs.workato.com/en/connectors/jamf/new-event-trigger.md'
description: >-
  The New event trigger fires when a JAMF Pro webhook event occurs, including
  computer enrollment, check-in, inventory, and policy events.
---

# JAMF - New event trigger

The **New event** trigger starts a recipe when a JAMF Pro webhook event fires. The trigger registers a webhook in JAMF Pro that points to a Workato-provided URL, then processes events as JAMF Pro delivers them.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the JAMF webhook event to subscribe to. |

Additional input fields are dynamically generated based on the object you select.

## Output

Output fields are dynamically generated based on the object you select.

---
