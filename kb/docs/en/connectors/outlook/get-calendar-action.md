---
url: 'https://docs.workato.com/en/connectors/outlook/get-calendar-action.md'
description: >-
  The Get calendar by ID action in the Outlook connector lets you retrieve the
  details of a specific calendar using its calendar ID.
---

# Outlook - Get calendar by ID action

This action retrieves calendar details from Outlook using the calendar ID.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar from list. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique ID of the calendar. |
| Name | The name of the calendar. |
| Color | The color of the calendar. |
| Hex color | The hex color of the calendar. |
| Is default calendar | Indicates whether the calendar is the default calendar. |
| Change key | The change key of the calendar. |
| Can share | Indicates whether the calendar can be shared. |
| Can edit | Indicates whether the calendar can be edited. |
| Allowed online meeting providers | The allowed online meeting providers for the calendar. |
| Default online meeting provider | The default online meeting provider for the calendar. |
| Can view private items | Indicates whether private items can be viewed in the calendar. |
| Is tallying responses | Indicates whether responses are being tallied for the calendar. |
| Is removable | Indicates whether the calendar is removable. |
| Owner | The owner of the calendar. |

---
