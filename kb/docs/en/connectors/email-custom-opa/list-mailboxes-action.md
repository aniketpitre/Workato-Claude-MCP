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
