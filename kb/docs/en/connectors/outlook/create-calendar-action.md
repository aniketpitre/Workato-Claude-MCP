---
url: 'https://docs.workato.com/en/connectors/outlook/create-calendar-action.md'
description: >-
  The Create calendar action in the Outlook connector lets you create a new
  calendar with a name and color.
---

# Outlook - Create calendar action

This action creates a calendar in Outlook.

## Input

| Field | Description |
| --- | --- |
| Shared calendar | Provide the email address of the user who owns the shared calendar, so Workato can fetch the shared calendars. For example, `support@example.onmicrosoft.com`. If left blank, Workato shows your default calendars. |
| Calendar | Provide a name for the calendar. |
| Color | Provide the color of the calendar. This can be used to distinguish between other calendars in the UI. |

## Output

| Field | Description |
| --- | --- |
| ID | The unique ID of the calendar. |
| Name | The name of the calendar. |
| Color | The color of the calendar. |
| Hex color | The hex color of the calendar. |
| Is default calendar | Indicates whether the calendar is the default calendar. |
| Change key | The change key of the calendar. |
| Can share | Indicates whether the calendar can be shared. |
| Can edit | Indicates whether the calendar can be edited. |
| Allowed online meeting providers | A list of the allowed online meeting providers. |
| Default online meeting provider | The default online meeting provider. Possible values include `unknown`, `skypeForBusiness`, `skypeForConsumer`, and `teamsForBusiness`. |
| Can view private items | Indicates whether the user can read calendar items that have been marked private. |
| Is tallying responses | Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses. |
| Is removable | Indicates whether this user calendar can be deleted from the user mailbox. |
| Owner | If set, this represents the user who created or added the calendar. For a calendar that the user created or added, the owner property is set to the user. For a calendar shared with the user, the owner property is set to the person who shared that calendar with the user. |

---
