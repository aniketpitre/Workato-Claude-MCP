---
url: 'https://docs.workato.com/en/connectors/gmail/download-attachment-action.md'
description: >-
  The Download attachment action downloads an email attachment from your Gmail
  account.
---

# Gmail - Download attachment action

The **Download attachment** action downloads an email attachment from your Gmail account. Each attachment is processed as an individual job.

## Input

| Input field | Description |
| --- | --- |
| Email ID | Enter the ID of the email containing the attachment. You obtain this value from the output of the **New email** trigger. |
| Attachment ID | Enter the ID of the attachment you plan to download. You obtain this value from the output of the **New email** trigger. |

## Output

The output of the **Download attachment** action is a datatree that contains information about the downloaded [attachment](https://developers.google.com/gmail/api/reference/rest/v1/users.messages.attachments).

| Output field | Description |
| --- | --- |
| Content bytes | The content of the downloaded attachment. |
| File size | The size of the downloaded attachment. |

---
