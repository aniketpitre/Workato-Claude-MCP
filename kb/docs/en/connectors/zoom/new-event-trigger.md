---
url: 'https://docs.workato.com/en/connectors/zoom/new-event-trigger.md'
description: >-
  The New event trigger in the Zoom connector monitors Zoom for new meeting,
  webinar, cloud recording, and user events in real time.
---

# Zoom - New event trigger

The **New event** trigger monitors Zoom for new events in real-time. Workato creates a job for each new event.

## Input

| Input field | Description |
| --- | --- |
| Event category | Select the event category. Categories enable you to filter events by type, such as webinar or meeting events. |
| Event | Select the [event](#event-types) that activates the trigger. |

> **ORGANIZATION-LEVEL EVENT MONITORING**
> 
> Events are triggered at the organization level. For example, if this trigger monitors ended meetings, a new job is created for every meeting ended by any user in the connected Zoom organization. You can use a meeting’s or webinar’s tracking fields to [filter relevant events](/en/connectors/zoom/best-practices#filtering-trigger-events-on-zoom).

## Output

The output varies based on the event selected in the trigger configuration.

## Event types

This trigger allows you to monitor the following Zoom events:

| Category | Event | Description |
| --- | --- | --- |
| Meeting | Meeting alerts | Triggers when a meeting has alerts, such as bad connection or unstable video. |
| Meeting | Meeting started | Triggers when a meeting begins. |
| Meeting | Meeting ended | Triggers when a meeting concludes. |
| Meeting | Meeting created | Triggers when a new meeting is created. |
| Meeting | Meeting updated | Triggers when a meeting's details, such as time or participants, are modified. |
| Meeting | Meeting deleted | Triggers when a meeting is deleted. |
| Meeting | Meeting registration created | Triggers when a participant registers for a meeting that requires registration. |
| Meeting | Meeting registration approved | Triggers when a meeting registration request is approved. |
| Meeting | Meeting registration cancelled | Triggers when a participant cancels their registration for a meeting. |
| Meeting | Meeting sharing started | Triggers when a participant starts sharing their screen during a meeting. |
| Meeting | Meeting sharing ended | Triggers when a participant stops sharing their screen during a meeting. |
| Meeting | Host/Participant joined | Triggers when the host or a participant enters a meeting. |
| Meeting | Host/Participant left | Triggers when the host or a participant exits a meeting. |
| Meeting | Participant waiting for Host | Triggers when a participant is in the waiting room waiting for the host to start the meeting. |
| Meeting | Participant joined before host | Triggers when a participant joins a meeting before the host arrives. |
| Webinar | Webinar alerts | Triggers when a webinar has alerts, such as bad connection or unstable video. |
| Webinar | Webinar started | Triggers when a webinar begins. |
| Webinar | Webinar ended | Triggers when a webinar concludes. |
| Webinar | Webinar created | Triggers when a new webinar is created. |
| Webinar | Webinar updated | Triggers when a webinar’s details, such as time or participants, are modified. |
| Webinar | Webinar sharing started | Triggers when a participant starts sharing their screen during a webinar. |
| Webinar | Webinar sharing ended | Triggers when a participant stops sharing their screen during a webinar. |
| Webinar | Webinar registration created | Triggers when a participant registers for a webinar that requires registration. |
| Webinar | Webinar registration approved | Triggers when a webinar registration request is approved. |
| Webinar | Webinar registration cancelled | Triggers when a participant cancels their webinar registration. |
| Webinar | Webinar registration denied | Triggers when a webinar registration request is denied. |
| Webinar | Host/Participant joined | Triggers when the host or a participant enters a webinar. |
| Webinar | Host/Participant left | Triggers when the host or a participant exits a webinar. |
| Cloud recording | Cloud recording started | Triggers when a cloud recording starts during a meeting or webinar. |
| Cloud recording | Cloud recording paused | Triggers when a cloud recording is temporarily paused. |
| Cloud recording | Cloud recording resumed | Triggers when a paused cloud recording is resumed. |
| Cloud recording | Cloud recording stopped | Triggers when a cloud recording is manually stopped. |
| Cloud recording | Cloud recording completed | Triggers when a cloud recording finishes processing and becomes available. |
| Cloud recording | Cloud recording renamed | Triggers when the name of a cloud recording is changed. |
| Cloud recording | Cloud recording trashed | Triggers when a cloud recording is moved to the trash. |
| Cloud recording | Cloud recording deleted | Triggers when a cloud recording is permanently deleted. |
| Cloud recording | Cloud recording recovered | Triggers when a cloud recording is restored from the trash. |
| Cloud recording | Cloud recording transcript completed | Triggers when the transcript for a cloud recording becomes available. |
| Cloud recording | Cloud recording registration created | Triggers when a participant registers for a cloud recording that requires registration. |
| Cloud recording | Cloud recording registration approved | Triggers when a cloud recording registration request is approved. |
| Cloud recording | Cloud recording registration denied | Triggers when a cloud recording registration request is denied. |
| User | User created | Triggers when a new Zoom user account is created. |
| User | User updated | Triggers when a user’s profile details are updated. |
| User | User invitation accepted | Triggers when a user accepts an invitation to join a Zoom account. |
| User | User settings updated | Triggers when a user updates their profile settings, such as email, display name, or preferences. |
| User | User deactivated | Triggers when a user account is deactivated. |
| User | User activated | Triggers when a user account is activated. |
| User | User disassociated | Triggers when a user is removed from a Zoom account. |
| User | User deleted | Triggers when a Zoom user account is permanently deleted. |
| User | User presence status updated | Triggers when a user’s availability status is updated. |
| User | User personal notes updated | Triggers when a user updates their personal note at the top of their Zoom chat profile. |
| User | User signed in | Triggers when a user signs in to their Zoom account. |
| User | User signed out | Triggers when a user signs out of their Zoom account. |

---
