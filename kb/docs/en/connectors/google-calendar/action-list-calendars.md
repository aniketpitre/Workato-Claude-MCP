---
url: >-
  https://docs.workato.com/en/connectors/google-calendar/action-list-calendars.md
description: >-
  The List calendars action retrieves all calendars from your connected Google
  Calendar account.
---

# Google Calendar - List calendars action

The **List calendars** action retrieves all calendars from your connected Google Calendar account.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendars you plan to retrieve are accessible from your connected account.

## Input

| Input field | Description |
| --- | --- |
| Minimum access role | Select the minimum role the connected account must have in a calendar to retrieve it. |
| Show deleted | Select whether to retrieve deleted calendars. |
| Show hidden | Select whether to retrieve hidden calendars. |

## Output

| Output field | Definition |
| --- | --- |
| Kind | The type of the resource. |
| Etag | The Etag of the calendar. |
| ID | The Google ID for the calendar. |
| Summary | The title of the calendar. |
| Description | The description of the calendar. |
| Time zone | The time zone of the calendar. |
| Color ID | The Google ID for the color attached to the calendar. |
| Background color | The calendar's background color. |
| Foreground color | The calendar's foreground color. |
| Selected | Indicates whether the calendar is selected in Google calendar. |
| Access role | The access roles assigned to the calendar, such as `reader`, `writer`, and `owner`. |
| Default reminders | Contains the reminder settings for the calendar, such as: **Method:** The method of the reminder, such as `email` or `popup`.; **Minutes:** The number of minutes before an event the reminder occurs.; **List size:** The total number of reminders set for an event.; **List index:** The position of this specific reminder in the list of reminders. |
| Notification settings | Contains a list of the settings for each of the calendar's notifications, including their: **Type:** The type of notification.; **Method:** The method of notification, such as `email` or `popup`.; **List size:** The total number of notifications set for this calendar.; **List index:** The position of this specific notification in the list of notifications. |
| Primary | Indicates whether the calendar is set as primary in Google calendar. |
| Conference properties | Contains the calendar's conference properties, such as: **Allowed conference solution types:** The platform used for conferences in the calendar. |
| List size | The total number of calendars retrieved. |
| List index | The position of this specific calendar in the list of calendars. |
