---
url: 'https://docs.workato.com/en/connectors/email-custom-opa/delete-email-action.md'
description: >-
  Delete an email by UID using IMAP through the Email (Custom) OPA on-prem agent
  extension.
---

# Email (Custom) OPA - Delete email action

The **Delete email** action deletes an email by marking it for deletion and expunging the mailbox, using **IMAP** through your on-prem agent extension. This action requires IMAP configuration.

## Input

| Input field | Description |
| --- | --- |
| Email UID | Enter the UID of the email to delete. |

## Output

| Output field | Description |
| --- | --- |
| Result | A message confirming the email was deleted, for example `Email UID 1 deleted`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/email-custom-opa/list-mailboxes-action.md
description: >-
  List the mailboxes in an account using IMAP through the Email (Custom) OPA
  on-prem agent extension.
---

# Email (Custom) OPA - List mailboxes action

The **List mailboxes** action retrieves a list of mailboxes using **IMAP** through your on-prem agent extension. This action requires IMAP configuration.

## Input

This action doesn't require any input fields.

## Output

| Output field | Description |
| --- | --- |
| Mailboxes | A list of mailboxes in the account. |
| Name (Mailboxes) | The mailbox's name, for example `INBOX`. |
| Delimiter (Mailboxes) | The character that separates levels in the mailbox's hierarchy, for example `/`. |
| Attributes (Mailboxes) | A list of IMAP attributes for the mailbox, for example `Hasnochildren`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/email-custom-opa/mark-email-as-read-action.md
description: >-
  Mark an email as read using IMAP through the Email (Custom) OPA on-prem agent
  extension.
---

# Email (Custom) OPA - Mark email as read action

The **Mark email as read** action marks an email as read by setting the Seen flag, using **IMAP** through your on-prem agent extension. This action requires IMAP configuration.

## Input

| Input field | Description |
| --- | --- |
| Email UID | Enter the UID of the email to mark as read. |

## Output

| Output field | Description |
| --- | --- |
| Result | A message confirming the email was marked as read, for example `Email UID 1 marked as read`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/email-custom-opa/retrieve-emails-action.md
description: >-
  Retrieve emails using IMAP or POP3 through the Email (Custom) OPA on-prem
  agent extension.
---

# Email (Custom) OPA - Retrieve emails action

The **Retrieve emails** action retrieves emails using **IMAP** or **POP3** through your on-prem agent extension. With **IMAP**, it retrieves emails matching the search criteria from the specified mailbox. With **POP3**, it retrieves all emails in the mailbox. This action requires IMAP or POP3 configuration.

## Input

With **IMAP** configured, the following input fields are available. With **POP3** configured, this action doesn't require any input fields.

| Input field | Description |
| --- | --- |
| Mailbox | Select or enter the mailbox to retrieve emails from, for example `INBOX`. |
| Search criteria | Optional. Select or enter a criterion to filter the emails. Defaults to **ALL** if left blank. |
| Search criteria value | Optional. Enter the search value for the selected criterion, for example `Testing`, `01-Jan-2023`, or `cc@example.com`. The **Search criteria value** field isn't available for criteria that don't take a value, such as **ALL** or **SEEN**. |

## Output

| Output field | Description |
| --- | --- |
| Emails | A list of matching emails. |
| UID (Emails) | The email's unique identifier. |
| From (Emails) | The sender of the email. |
| Date (Emails) | The date and time the email was received in the mailbox. |
| Subject (Emails) | The subject of the email. |
| Body (Emails) | The plain text message content of the email. |
| HTML body (Emails) | The HTML message content of the email, if available. |
| Attachments (Emails) | A list of attachments for the email, if applicable. Each item includes a file name and its base64-encoded content. |

---
