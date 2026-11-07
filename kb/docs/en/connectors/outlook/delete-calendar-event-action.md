---
url: 'https://docs.workato.com/en/connectors/outlook/delete-calendar-event-action.md'
description: >-
  The Delete calendar event action in the Outlook connector lets you delete a
  calendar event using its event ID.
---

# Outlook - Delete calendar event action

Use this action to delete a calendar event using the event ID.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar you plan to monitor from the list. |
| Event ID | Provide the ID of the event to delete. You can find the event ID in the event URL or use the [Search calendar event action](/en/connectors/outlook/search-calendar-events-action) to fetch the event and get the ID. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the event was deleted successfully. |

---
