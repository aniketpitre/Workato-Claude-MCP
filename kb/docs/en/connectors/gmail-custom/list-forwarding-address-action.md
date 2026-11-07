---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/list-forwarding-address-action.md
description: >-
  The List forwarding address action lists the forwarding addresses configured
  for a Gmail mailbox.
---

# Gmail (Custom) - List forwarding address action

The **List forwarding address** action lists the forwarding addresses configured for a Gmail mailbox. This action requires one of the following OAuth scopes: `https://www.googleapis.com/auth/gmail.settings.basic`, `https://mail.google.com/`, `https://www.googleapis.com/auth/gmail.modify`, or `https://www.googleapis.com/auth/gmail.readonly`.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |

## Output

| Output field | Description |
| --- | --- |
| Forwarding addresses | Array of forwarding addresses configured for the mailbox. Each entry includes a forwarding email and a verification status. |
| User id | The user's email address. |
