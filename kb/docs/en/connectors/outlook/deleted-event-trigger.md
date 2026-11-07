---
url: 'https://docs.workato.com/en/connectors/outlook/deleted-event-trigger.md'
description: >-
  The Deleted event trigger in the Outlook connector monitors your calendar or a
  shared calendar and fires instantly when an event is deleted.
---

# Outlook - Deleted event trigger (real-time)

This trigger monitors your Outlook calendar or a shared calendar for deleted events. It is a real-time trigger, meaning that deleted events in the selected calendar create a trigger event instantly.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Select the calendar you plan to monitor from the list. |

## Output

The output datatree contains information about the deleted event. This includes the event ID and other event details.

| Field | Description |
| --- | --- |
| Subscription ID | The subscription ID for the deleted event. |
| Subscription expiration date time | The expiration date and time of the subscription. |
| Change type | The type of change (deleted). |
| Resource | The resource of the deleted event. |
| Resource data | The data of the deleted event. |
| ID | The ID of the deleted event. |
| Client state | The client state of the deleted event. |
| Tenant ID | The tenant ID of the deleted event. |

---
