---
url: 'https://docs.workato.com/en/connectors/outlook/trigger-new-email.md'
description: >-
  The New email trigger in the Outlook connector monitors an inbox or shared
  mailbox and fires in real time when new emails arrive.
---

# Outlook - New email trigger (real-time)

The new email trigger in Outlook monitors an inbox or a shared inbox for new incoming emails. It is a real-time trigger, meaning that new emails received in the inbox will trigger the recipe and create a trigger event instantly.

By default, the trigger monitors emails sent to the connected Outlook account. However, you can choose to monitor emails in a shared mailbox by providing the email address of that shared mailbox.

If the connected user has no permissions to access the shared mailbox, or if an incorrect shared mailbox email address is entered, a `404` error occurs.

## Trigger behavior when recipe is stopped and restarted

Even if the recipe is stopped, when it's restarted again, all emails created in the time during which the recipe was stopped will be picked up by the recipe.

## Input

| Field | Description |
| --- | --- |
| Shared mailbox | Provide the email address of the shared mailbox if you plan to monitor emails in shared mailboxes. If left blank, Workato connects to your default mailbox. |
| Folder | Select the folder in the mailbox to monitor for emails. |
| When first started, this recipe should pick up events from | When you start a recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get records added one hour ago. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

The output datatree contains information about the email. This includes the sender, recipients, subject, body, and other email details.

| Field | Description |
| --- | --- |
| ID | The unique identifier for the email. |
| Change key | The change key for the email. |
| Created date time | The date and time the email was created. |
| Last modified date time | The date and time the email was last modified. |
| Received date time | The date and time the email was received. |
| Meeting message type | The type of email. |
| Has attachments | Indicates whether the email has attachments. |
| Subject | The subject of the email. |
| Body | The body of the email. |
| Content | The content of the body of the email. |
| Content type | The type of the content. |
| Body preview | A preview of the body of the email. |
| Importance | The importance of the email. |
| Sender | The sender of the email. This object contains the sender's email address and name. |
| From | The sender of the email. This object contains the sender's email address and name. |
| To recipients | The recipients of the email. This object includes the email address and name of the recipient. |
| CC recipients | The CC recipients of the email. This object contains the email addresses and names of the CC recipients. |
| BCC recipients | The Bcc recipients of the email. This object contains the email addresses and names of the Bcc recipients. |
| Conversation ID | The conversation ID of the email. |
| Is delivery receipt requested | Indicates whether a delivery receipt is requested for the email. |
| Is read receipt requested | Indicates whether a read receipt is requested for the email. |
| Is read | Indicates whether the email is read. |
| Is draft | Indicates whether the email is a draft. |
| Web link | The web link to the email. |

---
