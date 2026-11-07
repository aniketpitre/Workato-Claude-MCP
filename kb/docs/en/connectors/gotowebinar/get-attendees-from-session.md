---
url: >-
  https://docs.workato.com/en/connectors/gotowebinar/get-attendees-from-session.md
description: >-
  The Get attendees from session action in the GoTo Webinar connector lets you
  retrieve attendees from a webinar session using a webinar and session key.
---

# GoTo Webinar - Get attendees from session action (batch)

The **Get attendees from session** action retrieves attendees from a session using a session ID.

## Input

| Input field | Description |
| --- | --- |
| Webinar key | Enter the webinar's unique ID located at the end of the webinar URL. Alternatively, you can map in the **Webinar key** from the output of the GotoWebinar **New webinar session** trigger. |
| Session key | Enter the key of the webinar session. You can map in the session key from the output of the GotoWebinar **New webinar session** trigger. |

## Output

| Output field | Description |
| --- | --- |
| Attendees | A list of session attendees. |
| First name | The attendee's first name. |
| Last name | The attendee's last name. |
| Email | The attendee's email address. |
| Registrant key | The key of the webinar attendee. |
| Session key | The unique key of the webinar session. |
| Attendance time in seconds | The total attendance time in seconds. |
| Attendance | The list of times the attendee joined and left the webinar session. |
| Join time | The time the attendee joined a webinar session. |
| Leave time | The time the attendee left a webinar session. |
