---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/list-email-delegates-action.md
description: The List email delegates action lists the delegates for a Gmail mailbox.
---

# Gmail (Custom) - List email delegates action

The **List email delegates** action lists the delegates for a Gmail mailbox. This action requires one of the following OAuth scopes: `https://www.googleapis.com/auth/gmail.settings.basic`, `https://mail.google.com/`, `https://www.googleapis.com/auth/gmail.modify`, or `https://www.googleapis.com/auth/gmail.readonly`.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |

## Output

| Output field | Description |
| --- | --- |
| Delegates | Array of delegates for the mailbox. Each entry includes a delegate email and a verification status. |
| User id | The user's email address. |
