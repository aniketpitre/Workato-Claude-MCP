---
url: 'https://docs.workato.com/en/connectors/azure-ad/new-deleted-user-trigger.md'
description: >-
  The New deleted user trigger in the Microsoft Entra ID connector fires when a
  user is deleted from your directory.
---

# Microsoft Entra ID - New deleted user trigger

The **New deleted user** trigger detects when a Microsoft Entra ID user is deleted.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Choose how frequently to check for new events. |
| When first started, this recipe should pick up events from | Choose a start date and time to retrieve trigger events. Leave blank to start with events from one hour ago. |
| Output fields | Choose fields to include in the response. Leave blank to return default fields. |
| Additional fields | Add fields with JSON or enter them manually. |
| Set trigger condition | Define conditions to filter trigger events before processing. |

## Output

| Output field | Description |
| --- | --- |
| User ID | A unique identifier assigned to each user in Microsoft Entra ID. |
| Business phones | The primary business contact number(s) associated with the user. |
| Display name | The full name displayed for the user in the directory. |
| Given name | The user’s first name, typically used to address them informally or in combination with their surname. |
| Job title | The user’s role or position in the organization. |
| Mail | The user’s primary email address.registered in Microsoft Entra ID. |
| Mobile phone | The user’s mobile phone number. |
| Office location | The user’s primary office location. |
| Preferred language | The user’s preferred language for communication. |
| Surname | The user’s last name. |
| User principal name | The user’s login name in Microsoft Entra ID. |
| Reason | The reason for deleting the user. |

---
