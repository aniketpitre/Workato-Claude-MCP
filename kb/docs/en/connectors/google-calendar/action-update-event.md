---
url: 'https://docs.workato.com/en/connectors/google-calendar/action-update-event.md'
description: The Update event action updates an existing Google Calendar event you specify.
---

# Google Calendar - Update event action

The **Update event** action updates an existing Google Calendar event you specify. The action appends new attendees to the existing participants list. If a duplicate email address is included in the list, it overwrites the existing attendee's response and comments. To add attendees without affecting the existing list, use the [Add attendees to an event action](/en/connectors/google-calendar/action-add-guest). Updated events are assigned to the connected account's time zone.

> **ENSURE CALENDAR ACCESS**
> 
> Ensure the calendar you plan to modify is accessible from your connected account and that you have the necessary permissions to edit events.

## Input

| Input field | Description |
| --- | --- |
| Event ID | Enter the Google Calendar ID of the event you plan to update. You can obtain the event ID from the event's URL or the output of the [Search events](/en/connectors/google-calendar/action-search-events) action. |
| Calendar | Select the calendar in which you plan to update an event. |
| Start date time | Specify the starting date and time for the event. |
| End date time | Specify the ending date and time for the event. |
| Displayed time zone | Select the time zone for displaying event times. |
| Name | Enter a name for the event. |
| Event description | Enter a description for the event. |
| Location | Enter the location where you plan for the event to take place. |
| Attendee emails | Enter a comma-separated list of attendee emails to invite to the event. |
| Send notifications? | Select whether to send attendees a notification about the updates to the event. This field is deprecated and is overridden by the **Send updates** field. |
| Send updates | Select who to notify about the updates to the event. |
| Guests can modify? | Select whether to allow guests to modify the event. |
| Display guests list? | Select whether to display the list of guests on the event. |
| Status | Select the status of the event, such as `Confirmed` or `Canceled`. |
| Visibility | Select the visibility of the event, such as `Public`, `Private`, or `Default`. The calendar's `Default` visibility is used if this field is left empty. |
| Show me as | Select the availability to display during the event, such as `busy` or `available`. This field defaults to `Busy` if left empty. |
| All day | Select whether the event spans the entire day or a specific time frame. |

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
| Attachments | Contains information about the event's attachments, such as: **File URL:** The URL of the attached file., **Title:** The title of the attachment., **Mime type:** MIME type of the file., **Icon link:** A link to the icon representing the file type., **File ID:** A unique identifier for the file., **List size:** The number of attachments., **List index:** The position of this attachment in the list. |

---
