---
url: 'https://docs.workato.com/en/connectors/bluesky/new-notification-trigger.md'
description: >-
  The New notification trigger monitors Bluesky for new notifications, such as
  likes, mentions, and replies.
---

# Bluesky - New notification trigger

The **New notification** trigger monitors Bluesky for new notifications.

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events | Select from when notifications the recipe picks up when it first runs, such as `From now`, `From a date`, or `All existing notifications`. |
| Reasons | Select filters for specific notification reasons, such as `like`, `mention`, or `reply`. Leave blank for all notification types. |
| Priority | Select whether to return only priority notifications. |

## Output

| Output field | Description |
| --- | --- |
| AT-URI | Unique identifier of the notification. |
| CID | Content identifier of the notification. |
| Author | Profile of the account that triggered the notification. |
| Reason | Type of notification. For example, `like`, `mention`, or `reply`. |
| Reason subject | AT-URI of the record the notification relates to, if applicable. |
| Is read | Whether you've already read the notification. |
| Indexed at | Date and time when Bluesky indexed the notification. |
| Record | Underlying record that triggered the notification, such as a post, like, or follow. |
| Labels | List of labels applied to the notification, if applicable. |

---
