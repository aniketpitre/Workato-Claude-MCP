---
url: 'https://docs.workato.com/en/connectors/calcom/reschedule-booking-action.md'
description: >-
  The Reschedule booking action moves an existing booking to a new time slot in
  Cal.com.
---

# Cal.com - Reschedule booking action

The **Reschedule booking** action moves an existing booking to a new time slot in Cal.com. The new start time must match an available slot from the [Get record](/en/connectors/calcom/get-record-action) action.

## Input

| Input field | Description |
| --- | --- |
| Metadata output fields | Enter comma-separated metadata keys, for example `orderId`, to expose as individual output datapills. |
| Booking UID | Required. Enter the unique identifier of the booking you plan to reschedule. |
| New start time | Required. Enter the new start time, in ISO 8601 format. Must match an available slot from the Get record action. |
| Rescheduled by | Enter the email of the person rescheduling. Using the event type owner's email auto-confirms the reschedule. |
| Rescheduling reason | Enter the reason for the reschedule. Included in notification emails. |
| Seat UID | Enter the UID of the specific seat to reschedule for seated bookings. |
| Email verification code | Enter an email verification code. Required when the event type has email verification enabled. |
| Allow conflicts | Select `Yes` or `No` to bypass availability conflict checks. Host only. |
| Allow booking out of bounds | Select `Yes` or `No` to bypass scheduling-window checks. Host only. |
| Skip booking quotas | Enable to bypass booking quota checks, including per-day, per-week, per-month, per-year, and duration quotas. Host only. |

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
| Cancellation reason | The reason for the cancellation, if the booking was cancelled. |
| Cancelled by email | The email address of the person who cancelled the booking. |
| Rescheduling reason | The reason for the reschedule. |
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
