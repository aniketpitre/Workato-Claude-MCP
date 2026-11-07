---
url: 'https://docs.workato.com/en/connectors/google-calendar/action-all-day-event.md'
description: >-
  The Create all day event action schedules an all-day event in a calendar you
  specify.
---

# Google Calendar - Create all day event action

The **Create all day event** action schedules an all-day event in a calendar you specify. You can create events in calendars that belong to other Google users if you have the permissions to change events.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to modify is accessible from your connected account and that you have the necessary permissions to add events.

## Input

| Input field | Definition |
| --- | --- |
| Calendar | Select the Google Calendar in which you plan to create an event. |
| Start date | Specify the starting date for the all-day event. |
| End date | Specify the ending date for the all-day event. |
| Displayed time zone | Select the time zone for displaying event times. |
| Name | Enter a name for the event. |
| Event description | Enter a description for the event. |
| Location | Enter a location for the event, if applicable. |
| Attendee emails | Enter a comma-separated list of attendee emails to invite to the event. |
| Send notifications? | Select whether to send notifications to attendees when events are created or updated. This field is deprecated and will be overridden by the send updates field. |
| Send updates | Select who to notify about the updates to the event. |
| Guests can modify? | Select whether to allow guests to modify the event. |
| Display guests list? | Select whether to display the list of guests on the event. |
| Status | Select the status of the event, such as `Confirmed` or `Canceled`. |
| Visibility | Select the visibility of the event, such as `Public`, `Private`, or `Default`. The calendar's `Default` visibility is used if this field is left empty. |
| Show me as | Select the availability to display during the event, such as `busy` or `available`. This field defaults to `Busy` if left empty. |

## Output

| Output field | Definition |
| --- | --- |
| Kind | The type of the resource, such as `calendar#event`. |
| Etag | The etag for the event. |
| Color ID | The Google ID for the color attached to the event. |
| Event import ID | The Google import ID for the event. |
| ID | The Google ID for the event. |
| Status | The status of the event, such as `confirmed` or `cancelled`. |
| URL | The URL for the event. |
| Created | A timestamp indicating when the event was created. |
| Updated | A timestamp indicating when the event was last updated. |
| Summary | The title of the event. |
| Description | The description of the event. |
| Location | The location of the event. |
| Start | The start time of the event. |
| End | The end time of the event. |
| Recurrence | The recurrence rules for the event. |
| Recurring event ID | The Google ID of the recurring event. |
| Original start time | Contains information about the start time of the event, such as: **Date time:** The date and time of the event., **Time zone:** The time zone of the event. |
| Visibility | The visibility of the event, such as `Public` or `Private`. |
| Reminders | Contains information about the event's reminder settings, such as: **Use default:** Indicates whether the default reminder settings are used., **Overrides:** Contains specific reminder overrides for this event. |
| Show me as | The availability to display during the event, such as `Busy` or `Available`. |
| Hangout link | A link to the Google Hangout associated with the event. |
| Sequence | The sequence number of the event. |
| Guests can modify | Indicates whether guests can modify the event. |
| Guests can see other guests | Indicates whether guests can see other guests. |
| Attendees | Contains information about the event's attendees, such as: **ID:** A unique identifier for the attendee., **Email:** The email address of the attendee., **Name:** The name of the attendee., **Self:** Indicates whether the attendee is the user managing the calendar., **Response status:** The attendee's response status for the event invitation., **Comment:** Any comment provided by the attendee., **List size:** The number of attendees in the list., **List index:** The position of the current attendee in the list. |
| Creator | Contains information about the event's creator, such as: **ID:** A unique identifier for the creator., **Email:** The email address of the creator., **Name:** The name of the creator., **Self:** Indicates whether the creator is the user managing the calendar. |
| Organizer | Contains information about the event's organizer, such as: **ID:** A unique identifier for the organizer., **Email:** The email address of the organizer., **Name:** The name of the organizer., **Self:** Indicates whether the organizer is the user managing the calendar. |

---

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

---

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

---

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

---
