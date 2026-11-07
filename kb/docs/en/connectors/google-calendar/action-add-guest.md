---
url: 'https://docs.workato.com/en/connectors/google-calendar/action-add-guest.md'
description: >-
  The Add attendees to an event batch action adds participants to an existing
  event in a calendar you specify.
---

# Google Calendar - Add attendees to an event action (batch)

The **Add attendees to an event** batch action adds participants to an existing event in a calendar you specify. The action appends the new attendees to the existing participants list. If a duplicate email address is included in the list, it overwrites the existing attendee's response and comments.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to modify is accessible from your connected account and that you have the necessary permissions to manage and modify events.

## Input

| Input field | Definition |
| --- | --- |
| Calendar | Select the calendar that contains the event in which you plan to add attendees. |
| Event ID | Enter the Google Calendar ID of the event in which you plan to add attendees. |
| Attendees source list | Provide a list datapill from which to pull attendee information. |
| Attendee email | Enter a comma-separated list of attendee emails to invite to the event. |
| Comment | Enter a comment to attach to the attendee's response. |
| Optional | Select whether the to make the attendee optional for the event. |
| Response status | Set the response status for each attendee, such as `accepted`, `declined`, `tentative`, or `needsAction`. |
| Send notifications? | Select whether to notify all attendees about the event. |

## Output

| Output field | Description |
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
| Creator | Contains information about the event's creator, such as: **Email:** The email address of the creator., **Self:** Indicates whether the creator is the user managing the calendar. |
| Organizer | Contains information about the event's organizer, such as: **Email:** Email address of the organizer., **Self:** Indicates if the organizer is the user managing the calendar. |
| Attendees | Contains information about the event's attendees, such as: **Email:** The email address of the attendee., **Name:** The name of the attendee., **Response status:** The attendee's response status for the event invitation., **Comment:** Any comment provided by the attendee., **Optional:** Indicates whether the current attendee is optional for this event., **Organizer:** Indicates whether the current attendee is the event's organizer., **Self:** Indicates whether the attendee is the user managing the calendar., **List size:** The number of attendees in the list., **List index:** The position of the current attendee in the list. |
| Attachments | Contains information about the event's attachments, such as: **File URL:** The URL of the attached file., **Title:** The title of the attachment., **Mime type:** MIME type of the file., **Icon link:** A link to the icon representing the file type., **File ID:** A unique identifier for the file., **List size:** The number of attachments., **List index:** The position of this attachment in the list. |

---
