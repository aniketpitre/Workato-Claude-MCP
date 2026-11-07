---
url: 'https://docs.workato.com/en/connectors/google-calendar/action-remove-guest.md'
description: >-
  The Delete attendees from an event batch action removes participants you
  specify from an existing event.
---

# Google Calendar - Delete attendees from an event action (batch)

The **Delete attendees from an event** batch action removes participants you specify from an existing event.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to modify is accessible from your connected account and that you have the necessary permissions to manage and modify events.

## Input

| Input field | Description |
| --- | --- |
| Calendar | Select the calendar that contains the event to remove attendees from. |
| Event ID | The Google Calendar ID of the event for deleting attendees. |
| Attendees source list | Provide a list datapill from which to pull attendee information. |
| Attendee email | Enter the email address of the attendee to remove. |
| Send notifications? | Select whether to notify all attendees of the update to the event. |

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
| Description | The description attached to the event. |
| Location | The location where the event takes place. |
| Start | The start time of the event. |
| End | The end time of the event. |
| Recurrence | The recurrence rules for the event. |
| Recurring event ID | The Google ID of the recurring event. |
| Original start time | Contains information about the start time of the event, such as: **Date time:** The date and time of the event., **Time zone:** The time zone of the event. |
| Visibility | The visibility of the event, such as `Public` or `Private`. |
| Reminders | Contains information about the event's reminder settings, such as: **Overrides:** Contains specific reminder overrides for this event. |
| Show me as | The availability to display during the event, such as `Busy` or `Available`. |
| Hangout link | A link to the Google Hangout associated with the event. |
| Sequence | The sequence number of the event. |
| Guests can modify | Indicates whether guests can modify the event. |
| Guests can see other guests | Indicates whether guests can see other guests. |
| Creator | Contains information about the event's creator, such as: **Email:** The email address of the creator., **Self:** Indicates whether the creator is the user managing the calendar., **Display name:** The display name of the creator. |
| Organizer | Contains information about the event's organizer, such as: **ID:** A unique identifier for the organizer., **Email:** The email address of the organizer., **Name:** The name of the organizer., **Self:** Indicates whether the organizer is the user managing the calendar. |
| Attendees | Contains information about the event's attendees, such as: **ID:** A unique identifier for the attendee., **Email:** The email address of the attendee., **Name:** The name of the attendee., **Self:** Indicates whether the attendee is the user managing the calendar., **Additional guests:** The number of additional guests for this event., **Response status:** The attendee's response status for the event invitation., **Comment:** Any comment provided by the attendee., **List size:** The number of attendees in the list., **List index:** The position of the current attendee in the list. |
| Attachments | Contains information about the event's attachments, such as: **File URL:** The URL of the attached file., **Title:** The title of the attachment., **Mime type:** MIME type of the file., **Icon link:** A link to the icon representing the file type., **File ID:** A unique identifier for the file., **List size:** The number of attachments., **List index:** The position of this attachment in the list. |

---
