---
url: 'https://docs.workato.com/en/connectors/outlook/new-event-trigger.md'
description: >-
  The New event trigger in the Outlook connector picks up new calendar events in
  real time and processes each event as a separate job.
---

# Outlook - New event trigger (real-time)

This trigger picks up new events in your Outlook calendar. It checks for new events in real-time and processes each event as a separate job.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar to search in. |
| When first started, this recipe should pick up events from | When you start a recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records added or updated one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output datatree contains information about the event. This includes the event ID, subject, start and end times, and other event details.

| Field | Description |
| --- | --- |
| ID | The unique identifier for the event. |
| Change key | The change key for the event. |
| Created date time | The date and time the event was created. |
| Last modified date time | The date and time the event was last modified. |
| Response status | The status of the response. This object includes the response to the event and the time of the response. |
| Has attachments | Indicates whether the event has attachments. |
| Subject | The subject of the event. |
| Body | The body of the event. This object includes the event content and content type. |
| Body preview | The preview of the body of the event. |
| Importance | The importance of the event. |
| Sensitivity | The sensitivity of the event. |
| Series master ID | The master ID of the event. |
| Show as | The status to show for the event. |
| Online meeting URL | The URL of the event if the event is online. |
| Is online meeting | Indicates whether the event is online. |
| Online meeting provider | The online provider of the event. |
| Online meeting | The online meeting name. |
| Allow new time proposals | Indicates whether the event host allows new time proposals for the event. |
| Occurrence ID | The ID of the event occurrence. |
| Is draft | Whether the event is a draft event. |
| Hide attendees | Indicates whether the event host has hidden the event attendees. |
| Start | The start time of the event. This object includes the event start date and time zone. |
| End | The end time of the event. This object includes the event end date and time zone. |
| Is all day | Indicates whether the event is an all-day event. |
| Is cancelled | Indicates whether the event is cancelled. |
| Is organizer | Indicates whether the user is the organizer of the event. |
| Is reminder on | Indicates whether a reminder is set for the event. |
| Response requested | Indicates whether a response is requested. |
| Type | The type of event. Possible values include: `singleInstance`, `occurrence`, `exception`, and `seriesMaster`. |
| Original start time zone | The start time zone that was set when the event was created. |
| Original end time zone | The end time zone that was set when the event was created. |
| Reminder minutes before start | The number of minutes before the event start time that the reminder alert occurs. |
| Attendees | The attendees of the event. This object includes the attendee names, email addresses, status (response and time of response), and types of attendees. |
| Location | The location of the event. This object includes the name of the location, location type, address, and unique ID and unique ID type of the location. |
| Locations | The locations of the event. This object includes the display names of attendees, the location URI, location type, address, coordinates, and unique ID and unique ID type of the location. |
| Recurrence | If this is a recurring meeting, this object contains the meeting pattern and the range of occurrences. |
| Organizer | This object includes the name and email address of the event organizer. |
| Web link | The web link to the event. |
| Transaction ID | The unique identifier of the event. |

---
