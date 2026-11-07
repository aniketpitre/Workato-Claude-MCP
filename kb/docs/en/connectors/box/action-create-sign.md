---
url: 'https://docs.workato.com/en/connectors/box/action-create-sign.md'
description: >-
  The Create sign request action creates a sign request in Box on one or more
  files and sends email notifications to signers.
---

# Box - Create sign request action

The **Create sign request** action creates a sign request in Box on one or more files. You can notify signers by email, use predefined templates, and configure expiration, reminders, and security settings.

## Input

| Input field | Description |
| --- | --- |
| Name | Enter a name for the sign request. |
| Sign template | Select a predefined sign template or provide a template ID. This fetches signers, source files, and destination folder details. |
| Files | Select up to 10 files for the sign request. |
| Signers | Add up to 35 signers. Signers don't need a Box account. |
| Destination folder | Select the folder where Box stores the signed documents and signing log. |
| Enable reminders | Select **Yes** to send reminders on days 3, 8, 13, and 18. Defaults to **Yes**. |
| Enable text signature | Select **Yes** to allow text-based signatures. Defaults to **Yes**. |
| Validity days | Enter the number of days before the request expires. |
| Default declined redirect URL | Enter the URL where signers are redirected if they decline to sign. |
| Email message | Enter a message to include in the sign request email. Supports limited HTML tags. |
| Email subject | Enter the subject line for the sign request email. Defaults to a system subject if blank. |
| External ID | Provide an ID from an external system to associate with the sign request. |
| Is document preparation needed? | Select **Yes** to require the sender to prepare the document before sending. |
| Is phone verification needed? | Select **Yes** to require signers to verify by SMS before viewing the document. |
| Prefill tags | Add tags for prefilling document content. |
| Redirect URL | Enter the URL where signers are redirected after signing. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier for the sign request. |
| Type | The type of action performed. |
| Are reminders enabled | Status of reminder enablement. |
| Are text signatures enabled | Status of text signature enablement. |
| Auto expire at | Timestamp when the request will automatically expire. |
| Days valid | Number of days the request remains valid. |
| Declined redirect URL | URL where signers are redirected if they decline to sign a document. |
| Email message | Email message content sent with the sign request. |
| Email subject | Subject line of the sign request email. |
| External ID | An external identifier for the sign request. |
| Is document preparation needed | Indicates if document preparation is required. |
| Is phone verification required to view | Indicates if phone verification is required to view the document. |
| Name | Name given to the sign request. |
| Parent folder | Folder where the signed document is stored. |
| Prefill tags | Tags used for prefilling content in the document. |
| Prepare URL | URL provided for document preparation. |
| Redirect URL | URL for redirecting after the document is signed. |
| Sign files | Files that are part of the sign request. |
| Signature color | Color specified for the signature. |
| Signers | List of signers involved in the sign request. |
| Signing log | Log detailing the signing process. |
| Source files | Original files used for the sign request. |
| Status | Current status of the sign request. |
| Template ID | The ID of the template used in the request. |

---
