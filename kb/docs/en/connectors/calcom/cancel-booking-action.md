---
url: 'https://docs.workato.com/en/connectors/calcom/cancel-booking-action.md'
description: The Cancel booking action cancels an existing booking by its UID in Cal.com.
---

# Cal.com - Cancel booking action

The **Cancel booking** action cancels an existing booking by its UID in Cal.com. Optionally include a cancellation reason that's added to notification emails.

## Input

| Input field | Description |
| --- | --- |
| Metadata output fields | Enter comma-separated metadata keys, for example `orderId`, to expose as individual output datapills. |
| Booking UID | Required. Enter the unique identifier of the booking you plan to cancel. |
| Cancellation reason | Enter a reason for the cancellation. Included in notification emails to attendees. |
| Seat UID | Enter the UID of the seat, present for seated bookings. |
| Cancelled subsequent bookings | Select to cancel subsequent bookings. Only available for recurring non-seated bookings. |

## Output

| Output field | Description |
| --- | --- |
| Booking ID | The numeric ID of the booking. |
| Booking UID | The unique identifier for the booking. Use this in other actions. |
| Title | The title of the booking. |
| Description | The description of the booking. |
| Status | The booking status: `accepted`, `cancelled`, `rejected`, or `pending`. |
| Start time | The start time of the booking. |
| End time | The end time of the booking. |
| Duration (minutes) | The duration of the booking, in minutes. |
| Event type ID | The ID of the event type that was booked. |
| Event type | The event type's ID and slug. |
| Location | The location of the booking. |
| Meeting URL | The video conferencing or meeting link for the booking. |
| Hosts | The hosts assigned to the booking, including each host's ID, name, email, username, and time zone. |
| Attendees | The attendees on the booking, including each attendee's name, email, time zone, phone number, and responses to the event type's booking fields. |
| Guests | Additional guest email addresses. |
| Cancellation reason | The reason for the cancellation. |
| Cancelled by email | The email address of the person who cancelled the booking. |
| Rescheduling reason | The reason for the reschedule, if the booking was previously rescheduled. |
| Rescheduled by email | The email address of the person who rescheduled the booking. |
| Rescheduled from UID | The UID of the booking this one was rescheduled from. |
| Rescheduled to UID | The UID of the booking this one was rescheduled to. |
| Booking fields responses | Responses to the event type's booking fields, for example name, email, guests, location, and notes. |
| Metadata | Custom metadata attached to the booking. Declare keys in the **Metadata output fields** input to expose them as individual output datapills. |
| Created at | The date and time the booking was created. |
| Updated at | The date and time the booking was last updated. |
| Recurring booking UID | The UID shared by all bookings in the same recurring series. |
| ICS UID | The calendar (ICS) unique identifier for the booking. |
| Rating | The rating given to the booking, if any. |
| Absent host | Whether the host was marked absent for this booking. |
| Seat UID | The UID of the seat, present for seated bookings. |
| Is platform managed user booking | Whether the booking belongs to a Cal.com platform-managed user. |

---
