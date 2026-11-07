---
url: 'https://docs.workato.com/en/connectors/outlook/search-calendar-action.md'
description: >-
  The Search calendar action in the Outlook connector lets you retrieve
  calendars that match your criteria, with batches of up to 1000 results.
---

# Outlook - Search calendar action (batch)

This action retrieves the calendar details that match your criteria in Outlook.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Filter | Query to filter the records you want. |
| Search by | Search for specific Outlook calendars by specifying search by fields. Fields you can search by include **Name**, **Color**, **Is default calendar?**, **Default online meeting provider**, **Can view private items?**, **Is tallying responses?**, and **Is removable?** |
| Limit | Maximum number of rows to return. Limit is 1000 and default is 10. |
| Offset | The number of rows to skip. For example, 100. |

## Output

| Field | Description |
| --- | --- |
| Calendar | A list of calendars matching the search criteria. |

---

---
url: >-
  https://docs.workato.com/en/connectors/outlook/search-calendar-events-action.md
description: >-
  The Search calendar events action in the Outlook connector lets you search a
  specific calendar for events within a date range, in batches.
---

# Outlook - Search calendar events action (batch)

This action searches for events in a specific calendar in Outlook Calendar.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar to search in. |
| Start date | Fetch events that start on this date. |
| End date | Fetch events that end on this date. |
| Subject | Exact name of the event. Value is case-insensitive. |
| Importance | Fetch events with this level of importance. |
| Is all day | If true, only all-day events will be fetched. |
| Limit | Maximum number of rows to return. Limit is 1000 and default is 200. |
| Offset | Number of rows to skip, for example, 100. |

## Output

| Field | Description |
| --- | --- |
| Events | A list of events matching the search criteria. |

---
