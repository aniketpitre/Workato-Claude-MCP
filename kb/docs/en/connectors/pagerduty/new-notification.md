---
url: 'https://docs.workato.com/en/connectors/pagerduty/new-notification.md'
description: >-
  The New notification trigger in the PagerDuty connector picks up new
  notifications on each poll interval, processing each one as a separate job.
---

# PagerDuty - New notification trigger

This trigger checks for new notifications in PagerDuty. Checks for new notifications on every poll interval. Each notification is processed as a separate job.

## Input

| Field | Description |
| --- | --- |
| Trigger poll interval | Select from the picklist or input your own value. Choose from how frequently to check for new events. |
| When first started, this recipe should pick up events from | Get notifications created since the given date/time. Leave empty to get incidents created since the recipe starts. Once recipe has been run or tested, this value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Field | Description |
| --- | --- |
| ID | The notification ID. |
| Type | The type of notification. |
| User | The user who created this notification. It contains the following fields. Name, Email, Time zone, Color, Avatar URL, Billed, Role, Description, Invitation sent, Contact methods, Notification rules, Job title, Teams, Coordinated incidents, ID, Type, Summary, Self, HTML URL |
| Started at | The time at which the notification was sent. |
| Address | The address where the notification was sent. This will be null for notification type push\_notification. |

---
