---
url: 'https://docs.workato.com/en/connectors/gmail-custom/update-imap-action.md'
description: The Update IMAP action updates the IMAP settings for a Gmail mailbox.
---

# Gmail (Custom) - Update IMAP action

The **Update IMAP** action updates the IMAP settings for a Gmail mailbox. This action requires the `https://www.googleapis.com/auth/gmail.settings.basic` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Enabled | Select to enable IMAP for the account. |
| Auto expunge | Set to `Yes` for Gmail to immediately expunge a message when it's marked as deleted in IMAP. Gmail waits for an update from the client before expunging deleted messages if set to `No`. |
| Expunge behavior | Select the action to take on a message when it's marked as deleted and expunged from the last visible IMAP folder. |
| Max folder size | Enter an optional limit on the number of messages an IMAP folder can contain. Valid values are `0`, `1000`, `2000`, `5000`, or `10000`. A value of `0` means there's no limit. |

## Output

| Output field | Description |
| --- | --- |
| Enabled | Whether IMAP is enabled for the account. |
| Auto expunge | Whether Gmail immediately expunges deleted messages. |
| Expunge behavior | The action taken on a message when it's marked as deleted and expunged. |
| Max folder size | The maximum number of messages an IMAP folder can contain. |
| User id | The user's email address. |

---

---
url: >-
  https://docs.workato.com/en/connectors/gmail-custom/update-vacation-settings-action.md
description: >-
  The Update vacation settings action updates the vacation responder settings
  for a Gmail mailbox.
---

# Gmail (Custom) - Update vacation settings action

The **Update vacation settings** action updates the vacation responder settings for a Gmail mailbox. This action requires the `https://www.googleapis.com/auth/gmail.settings.basic` OAuth scope.

## Input

| Input field | Description |
| --- | --- |
| User id | Enter the user's email address. |
| Enable auto-reply | Select to enable Gmail automatic replies to messages. |
| Response subject | Enter text to prepend to the subject line in vacation responses. The response subject or the response body must not be empty. |
| Response body type | Select the format of the response body: `Plain text` or `HTML`. |
| Response body plain text | Enter the response body in plain text format. Shown when **Response body type** is set to plain text. If both the plain text and HTML response bodies are specified, the HTML version is used. |
| Response body HTML | Enter the response body in HTML format. Shown when **Response body type** is set to HTML. Gmail sanitizes the HTML before storing it. |
| Restrict to contacts | Select to send auto-replies only to recipients in the mailbox owner's contacts. |
| Restrict to domain | Select to send auto-replies only to recipients inside the mailbox owner's domain. Available only for Google Workspace accounts. |
| Start time | Enter the start time for sending auto-replies. If specified, Gmail only replies to messages received after this time. If both start time and end time are specified, start time must precede end time. |
| End time | Enter the end time for sending auto-replies. If specified, Gmail only replies to messages received before this time. If both start time and end time are specified, start time must precede end time. |

## Output

| Output field | Description |
| --- | --- |
| Enable auto-reply | Whether Gmail automatically replies to messages. |
| Response subject | The text prepended to the subject line in vacation responses. |
| Response body plain text | Response body in plain text format. |
| Response body HTML | Response body in HTML format. |
| Restrict to contacts | Whether responses are sent only to recipients in the mailbox owner's contacts. |
| Restrict to domain | Whether responses are sent only to recipients inside the mailbox owner's domain. |
| Start time | The start time for sending auto-replies. |
| End time | The end time for sending auto-replies. |
| User id | The user's email address. |

---
