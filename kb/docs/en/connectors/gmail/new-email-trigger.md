---
url: 'https://docs.workato.com/en/connectors/gmail/new-email-trigger.md'
description: The New email trigger picks up new emails in your Gmail account.
---

# Gmail - New email trigger

The **New email** trigger picks up new emails in your Gmail account. It performs a single check for new emails for each poll interval. Workato processes each email as a separate job.

## Input

| Input fields | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Enter the time from which the recipe picks up events from. The trigger processes emails created after this time. If left blank, the trigger picks up emails created one hour before the first time this recipe starts. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Enter the trigger poll interval to determine how frequently to check for new events. Defaults to five minutes if left blank. Minimum value allowed is five minutes. |
| Label | Specify the labels you plan to fetch emails associated with. All emails are fetched if left blank. |
| Include spam and trash | Select to include emails from spam and trash in the results. Defaults to `No` if left blank. |

## Output

The output datatree contains information about the [email](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get).

| Output field | Description |
| --- | --- |
| ID | The unique ID for the email. |
| Thread ID | The ID of the email thread. |
| Subject | The subject of the email. |
| Snippet | The snippet of the email. |
| Body as plain text | The body of the email as plain text. |
| Body as HTML | The body of the email as HTML. |
| From email | The email address of the sender. |
| Label IDs | The IDs of the labels attached to the email. |
| To emails | The email addresses of the recipients. |
| Cc emails | The email addresses of the cc recipients. |
| Received time | The time the email was received. |
| Attachments | The attachments of the email. |

---
