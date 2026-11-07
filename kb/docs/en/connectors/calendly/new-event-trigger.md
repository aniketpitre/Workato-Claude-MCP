---
url: 'https://docs.workato.com/en/connectors/calendly/new-event-trigger.md'
description: >-
  The New event trigger activates when trigger events, such as invitee created,
  occur in Calendly.
---

# Calendly - New event trigger

The **New event** trigger activates when trigger events, such as invitee created, occur in Calendly.

## Input

| Input field | Description |
| --- | --- |
| Scope | Select the scope from the drop-down menu. |
| Event | Select the events from the drop-down menu. |

## Output

| Output field | Description |
| --- | --- |
| Event | The event that caused the webhook to fire. |
| Created at | The timestamp when the webhook event was created. |
| Created by | The API URL of the user who created the Calendly event. |
| First name | The first name of the invitee. |
| Last name | The last name of the invitee. |
| Cancel URL | The link the invitee can use to cancel the scheduled event. |
| Created at | The timestamp when the event registration was processed. |
| Email | The email address of the invitee. |
| Event | A reference to the event. |
| Name | The full name of the invitee. |
| New invitee | A link to new invitee, after reschedule. |
| Old invitee | A reference to old Invitee instance that got rescheduled. |
| Questions and answers | A collection of the invitee's responses to questions on the event booking confirmation form. |
| Reschedule URL | A link to rescheduling the event for the invitee |
| Rescheduled | Indicates if the invitee has rescheduled. |
| Status | Indicates if the invitee is active or canceled. |
| Text reminder number | Phone number for SMS reminders. |
| Timezone | Time zone to use when displaying time to the invitee. |
| Tracking | The UTM and Salesforce tracking parameters associated with an Invitee. |
| Updated at | The moment when the event was last updated. |
| URI | Canonical reference (unique identifier) for the invitee. |
| Routing form submission | Reference to a routing form submission that redirected the invitee to a booking page. |
| Cancellation | The object provides data pertaining to the cancellation of the Event or the Invitee. |
| Payment | The object containing information about invitee payment. |
| No show | Provides data pertaining to the associated no show for the Invitee. |
| Reconfirmation | When reconfirmation is requested, this object is present with a `created_at` that reflects when the reconfirmation notification was sent. When the invitee reconfirms, the `confirmed_at` attribute changes from null to a timestamp that reflects when they took action. |

---
