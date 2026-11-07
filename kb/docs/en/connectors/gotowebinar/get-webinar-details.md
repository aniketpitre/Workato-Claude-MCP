---
url: 'https://docs.workato.com/en/connectors/gotowebinar/get-webinar-details.md'
description: >-
  The Get webinar details action in the GoTo Webinar connector lets you retrieve
  webinar details such as times, registrants, and subject by webinar key.
---

# GoTo Webinar - Get webinar details action

The **Get webinar details** action retrieves webinar details from GoTo Webinar.

## Input

| Input field | Description |
| --- | --- |
| Webinar key | Enter the webinar's unique ID that is found at the end of the URL. Alternatively, you can map in the **Webinar key** from the output of the GoToWebinar **New webinar session** trigger. |

## Output

| Output field | Description |
| --- | --- |
| Number of registrants | The number of registrants at the webinar. |
| Times | A list with the webinar session's start and end times. |
| Start time | The starting time of the webinar, such as `2020-03-13T10:00:00Z`. |
| End time | The ending time of the webinar, such as `2020-03-13T22:00:00Z`. |
| Description | A short description of the webinar. |
| Subject | The webinar subject. |
| In session | Indicates whether there is a webinar session currently in progress. |
| Organizer key | The key of the webinar organizer. |
| Webinar ID | The 9-digit webinar ID. |
| Webinar key | Enter the webinar's unique ID located at the end of the webinar URL. |
| Time zone | The timezone where the webinar is taking place. |
| Number of opened invitations | The number of times the webinar invitation was opened. |
| Registration URL | The URL the webinar invitees can use to register. |
| Number of registration link clicks | The number of times the registration link was clicked. |

---

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

---
