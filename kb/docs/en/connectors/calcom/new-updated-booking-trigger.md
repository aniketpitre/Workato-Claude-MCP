---
url: 'https://docs.workato.com/en/connectors/calcom/new-updated-booking-trigger.md'
description: >-
  The New/updated booking trigger fires when a booking is created, cancelled, or
  rescheduled in Cal.com.
---

# Cal.com - New/updated booking trigger

The **New/updated booking** trigger fires when a booking is created, cancelled, or rescheduled in Cal.com. This trigger registers a webhook when the recipe starts and removes it when the recipe stops.

## Input

| Input field | Description |
| --- | --- |
| Events | Select which booking events trigger this recipe. Options include `Booking created`, `Booking cancelled`, and `Booking rescheduled`. Leave blank to receive all of them. |
| Metadata output fields | Enter comma-separated metadata keys, for example `orderId`, to expose as individual output datapills. |

## Output

| Output field | Description |
| --- | --- |
| Trigger event | The webhook event that fired: `BOOKING_CREATED`, `BOOKING_CANCELLED`, or `BOOKING_RESCHEDULED`. |
| Booking UID | The unique identifier of the booking. |
| Booking ID | The numeric ID of the booking. |
| Status | The uppercase booking status from the webhook, for example `ACCEPTED`, `CANCELLED`, or `PENDING`. |
| Title | The title of the booking. |
| Event title | The title of the event type. |
| Description | The description of the booking. |
| Event type slug | The slug of the event type. |
| Event type ID | The ID of the event type that was booked. |
| Event type title | The title of the event type. |
| Start time | The start time of the booking. |
| End time | The end time of the booking. |
| Duration (minutes) | The duration of the booking, in minutes. |
| Location | The location of the booking. |
| Booker URL | The URL of the Cal.com instance the booking was made on. |
| Requires confirmation | Whether the booking requires confirmation before it's accepted. |
| Cancellation reason | The reason for the cancellation, if the booking was cancelled. |
| Rejection reason | The reason for the rejection, if the booking was rejected. |
| Organizer | The booking's organizer, including their ID, name, email, username, and time zone. |
| Attendees | The attendees on the booking, including each attendee's name, email, time zone, and metadata. |
| Responses | Answers to the booking form fields, such as name, email, and notes. |
| Video call data | The video call type, ID, password, and URL for the booking. |
| Metadata | Custom metadata attached to the booking. Includes the video call URL. Declare additional keys in the **Metadata output fields** input to expose them as individual output datapills. |

Cal.com's webhook payload includes many additional booking configuration fields. Refer to the [Cal.com](https://cal.com/docs/api-reference/v2/introduction) documentation for a complete list of output fields.

---
