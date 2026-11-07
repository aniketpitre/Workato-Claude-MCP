---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/create-email-delegation-access-action.md
description: >-
  The Create email delegation access action adds a delegate to a Gmail mailbox
  with its verification status set to accepted.
---

# Gmail (Custom) - Create email delegation access action

The **Create email delegation access** action adds a delegate to a Gmail mailbox and sets its verification status to **accepted** without sending a verification email. The delegate must be a member of the same Google Workspace organization as the mailbox owner. This action requires the `https://www.googleapis.com/auth/gmail.settings.sharing` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Delegate email | Enter the email address of the user to add as a delegate. |

## Output

| Output field | Description |
| --- | --- |
| Delegate email | The delegate's email address. |
| Verification status | The verification status of the delegate, such as `accepted` or `pending`. |
| User id | The user's email address. |
