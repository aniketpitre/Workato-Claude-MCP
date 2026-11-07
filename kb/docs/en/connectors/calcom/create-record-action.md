---
url: 'https://docs.workato.com/en/connectors/calcom/create-record-action.md'
description: The Create record action creates a new booking in Cal.com.
---

# Cal.com - Create record action

The **Create record** action creates a new booking in Cal.com. The start time must match an available slot from the [Get record](/en/connectors/calcom/get-record-action) action.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record you plan to create. Only **Booking** is supported. |
| Metadata output fields | Enter comma-separated metadata keys, for example `orderId`, to expose as individual output datapills. |
| Start time | Required. The booking start time. |
| Attendee name | Required. The full name of the person booking the meeting. |
| Attendee email | Required. The email address of the person booking the meeting. |
| Attendee time zone | Required. The IANA time zone of the attendee, for example `America/New_York`. |
| Event type | The event type to book. Use this or the event type slug and username combination below. |
| Event type slug | The slug of the event type, for example `30min`. Must be used together with **Username**. |
| Username | The Cal.com username of the host. Must be used together with **Event type slug**. |
| Attendee phone number | Required if you enable SMS reminders. The phone number of the person attending the meeting. |
| Attendee language | The language code for the person attending the meeting. |
| Guests | Email addresses of additional guests. |
| Location type | The meeting location type. Leave blank to use the event type's default location. |
| Location integration | The meeting location integration name. This input field is used with **Location type**. |
| Booking field responses | Responses to the event type's custom booking fields. |
| Metadata | Enter up to 50 metadata key-value pairs. |
| Duration | Enter the duration of the booking in minutes. This field overrides the event type's default duration. |
| Team slug | The slug of the team that owns the event type. Use with **Event type slug** instead of **Username** for team bookings. |
| Organization slug | The slug of the organization. Only needed when booking with **Event type slug** and **Username**, or **Event type slug** and **Team slug**, within an organization. |
| Email verification code | Required when the event type has email verification enabled. |
| Allow conflicts | Host only. Enable to bypass availability conflict checks. |
| Allow booking out of bounds | Host only. Enable to bypass scheduling-window checks. |
| Skip booking limits | Host only. Enable to bypass booking quota checks, including per-day, per-week, per-month, per-year, and duration quotas. |

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
| Rescheduling reason | The reason for the reschedule, if the booking was rescheduled. |
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
