---
url: 'https://docs.workato.com/en/connectors/outlook/get-calendar-event-action.md'
description: >-
  The Get calendar event by ID action in the Outlook connector lets you retrieve
  an event from a specific calendar using its event ID.
---

# Outlook - Get calendar event by ID action

This action retrieves an event in a specific calendar in Outlook Calendar using the event ID.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar to search in. |
| Event ID | The ID of the event to retrieve. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique ID of the event. |
| Change key | The change key of the event. |
| Created date time | The timestamp when the event was created. |
| Last modified date time | The timestamp when the event was last modified. |
| Response status | The response status of the event. |
| Has attachments | Indicates whether the event has attachments. |
| Subject | The subject of the event. |
| Body | The body content of the event. |
| Body preview | The preview of the body content. |
| Importance | The importance of the event. |
| Sensitivity | The sensitivity of the event. |
| Series master ID | The series master ID of the event. |
| Show as | The status to show for the event. |
| Online meeting URL | The URL for the online meeting. |
| Is online meeting | Indicates whether the event is an online meeting. |
| Online meeting provider | The provider for the online meeting. |
| Online meeting | The online meeting details. |
| Allow new time proposals | Indicates whether new time proposals are allowed. |
| Occurrence ID | The occurrence ID of the event. |
| Is draft | Indicates whether the event is a draft. |
| Hide attendees | Indicates whether attendees are hidden. |
| Start | The start time of the event. This object includes the start time and time zone of the event. |
| End | The end time of the event. This object includes the end time and time zone of the event. |
| Is all day | Indicates whether the event is an all day event. |
| Is cancelled | Indicates whether the event is cancelled. |
| Is organizer | Indicates whether the user is the organizer of the event. |
| Is reminder on | Indicates whether a reminder is set for the event. |
| Response requested | Indicates whether a response is requested for the event. |
| Type | The type of the event. |
| Original start time zone | The original start time zone of the event. |
| Original end time zone | The original end time zone of the event. |
| Reminder minutes before start | The number of minutes before the event start time when the reminder alert occurs. |
| Attendees | The attendees of the event. This object includes the attendee names, email addresses, status (response and time of response), and types of attendees. |
| Location | The location of the event. This object includes the name of the location, location type, address, and unique ID and unique ID type of the location. |
| Locations | The locations of the event. This object includes the display names of attendees, the location URI, location type, address, coordinates, and unique ID and unique ID type of the location. |
| Recurrence | If this is a recurring meeting, this object contains the meeting pattern and the range of occurrences. |
| Organizer | This object includes the name and email address of the event organizer. |
| Web link | The web link to the event. |
| Transaction ID | The transaction ID of the event. |

---
