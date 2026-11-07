---
url: 'https://docs.workato.com/en/connectors/email-custom-opa/new-email-trigger.md'
description: >-
  Poll for new emails using IMAP or POP3 through the Email (Custom) OPA on-prem
  agent extension.
---

# Email (Custom) OPA - New email trigger

The **New email** trigger polls for new emails using **IMAP** or **POP3** through your on-prem agent extension. Use the **IMAP** option to poll for new unseen emails in the specified mailbox based on search criteria. Use the **POP3** option to poll for all emails in the mailbox.

## Input

| Input field | Description |
| --- | --- |
| Mailbox | Select or enter the mailbox to retrieve emails from, for example `INBOX`. The **Mailbox** field is only available with **IMAP**. |
| Search criteria | Optional. Select or enter a criterion to filter the emails. The **Search criteria** field is only available with **IMAP**. Defaults to **ALL** if left blank. |
| Search criteria value | Optional. Enter the search value for the selected criterion, for example `Testing`, `01-Jan-2023`, or `cc@example.com`. The **Search criteria value** field isn't available for criteria that don't take a value, such as **ALL** or **SEEN**. |
| Trigger poll interval | Optional. Enter how frequently the trigger checks for new events. |

## Output

| Output field | Description |
| --- | --- |
| UID | The email's unique identifier. |
| From | The sender of the email. |
| Date | The date and time the email was received in the mailbox. |
| Subject | The subject of the email. |
| Body | The plain text message content of the email. |
| HTML body | The HTML message content of the email, if available. |
| Attachments | A list of attachments for the email, if applicable. Each item includes a file name and its base64-encoded content. |
| Digest | A content hash for the email, combined with **UID** to detect duplicate trigger events. |

---
