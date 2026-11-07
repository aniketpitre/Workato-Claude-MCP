---
url: 'https://docs.workato.com/en/connectors/gotowebinar/new-webinar-session.md'
description: >-
  The New webinar session trigger in the GoTo Webinar connector picks up new
  webinar session events from a specified time range on a polling interval.
---

# GoTo Webinar - New webinar session trigger

The **New webinar session** trigger picks up events from a specified time range.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Select the date and time from which Workato picks up new webinar sessions. Leave this field blank to retrieve sessions created one hour ago. You can't change this value after running or testing the recipe. |
| Trigger poll interval | Specify how frequently the recipe checks for new events. The default is five minutes if left blank. The minimum value allowed is five minutes. |

## Output

| Output field | Description |
| --- | --- |
| Session key | The unique key of the webinar session. |
| Webinar ID | The 9-digit webinar ID. |
| Webinar key | The webinar's unique ID. |
| Registrants attended | The number of registered attendees in the session. |
| Start time | The starting time of the webinar, such as `2020-03-13T10:00:00Z`. |
| End time | The ending time of the webinar, such as `2020-03-13T22:00:00Z`. |

---
