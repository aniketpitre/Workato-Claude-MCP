---
url: 'https://docs.workato.com/en/connectors/email-custom/new-email-trigger.md'
description: The New email trigger polls for new emails using IMAP or POP3.
---

# Email (Custom) - New email trigger

The **New email** trigger polls for new emails using **IMAP** or **POP3**. With **IMAP**, it polls for unseen emails in the specified mailbox based on search criteria. With **POP3**, it polls for all emails in the mailbox.

## Input

| Input field | Description |
| --- | --- |
| Mailbox | Select or enter the mailbox to retrieve emails from. Available only with **IMAP**. |
| Search criteria | Select or enter a criterion to filter the emails. Available only with **IMAP**. |
| Search criteria value | Specify the search value for the selected criterion. Available only with **IMAP**. |
| Trigger poll interval | Specify how frequently the trigger checks for new events. |

## Output

| Output field | Description |
| --- | --- |
| UID | The unique identifier for the email. |
| From | The sender of the email. |
| Date | The date and time the email was received in the mailbox. |
| Subject | The subject of the email. |
| Body | The message content of the email. |
| Attachments | A list of attachments for the email, if applicable. |

---
