---
url: >-
  https://docs.workato.com/en/connectors/google-calendar/action-get-calendar-by-id.md
description: >-
  The Get calendar by ID action retrieves a calendar you specify by its Google
  Calendar ID.
---

# Google Calendar - Get calendar by ID action

The **Get calendar by ID** action retrieves a calendar you specify using its Google Calendar ID.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to retrieve is accessible from your connected account.

## Input

| Input field | Description |
| --- | --- |
| Calendar ID | Provide the Google Calendar ID of the calendar you plan to retrieve. |

## Output

| Output field | Definition |
| --- | --- |
| Kind | The type of the resource, such as `calendar#event`. |
| Etag | The etag for the calendar. |
| ID | The Google ID for the calendar. |
| Summary | The title of the calendar. |
| Description | The description of the calendar. |
| Location | The location of the calendar. |
| Time zone | The time zone of the calendar. |
| Access role | The access roles assigned to the calendar, such as `reader`, `writer`, and `owner`. |
| Conference properties | Contains the calendar's conference properties, such as: **Allowed conference solution types:** The platform used for conferences in the calendar. |
