---
url: 'https://docs.workato.com/en/connectors/outlook/list-events-action.md'
description: >-
  The List all instances of an event action in the Outlook connector lets you
  list every occurrence of a recurring calendar event series.
---

# Outlook - List all instances of an event action (batch)

This action lists all individual instances or occurrences of a calendar event series in Outlook.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar. |
| Event ID | The ID of the event to list all the individual instances. |
| Start time | Start time denotes the timestamp from which to pick up the occurrences. |
| End time | End time denotes the timestamp until which to pick up the occurrences. |
| Next page URL | Next page URL, returned by a previous call, to request the next page of results. |

## Output

| Field | Description |
| --- | --- |
| Next page URL | The URL for the next page of results. |
| Total records | The total number of records. |
| Occurrences | A list of occurrences of the event. |

---
