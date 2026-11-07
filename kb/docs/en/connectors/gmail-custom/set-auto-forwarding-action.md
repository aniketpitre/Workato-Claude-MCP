---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/set-auto-forwarding-action.md
description: >-
  The Set auto-forwarding action updates the auto-forwarding setting for a Gmail
  mailbox.
---

# Gmail (Custom) - Set auto-forwarding action

The **Set auto-forwarding** action updates the auto-forwarding setting for a Gmail mailbox. A verified forwarding address must be specified when auto-forwarding is enabled. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Enabled | Select `Yes` to automatically forward all incoming mail to another address. |
| Email address | Enter the email address that all incoming messages are forwarded to. This address must be a verified forwarding address. |
| Disposition | Select the state a message is left in after it's forwarded. |

## Output

| Output field | Description |
| --- | --- |
| Enabled | Whether all incoming mail is automatically forwarded to another address. |
| Email address | The email address that all incoming messages are forwarded to. |
| Disposition | The state a message is left in after it's forwarded. |
| User id | The user's email address. |
