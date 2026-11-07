---
url: >-
  https://docs.workato.com/en/connectors/google-calendar/action-create-calendar.md
description: >-
  The Create calendar action creates a new calendar with the name, description,
  and time zone you specify.
---

# Google Calendar - Create calendar action

The **Create calendar** action creates a new calendar with the name, description, and time zone you specify.

## Input

| Input field | Description |
| --- | --- |
| Calendar name | Enter a name for the new calendar. |
| Description | Enter a description for the new calendar. |
| Time zone | Select a time zone for the new calendar. |

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
