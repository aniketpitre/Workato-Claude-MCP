---
url: >-
  https://docs.workato.com/en/connectors/eventbrite/updated-attendee-real-trigger.md
description: >-
  The New/updated event attendee registered for event (real-time) trigger in the
  Eventbrite connector fires via webhook as attendees are added or changed.
---

# Eventbrite - New/updated event attendee registered for event (real-time) trigger

The **New/updated event attendee registered for event (real-time)** trigger fetches attendees as soon as they are added or changed in Eventbrite. This real-time trigger creates a webhook that you can find in your Eventbrite account under the Webhooks Dashboard.

![New/updated event attendee registered (real-time) trigger](/assets/updated-attendee-real-trigger.Bwf8Gbbn.png)_Eventbrite - New/updated event attendee registered for event (real-time) trigger_

## Input

| Input field | Description |
| --- | --- |
| Organization | Select the organization within Eventbrite. If left blank, the organization specified in the connection is used. |
| Event | Choose the specific event to monitor for attendee updates. Leave blank to fetch attendees for all events owned by the connected Eventbrite user. |

## Output

| Output field | Description |
| --- | --- |
| Event | The event associated with the attendee. |
| Costs | The cost information for the attendee's ticket. |
| Resource URL | The URL to the attendee's resource on Eventbrite. |
| Variant ID | The variant ID of the ticket. |
| Cancelled | Indicates if the registration has been cancelled. |
| Refunded | Indicates if the ticket has been refunded. |
| Affiliate | The affiliate code if the ticket was sold through an affiliate. |
| Guestlist ID | The ID of the guestlist that includes the attendee. |
| Invited by | Information on who invited the attendee, if applicable. |
| Ticket class name | The name of the ticket class purchased by the attendee. |
| Event ID | The unique identifier of the event. |
| Order ID | The unique identifier of the order. |
| Order | Detailed information about the order. |
| Date changed | The date and time when the attendee's registration was last updated. |
| Date created | The date and time when the attendee registered. |
| ID | The unique identifier for the attendee. |
| Checked In | Indicates whether the attendee has checked in. |
| Status | The current status of the attendee's registration. |
| Ticket ID | The unique identifier for the attendee's ticket. |
| Ticket type | The type of ticket purchased by the attendee. |
| Email | The email address of the attendee. |
| Quantity | The quantity of tickets registered by the attendee. |
| Profile | The profile information of the attendee. |
| Barcodes | The barcodes associated with the attendee's tickets. |
