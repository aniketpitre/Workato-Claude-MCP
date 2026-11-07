---
url: >-
  https://docs.workato.com/en/connectors/google-calendar/trigger-event-updated.md
description: >-
  The New/updated event monitors a calendar you specify for newly created or
  updated events.
---

# Google Calendar - New/updated event trigger

The **New/updated event** monitors a calendar you specify for newly created or updated events. This trigger first fetches events created or updated within the last hour. On subsequent runs, it monitors the selected calendar in real time, fetching new or updated events as they occur.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to monitor is accessible from your connected account and that you have the necessary permissions to access events.

## Input

| Input field | Description |
| --- | --- |
| Calendar | Select the calendar you plan to monitor for new or updated events. |
| Include deleted events? | Select whether to trigger jobs for deleted events. |

## Output

| Output field | Description |
| --- | --- |
| Calendar ID | The Google ID of the calendar that contains the event. |
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
| Attachments | Contains information about the event's attachments, such as: **File URL:** The URL of the attached file., **Title:** The title of the attachment., **Mime type:** MIME type of the file., **Icon link:** A link to the icon representing the file type., **File ID:** A unique identifier for the file., **List size:** The number of attachments., **List index:** The position of this attachment in the list. |
| Attendees | Contains information about the event's attendees, such as: **ID:** A unique identifier for the attendee., **Email:** The email address of the attendee., **Name:** The name of the attendee., **Self:** Indicates whether the attendee is the user managing the calendar., **Response status:** The attendee's response status for the event invitation., **Comment:** Any comment provided by the attendee., **List size:** The number of attendees in the list., **List index:** The position of the current attendee in the list. |
| Creator | Contains information about the event's creator, such as: **ID:** A unique identifier for the creator., **Email:** The email address of the creator., **Name:** The name of the creator., **Self:** Indicates whether the creator is the user managing the calendar. |
| Organizer | Contains information about the event's organizer, such as: **ID:** A unique identifier for the organizer., **Email:** The email address of the organizer., **Name:** The name of the organizer., **Self:** Indicates whether the organizer is the user managing the calendar. |
