---
url: 'https://docs.workato.com/en/connectors/email-custom/retrieve-emails-action.md'
description: >-
  The Retrieve emails action enables you to retrieve emails using the IMAP/POP3
  protocol in Email (Custom).
---

# Email (Custom) - Retrieve emails action

The **Retrieve emails** action retrieves emails using **IMAP** or **POP3**. With **IMAP**, it can filter emails by search criteria. With **POP3**, it retrieves all emails in the mailbox.

## Input

| Input field | Description |
| --- | --- |
| Mailbox | Select or enter the mailbox to retrieve emails from. Available only with **IMAP**. |
| Search criteria | Select or enter a criterion to filter the emails. Available only with **IMAP**. |
| Search criteria value | Specify the search value for the selected criterion. Available only with **IMAP**. |

## Output

| Output field | Description |
| --- | --- |
| Emails | A list of email objects. |
| UID | The unique identifier for the email. |
| From | The sender of the email. |
| Date | The date and time the email was received in the mailbox. |
| Subject | The subject of the email. |
| Body | The message content of the email. |
| Attachments | A list of attachments for the email, if applicable. |

---
